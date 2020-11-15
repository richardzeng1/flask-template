from flask import Flask, Response
from flask_mongoengine import MongoEngine
from database.db import initialize_db
from resources.example import example
from flask_bcrypt import Bcrypt
import os

# Google auth
from authlib.integrations.requests_client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery
import google_auth # local file

app = Flask(__name__)

# app.config['MONGODB_SETTINGS'] = {
#     'host': 'mongodb://richard:richardtest01@ds361998.mlab.com:61998/dev-budget-tracker',
#     'retryWrites':'false'
# }

initialize_db(app)
app.register_blueprint(example)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)

# app.register_blueprint(google_auth.app)

bcrypt = Bcrypt(app)

# @app.before_request
# def before_request_func():
#     if not (google_auth.is_logged_in()):
#         return Response("Forbidden", mimetype="application/json", status=403)

if __name__ == "__main__":
    app.run()
