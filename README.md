# Construction Website
Django App to serve website + statics

## Setup

The following instructions will allow you to get a version of this app up and running locally. Make sure you have psql.

**1) Get this repo, install requirements, and create local db**

~~~bash
$ cd ~/construction-website
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ createdb constructiondb
~~~

**2) Run a local server**

~~~bash
$ cd ~/construction-website
$ source venv/bin/activate
$ python manage.py runserver
~~~
