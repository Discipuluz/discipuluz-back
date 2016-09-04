utils = [
    'mongodb'
]

def post(req, api):
    """
    Input:
        answers: [int]

    Output:
        response:
            error: boolean
            session: string
    """

    answers = req.params["answers"]
    results = [0 for x in range(6)]

    error = None

    for i in range(0, 6):
        for j in range(i, 78, 6):
            results[i] += answers[j]
    
    try:
        index = api.mongodb.insert(api, 'holland_answers',{
            'answers': results
        })
    except Exception as e:
        error = e
        
    if not error:
        req.send({
            'error': False,
            'session': str(index)
        })
    else:
        req.send({
            'error': True,
            'message': str(error)
        })
