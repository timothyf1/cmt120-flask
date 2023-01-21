# CMT120 Fundamentals of Programming CW2

Username - d1323632

Openshift - [https://d1323632-cmt120-cw2.apps.openshift.cs.cf.ac.uk/](https://d1323632-cmt120-cw2.apps.openshift.cs.cf.ac.uk/)

## Creating the portfolio

### Environment variables

The following environment variables are used and **MUST** be configured.

- SECRET_KEY - The secret key used by flask for session signing cookies.
- SQLALCHEMY_DATABASE_URI - The database connection URI, for example `mysql+pymysql://username:password@host/db_name`

### Creating the db

Run the python script `create_db.py` will create the database structure. Then create the admin account and add some sample data to the database.

### Default login

Default username and password are as follows:

- Username: admin
- Password: password

Upon first login you will be prompted to change the password

### Image uploads

For the topic pages it is possible to upload pictures to be used within these pages. Images are uploaded to `portfolio/static/upload` within this directory a sub folder will be created with the `topic_id` as the folder name. Inside the `topic_id` folder is where the images will be uploaded.

Even though this folder can be changed in the app config it **MUST** however be located in the `static` folder. If this is moved outside the `static` Flask will be unable to serve the images.

## Portfolio Structure

The portfolio is structured into two main areas: Education and Expeience. In addition there are also authentication, profile and home sections. Each of the sections have been given their own blueprint in flask.

### Education

The main section of the portfolio. Within this section courses can be added. Each course can have multiple modules. Within each module there are topics which are articles.

### Expeience

This is a page for entering previours working expeience.

## Packages used

Below is a list of packages used with a link to the documentation. There are other packages installed which are dependencies of those listed below.

- [bleach](https://bleach.readthedocs.io/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-Breadcrumbs](https://flask-breadcrumbs.readthedocs.io/)
- [Flask-Login](https://flask-login.readthedocs.io/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/)
- [Gunicorn](https://docs.gunicorn.org/)
- [Markdown](https://python-markdown.github.io/)
- [MarkupSafe](https://markupsafe.palletsprojects.com/)
- [PyMySQL](https://pymysql.readthedocs.io/)
- [Werkzeug](https://werkzeug.palletsprojects.com/)
- [WTForms](https://wtforms.readthedocs.io/)
