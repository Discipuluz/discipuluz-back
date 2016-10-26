utils = [
    'mongodb'
]

def get(req, api):
    """
    List all universities

    Input: None

    Output:
        error: boolean
        universities: [Object]
    """

    error = None
    universities = []

    try:
        for u in api.mongodb.select(api, 'universities'):
            universities.append(u)
    except Exception as e:
        error = e

    if not error:
        return {
            'error': False,
            'universities': str(universities)
        }
    else:
        return {
            'error': True,
            'message': str(error)
        }