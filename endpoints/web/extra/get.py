utils = [
    'mongodb'
]

def post(req, api):
    """
    Get records from upa

    Input:

    Output:
        error: boolean
        results: [Object]
    """

    error = None

    results = []

    try:
        for record in api.mongodb.select(api, 'Upa'):
            results.append(record)
    except Exception as e:
        error = e

    if not error:
        return {
            'error': False,
            'results': str(results)
        }
    else:
        return {
            'error': True,
            'message': str(error)
        }
