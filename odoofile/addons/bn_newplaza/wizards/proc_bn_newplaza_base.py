from odoo import models, api
from odoofile.addons.bn_newplaza.models.Entity.Floor import Floor


class bn_newplaza_proc_wizard(models.TransientModel):
    _name = "bn.newplaza.proc.wizard"
    _description = "bn.newplaza.proc.wizard"

    @api.multi
    def sync_floor_button(self):
        np=Floor()
        floors=np.get_floor_all()
        print(floors)
        pass


    @api.multi
    def sync_resourcetype_button(self):
        pass


    @api.multi
    def sync_pm_salearea_button(self):
        pass


    @api.multi
    def sync_pm_plan_button(self):
        pass