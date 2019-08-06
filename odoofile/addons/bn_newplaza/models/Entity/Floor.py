# -*- coding: utf-8 -*-
from .BnEntity import BnEntity


class Floor(BnEntity):

    def __init__(self):
        BnEntity.__init__(self)

    def get_floor_all(self):
        sql ="""
          select strenumid,stritemname,lngItemValue,stritemcode 
          from Pm_Enum where lngenumtypeid=7
        
        """
        rst = self.get_remote_result_by_sql(sql)
        return rst

