import logging
import sqlite3

import pymysql

from app.config import CONFIG

logger = logging.getLogger(__name__)


class Database:
    def __init__(self):
        config = CONFIG["database"]
        if config["sqlite"]:
            self._connection = sqlite3.connect(config["sqlite"])
        else:
            for _ in range(config["retry"]):
                try:
                    self._connection = pymysql.connect(host=config["host"],
                                                       port=config["port"],
                                                       user=config["user"],
                                                       password=config["password"],
                                                       database=config["database"],
                                                       charset="utf8")
                    break
                except Exception as e:
                    logger.error(f"Cannot connect to database: {e}.")

    def queryall(self, sql):
        """负责查询功能"""
        with self._connection.cursor() as cursor:
            cursor.execute(sql)  # 执行SQL语句
            return cursor.fetchall()  # 获取查询结果, 将结果返回

    def queryone(self, sql):
        """负责查询功能"""
        with self._connection.cursor() as cursor:
            cursor.execute(sql)  # 执行SQL语句
            return cursor.fetchone()  # 获取查询结果, 将结果返回

    def update(self, sql):
        """负责更行功能"""
        with self._connection.cursor() as cursor:
            cursor.execute(sql)  # 利用游标对象执行SQL语句
        self._connection.commit()  # 提交 如果不进行提交，所有的改变(insert, delete, update)不会生效
        logger.info("更新成功！")

    def __del__(self):
        self._connection.close()
