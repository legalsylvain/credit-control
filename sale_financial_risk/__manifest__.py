# Copyright 2016-2020 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Sale Financial Risk",
    "summary": "Manage partner risk in sales orders",
    "version": "15.0.1.0.2",
    "category": "Sales Management",
    "license": "AGPL-3",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/credit-control",
    "depends": ["sale", "account_financial_risk"],
    "data": ["views/res_partner_view.xml", "views/sale_financial_risk_view.xml"],
    "installable": True,
    "pre_init_hook": "pre_init_hook",
}
