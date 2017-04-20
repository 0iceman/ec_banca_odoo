# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, date

from odoo import models, fields, api 

class fin_cuentas(models.Model):

    _name = 'fin.cuentas'

    name = fields.Char("Cuenta")
    active = fields.Boolean("Activa")
    tipo_cuenta = fields.Selection([(1,"Ahorros"),(2,"Corriente"),(3,"Credito Consumo"),(4,"Credito Hipotecario"),(5,"Credito emergente"),(6,"Certificado de Aportacion"),(7,"Horros a plazo fijo")])
    fecha_apertura = fields.Date("Fecha Apertura", required=True)
    fecha_cierre = fields.Date("Fecha Cierre")
    cuenta_id = fields.Many2one('res.partner', string="Socio", index=True)
    account_debe_id = fields.Many2one('account.account', string="Cuenta debe", index=True)
    account_haber_id = fields.Many2one('account.account', string="Cuenta haber", index=True)
    #lugar_apertura = fields.Char("Lugar apertura", required=True)
    debe = fields.Float("Debe", digits=(6, 2), help="Duration in days")
    haber = fields.Float("Haber", digits=(6, 2), help="Duration in days")

class fin_adjuntos(models.Model):

    _name = 'fin.adjuntos'

    name = fields.Char("Documento")
    active = fields.Boolean("Activa")
    tipo_adjunto = fields.Selection([(1,"Cedula"),(2,"Pasaporte"),(3,"Licencia de conducir"),(4,"Titulo"),(5,"Hoja de vida"),(6,"Certificados"),(7,"otros")])
    fecha_regitro = fields.Date("Fecha regitro", required=True)
    partner_id = fields.Many2one('res.partner', string="Socio", index=True)
    image_doc = fields.Binary("Adjunto", attachment=True,
        help="Medium-sized logo of the brand. It is automatically "
             "Use this field in form views or some kanban views.")
    image_doc_filename = fields.Char("Documento")




class fin_tipo_relacion(models.Model):

    _name = 'fin.tipo.relacion'

    name = fields.Char("Relacion")
    active = fields.Boolean("Activa")
    tipo_relacion = fields.Selection([(1,"Familiar"),(2,"Laboral"),(3,"Garante"),(4,"Conyugue"),(5,"Amistades")])
    fecha_apertura = fields.Date("Fecha Apertura", required=True)
    partner_id = fields.Many2many('res.partner', string="Partner")
    account_haber_id = fields.Many2one('account.account', string="Cuenta haber", index=True)
    #lugar_apertura = fields.Char("Lugar apertura", required=True)
    debe = fields.Float("Debe", digits=(6, 2), help="Duration in days")
    haber = fields.Float("Haber", digits=(6, 2), help="Duration in days")




class fin_socios(models.Model):

    _inherit = 'res.partner'

    edad = fields.Integer("Edad")
    socio = fields.Boolean("Socios", default=True)
    fecha_activacion = fields.Date("Fecha Activacion", required=True)
    fecha_nacimiento = fields.Date("Fecha Nacimiento", required=True)
    lugar_nacimiento = fields.Char("Lugar Nacimiento", required=True)
    genero = fields.Selection([('F', "Femenino"),('M', "Masculino")], string='Genero', store=True,
        help='Genero de socio', required = True)
    pregunta_secreta = fields.Char("Pregunta Secreta")
    respuesta_secreta = fields.Char("Respuesta Secreta")
    image_firma = fields.Binary("Firma", attachment=True,
        help="Medium-sized logo of the brand. It is automatically "
             "Use this field in form views or some kanban views.")
    cuenta_ids = fields.One2many('fin.cuentas', 'cuenta_id', string="Cuentas")
    adjunto_ids = fields.One2many('fin.adjuntos', 'partner_id', string="Adjuntos")
    relacion_id = fields.Many2many('fin.tipo.relacion', string="Relacion")
    
@api.onchange('fecha_nacimiento')
def _onchange_fecha_nac(self,fecha_nacimiento):
    # set auto-changing field
   #! edad = datetime.now().date() - datetime.strptime(self.fecha_nacimiento, '%Y-%m-%d').date()).days / 365
    edad = 17
  #  self.update(values)
    return {'value':{'edad' : edad}}
    # Can optionally return a warning and domains
   


@api.constrains('edad')
def _check_something(self):
    for record in self:
        if record.edad <= 18:
            raise ValidationError("Registro un menos de edad debe validar el documento habilitante, edad: %s" % record.edad)
    # all records passed the test, don't return anything

