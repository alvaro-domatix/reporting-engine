from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    num_copies = fields.Integer(
        'Nº of copies',
        help="Number of copies to print of watermark report."
    )
