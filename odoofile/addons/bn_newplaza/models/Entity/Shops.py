# -*- coding: utf-8 -*-
from odoofile.addons.bn_newplaza.models.Entity.BnEntity import BnEntity


class Shops(BnEntity):

    def __init__(self):
        BnEntity.__init__(self)

    def get_all(self):
        sql ="""
             select lngshopid,strshopname,strShortName
             from Pm_Shop where isnull(blisshop,0)=1 and strshortname like '%店%'
        """
        rst = self.get_remote_result_by_sql(sql)
        return rst

