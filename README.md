# PyShop
**PyShop** is first python django framework project by professor **Asmony** 2021.

## Table of Contents

- [Introduction](#pyshop)
- [Installation 📦](#django-installation)
- [Create Project and apps](#create-project-and-apps)
- [Web Development Server](#servers)
- [Memo 💡](#memo)


# Django Installation

OS X 

```sh
$pip install Django==3.1.7
```


# Create project and apps

for **project** `django-admin startproject project_name` . (.is called period which indicates the current location in the project). for **apps** `python3 manage.py startapp app_name`.

```sh
project

$django-admin startproject pyshop . 

app

$python3 manage.py startapp

```


# Servers

after creating the django-admin project we need to run the web development server with following command windows `python`, mac `python3`
Starting development server at `http://127.0.0.1:8000/`.
```sh
$python3 manage.py runserver

```


# Memo 💡

The project structure description.

Parameter   | Description
----------- | -----------
__init__.py       | The `__init__.py` is the initialization of the package. This is reusable to other python developer to resuse this package and saves the time.
admin.py    | The `admin.py` module is used to define how the adminstratative panel of this app will looks like.
apps.py        | The `apps.py` module will store the various configuration setting of the particular app but it's little bit confuse because it's better to call config.py.
models.py   | The `models.py` module is used to define `Classes` and `New Types` for modeling the concept in the app. For example products, categories and reviews 
tests.py | The `tests.py` module is used to define the automated test for the app.
views.py    | The `views.py` will defines what should the user see when navigating to the certain `url/user/1` page in the browser.

# View Function

How to create first view / view function in django. A view function is a `=>(), function()` that get calls by django when the user navigates to the perticular page. For example when user navigates to  `http://127.0.0.1:8000/products`. a browser sends `http request` for web server at that point django takes that request it inspect the url address then it figures it outs that it is going to see the list of all products content then it will call the function which call a view function. And the job of this function is to return the response to the browser or the client so this function will generates shome `HTML markups` to return to the client. And browser will get the contents and displays the page in the window.

let's work on views.py module:
default we see some boilerplates-code (that are repeated in multiple places with little to no variation) `from django.shortcuts import render` here `django` is a package `shortcuts` is a module and `render` is a function.

to define the **view function()** 
    `def index()` it's the main page of an app so we call it by convention like `index()`
    the `viw function(request)` alwasy takes a parameter that is `http request`
    we need to import the `HttpResponse` class `from django.http import HttpResponse` which handles response and returns to the client or browser. and needs to return the `return HttpResponse` object instance of that `HttpResponse` Class.
    
**View Function():**

```python
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello Products!')

```

**URL Maping** => we have done the view function but the django will not understant that it should call the view function when we send the request to `/products` so we need to tell that django whenever there is a request to `/products` then call to the `index()` function. That's why, we need to map `/products` url to the `index()` function.

**Steps:**
- navigate to the app folder, right click and add new python file urls.py. (we have to create ourselves urls.py file)
We have to define the variables as rules no -, caps and so on. Should be all in lowercase. And should set to the list object. Inside this list we map various urls to the `view function()`. To reference the url we need to import the `path function()`. With the path() function we can map the url to the view function so we need to pass the path() function. The first argument is the string that specifies the url end point. path('') the empty string referes as the root end point. As a second arguments we need to specify the view function, that is defined `inside of the views.py module` so we need to import the `views.py` module in the `urls.py` module for example `from . import views`. To access the `index function` we have to act as like object of views module like `views.index()` in to the `urls.py` module. 

- Notes: we don't need to pass the function like `path('', views.index)` because we just need to pass the references.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]

```

- One more step left because django is not stil ready over the `products` app so, we need to tell the django about `products` app to reference `products` app. So what we need to do is just collapse the `products` app folder and jump to the `pyshop` app folder and there is another `urls.py` module so this is like the parent and root urls module in the django project.

**pyshop/urls.py**

```python

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls)
]


```
- so what happened so far in the pyshop/urls.py so we need to define another path object function and inform to the django any path any urls that starts with the `product/` and deligates(authorize) them to the products app. So we want the django that deligate the handling request to the defined url modules in the `products/urls.py` ('', 'products/new', 'products/add', 'products/1') module. To deligate the we need to improt `include function` in the root urls.py


```python

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls'))
]


```
`path('products/', include('products.urls'))` any urls start with products/ then send to the `urls.py` module in the products app.

# Model

Madel is a representation of real world concept. For example in online shopping we have `orders, customer, shopping_cart, product and review` so on.
We need to inherit the model class in django

```python
    from django.db import models

    class Product(models.Model):

```
==> We peform certain operation in model objects like add, delete, update and so on.

```python
    from django.db import models
    
    
    class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

```
- in the above Product class we defined the attributes of that class.

# Migration
DB Browser for Sqlite[https://sqlitebrowser.org/dl/]

- After creating the model class we need to register the `Products` app to the `settings.py` module under the `INSTALLED_APSS = []` list in the root folder.

```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products.apps.ProductsConfig'
]
```
In the `settings.py` module we registered our apps `products.apps.ProductsConfig`. Then after do the following steps to migrate the database. (*Reminder: you need to register each and every apps under the parent settings.py module*).

**Migrate** it to the database run following command:

`python3 manage.py makemigrations`

We will see the following result

```
- ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `#f03c15`
Migrations for 'products':
  products/migrations/0001_initial.py
    - Create model Product
```

