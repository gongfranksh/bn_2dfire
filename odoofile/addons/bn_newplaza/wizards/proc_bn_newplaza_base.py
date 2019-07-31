# -*- coding: utf-8 -*-
from odoo import models, api, fields
from odoo.fields import Field
from odoofile.addons.bn_newplaza.wizards.proc_bn_newplaza_method import proc_sync_floor, proc_sync_resourcetype, \
    proc_sync_salearea, proc_sync_shop, proc_sync_floorplan_data, proc_sync_pmplan


class bn_newplaza_proc_wizard(models.TransientModel):
    _name = "bn.newplaza.proc.wizard"
    _description = "bn.newplaza.proc.wizard"
    dtDate = fields.Date(string=u'执行日期')

    @api.multi
    def sync_floor_plan(self):
        self.ensure_one()
        proc_sync_floorplan_data(self)


    @api.multi
    def sync_floor_button(self):
         proc_sync_floor(self)

    @api.multi
    def sync_resourcetype_button(self):
        proc_sync_resourcetype(self)
        pass

    @api.multi
    def sync_pm_salearea_button(self):
        proc_sync_salearea(self)
        pass

    @api.multi
    def sync_pm_plan_button(self):
        proc_sync_pmplan(self)

    @api.multi
    def sync_pm_shop_button(self):
        proc_sync_shop(self)
        pass

    @api.multi
    def sync_all_button(self):
        proc_sync_floor(self)
        proc_sync_resourcetype(self)
        proc_sync_salearea(self)
        proc_sync_shop(self)
        pass