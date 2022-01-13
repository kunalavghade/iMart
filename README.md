
# iMart

iMart is Django based website which is based on Finance and Share Market.

### Features
- Authantication System
- Graphical stock visualizaion
- Recent stock information
- Stock suggestion 
- About section
- Contact section


## Preview
To viwe preview of website click here [Click here](https://linktodocumentation)


## Installation


To Install necessary Librarys for this project run.

Note: Python 3.8 or greater verion is required.

```bash
pip install django
```

```bash
pip install yfinance
```

```bash
pip install requests
```    
## Run Locally

Clone the project

```bash
  git clone https://github.com/kunalavghade/iMart.git
```

Go to the project directory

```bash
  cd iMart
```

create folder Named migrations along with file __init__.py
```bash
cd Mart && mkdir migrations && cd migrations && echo > __inti__.py
```

To create database run
```bash
  python manage.py migrate
```
```bash
  python manage.py makemigrations
```

Inside iMart folder run server
```bash
  python manage.py runserver
```

## Tech Stack

**Client:** HTML, JS, CSS

**Server:** Django, Python

