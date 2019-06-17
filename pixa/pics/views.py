from django.shortcuts import render, redirect
from .models import Category,Location, Image
from django.http  import HttpResponse, Http404

# Create your views here.
def home(request):

    images = Image.objects.all()

    return render(request, 'index.html',{"images":images,})

def category_search(request):
    if 'category' in request.GET and request.GET['category']:
    #     search_term = request.GET.get("category")
    #     search_findings = Image.search_by_category(search_term)
        
    #     message = f"{search_term}"
         
    #     return render(request, 'search.html',{"message":message,"categories":search_findings})
    
    # else:
    #     message = "You haven't searched for anything"
    #     return render(request, 'search.html',{"message":message})
    
   
    
       search_term = request.GET.get('category')
       print(search_term)
       search_category=Category.objects.filter(name=search_term)
       print(searched_categories)
       get_images=[]
      
       for category in search_category:
          category_id=category.id
          searched_images=Image.search_by_category(category_id)
          get_images.extend(searched_images)
       message=f'{search_term}'
       return render(request, 'search.html',{'message':message,'get_images':get_images})
    else:
       message=')Ooops!!! You have not searched anything'
       return render(request, 'search.html',{"message":message})

