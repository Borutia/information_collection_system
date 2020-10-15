from ext import db
from datetime import datetime
from sqlalchemy import func


class Information_cpu(db.Model):
    __tablename__ = 'information_cpu'

    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    load_cpu = db.Column(db.Float, nullable=False)

    def __init__(self, load_cpu=None):
        self.load_cpu = load_cpu

    @staticmethod
    def get_last_limit_record(data, limit):
        data_cpu = Information_cpu.query.order_by(Information_cpu.date_time.desc()).limit(limit).all()
        limit_records = []
        for counter, element in enumerate(data_cpu):
            limit_records.append({
                'id': element.id,
                'date_time': element.date_time,
                'load_cpu': element.load_cpu
            })
        data['limit_records'] = limit_records

    @staticmethod
    def get_aggregated_last_limit_records(data, limit=None):
        if limit:
            query = db.session.query(Information_cpu.load_cpu).limit(limit).subquery()
            min_cpu, max_cpu, avg_cpu = db.session.query(func.min(query.c.load_cpu),
                                                         func.max(query.c.load_cpu),
                                                         func.avg(query.c.load_cpu)).first()
            data['aggregated_last_limit_min'] = min_cpu
            data['aggregated_last_limit_max'] = max_cpu
            data['aggregated_last_limit_avg'] = round(avg_cpu, 1)

    @staticmethod
    def get_aggregated_all_records(data):
        query = db.session.query(Information_cpu.load_cpu).subquery()
        min_cpu, max_cpu, avg_cpu = db.session.query(func.min(query.c.load_cpu),
                                                     func.max(query.c.load_cpu),
                                                     func.avg(query.c.load_cpu)).first()
        data['aggregated_all_min'] = min_cpu
        data['aggregated_all_max'] = max_cpu
        data['aggregated_all_avg'] = round(avg_cpu, 1)

