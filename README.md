
![Venzo Logo](https://venzotechnologies.com/static/media/logo.20c3af3bf8b6aedba1ed0e68ca927882.svg)

# Venzo Django Starter Pack

Welcome to the venzo Django Starter Pack! This starter pack is designed to help you kickstart your Django projects with some essential configurations and features.

## Getting Started

Follow these steps to get your project up and running:

### Prerequisites

Make sure you have the following installed on your machine:
- docker 
- python
- pip

#### Install docker 

https://docs.docker.com/engine/install/



#### Required packages
- [Python](https://www.python.org/downloads/) (3.11 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [flake8](https://pypi.org/project/flake8/)
- [pylint](https://pypi.org/project/pylint/)


### Clone the Repository
```bash
git clone https://github.com/venzo-tech/venzo_django_starter.git
cd venzo_django_starter
```


### Install required vs code extensions
- Open Visual Studio Code on your local machine.
- Navigate to .devcontainer/devcontainer.json .
- Press Ctrl + P (Windows/Linux) or Cmd + P (Mac) to open the command palette.
- Enter > ***Extensions: Install Extensions*** and press Enter.


### Run via docker 

#### do the collecstatic and migrations
```bash
docker-compose run django python manage.py collectstatic
docker-compose run django python manage.py makemigrations
docker-compose run django python manage.py migrate
```


#### create superuser if required

```bash
docker-compose run django python manage.py createsuperuser
```

#### build and run
```bash
docker-compose build
docker-compose up
```


