# -*- coding: utf-8 -*-
from odoo import models, api
from odoofile.addons.bn_newplaza.wizards.proc_bn_newplaza_method import proc_sync_floor, proc_sync_resourcetype, \
    proc_sync_salearea, proc_sync_shop


class bn_newplaza_proc_wizard(models.TransientModel):
    _name = "bn.newplaza.proc.wizard"
    _description = "bn.newplaza.proc.wizard"

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
        pass

    @api.multi
    def sync_pm_shop_button(self):
        proc_sync_shop(self)
        pass