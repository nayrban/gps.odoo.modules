from odoo import api, fields, models
from datetime import datetime


class message_of_the_day(models.Model):
    _name = "oepetstore.message_of_the_day"

    @api.model
    def my_method(self):
        return {"hello": "world"}

    message = fields.Text()
    color = fields.Char(size=20)


class product(models.Model):
    _inherit = "product.product"

    max_quantity = fields.Float(string="Maximum Quantity")

class PetModel(models.Model):
    _name = "pet.model"

    @api.depends('dob')
    def calculate_age(self):
        """ Description:- This method calculates the age on the basis of the
        Birth Date entered in the 'dob' field. """
        for data in self:
            if data.dob:
                current_year = datetime.now().year
                birth_year = datetime.strptime(data.dob, "%Y-%m-%d").year
                age = current_year - birth_year
                data.age = age
    # Basic Fields
    client_id = fields.Many2one('client.model', 'Client', required=True)
    name = fields.Char('Name')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    age = fields.Float(compute=calculate_age, string='Age')
    dob = fields.Date('Date of Birth')
    breed = fields.Char('Breed')
    pet_image = fields.Binary("Image", attachment=True, help="This field holds the image used as avatar for this contact, limited to 1024x1024px",)


class ClientModel(models.Model):
    _name = "client.model"
    _rec_name = "firstName"

    @api.depends('dob')
    def calculate_age(self):
        """ Description:- This method calculates the age on the basis of the
        Birth Date entered in the 'dob' field. """
        for data in self:
            if data.dob:
                current_year = datetime.now().year
                birth_year = datetime.strptime(data.dob, "%Y-%m-%d").year
                age = current_year - birth_year
                data.age = age

    # Basic Fields
    pet_model_ids = fields.One2many('pet.model', 'client_id',
                                   string='Pet'),
    firstName = fields.Char("First Name")
    lastName = fields.Char("Last Name")
    age = fields.Float(compute=calculate_age, string='Age')
    dob = fields.Date('Date of Birth')
    grade = fields.Selection([("sr", "Sr."), ("Mr", "Mr.")], string="Grade")
    city = fields.Char("City")
    state = fields.Char("State")
    image = fields.Binary("Image", attachment=True, help="This field holds the image used as avatar for this contact, limited to 1024x1024px",)
