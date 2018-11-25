# Construction Website
Django App to serve website + statics

## Setup

The following instructions will allow you to get a version of this app up and running locally. Make sure you have psql.

**1) Get this repo, install requirements, and create local db**

~~~bash
$ cd ~/construction-website
$ virtualenv venv
$ source venv/bin/activateA
$ cd construction
$ pip install -r requirements.txt
$ createuser -d BobTheBuilder
$ createdb -U BobTheBuilder constructiondb
$ python manage.py migrate
~~~

**2) Run a local server**

~~~bash
$ cd ~/construction-website
$ source venv/bin/activate
$ cd construction
$ python manage.py runserver
~~~

Now visit `localhost:8000`. Your django site is live! 🚀

**3) Admin Site**

~~~bash
$ cd construction-website/construction
$ python manage.py createsuperuser
~~~

Now visit `localhost:8000/admin` to visit the admin view of the website & login with your super user credentials. 


## Zappa

### Configuring S3 bucket for static assets

```bash
$ aws s3 mb s3://zappa-static-construction  --endpoint-url https://s3.us-east-1.amazonaws.com
$ aws s3api put-bucket-cors --bucket zappa-static-construction --cors-configuration file://.cors-policy.json
```