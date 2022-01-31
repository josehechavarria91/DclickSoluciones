{
    'name': "Gamma partners",

    'summary': """
        Working with gamma partners""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Jose E Hechavarría Rondon",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'product',
                'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/suppliers_report_view.xml',
        'views/views.xml',
        'report/suppliers.xml',
        'report/report_suppliers_more_than_five.xml',
        'report/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
# -*- coding: utf-8 -*-



