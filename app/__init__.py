from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
load_dotenv()

# initializing Flask app
app = Flask(__name__)
 

# configuration
app.config["SECRET_KEY"] = "yoursecretkey"
app.config["SQLALCHEMY_DATABASE_URI"]= os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
CORS(app)
db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views  # important to retrieve routes despite not being strictly used, must be in last line, otherwise routes will not be retrieved
