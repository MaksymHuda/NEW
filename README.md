To run this project in your development machine, follow these steps:


(optional) Create and activate a virtualenv (you may want to use virtualenvwrapper).

Fork this repo and clone your fork:
git clone https://github.com/MaksymHuda/NEW.git


Install dependencies:
pip install -r requirements.txt


Create a development database:
./manage.py migrate


If everything is alright, you should be able to start the Django development server:
./manage.py runserver


Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.


API endpoints

1.Отримати список напрямків --> http://127.0.0.1:8000/directions/
2.Отримати список лікарів --> http://127.0.0.1:8000/doctors/
3.Отримання інформації про лікаря --> http://127.0.0.1:8000/doctors/N/  (N = Номер лікаря (1, 2, 3) - INT )
