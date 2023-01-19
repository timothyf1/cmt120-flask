# CMT120 Fundamentals of Programming CW2

Username - d1323632

Openshift - [https://d1323632-cmt120-cw2.apps.openshift.cs.cf.ac.uk/](https://d1323632-cmt120-cw2.apps.openshift.cs.cf.ac.uk/)

## Creating the portfolio

### Environment variables

The following environment variables are used and **MUST** be configured.

- SECRET_KEY
- SQLALCHEMY_DATABASE_URI

### Creating the db

Run the python script `create_db.py` will create the database structure and add some sample data to the database.

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
