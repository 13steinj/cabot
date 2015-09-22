#!/usr/bin/env python
from setuptools import setup, find_packages
from os import environ as env

# pull in active plugins
plugins = env['CABOT_PLUGINS_ENABLED'].split(',') if 'CABOT_PLUGINS_ENABLED' in env else ["cabot_alert_hipchat", "cabot_alert_twilio", "cabot_alert_email"]

setup(
    name='cabot',
    version='0.0.1-dev',
    description="Self-hosted, easily-deployable monitoring and alerts service"
                " - like a lightweight PagerDuty",
    long_description=open('README.md').read(),
    author="Arachnys",
    author_email='info@arachnys.com',
    url='http://cabotapp.com',
    license='MIT',
    install_requires=[
        'Django==1.6.8',
        'Markdown==2.5',
        'PyJWT==0.1.2',
        'South==1.0',
        'amqp==1.3.3',
        'anyjson==0.3.3',
        'argparse==1.2.1',
        'billiard==3.3.0.13',
        'celery==3.1.7',
        'dj-database-url==0.2.2',
        'django-appconf==0.6',
        'django-celery==3.1.1',
        'django-celery-with-redis==3.0',
        'django-compressor==1.4',
        'django-filter==0.7',
        'django-jsonify==0.2.1',
        'django-mptt==0.6.0',
        'django-polymorphic==0.5.6',
        'django-redis==1.4.5',
        'django-smtp-ssl==1.0',
        'djangorestframework==2.4.2',
        'gevent==1.0.1',
        'hiredis==0.1.1',
        'httplib2==0.7.7',
        'icalendar==3.2',
        'kombu==3.0.8',
        'mock==1.0.1',
        'psycogreen==1.0',
        'psycopg2==2.5.1',
        'pytz==2014.10',
        'redis==2.9.0',
        'requests==2.7.0',
        'six==1.5.1',
        'twilio==3.4.1',
        'wsgiref==0.1.2',
        'python-dateutil==2.1',
        'django-auth-ldap==1.2.6',
    ] + plugins,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
