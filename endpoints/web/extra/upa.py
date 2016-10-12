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

    index = None
    error = None

    print(req.params)

    try:
        index = api.mongodb.insert(api, 'Upa', req.params)
    except Exception as e:
        error = e

    if index:
        return {
            'error': False
        }
    else:
        return {
            'error': True,
            'message': str(error)
        }
