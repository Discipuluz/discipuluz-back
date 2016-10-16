utils = [
    'mongodb'
]

def post(req, api):
    """
    Save contact to database and send an email

    Input:
        name: string
        email: string
        comment: string

    Output:
        response:
            error: boolean
            message: string
    """

    name = req.params['name']
    email = req.params['email']
    message = req.params['message']

    index = None
    error = None

    try:
        index = api.mongodb.insert(api, 'Contacts', {
            'name': name,
            'email': email,
            'message': message
        })
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