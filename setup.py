from distutils.core import setup


setup(
    name='texter',
    packages=['texter'],
    version='0.5',
    description='Send text messages using SMS gateways',
    author='Matt Butterfield',
    author_email='deneb150@gmail.com',
    url='https://github.com/m-butterfield/texter',
    download_url='https://github.com/m-butterfield/texter/tarball/0.5',
    keywords=['sms', 'text', 'texting'],
    install_requires=[
        'docopt==0.6.2',
        'mock==1.3.0',
        'Flask==1.0',
        'Flask-RESTful==0.3.4',
    ],
)
