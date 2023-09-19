from datetime import datetime, timedelta
from odoo import models, fields


class TestModel(models.Model):
    _name = "test_model"
    _description = "Test Model"

    name = fields.Char(required=True, default = "Unknown")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        copy = False,
        default=lambda self:(datetime.now() + timedelta(days=90)).date()
    )
    check_box = fields.Boolean(default = False)
    simple_integer = fields.Integer(default = 50)
    choises_selecction = fields.Selection(
        required = True,
        copy = False,
        selection = [
                ('option 1','Option 1'),
                ('option 2', 'Option 2'),
                ('option 3','Option 3'),
                ('option 4', 'Option 4'),
            ],
        string = 'List of Choises',
        default = 'option1'
    )
    active_property = fields.Boolean(default = True)
    selling_price = fields.Float(required=True, readonly = True, copy = False)
