utils = [
    'mongodb'
]

def post(req, api):
    """
    Get a course by id/name

    Input:
        id: string

    Output:
        error: boolean
        course: Object
    """
    name = None

    if 'name' in req.params:
        name = req.params['name']
    else:
        id = api.mongodb.toObjectId(req.params["id"])

    error = None

    try:
        if not name:
            result = api.mongodb.select(api, 'courses', {'_id': id})
        else:
            result = api.mongodb.select(api, 'courses', {'name': name})
    except Exception as e:
        error = e

    if not error:
        req.send({
            'error': False,
            'course': str(result.next())
        })
    else:
        return {
            'error': True,
            'message': str(error)
        }
