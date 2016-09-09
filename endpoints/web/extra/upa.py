utils = [
    'mongodb'
]

def post(req, api):
    """
    Save contact to database and send an email

    Input:
        name: string
		facebook: string
        email: string
		phone: string
		course: string
		info: string
		message: string

    Output:
        response:
            error: boolean
            message: string
    """

    name = req.params['name']
	facebook = req.params['facebook']
    email = req.params['email']
	celular = req.params['phone']
	course = req.params['course']
	info = req.params['info']
    message = req.params['message']

    index = None
    error = None

    try:
        index = api.mongodb.insert(api, 'Upa', {
            'name': name,
			'facebook': facebook,
            'email': email,
			'phone': phone,
			'course': course,
			'info': info,
            'message': message
        })
    except Exception as e:
        error = e

    if index:
        req.send({
            'error': False
        })
    else:
        req.send({
            'error': True,
            'message': str(error)
        })
