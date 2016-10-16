utils = [
    'mongodb'
]

def post(req, api):
    """
    List all courses / courses by university

    Input:
        university: string

    Output:
        error: booleanin req.params:
        courses: [Object]
    """

    error = None
    courses = []
    university = None

    if 'university' in req.params:
        university = req.params['university']

    try:
        for u in api.mongodb.select(api, 'courses', {'universities.name': university}):
            courses.append(u)
    except Exception as e:
        error = e

    if not error:
        return {
            'error': False,
            'courses': str(courses)
        }
    else:
        return {
            'error': True,
            'message': str(error)
        }
