Texter
======

Send text messages using your Gmail account and [SMS gateways](https://en.wikipedia.org/wiki/SMS_gateway)  

Live demo: [texter.mattbutterfield.com](http://texter.mattbutterfield.com)

## Setup

First, install this package with pip:

    $ pip install texter

Then, set some environment variables so texter can send mail from your Gmail account:

    $ export GMAIL_EMAIL=<email>
    $ export GMAIL_PASSWORD=<password>

## Usage

```python
from texter import send_message

send_message('1234567890', 'verizon', 'Hello from texter.')
```

There is also a standalone script you can use:

    $ bin/send_message 1234567890 verizon "Hello from texter."

## Web site:

To start your own version of the web site:

### Set up environment:

Install [node](https://nodejs.org/en/) and [postgresql](http://www.postgresql.org/), then install the required python packages, create the database and set the uri environment variable:

    $ pip install -r app_requirements.txt
    $ createdb texter
    $ export DATABASE_URI=postgresql://localhost/texter
    
Download static dependencies and start the app:

    $ cd app/static/
    $ npm install
    $ cd ../../
    $ python run_app.py
