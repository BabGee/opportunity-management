# Opportunity Management System

Opportunity management is a web-based system with the following functionalities.
1. Register new users.
2. Log in registered users.
3. Logged in users can create Accounts and Opportunities.
4. Logged in users can view created Accounts and Opportunities.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites
You will find hereafter what I use to develop and to run the project
* Python 3.9.1
* Django 3.1.5
* pipenv (not mandatory but highly recommended)

### Installation

Get a local copy of the project directory by cloning "opportunity-management" from github.

```bash
git clone git@github.com:BabGee/opportunity-management.git
```

I use pipenv for developing this project so I recommend you to create a virtual environment and activate it.

```bash
python -m pipenv shell
```

Install the requirements

```bash
python -m pip install -r requirements.txt
```

Then follow these steps:
1. Move to root folder 

```bash
cd opportunity_management
```
2. Create a `.env` file in the root folder, provide the required database information  to the `.env` file (.env.example file is provided to help set this information)

3. Create the tables with the django command line

```bash
python manage.py makemigrations
```
then migrate the changes
 
```bash
python manage.py migrate
```

5. Finally, run the django server

```bash
python manage.py runserver
```

## Built With

* [Python 3](https://www.python.org/downloads/) - Programming language
* [Django](https://www.djangoproject.com/) - Web framework 


## Versioning
I use exclusively Github

## License

This is an open source project not under any particular license.
However framework, packages and libraries used are on their own licenses.
