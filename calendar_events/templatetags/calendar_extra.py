from django.template.defaulttags import register

@register.filter(name='get_item_2')
def get_item_2(dictionary, key):
	return dictionary.get(key)