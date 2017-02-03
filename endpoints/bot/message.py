utils = [
    'bot',
    'regex',
    'mongodb'
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

    api.debug('User ' + email + ' send text: ' + text)

    # TESTES, TODO: REMOVER
    if api.regex.match(r'(Conte-me sobre a )?Unicamp', text):
        university = api.mongodb.select(api, 'universities', {'name': 'Unicamp'}, ['description', 'public'])
        api.bot.message(api, user_id, email, university[0]['description'])

    elif api.regex.match(r'(Conte-me sobre a )?Usp', text):
        university = api.mongodb.select(api, 'universities', {'name': 'Usp'}, ['description', 'public'])
        api.bot.message(api, user_id, email, university[0]['description'])

    return {
        'error': False
    }