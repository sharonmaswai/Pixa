#Pixa

## Description

This is an app that displays images, with different locations and categories.

## SETUP INSTRUCTIONS:

### Installation

1.Python 3.6.5 

2.Django 1.11

### Cloning the repository

git clone https://github.com/sharonmaswai/pixa.git && cd My-Gallery

### Creating a virtual environment

sudo apt-get install python3.6-venv python3.6 -m venv --without-pip virtual source virtual/bin/activate

### Installing dependencies

pip install -r requirements.txt

### Running tests

python3.6 manage.py test photos

### Running the Development server

python3.6 manage.py runserver

## BEHAVIOUR DRIVEN DEVELOPMENT

| Behaviour | Input  | Output |
| -- |-- |--|
|User(admin)| Enter login credentials| Access admin portal|
|Add image|Click add image |New Image object|
|Add category|Click add category |New category object|
|Add Location|Click add location |New location object|
|Display image details|click image name|Display image modal with details|
|Show images in category|Enter image category|Display images in the category|





##CONTACTS

For more information and clarification contact me through chepsharon@gmail.com

## LICENSE

MIT License

Copyright (c) [2019] [SharonMaswai]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
