# Build Multi-tenant Blog APP With Python on Google Serverless App Engine

  In this project, we have two subfolders (Backend and frontend)
  In order to run them locally, do these steps for each subfolder:

 1. `virtualenv venv`
 2. `source env/bin/activate`
 3. `pip install -r requirements.txt`
 4. `python3 main.py`

Note: all these commands are for unix based systems if you use windows, it is very similar, just go to this url: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

After having the two instances running **backend** on port **5001** and **frontend** on port **5000**, you can start exploring it.

To deploy to gcloud app engine just checkout my video and you will get it.

In order to connect to datastore locally you can use this documentation: [https://googleapis.dev/python/google-api-core/latest/auth.html](https://googleapis.dev/python/google-api-core/latest/auth.html)

To know a bit more app engine just follow this link: [https://cloud.google.com/appengine/docs/standard/python3](https://cloud.google.com/appengine/docs/standard/python3)

If you want to access the application that I just deployed to App Engine you can use the following urls:
Backend - [https://backend-dot-blog-app-edu.appspot.com/post](https://backend-dot-blog-app-edu.appspot.com/post)
Frontent - [https://frontend-dot-blog-app-edu.appspot.com/](https://frontend-dot-blog-app-edu.appspot.com/)

Any questions that you may have, just post them in the comments I will be glad to help.