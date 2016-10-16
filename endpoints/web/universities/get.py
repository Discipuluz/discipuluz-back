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
        return {
            'error': False,
            'university': str(result)
        }
    else:
        return {
            'error': True,
            'message': str(error)
        }
