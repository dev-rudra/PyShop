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
    we need to import the `HTTPResponse` class `from django.http import HttpResponse` which handles response and returns to the client or browser. and needs to return the `return HTTPResponse` object instance of that `HTTPResponse` Class.
