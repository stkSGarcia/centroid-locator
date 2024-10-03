import pymysql
import os

_connection = None

def init_connection(config):
    # 1. 链接数据库， 得到一个对象
    global _connection
    try:
        _connection = pymysql.connect(host=config["host"],
                                      port=config["port"],
                                      user=config["user"],
                                      password=config["password"],
                                      database=config["database"],
                                      charset="utf8")
    # except Ellipsis as e:
    except Exception as e:
        print(e)
        os._exit(0)   # 如果第一步的链接失败，下面的所有代码都不用走，直接退出

def queryall(sql):
    """负责查询功能"""
    with _connection.cursor() as cursor:
        #3 执行SQL语句
        cursor.execute(sql)
        #4.获取查询结果
        result = cursor.fetchall()
    return result    #将结果返回


def queryone(sql):
    """负责查询功能"""
    with _connection.cursor() as cursor:
        #3 执行SQL语句
        cursor.execute(sql)
        #4.获取查询结果
        result = cursor.fetchone()
    return result    #将结果返回

def update(sql):
    """负责更行功能"""
    with _connection.cursor() as cursor:
    # 3 利用游标对象执行SQL语句
        cursor.execute(sql)
    
    #4.提交 如果不进行提交，所有的改变(insert, delete, update)不会生效
    _connection.commit()
    print("更新成功！")

def close_database():
    _connection.close()

