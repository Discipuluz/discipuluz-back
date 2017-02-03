utils = [
    'bot'
    'regex'
]

def post(req, api):
    """
    
    Input:
        id: string
        from: string
        to: string
        type: string
        content: string

    Output:
        None
    """

    user_id = req.params['id']
    email = req.params['from']
    text = req.params['content']

    # TESTES, TODO: REMOVER
    if api.regex.match(r'[a-zA-Z]test', text):
        api.bot.message(api, user_id, email, 'Esse é um teste apenas!!')

    elif api.regex.match(r'(test2)+', text):
        api.bot.message(api, user_id, email, 'Esse é outro teste apenas!!')

    return {
        'error': False
    }