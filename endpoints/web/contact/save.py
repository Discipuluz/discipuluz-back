utils = [
    'mysql'
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
    comment = req.params['comment']

    index = None
    error = None

    try:
        index = api.mysql.insert(api, 'Contacts', {
            'name': name,
            'email': email,
            'comment': comment
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
            'message': error
        })