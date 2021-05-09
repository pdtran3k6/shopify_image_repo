# Shopify Image Repository

An image repository that allows users to upload photos.

Feature:
--------
- User authentication
- Upload one / many photos at a time
- Private repo (only you can see what you upload)
- Security check to prevent malicious file upload

Requirements
------------
Python >= 3.5 and Flask 1.1.1 (`pip install flask`)

Start
-----
Clone the project
```
$ git clone https://github.com/pdtran3k6/shopify_image_repo.git
```
Setting up database for user (make sure that you're outside of the project's folder)
```
$ python3
>>> from shopify_image_repo import db, app
>>> db.create_all(app=app)
```
Inside the project folder, set up configuration and run the app
```
$ export FLASK_APP=.
$ export FLASK_ENV=development
$ flask run
```
Visit `localhost:5000` on your browser to see the app
