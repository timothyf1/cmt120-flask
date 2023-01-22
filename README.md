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

## References

### Packages used

Below is a list of packages used with a link to the documentation which I have used. There are other packages installed which are dependencies of those listed below.

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

### Other references

Below is a list 3rd party references I have used when writing the code.

- Code to set default breadcrumb.
  Github comment by jirikuncar on 2016-09-05
  [https://github.com/inveniosoftware/flask-breadcrumbs/issues/33#issuecomment-244692682](https://github.com/inveniosoftware/flask-breadcrumbs/issues/33#issuecomment-244692682)
  Accessed on 2023-01-09
- Function to insert text into a textfield at the current location
  Stack Overflow post by GMKHussain 2021-01-19
  [https://stackoverflow.com/a/65793635](https://stackoverflow.com/a/65793635)
  Accessed on 2023-01-12
- Jinja code to count how many items in a object has an attribute
  Stack Overflow post by Marc8 2018-12-7
  [https://stackoverflow.com/a/53671429/](https://stackoverflow.com/a/53671429/)
  Accessed on 2023-01-17
- Change radio button default dynamically
  Stack Overflow post by jeinarsson 2015-01-15
  [https://stackoverflow.com/a/34820107/](https://stackoverflow.com/a/34820107/)
  Accessed on 2023-01-05
- CSS to prevent word wrapping
  css-tricks post by Sara Cope updated on 2022-09-28
  [https://css-tricks.com/almanac/properties/w/whitespace/](https://css-tricks.com/almanac/properties/w/whitespace/)
  Accessed on 2023-01-23
- Import a file depending on media query
  Stack Overflow post by Drew Altukhov 2013-09-05
  [https://stackoverflow.com/a/18636027/](https://stackoverflow.com/a/18636027/)
  Accessed on 2022-12-31
- JS function to add and remove class
  w3schools - How TO - Sticky/Affix Navbar
  [https://www.w3schools.com/HOWTO/howto_js_navbar_sticky.asp](https://www.w3schools.com/HOWTO/howto_js_navbar_sticky.asp)
  Accessed on 2023-01-05
