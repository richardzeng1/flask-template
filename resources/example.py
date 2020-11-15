import json
import datetime
from flask import Blueprint, request, Response, jsonify
from database.models import TestModel

example = Blueprint('example', __name__)

@example.route('/', methods=['GET'])
def post_expense_type():
    return {'id': 1}, 200
