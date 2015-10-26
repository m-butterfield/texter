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

    $ ./send_message 1234567890 verizon "Hello from texter."

## Demo site:

To start your own version of the demo site (requires [node](https://nodejs.org/en/)):

    $ cd demo_site/static/
    $ npm install
    $ cd ../../
    $ python demo_site.py
