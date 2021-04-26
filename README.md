# personal blog web site
> This is a personal blog web site developped using Python Django.

## Requirements
* Python 3
* PostgreSQL 13

## Installation

Navigate to a new folder using your command prompt and type :

`git clone https://github.com/AbdellaouiSofiane/personal_blog.git`

Navigate to the project directory (make sure to activate your virtual enviroment) and type :

`python -m pip install -r requirements.txt`

Launch the developpement server :

`python manage.py runserver`

Visite http://127.0.0.1:8000/ in your browser.

Note : This project make use of PostegreSQL, so you should create a dadabase before running the server. 
Go to mysite/mysite/settings in line 91 to 100 and configure the database settings accordingly.

## Screenshots

![image](https://user-images.githubusercontent.com/62038668/116013184-13281600-a62f-11eb-9bb7-17488649ba43.png) 

![image](https://user-images.githubusercontent.com/62038668/116013223-3fdc2d80-a62f-11eb-9a64-62cbf72de64f.png)

![image](https://user-images.githubusercontent.com/62038668/116013248-67cb9100-a62f-11eb-8441-477309cee521.png)

![image](https://user-images.githubusercontent.com/62038668/116013315-d7418080-a62f-11eb-837a-b407547b7b1b.png)

## Features

* Tagging funtionnality for content posted
* PostegreSQL full search functionnality
* Search by tag name
* Makdown functionnality for writing posts 
* Lastest posts feature
* Posts recommendations feature
* Commenting system
* Sharing by email functionnality
* Pagination

## Tech Stack / Built With

1. [Django](https://docs.djangoproject.com/en/3.1/) - The Python framework
2. [Bootstrap4](https://getbootstrap.com/) - A CSS framework
3. [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html) - A django 3rd party package
4. [django-taggit](https://django-crispy-forms.readthedocs.io/en/latest/index.html) - A django 3rd party package

## Authors

Sofiane Abdellaoui - abdellaoui.sofiane.esb@gmail.com

## Credits

This project was inspired by chapter 1 to 3 from the book :

Django 3 By Example - Build powerful and reliable Python web applications from scratch (author Antonio Melé)

