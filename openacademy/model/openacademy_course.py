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
   responsible_id = fields.Many2one('res.users', ondelete='set null',
       string='Responsible', index=True)

   session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")

