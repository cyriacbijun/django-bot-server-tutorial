# django-bot-server-tutorial

Accompanying repository for a seminar on creating a django based bot server that uses django-channels for  WebSockets connection. This borrows heavily from the code at https://github.com/andrewgodwin/channels-examples. 

I have used the repo https://github.com/vaisaghvt/django-bot-server-tutorial as the template. This repo enables a user to set up bot server using websockets in an updated environment of

- Fedora 33
- Python 3.9

and enables to understand the usage of spacy, an NLP library. I have made the following changes to get it working:

- `pip install setuptools==45` , this is to get Twisted library working
- changed django version to `1.11.29` , for compatibility with new version of python
- `pip install attrs==19.1.0` , to solve attrs problem when installing new django

# What is this useful for?

- Get an idea how to get django-channels working
- Get some sample code for a simple working front end that uses web sockets for a connection
- Get an idea to use spacy library to extract name of person from their introduction statement

# How to use this branch

This part of the seminar involves installing and getting started with django channels.

To get this running, simply run the  the following 

## Step 1: Install requirements.txt

```
pip install setuptools==45 
pip install attrs==19.1.0
pip install -r requirements.txt
pip install spacy
python -m spacy download en_core_web_sm
```

## Step 2: Create databases

Create the databases and the initial migrations with the following command:
`python manage.py migrate`

## Step 3: Run server

And start the server with 

`python manage.py runserver`

You should now be able to go to localhost:8000/chat/ and chat with the bot
