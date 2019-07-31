# -*- coding: utf-8 -*-
from odoofile.addons.bn_newplaza.models.Entity.Floor import Floor
from odoofile.addons.bn_newplaza.models.Entity.Plan import Plan
from odoofile.addons.bn_newplaza.models.Entity.ResourceType import ResourceType
from odoofile.addons.bn_newplaza.models.Entity.RptFloorPlan import RptFloorPlan
from odoofile.addons.bn_newplaza.models.Entity.SaleArea import SaleArea
from odoofile.addons.bn_newplaza.models.Entity.Shops import Shops
from odoofile.addons.bn_newplaza.models.bn_decorator import bnfunlog


@bnfunlog('')
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


@bnfunlog('')
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

@bnfunlog('')
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

@bnfunlog('')
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


@bnfunlog('')
def proc_sync_pmplan(self):
    rst=self.env['bn.rptfloorplan'].get_need_sync_pm_plan()
    if rst is not None:
        task_plan=Plan()
        plans=task_plan.get_all(rst)
        i = 0
        for plan in plans:
            print('pmplan==>current:' + str(i) + '-/-total:' + str(len(plans)))
            shopid = self.env['res.company'].query(plan['lngshopid']).id
            floorid = self.env['bn.floor'].query_by_value(plan['lngfloor']).id
            code=plan['strplanid']
            res={
               'code' :code,
               'name' :plan['strresourcename'],
               'decQuantity' :plan['decquantity'],
               'decSimpleShopPrice' :plan['decsimpleshopprice'],
               'lngPlanTypeId' :plan['lngresourcetype'],
               'blnIsCancel' :plan['blniscancel'],
               'strDescription' :plan['strresourcename'],
               'lngfloor' :plan['lngfloor'],
               'dtActiveDate' :plan['dtactivedate'],
               'dtCancleDate' :plan['dtCancelDate'],
               'shopid' :shopid,
               'floorid' :floorid,
            }
            rst=self.env['bn.pmplan'].query_by_id(code)
            if rst is  None:
                nplan=self.env['bn.pmplan'].create(res).id
                query="""
                  update bn_rptfloorplan  set plan_id={0} where plan_strid='{1}'
                """
                query=query.format(nplan,code)
                self.env.cr.execute(query)
            i+=1


@bnfunlog('')
def proc_sync_floorplan_data(self):
    rpt1=RptFloorPlan()
    reports= rpt1.get_all(self.dtDate)
    i=0
    for line in reports:
        print('floorplan_data==>current:'+str(i)+'-/-total:'+str(len(reports)))
        shopid=self.env['res.company'].query(line['lngshopid']).id
        floorid=self.env['bn.floor'].query_by_id(line['strFloor']).id
        resource_type_id=self.env['bn.resourcetype'].query_by_id(line['lngResourceType']).id

        plan_tmp=self.env['bn.pmplan'].query_by_id(line['strPlanID'])
        if plan_tmp is None :
            plan_id=None
        else:
            plan_id=plan_tmp.id

        res={
            'dtDate':self.dtDate,
            'lngshopid': line['lngshopid'],
            'strfloor': line['strFloor'],
            'strresourcetype':  line['lngResourceType'],
            'decQuantity':  line['decAreaQuantity'],
            'plan_shopprice':  line['plan_shopprice'],
            'rent_shopprice':  line['rent_shopprice'],
            'real_factprice':  line['decRealFactPrice'],
            'ar_balance':  line['decArBalance'],
            'plan_strid':  line['strPlanID'],
            'resource_code':  line['strResourceCode'],
            'contract_id':  line['strContractID'],
            'business_id':  line['strBusinessID'],
            'shop_id':  shopid,
            'floor_id': floorid,
            'resource_type_id':  resource_type_id,
            'plan_id':  plan_id,
        }
        self.env['bn.rptfloorplan'].create(res)
        i+=1
    return True
