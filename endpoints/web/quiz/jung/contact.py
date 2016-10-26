utils = [
    'mongodb'
]

def post(req, api):
    """
    Save user contact

    Input:
        name: string
        school: string
        grade: string
        email: string
        session: string

    Output:
        response:
            error: boolean
            session: string
    """

    name = req.params["name"]
    school = req.params["school"]
    grade = req.params["grade"]
    email = req.params["email"]
    session = api.mongodb.toObjectId(req.params["session"])

    error = None

    try:
        index = api.mongodb.update(api, 'jung_answers', {'_id': session},{
            'name': name,
            'school': school,
            'grade': grade,
            'email': email,
        })
    except Exception as e:
        error = e

    if not error:
        return {
            'error': False,
            'session': str(index)
        }
    else:
        return {
            'error': True,
            'message': str(error)
        }
