from odoo import models, fields
import logging
_logger = logging.getLogger("RAMAERA")


class PurchaseOrder(models.Model):
    _inherit = 'purchase.report'
    user_id = fields.Many2one('res.users', 'Purchase Representative', readonly=True)

    _logger.debug('==------------',user_id)
