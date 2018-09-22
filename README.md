# Purpose

# References

## Creating Your First Python API with Flask
https://www.fernandomc.com/posts/your-first-flask-api/

## Redmond python meetup 2018-09-20

## basic_flask
https://github.com/beepscore/basic_flask

## Build a Python Web Server with Flask
https://projects.raspberrypi.org/en/projects/python-web-server-with-flask

# Results

## how to run app
start terminal

### activate virtual environment

    conda activate beepscore

### start server
    $ python app.py

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 250-850-674
127.0.0.1 - - [20/Sep/2018 19:35:39] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [20/Sep/2018 19:35:39] "GET /favicon.ico HTTP/1.1" 404 -

# Appendix configure flask for production
with default configuration, flask warns
   WARNING: Do not use the development server in a production environment.

## debug
To use in production, turn off debug mode.
In app.py call app.run(debug=False)
This way errors won't be exposed to user's browser.

## use a different server for large static files
Also by default flask serves all files.
In production, use a separate server to serve large static files such as images.
https://docs.djangoproject.com/en/2.1/howto/static-files/deployment/
Can use content delivery network or amazon s3 or apache or nginx.

