This is a working example of a django-fiber_-enabled web site.

Fiber may be installed with pip_, on a regular (although empty in this example) django app.

The installation procedure
--------------------------

Startup
=======
I usually create a virtual environment with virtualenvwrapper_'s mkvirtualenv, to isolate versions.
Then I install django::

    pip install django
    
Remember to setup DJANGO_SETTINGS_MODULE and PYTHONPATH environemnt variables in virtualenv's postactivate hook::

    #!/bin/bash
    # This hook is run after this virtualenv is activated.
    WORKING_PATH=~/Workspace/fibertest
    export OLD_PYTHONPATH=$PYTHONPATH
    export PYTHONPATH=$WORKING_PATH:$PYTHONPATH
    export DJANGO_SETTINGS_MODULE=fibertest.settings


Create a django project
=======================
right from your workspace directory::
    
    django-admin.py startproject fibertest

This will create a fibertest project and a fibertest application, inside that.

Add fiber
=========
To add fiber, just install it with::

    pip install django-fiber

And follow the instructions on the README on django-fiber_'s github repository.


.. _django-fiber: https://github.com/ridethepony/django-fiber
.. _pip: http://pypi.python.org/pypi/pip
.. _virtualenvwrapper: http://www.doughellmann.com/projects/virtualenvwrapper/