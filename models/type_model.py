from odoo import models, fields

class TypeModel(models.Model):
    _name = "type_model"
    _description = "Rappresents the various types of entries"
    _order = "sequence"

    name = fields.Char(required=True, default = "Unknown")
    sequence = fields.Integer('Sequence', default = 1)
