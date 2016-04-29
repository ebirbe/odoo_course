from openerp import fields, models

'''
Model class for Course
'''

class Course(models.Model):
   '''
   This class contains all data of a Course
   '''
   _name = 'openacademy.course'

   name = fields.Char(String='Title', requiered=True)
   description = fields.Text(string='Description')
