import uuid
from flask import Flask, request
from flask_smorest import abort
from db import items, stores

#### Middleware ####

#########
app = Flask(__name__)

@app.get("/store") # http://127.0.0.1:5000/store
def get_stores():
    return {"stores": list(stores.values())}