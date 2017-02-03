utils = [
    'mongodb'
]

def post(req, api):
    """
    Input:
        data: [Object]

    Output:
        response:
            error: boolean
            message: string
    """

    data = req.params['data']

    error = None

    try:
        for course in data:
            index = api.mongodb.insert(api, 'courses', course)
    except Exception as e:
        error = e

    if not error:
        return {
            'error': False,
            'message': 'Added ' + str(len(data)) + ' courses in database'
        }
    else:
        return {
            'error': True,
            'message': str(error)
        }
