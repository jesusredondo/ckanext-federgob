import ckan.plugins as p


class federgobPlugin(p.SingletonPlugin):
	p.implements(p.IAuthFunctions, inherit=True)
	p.implements(p.IConfigurer)
	def update_config(self, config):
		p.toolkit.add_template_directory(config, 'templates')
		p.toolkit.add_public_directory(config, 'public')