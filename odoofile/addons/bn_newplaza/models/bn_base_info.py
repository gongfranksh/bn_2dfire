# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bn_flooor(models.Model):
    _name = 'bn.flooor'
    code = fields.Char(string=u'编号', required=True)
    name = fields.Char(string=u'名称', required=True)
    lngitemvalue = fields.Integer(string=u'内部值', required=True)

class bn_resourcetype(models.Model):
    _name = 'bn.resourcetype'
    code = fields.Char(string=u'编号', required=True)
    name = fields.Char(string=u'名称', required=True)
    itemcode = fields.Char(string=u'内部编号', required=True)


class bn_salearea(models.Model):
    _name = 'bn.salearea'
    code = fields.Char(string=u'编号', required=True)
    name = fields.Char(string=u'名称', required=True)


class bn_pmplan(models.Model):
    _name = 'bn.pmplan'
    code = fields.Char(string=u'编号', required=True)
    name = fields.Char(string=u'名称', required=True)
    resourcetype = fields.Char(string=u'类型')
    salearea  = fields.Char(string=u'区域')
    decQuantity  = fields.Float(string=u'面积')
    decSimpleShopPrice = fields.Float(string=u'底价')
    lngPlanTypeId=fields.Integer(string=u'席位类型')
    blnIsCancel  = fields.Selection([('1', '作废'), ('0', '有效')], string='作废标志', default='0')
    strDescription  = fields.Char(string=u'描述')
    lngfloor  = fields.Integer(string=u'楼层')
    dtActiveDate  = fields.Datetime(string=u'激活日期')
    dtCancleDate  = fields.Datetime(string=u'取消日期')

class res_company(models.Model):
    _name = 'res.company'
    _inherit = 'res.company'
    lngshopid=fields.Integer(string='lngshopid' )
    bn_strShopName=fields.Char(string=u'店名称' )
    bn_strShortName=fields.Char(string=u'店简称' )
    bn_sign_contractor_desc=fields.Char(string=u'换约信息' )
    bn_sign_contractor_date=fields.Datetime(string=u'换约日期' )
