# -*- coding: utf-8 -*-
import logging
import threading
import datetime

from odoo import api, models, tools, registry, exceptions
from .bn_2dfire import *

_logger = logging.getLogger(__name__)


class bn_2dfire_shops(models.Model):
    _name = 'bn.2dfire.shops'
    _description = 'bn.2dfire.shops'

    name = fields.Char(string=u'门店名称')
    code = fields.Char(string=u'门店编号')
    address = fields.Char(string=u'地址')
    entityId = fields.Char(string=u'门店entityId')
    memo = fields.Char(string=u'备注')
    isAdd = fields.Boolean(string=u'是否已经加入')

    def get_2dfire_shop_from_api(self):
        print('get_2dfire_shop_from_api')
        _logger.info('get_2dfire_product_from_api')
        MY_URL = self.env['bn.2dfire.url'].search([('code', '=', 'shoplistv20')])
        MY_APPID = self.env['bn.2dfire.appid'].search([('code', '=', 'hq-it')])

        ewh_request = bn_2dfire_connect_Request()
        MY_DATA = {
            "method": str(MY_URL['bn_2dfire_function_method']),
            "appKey": MY_APPID['bn_2dfire_app_key'],
            "v": "1.0",
            "timestamp": str(int(time.time() * 1000)),
            "lang": '',
        }

        recordset = ewh_request.get_json(MY_URL['bn_2dfire_function_api'], MY_APPID, MY_DATA)
        if recordset is not None:
            if 'data' in recordset:
                _logger.info(recordset)
                self.insert_2dfire_shops(recordset['data']['data'])

        return True

    def insert_2dfire_shops(self, recordsets):
        if (len(recordsets) == 0):
            return
        for rec in recordsets:
            print(rec)
            shop = rec['shop']
            vals = []
            vals = {
                'entityId': shop['entityId'],
                'code': shop['code'],
                'name': shop['name'],
                'memo': shop['memo'],
            }

            if 'address' in shop:
                vals['address'] = rec['shop']['address']

            c01 = self.env['bn.2dfire.shops'].search([('entityId', '=', rec['shop']['entityId'])])
            if not c01:
                self.env['bn.2dfire.shops'].create(vals)
            else:
                print(rec['shop']['entityId'], rec['shop']['name'], "Already Done")

        return True

    @api.multi
    def btn_authorized_url(self):
        action = {
                    "type": "ir.actions.act_url",
                    "url": "https://open.2dfire.com/page/auth.html#/login?appId=35468986",
                    "target": "new",
                    # "target": "self",
                 }
        return action




    @api.multi
    def btn_insert_branches(self):
            b01=self.env['bn.2dfire.branchs'].search_bycode(self.entityId)
            if not b01:
                appids = self.env['bn.2dfire.appid'].search([('code', '=', 'hq-it')]).id
                companyids = self.env.user.company_id.id

                branch_ids = self.env['bn.2dfire.branchs'].create(
                    {'code': self.entityId, 'name': self.name, 'appids': appids, 'company_id': companyids})

                action = {
                    'type': 'ir.actions.act_window',
                    'view_mode': 'form',
                    "views": [[False, "form"]],
                    'res_model': 'bn.2dfire.branchs',
                    'res_id': branch_ids.id,
                    'target': 'new',
                }

                self.write({'isAdd': True})
                return action
            else:
                raise exceptions.RedirectWarning("该门店已经加入同步列表")
