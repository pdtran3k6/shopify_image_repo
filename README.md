# Shopify Image Repository

An image repository that allows users to upload photos.

Feature:
--------
- Upload one / many photos at a time
- Private repo (only you can see what you upload)
- Security check to prevent malicious file upload

Requirements
------------
Python 3.7.4 and Flask 1.1.1 (`pip install flask`)


Start
-----
Setting up database for user
```
// go outside the project's folder, activate Python REPL
>>> from image_repo import db, app
>>> db.create_all(app)
```
Set up configuration and run the app
```
$ export FLASK_APP=.
$ export FLASK_ENV=development
$ flask run
```
Visit `localhost:5000` on your browser to see the app
