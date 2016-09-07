utils = [
    'mongodb'
]

def post(req, api):
    """
    Get a course by id

    Input:
        id: string

    Output:
        error: boolean
        course: Object
    """

    id = api.mongodb.toObjectId(req.params["id"])

    error = None

    try:
        result = api.mongodb.select(api, 'courses', {'_id': id})
    except Exception as e:
        error = e

    if not error:
        req.send({
            'error': False,
            'course': str(result.next())
        })
    else:
        req.send({
            'error': True,
            'message': str(error)
        })