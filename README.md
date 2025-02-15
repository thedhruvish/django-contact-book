# Django-contact-book

## Topics

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation & Configuration](#installation-and-configuration)
4. [License](#license)
5. [Security Vulnerabilities](#security-vulnerabilities)

### Introduction

- This Project are the only Learning purpose to created
- contact is the CURD ( Create, Update, Read, Delete )

### Requirements

- **RAM**: 3 GB or higher.
- **[Python]([text](http://python.org/))**: 3.10 or higher
- **[pip](https://pypi.org/)**: Python Package Managment

### Installation and Configuration

##### Execute these commands below, in order

```bash
pip install uv  # installl fast Python package and project manager

uv venv # Create a virtual environment

.venv\Scripts\activate # Active Env on Windown

```

- install the Django Requirements

```bash
uv pip install -r requirements.txt 
```

- Migration And Super User Create 

```bash
cd contact

python manage.py migrate

```
- Run the Server

```bash
python .\manage.py runserver        
```


### License

- This project is MIT licensed.

### Security

email us: thedhruvish@gmail.com