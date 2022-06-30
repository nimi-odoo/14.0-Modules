# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductList(models.Model):
    _name = "product.list"
    _description = "List of products"

    name = fields.Char(required=True)
    tag_ids = fields.Many2many(comodel_name="product.list.tag")
    product_ids = fields.Many2many(comodel_name="product.template")
    customer_ids = fields.One2many(comodel_name="res.partner", inverse_name="product_list_id")
    # customer_ids = fields.Many2many(comodel_name="res.partner")

    # @api.onchange("product_ids")
    # def onchange_product_ids(self):
    #     all_product_ids = self.env["product.template"].search([])
    #     print ('\n\n\n',self.env.user)
    #     for record in self:
    #         print(record.name)
    #         # for id in record.product_ids: print(id.name)
    #         product_ids_names = [p.name for p in record.product_ids]
    #         print(product_ids_names)
    #         # for name in product_ids_names: print(name, len(name))

    #         print("\n")
    #         for product in all_product_ids: print(product.name, len(product.name))
    #         print ("\n")

    #         for product in all_product_ids:
    #             product.is_published = True
                # print (f"checking {product.name}")
                # if product.name not in product_ids_names:
                #     product.is_published = False
                #     print(product.name, product.is_published)
                # else:
                #     product.is_published = True
                #     print(product.name, product.is_published)
        # print ('\n\n\n')
