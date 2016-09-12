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

    if 'name' in req.params:
        name = req.params['name']
    if 'facebook' in req.params:
        facebook = req.params['facebook']
    if 'email' in req.params:
        email = req.params['email']
    if 'phone' in req.params:
        phone = req.params['phone']
    if 'course' in req.params:
        course = req.params['course']
    if 'info' in req.params:
        info = req.params['info']
    if 'message' in req.params:
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
