# Django ORM Models Data Navigation With Jupyter Notebook and Pandas

# Installation

## Install  Python Libraries
```
$ pip install django-extensions
$ pip install ipython
$ pip install https://github.com/ThiagueraBarao/jupyterDjangoORM/archive/main.zip
```
## Django ``Settings.py``

### Django Extensions

Add django_extensions to your project ``Settings.py``;
```
# settings.py

INSTALLED_APPS = INSTALLED_APPS + [
    # ...
    'django_extensions',
]

```

### Django Allow Async Unsafe

Allow assync requisitions from Jupyter: ``os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"``;

* **Explanation** : When we a task from an external environment, such as in a Jupyter notebook. If you are sure there is no chance of the code being run concurrently, and you absolutely need to run this sync code from an async context, then you can disable the warning by setting the DJANGO_ALLOW_ASYNC_UNSAFE environment variable to any value.


```
# settings.py

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
```



> :warning: **Don't use this in production environments!!** : If you enable this option and there is concurrent access to the async-unsafe parts of Django, you may suffer data loss or corruption. Be very careful and do not use this in production environments.

## ``Requirements.txt``

Add django_extensions to your project ``Requirements.txt``

Get the installed version of 

```
$ pip freeze | Select-String -Pattern "django-extensions"
> django-extensions==3.0.9
```

Copy and paste response in ``Requirements.txt``
```
...
django-extensions==3.0.9
...
```

# How to Use

## Start Shell
```
$ python <YourDjangoDirectory>\manage.py shell_plus --notebook
```

## Example Notebook Use
```
...jupyterDjangoORM/Notebooks/Example.ipynb
```
## Django ORM Queries Documentation
https://docs.djangoproject.com/en/3.1/topics/db/queries/#retrieving-objects