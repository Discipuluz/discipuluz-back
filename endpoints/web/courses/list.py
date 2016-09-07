utils = [
    'mongodb'
]

def get(req, api):
    """
    List all courses

    Input: None

    Output:
        error: boolean
        courses: [Object]
    """

    error = None
    courses = []

    try:
        for u in api.mongodb.select(api, 'courses'):
            courses.append(u) 
    except Exception as e:
        error = e

    if not error:
        req.send({
            'error': False,
            'courses': str(courses)
        })
    else:
        req.send({
            'error': True,
            'message': str(error)
        })