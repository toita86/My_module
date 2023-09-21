from odoo import models, fields

class TypeModel(models.Model):
    _name = "type_model"
    _description = "Rappresents the various types of entries"

    name = fields.Char(required=True, default = "Unknown")
