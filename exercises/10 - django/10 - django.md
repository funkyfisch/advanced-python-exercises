## Django exercise

* We will start by installing Django in a virtual environment with `venv`.
  Create a new directory and copy `requirements.txt` into this directory.
  Then execute:

```bash
python3 -m venv ./env
source ./env/bin/activate
pip3 install -r requirements.txt
```

Check what was installed with

```bash
pip3 list
```

* Now we will initialize a Django project. From the same directory issue the command
  `django-admin startproject products`. (`products` here is the name
  of our new project.)

* Have a look around in the newly created directory `products`.

It should look like this:

```
products/
    manage.py           -- command-line project admin tool
    products/           -- holds your project package
        __init__.py     -- empty. tells Python this is a package
        settings.py     -- configuration
        urls.py         -- for the URL dispatcher
        wsgi.py         -- for the web server
```

* Try that it all works. Enter into that outer `products/` directory, and run
  `python3 manage.py runserver`.

You should see some output ending with this, or something very similar:

```
Django version 2.2.7, using settings 'products.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

* Edit the `products/settings.py` file and fill in the following value:
    * `TIME_ZONE: 'Europe/Stockholm'`
    * (also, while you are in this file, have a look at the `INSTALLED_APPS`
      setting. you don't need to change anything, just have a look)

* Save the file.

* Time to auto-generate all the database tables we need. In the terminal, run
  `python3 manage.py migrate` to do this.

* Time to create our first application in this project. Run the command
  `python3 manage.py startapp inventory`. This creates a new subdirectory
  `inventory/`.

* Now it's time to create the application data model.

Open `inventory/models.py` and replace its contents with this (code also exists
in `models-v1.py`):

```python
from django.db import models

class Type(models.Model):
    description = models.CharField(max_length=80)

class Product(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    shelf = models.CharField(max_length=10)
```

(As you see, it's simply two class declarations with some attribute
declarations. Everything uses things from the `django.db.models` namespace,
declaring data types and class relationships.)

* Now you'll need to go back into `products/settings.py` and edit the
  `INSTALLED_APPS` setting you looked at before. Add the string
  `'inventory.apps.InventoryConfig'` at the end of that list. Save and exit.

* Now run `python3 manage.py makemigrations inventory`.  This will generate
  the initial database schema for your module.   It should output something
  like:

```
Migrations for 'inventory':
  inventory/migrations/0001_initial.py
    - Create model Type
    - Create model Product
```

* Now run `python3 manage.py sqlmigrate inventory 0001`. You should get the SQL
  that corresponds to the model code you just wrote. It doesn't
  actually update the database yet, though. But it's pretty cool that it took
  your Python classes and made SQL `CREATE TABLE` statements out of them,
  isn't it?

* Run the `python3 manage.py migrate` command. This will update the database.

* Time to play around a little with the interactive shell. Run `python3 manage.py shell`.
  (Why not just `python3`? Because `manage.py` sets an
  environment variable `DJANGO_SETTINGS` which Django needs.)

Type the following into the shell:

```python
>>> from inventory.models import Type, Product
>>> Type.objects.all()
<QuerySet []>
>>> t = Type(description='wrench')
>>> t.save()
>>> t.id
1
>>> Type.objects.all()
<QuerySet [<Type: Type object (1)>]>
```

That last line of input is spectacularly unhelpful. Let's fix it.

* Time to go back into the data model.

Open `inventory/models.py` and add `__str__` methods:

```python
from django.db import models

class Type(models.Model):
    description = models.CharField(max_length=80)

    def __str__(self):
        return self.description

class Product(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    shelf = models.CharField(max_length=10)

    def __str__(self):
        return '{}, shelf {}'.format(self.type, self.shelf)
```

Back in `python3 manage.py shell`, this now looks much better:

```python
>>> from inventory.models import Type, Product
>>> Type.objects.all()
<QuerySet [<Type: wrench>]>
```

Yay. Time to add a couple of products:

```python
>>> t = Type.objects.get()
>>> t
<Type: wrench>
>>> Product(type = t, shelf = '19F').save()
>>> Product(type = t, shelf = '28B').save()
```

You can now query the type for all products of that type, for example:

```python
>>> t.product_set.count()
2
>>> t.product_set.all()
<QuerySet [<Product: wrench, shelf 19F>, <Product: wrench, shelf 28B>]>
```

Or you can filter products based on their type. Use double underscores to
separate relationships:

```python
>>> Product.objects.filter(type__description='wrench')
<QuerySet [<Product: wrench, shelf 19F>, <Product: wrench, shelf 28B>]>
```

* Now we will check out the admin interface. The first step is to
  create a superuser account by running `python3 manage.py createsuperuser`

* Run `python3 manage.py runserver`.
  Instead of going to http://127.0.0.1:8000/ as suggested, go to
  http://127.0.0.1:8000/admin/. You should be greeted with a login page.

* Log in. Use the user name and password for the superuser you created.

* Once logged in, you will see an administration pane. But our `inventory`
  application isn't there! Let's fix that.

Edit the file `inventory/admin.py`, and fill it with this content (which
you can also find in `inventory-admin.py`):

```python
from django.contrib import admin
from .models import Product, Type

admin.site.register(Product)
admin.site.register(Type)
```

* Now the "inventory" pane should show up when you go to
  http://127.0.0.1:8000/admin/. Browse around a little
  to your own satisfaction. Note that it's also possible to add more user data
  through the admin interface, and even to configure the interface to make this
  more smooth. That's outside of the scope of this exercise, however.

* Lastly, we add a view of our inventory.

Edit the file `inventory/views.py` (which you can also find in
`inventory-views-v1.py`):

```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('OH HAI, inventory index')
```

Also, add a file `inventory/urls.py` (which you can also find in
`inventory-urls.py`):

```python
from django.urls import path

from . import views

urlpatterns = [
    # ex: /inventory/
    path('', views.index, name='index'),
]
```

We're almost there. We also need to go back to `products/urls.py`, the global
URLs file, and add a link to our inventory urls like this:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls'))
]
```

* Save and browse to http://127.0.0.1:8000/inventory/ (Note `/inventory/` at the end.)

* You should be greeted with `OH HAI, inventory index`. This is what we wanted
  so far, but of course, we'd like our products to be shown here.

Let's wire up a minimal view that actually pulls products out of the database.
Replace the contents of `inventory/views.py` with this (also found in
`inventory-views-v2.py`):

```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    all_products = Product.objects.all()
    output = '\n'.join('<p>{}</p>'.format(pr) for pr in all_products)
    return HttpResponse(output)
```

* Save and browse to http://127.0.0.1:8000/inventory/ again. The products should now show up.
