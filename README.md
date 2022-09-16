# Hello World!
## Flask on Reclaim Cloud

[Reclaim Cloud](https://reclaim.cloud) offers Python hosting via Apache's `mod_wsgi`. The document root for Reclaim Cloud python environments is `/var/www/webroot/ROOT` and this starter kit should get you started with the following three files:

#### `wsgi.py`
Tells `mod_wsgi` where to find the application, in this the `hello.py` file. This is based on the default `wsgi.py` that comes when you deploy a Python environment on Reclaim Cloud and [Flask's mod_wsgi documentation](https://flask.palletsprojects.com/en/2.2.x/deploying/mod_wsgi/).

#### `hello.py`
A flask app that outputs "Hello, World!" to a webpage. This is taken from [Flask's Quickstart page](https://flask.palletsprojects.com/en/2.2.x/quickstart/).

#### `requirements.txt`
Tells Reclaim Cloud to install the `flask` module using pip [upon deployment](https://www.virtuozzo.com/application-platform-docs/deployment-guide/). You could also manually install packages listed in this file by running `pip install -r requirements.txt`, or skip the file entirely and manually install flask by running `pip install flask`.

### Further resources
We'd recommend checking out the follwoing resources for more info on Flask and Reclaim Cloud:
- [Virtuozzo PaaS Python Dev Center](https://www.virtuozzo.com/application-platform-docs/python-center/)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/)
  - [Quickstart](https://flask.palletsprojects.com/en/2.2.x/quickstart/)
  - [mod_wsgi](https://flask.palletsprojects.com/en/2.2.x/deploying/mod_wsgi/)
