# -*- coding: utf-8 -*-
from odoo import models, fields, api


class bn_RptContractFile(models.Model):
    _name = 'bn.rptcontractfile'
    dtDate = fields.Date(string=u'执行日期')
    contract_vol = fields.Integer(string=u'合同数量')
    filed = fields.Integer(string=u'归档数')
    unfiled = fields.Integer(string=u'未归档数')
    change_month = fields.Char(string=u'换约月份')
    tdays = fields.Integer(string=u'30天(含)')
    t2sdays = fields.Integer(string=u'31天-60天(含)')
    stondays = fields.Integer(string=u'61天-90天(含)')
    nabove = fields.Integer(string=u'91天以上')
    shop_id = fields.Many2one('res.company', u'门店')
    plantype_id = fields.Many2one('bn.plantype', u'规划类型')




