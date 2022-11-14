To run this project in your development machine, follow these steps:


(optional) Create and activate a virtualenv (you may want to use virtualenvwrapper).

Fork this repo and clone your fork:
git clone https://github.com/sclorg/django-ex.git


Install dependencies:
pip install -r requirements.txt


Create a development database:
./manage.py migrate


If everything is alright, you should be able to start the Django development server:
./manage.py runserver


Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.
