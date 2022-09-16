# Hello World!
## Flask on Reclaim Cloud

[Reclaim Cloud](https://reclaim.cloud) offers Python hosting via Apache's `mod_wsgi`. The document root for Reclaim Cloud python environments is `/var/www/webroot/ROOT` and our Flask starter kit installer will put the following files in the document root:

#### `wsgi.py`
Tells `mod_wsgi` where to find your application. I cobbled this together based on the default `wsgi.py` that comes when you deploy a Python environment on Reclaim Cloud and [Flask's mod_wsgi documentation](https://flask.palletsprojects.com/en/2.2.x/deploying/mod_wsgi/).

#### `hello.py`
A flask app that outputs "Hello, World!" to a webpage. This is taken from [Flask's Quickstart page](https://flask.palletsprojects.com/en/2.2.x/quickstart/).

#### `requirements.txt`
Tells Reclaim Cloud to install the `flask` module using pip upon deployment. You can also manually install flask via the terminal with `pip install flask`.

### Further resources
We'd recommend checking out the follwoing resources for more info on Flask and Reclaim Cloud:
- [Virtuozzo PaaS Python Dev Center](https://www.virtuozzo.com/application-platform-docs/python-center/)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/)
  - [Quickstart](https://flask.palletsprojects.com/en/2.2.x/quickstart/)
  - [mod_wsgi](https://flask.palletsprojects.com/en/2.2.x/deploying/mod_wsgi/)
