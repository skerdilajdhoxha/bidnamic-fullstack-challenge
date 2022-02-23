# Bidnamic challenge

## Installation
- Clone the project into your machine: `git clone <repo>`
- Cd into the project dir and create a virtual environment.

- `python3 -m pip venv <venv>` or `virtualenv <venv>`. The first one comes with Python 3
- Activate virtual environment: `source <venv>/bin/activate`. This command works only for Unix systems. For Windows `<venv>\Scripts\activate`
- Install dependencies: `pip install -r requireements/requireements.txt`.
- `cd src` then run:
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py collectstatic`
- `python manage.py createsuperuser`
- `python manage.py runserver`

## Installing third-party apps
- If you want to install new third-party apps, you can install it `pip install <name_of_the_app>`, copy/paste the app name into requirements.in then do `pip-compile requirements/requirements.in`. We use [pip-tools](https://github.com/jazzband/pip-tools) to maintain our dependencies.

## Notes

- The project uses Bootstrap 4 through a cdn.
- You have sign in to see the contents of the app.
- Task creation has two validations:
1- User has to be above 18 years old to fill the form
2- Google Ads Account ID has to be 10 letters
- The app has tests. You can run them: `python manage.py test`
- I have installed [coverage](https://github.com/nedbat/coveragepy). Usage:
Run tests: `coverage run manage.py test`
Report: `coverage report -m`
Html report: `coverage html`
