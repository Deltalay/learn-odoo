{
	'name': "Real Estate Ads",
	'version': '0.0.1',
	'author': 'Delta',
	'category': 'Human Resources',
	'description': """
	Real estate stuff
	""",
	'installable': True,
	'application': True,
	'data': [
		'security/ir.model.access.csv',
		'views/property_view.xml',
		'views/property_type_view.xml',
		'views/property_tag_view.xml',
		'views/menu_items.xml',
		'data/property_type.xml'
	],
	"demo": [
		'demo/property_tag.xml'
	],
	"depends": ['base']
}
