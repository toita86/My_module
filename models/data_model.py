from datetime import datetime, timedelta
from odoo import api, models, fields, exceptions
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_compare


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
    choises_selection = fields.Selection(
        required = True,
        copy = False,
        selection = [
                ('option 1','Option 1'),
                ('option 2', 'Option 2'),
                ('option 3','Option 3'),
                ('option 4', 'Option 4'),
            ],
        string = 'List of Choises',
        default = 'option 1'
    )
    active_property = fields.Boolean(default = True)
    selling_price = fields.Float(required=True, copy = False)
    #Buttons
    status = fields.Selection(
        selection = [
                ('new','New'),
                ('sold', 'Sold'),
                ('canceled','Canceled'),
            ],
        string = 'staus',
        default = 'new'
    )
    def action_sold(self):
        for record in self:
            if record.status == "canceled":
                raise exceptions.AccessDenied(message='Cancelled entries cannot be sold')
            record.status = "sold"
        return True
    def action_canceled(self):
        for record in self:
            record.status = "canceled"
        return True
    #Relations
    entrie_tag_ids = fields.Many2many('tag_model')
    entrie_type_id = fields.Many2one('type_model', string="Entrie type")
    buyer_id = fields.Many2one('res.users', string="buyer", copy=False)
    salesman_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    offers_ids = fields.One2many('offers_model','property_id', string = "Offers")
    #compute
    simple_integer = fields.Integer(default = 50)
    simple_integer_2 = fields.Integer(default = 150)
    total_computation = fields.Float(compute = "_compute_total")

    @api.depends("simple_integer", "simple_integer_2")
    def _compute_total(self):
        for record in self:
            record.total_computation = record.simple_integer + record.simple_integer_2

    best_offer = fields.Float(compute="_compute_offers")

    @api.depends("offers_ids.price")
    def _compute_offers(self):
        for record in self:
            max_offer = self.env['offers_model'].search([], order='price desc', limit=1)
            if max_offer.price:
                record._check_best_offer()
                record.best_offer = max_offer.price
            else:
                record.best_offer = 0.0

    onchange_check_box = fields.Boolean()
    onchange_integer = fields.Integer()
    onchange_selection = fields.Selection(
        selection = [
                ('red','Red'),
                ('blue', 'Blue'),
                ('green','Green'),
                ('magenta', 'Magenta'),
            ],
        string = 'List of colors',
    )

    @api.onchange("onchange_check_box")
    def _onchange_check_box(self):
        if self.onchange_check_box is True:
            self.onchange_integer = 10
            self.onchange_selection = 'green'
        else:
            self.onchange_integer = 0
            self.onchange_selection = ''
    #Costraint
    _sql_constraints = [
        ('check_simple_integer',
        'CHECK(simple_integer > 0)',
        'This integer must be better than 0')
        ]

    @api.constrains('best_offer', 'selling_price')
    def _check_best_offer(self):
        for record in self:
            expected_price_90_percent = record.selling_price*(90/100)
            compare_results = float_compare(record.best_offer, expected_price_90_percent, precision_digits=2)
            if compare_results < 0:
                raise ValidationError("The offer can't be lower then 90% of the selling price")
