# -*- coding: utf-8 -*-
from odoo import models, fields, api


class bn_RptFloorPlan(models.Model):
    _name = 'bn.rptfloorplan'

    dtDate = fields.Date(string=u'执行日期')
    lngshopid = fields.Integer(string=u'店号')
    strfloor = fields.Char(string=u'楼层')
    strresourcetype = fields.Char(string=u'资源类型')
    decQuantity = fields.Float(string=u'面积')
    plan_shopprice = fields.Float(string=u'规划底价')
    rent_shopprice = fields.Float(string=u'合同底价')
    real_factprice = fields.Float(string=u'合同单价')
    ar_balance = fields.Float(string=u'AR')
    plan_strid = fields.Char(string=u'席位id')
    resource_code = fields.Char(string=u'席位编号')
    contract_id = fields.Char(string=u'合同id')
    business_id = fields.Char(string=u'商家id')

    shop_id = fields.Many2one('res.company', u'门店')
    floor_id = fields.Many2one('bn.floor', u'楼层')
    resource_type_id = fields.Many2one('bn.resourcetype', u'资源类型')
    plan_id = fields.Many2one('bn.pmplan', u'席位')


    @api.multi
    def get_need_sync_pm_plan(self):
        rstlist = self.env['bn.rptfloorplan'].search([('plan_id', '=',None)])
        if len(rstlist) == 0:
            return None
        else:
            rst_tmp=[]
            for rec in rstlist:
                rst_tmp.append(rec.plan_strid)
            rst=list(set(rst_tmp))
            return rst

