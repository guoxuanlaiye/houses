# import pymysql
# from pymysql import DatabaseError
#
# conn = pymysql.connect("localhost", "root", "", "houses", use_unicode=True, charset="utf8")
# cursor = conn.cursor()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    Column,
    Integer,
    String
)

class Sql(object):

    engine = create_engine('mysql://root:@localhost:3306/houses?charset=utf8', encoding='utf8', echo=False)
    BaseDB = declarative_base()
    # session对象
    DBSession = sessionmaker(bind=engine)

    # 初始化数据库
    @classmethod
    def initDB(cls):
        cls.BaseDB.metadata.create_all(cls.engine)


'''
houses_name
houses_adress
average_price
around_ava_price
price_status
tags
houses_type
houses_area
'''
class Houses(Sql.BaseDB):
    __tablename__ = "anjuke_wuhan"

    id = Column(Integer, primary_key=True)
    houses_name = Column(String(50), nullable=False)
    houses_adress = Column(String(50), nullable=False)
    average_price = Column(Integer, nullable=True)
    around_ava_price = Column(Integer, nullable=True)
    price_status = Column(String(10), nullable=False)
    tags = Column(String(50), nullable=False)
    houses_type = Column(String(30), nullable=True)
    houses_area = Column(String(20), nullable=False)

    def __init__(self, houses_name, houses_adress, average_price, around_ava_price, price_status, tags, houses_type, houses_area):
        self.houses_name = houses_name
        self.houses_adress = houses_adress
        self.average_price = average_price
        self.around_ava_price = around_ava_price
        self.price_status = price_status
        self.tags = tags
        self.houses_type = houses_type
        self.houses_area = houses_area








