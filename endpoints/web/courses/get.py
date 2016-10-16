utils = [
    'mongodb'
]

def post(req, api):
    """
    Get a course by id/name

    Input:
        id: string
        col: [string]

    Output:
        error: boolean
        course: Object
    """
    name = None

    if 'name' in req.params:
        name = req.params['name']
    else:
        id = api.mongodb.toObjectId(req.params["id"])
    
    col = req.params["col"]
    error = None

    try:
        if not name:
            result = api.mongodb.select(api, 'courses', {'_id': id}, col)
        else:
            result = api.mongodb.select(api, 'courses', {'name': name}, col)
    except Exception as e:
        print(e)
        error = e

    if not error:
        return {
            'error': False,
            'course': result
        }
    else:
        return {
            'error': True,
            'message': str(error)
        }
