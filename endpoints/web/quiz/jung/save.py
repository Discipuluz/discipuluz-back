utils = [
    'mongodb'
]

def post(req, api):
    """
    Calculate quiz result and save it into db

    Input:
        answers: [string]
    
    Output:
          response:
            error: boolean
            message: string
    """

    answers = req.params['answers']

    pos = 0
    results = [0 for x in range(8)];
    string_result = ''
    
    for i in range(0, 4):
        for j in range(i, 28, 4):
            if answers[j] == 'A':
                results[pos] += 1
            else:
                results[pos + 1] += 1
        pos += 2

    chars_result = ['E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']
    for i in range(0, 4):
        if results[i*2] > results[i*2 + 1]:
            string_result += chars_result[i * 2]
        else:
            string_result += chars_result[i * 2 + 1]
    
    try:
        index = api.mongodb.insert(api, 'jung_answers', {
            'answers': answers,
            'result': string_result 
        })
    except Exception as e:
        error = e

    if index:
        req.send({
            'error': False,
            'session': str(index)
        })
    else:
        req.send({
            'error': True,
            'message': str(error)
        })