from flask import Blueprint, request
from information_cpu.models import Information_cpu
from ext import db
import json

information_cpu = Blueprint('information_cpu', __name__)


@information_cpu.route('/add_information_cpu', methods=['POST'])
def add_information_cpu():
    load_cpu = json.loads(request.form['load_cpu'])
    if load_cpu:
        create_rec = Information_cpu(load_cpu)
        db.session.add(create_rec)
        db.session.commit()
        return 'success', 200
    return 'error', 500


@information_cpu.route('/get_information_cpu', methods=['GET'])
def get_information_cpu():
    data = {}
    limit = 100
    Information_cpu.get_last_limit_record(data, limit)
    Information_cpu.get_aggregated_last_limit_records(data, limit)
    Information_cpu.get_aggregated_all_records(data)
    return data
