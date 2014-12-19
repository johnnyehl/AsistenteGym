
#backend : desde donde me estoy logeando desde que red social
#strategy : 
#details : trae el nombre y apellido, los detalles del user que se loguea
#response : toda la informacion de la red social (relacion, donde estudiastes, etc)
def get_avatar(backend, strategy, details, response, user=None,
		 *args, **kwargs):

	url = None
	if backend.name == 'facebook':
		url = "http://graph.facebook.com/%s/picture?=large"%response['id']
	if backend.name == 'twitter':
		url = response.get('profile_image_url', '').replace('_normal', '')
	if url:
		user.avatar = url
		user.save()
	