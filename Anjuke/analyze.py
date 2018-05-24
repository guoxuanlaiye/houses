from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    Column,
    Integer,
    String
)
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from itertools import groupby


class Sql(object):

    engine = create_engine('mysql://root:@localhost:3306/houses?charset=utf8', encoding='utf8', echo=False)
    # Base
    BaseDB = declarative_base()
    # session对象
    DBSession = sessionmaker(bind=engine)
    # 初始化数据库
    @classmethod
    def initDB(cls):
        cls.BaseDB.metadata.create_all(cls.engine)


class Houses(Sql.BaseDB):
    __tablename__ = "anjuke_chengdu"

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



def main():
    sql = Sql()
    session = sql.DBSession()
    # 返回list每个元素是个元组
    houses_price_list = session.query(Houses, Houses.average_price).filter(Houses.average_price > 5000).all()
    session.close()
    # print(type(houses_price_list))
    print(len(houses_price_list))
    prices = [price for item, price in houses_price_list]
    draw(city="chengdu", data=prices)


def draw(city, data):
    if not isinstance(data, list):
        return
    # 设置文字格式
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    # 排序
    data.sort()

    yticks = []
    x_display = []
    for k, g in groupby(data, key=lambda x: x//5000):
        count = len(list(g))
        x_display.append("%d-%d" % ((k*5000)/1000, ((k+1)*5000)/1000))
        yticks.append(count)
        # print("%s-%s:%s" % (k*5000, (k+1)*5000-1, count))

    xticks = range(len(x_display))
    print(yticks)

    plt.ylim(0, 400)
    plt.bar(x=range(len(yticks)), height=yticks, width=0.6, color="blue", label=city)

    plt.xlabel('价格(k)')
    plt.ylabel('总数(个)')
    plt.xticks(xticks, x_display)

    for x, y in zip(xticks, yticks):
        plt.text(x, y, y, ha='center', va='bottom')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()