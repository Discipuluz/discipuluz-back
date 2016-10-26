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

    col = ["id", "name", "description", "url"]
    error = None

    try:
        result = api.mongodb.select(api, 'universities', {'_id': id}, col)
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
