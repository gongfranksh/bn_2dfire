# -*- coding: utf-8 -*-

from odoofile.addons.bn_newplaza.models.Entity.Floor import Floor
from odoofile.addons.bn_newplaza.models.Entity.ResourceType import ResourceType
from odoofile.addons.bn_newplaza.models.Entity.SaleArea import SaleArea
from odoofile.addons.bn_newplaza.models.Entity.Shops import Shops


def proc_sync_floor(self):
    np = Floor()
    floors = np.get_floor_all()
    for fl in floors:
        res = {'code': fl['strenumid'],
               'name': fl['stritemname'],
               'lngitemvalue':fl['lngItemValue']
                    }
        rst= self.env['bn.floor'].query(res)
        if rst is None:
            self.env['bn.floor'].create(res)
    return True

def proc_sync_resourcetype(self):
    np = ResourceType()
    resources = np.get_all()
    for rs in resources:
        res = {'code': rs['strenumid'],
               'name': rs['stritemname'],
               'itemcode':rs['lngItemValue']
                    }
        rst= self.env['bn.resourcetype'].query(res)
        if rst is None:
            self.env['bn.resourcetype'].create(res)
    return True

def proc_sync_salearea(self):
    np = SaleArea()
    salesareas = np.get_all()
    for sl in salesareas:
        res = {'code': sl['strSaleAreaID'],
               'name': sl['strsaleareaname'],
                    }
        rst= self.env['bn.salearea'].query(res)
        if rst is None:
            self.env['bn.salearea'].create(res)
    return True

def proc_sync_shop(self):
    np = Shops()
    shops = np.get_all()
    for shop in shops:
        res = {'lngshopid': shop['lngshopid'],
               'name': shop['strshopname'],
               'bn_strShopName': shop['strshopname'],
               'bn_strShortName': shop['strShortName'],
                    }
        rst= self.env['res.company'].query(shop['lngshopid'])
        if rst is None:
            self.env['res.company'].create(res)
    return True