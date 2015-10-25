from distutils.core import setup
from pip.req import parse_requirements


requirements = [str(ir.req) for ir in parse_requirements('requirements.txt')]

setup(
    name='texter',
    packages=['texter'],
    version='0.2',
    description='Send text messages using SMS gateways',
    author='Matt Butterfield',
    author_email='deneb150@gmail.com',
    url='https://github.com/m-butterfield/texter',
    download_url='https://github.com/m-butterfield/texter/tarball/0.2',
    keywords=['sms', 'text', 'texting'],
    install_requires=requirements,
)
