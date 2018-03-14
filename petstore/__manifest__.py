{
    'name' : 'OpenERP Pet Store',
    'version': '1.0',
    'summary': 'Sell pet toys',
    'category': 'Tools',
    'description':
        """
OpenERP Pet Store
=================

A wonderful application to sell pet toys.
        """,
    'data': [
        'views/view.xml',
        "demo/petstore_data.xml",
        "oepetstore.message_of_the_day.csv"
    ],
    'depends' : ['sale_stock'],
    'qweb': ['static/src/xml/*.xml'],
    'application': True,
    'installable': True,
    'auto_install': False,
}
