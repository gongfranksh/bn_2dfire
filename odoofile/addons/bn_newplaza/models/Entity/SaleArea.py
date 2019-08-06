# -*- coding: utf-8 -*-
from .BnEntity import BnEntity



class SaleArea(BnEntity):

    def __init__(self):
        BnEntity.__init__(self)

    def get_all(self):
        sql ="""
         select strSaleAreaID,strsaleareaname from Pm_SaleArea
        
        """
        rst = self.get_remote_result_by_sql(sql)
        return rst

