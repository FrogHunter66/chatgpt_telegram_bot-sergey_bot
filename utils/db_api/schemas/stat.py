from utils.db_api.db_gino import BaseModel
from sqlalchemy import Column, String, sql, Integer


class EverydayStats(BaseModel):
    __tablename__ = 'everyday_stats'
    date_today = Column(String, primary_key=True, nullable=False, default='2023.04.19')
    num_of_new_users = Column(Integer, default=0)
    num_of_new_requests = Column(Integer, default=0)
    num_of_new_answers = Column(Integer, default=0)
    num_of_tokens = Column(Integer, default=0)

    query: sql.select
