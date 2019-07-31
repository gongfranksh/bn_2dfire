# -*- coding: utf-8 -*-
from odoofile.addons.bn_newplaza.models.Entity.BnEntity import BnEntity


class ResourceType(BnEntity):

    def __init__(self):
        BnEntity.__init__(self)

    def get_all(self):
        sql ="""
          select strenumid,stritemname,lngItemValue,stritemcode 
          from pm_enum where lngEnumTypeID=3 and isnull(isStop,0)=0
        
        """
        rst = self.get_remote_result_by_sql(sql)
        return rst

