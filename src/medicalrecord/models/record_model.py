from odoo import api, fields, models


class RecordModel(models.Model):
    _name = 'record.model'

    name = fields.Char(string='Name')