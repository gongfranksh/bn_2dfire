# -*- coding: utf-8 -*-

import json
import pymssql


# reload(sys)
# sys.setdefaultencoding("utf-8")
#
from ..Entity import db_host, db_user, db_pwd, db_dbname

class bnmssql(object):
    __pool=None

    def __init__(self):
        self.conn = bnmssql.getmssqlconn()
        self.cur = self.coon.cursor(cursor=pymssql.cursors.DictCursor)

    @classmethod
    def getmssqlconn(cls):

        if bnmssql.__pool is None:
            bnmssql.__pool=PooledDB(creator=pymssql, mincached=1, maxcached=20, host=mysqlInfo['host'], user=mysqlInfo['user'], passwd=mysqlInfo['passwd'], db=mysqlInfo['db'], port=mysqlInfo['port'], charset=mysqlInfo['charset'])


