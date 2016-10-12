utils = [
    'mongodb'
]

def post(req, api):
    """
    Save user's feedback from Holland forms

    Input:
        session: string
        score: string
        feedback: string

    Output:
        response:
            error: boolean
            session: string
    """

    session = api.mongodb.toObjectId(req.params["session"])
    score = req.params["score"]
    feedback = req.params["feedback"]

    error = None

    try:
        index = api.mongodb.update(api, 'holland_answers', {'_id': session},{
            'score': score,
            'feedback': feedback
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
