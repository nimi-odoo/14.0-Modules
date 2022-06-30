# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website_sale.controllers.main import TableCompute

class WebsiteSaleInherit(WebsiteSale):
    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
    def shop(self, page=0, category=None, search='', ppg=False, **post):

        res = super(WebsiteSaleInherit, self).shop()
        all_products = res.qcontext.get("products")

        attributes = res.qcontext.get("attributes")
        print(type(attributes))
        # attrs = dict(attributes)
        # attrs.update({"visibility": False})
        # print(attrs)

        # print(attributes["visibility"])
        # attributes.update({"visibility":False})
        print("Attributes")
        print(attributes)
        for k in attributes:
            print(k.name)

        # for rec in all_products:
        #     if rec.name not in product_list:
        #         rec.attributes.update({}) = "warranty."
                # ('visibility', '=', 'visible'),

        print("\n\nAll Products\n") 
        for p in all_products: print(p.name)
        print('\n')

        current_user = request.env['res.users'].browse(request.uid).partner_id
        print("Current user: ", current_user.name)
        product_list = current_user.product_list_id
        print("product list? ",product_list.product_ids)
        for p in product_list.product_ids:
            print(p.name)
        print('\n')

        if product_list:
            res.qcontext.update({"products": list(product_list.product_ids)})
            res.qcontext.update({"bins": TableCompute().process(
                res.qcontext.get("products"), 
                res.qcontext.get("ppg"),
                res.qcontext.get("ppr")
            )})

            print("updated\n")
            new_all_products = res.qcontext.get("products")
            print (f"type: {type(new_all_products)}")
            for p in new_all_products: print(p.name)

        bins = res.qcontext.get("bins")
        # print('\n')
        # for b in bins: print(b)
        # res.qcontext.update({"bins":[]})
        print("\n\n",bins)

        for outer in res.qcontext.get("bins"):
            for inner in outer:
                if inner.get("product") not in product_list.product_ids:
                    print("nope")
                    inner=[]
                else:
                    print("nice!")




        # print("\nres:\n", res.qcontext.get("products"))
        print("\nres: ", res.qcontext)
        # print(res.qcontext.get("bins"))

        return res


        res = super(WebsiteSaleInherit,self)._get_search_domain(search, category, attrib_values, search_in_description=True)
        print(res)

# class WebsiteSaleInherit(WebsiteSale):
#     @http.route([
#         '''/shop''',
#         '''/shop/page/<int:page>''',
#         '''/shop/category/<model("product.public.category"):category>''',
#         '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
#     ], type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
#     def shop(self, page=0, category=None, search='', ppg=False, **post):

#         return super(WebsiteSaleInherit, self).shop()