utils = [
    'mongodb'
]

def post(req, api):
    """
    Get an university by id

    Input:
        id: string

    Output:
        error: boolean
        university: Object
    """

    id = api.mongodb.toObjectId(req.params["id"])

    error = None

    try:
        result = api.mongodb.select(api, 'universities', {'_id': id})
    except Exception as e:
        error = e

    if not error:
        req.send({
            'error': False,
            'university': str(result.next())
        })
    else:
        req.send({
            'error': True,
            'message': str(error)
        })