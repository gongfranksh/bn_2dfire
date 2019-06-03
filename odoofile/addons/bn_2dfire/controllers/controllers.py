# -*- coding: utf-8 -*-
from odoo import http

class Bn2dfire(http.Controller):
    @http.route('/bn_2dfire/bn_2dfire_onboarding_panel/',  auth='user', type='json')
    def bn_2dfire_config_obboarding(self, **kw):
        # return "Hello, world"
        company = http.request.env.user.company_id
        shops = http.request.env['bn.2dfire.shops'].search([])[0]
        # rst=shops.get_and_update_2dfire_onboarding_state()

        result = {
            'html': http.request.env.ref('bn_2dfire.bn_2dfire_config_onboarding_panel').render({
                'company': company,
                'state': shops.get_and_update_2dfire_onboarding_state()
                # 'state': ['not_done']
            })

        }
        print(result)
        return result

#     @http.route('/bn_2dfire/bn_2dfire/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bn_2dfire.listing', {
#             'root': '/bn_2dfire/bn_2dfire',
#             'objects': http.request.env['bn_2dfire.bn_2dfire'].search([]),
#         })

#     @http.route('/bn_2dfire/bn_2dfire/objects/<model("bn_2dfire.bn_2dfire"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bn_2dfire.object', {
#             'object': obj
#         })