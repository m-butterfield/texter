Texter
======

Send text messages using [SMS gateways](https://en.wikipedia.org/wiki/SMS_gateway)

## Setup

First, you must have a mail server such as [Postfix](http://www.postfix.org/) installed and running on localhost.  Then, install this package with pip:

    $ pip install texter

## Usage

```python
from texter import send_message

send_message('1234567890', 'verizon', 'Hello from texter.')
```

There is also a standalone script you can use:

    $ ./send_message 1234567890 verizon "Hello from texter."
