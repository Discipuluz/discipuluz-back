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

    print str(universities)

    if not error:
        req.send({
            'error': False,
            'universities': str(universities)
        })
    else:
        req.send({
            'error': True,
            'message': str(error)
        })