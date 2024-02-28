from odoo import models, fields


class RapportInterventionImage(models.Model):
    _name = 'rapport.intervention.image'
    _description = 'Image pour Rapport d\'Intervention'

    image = fields.Binary("Image", attachment=True)
    description = fields.Char("Description")


class AccountMove(models.Model):
    _inherit = 'account.move'

    intervention_date = fields.Date("Date d'Intervention (champs non visible sur le rapport")
    intervention_address = fields.Char("Adresse d'Intervention")
    type_intervention = fields.Char("Type d'Intervention")
    treatment = fields.Text("Traitement Appliqué")
    technician_observations = fields.Text("Observations du Technicien")
    recommendations = fields.Text("Recommandations")
    arrival_time = fields.Char("Heure d'Arrivée")
    departure_time = fields.Char("Heure de Départ")
    intervention_date_char = fields.Char("Date d'intervention (saisie libre)")
    confirm_nuisible = fields.Char("Confirmation des nuisibles")
    process_treatment = fields.Char("Processus du traitement")
    available_personnel = fields.Char("Personnel Présent")
    next_action = fields.Text("Actions supplémentaires des techniciens")
    other_info = fields.Text("Informations supplémentaires")
    rapport_images_ids = fields.Many2many('rapport.intervention.image', string='Images du Rapport')

    def rapport_intervention(self):
        for rec in self:
            for im in rec.rapport_images_ids:
                if not im.image:
                    raise ValueError("Merci de rajouter une image à la description %s" % im.description)
        return self.env.ref('lereflexepro.action_report_invoice_intervention').report_action(self)
