# Apache Airflow

## Introduction
This is a clean environment to start an Apache Airflow container with everything you need to start cding


## Getting started

### Requirements
- Docker
- Docker compose
- Poetry
- Make

#### Steps
Be sure to have Make already installed in your sistem

### 1. Install Make

##### MacOS
Make comes with all the x-code bundle otherwise you can install it through Homebrew with
````
brew install make
````

##### Ubuntu
`````
apt install make
`````
If you still have an error try with:
`````
apt install build-essential
`````

##### Windows
You will make your life easier if you install the package manager Chocolately, follow the instructions in its [website](https://chocolatey.org/install), then you will be able to:

````
choco install make
````
### 2. Install Poetry
Poetry is a Python packaging and dependency management made easy. It is becoming very popular in the Pyhton ecosystem

##### osx / linux / bashonwindows install instructions
````
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
````

##### windows powershell install instructions
````
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
````

### 3. Run Make recipe and start Airflow
````
make airflow init
````
Once the process has finished you will be able to:
`````
docker-compose up
`````

#### Get Started


### The project


