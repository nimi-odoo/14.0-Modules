# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # product_list_id = fields.Many2
    # product_list_id = fields.Many2many(comodel_name="product.list")
    # customer_ids = fields.One2many(related="product_list_id.customer_ids")

    # check if the product is in the company environments product list??
    
    # @api.onchange("product_list_id")
    # def set_is_published(self):
    #     print ('\n\n\n')
    #     for record in self:
    #         print(record)
    #     print ('\n\n\n')
