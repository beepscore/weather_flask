# Purpose

# References

http://fernandomc.com

## Creating Your First Python API with Flask
https://www.fernandomc.com/posts/your-first-flask-api/

## Redmond python meetup 2018-09-20

# Appendix

## run server

In terminal
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
with default configuration, flask warns ~ "don't use in production"

## debug
To use in production, turn off debug mode.
This way errors won't be exposed to user's browser.

## content delivery network
Also by default flask serves all files.
In production, use a separate content delivery network to serve large static files such as images.
Tell flask to use cdn for those files.

