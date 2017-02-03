utils = [
    'bot',
    'regex',
    'mongodb'
]

async def post(req, api):
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

    api.debug(user_id + ') User ' + email + ' send text: ' + text)

    # MELHORES UNIVERSIDADES
    match = api.regex.match(r'(?i)^melhores faculdades (.+)$', text)
    if match:
        universities = api.mongodb.select(api, 'courses', {
            'name': {'$elemMatch':{'$eq': match.group(1)}}
        }, ['universities'])[0]['universities']
        sorted(universities, key=lambda u: u['score'])
        str_universities = ''
        for university in universities:
            str_universities += university['id'] + ': ' + str(university['score']) + '\n'
        api.debug(str_universities)
        await api.bot.message(api, user_id, email, str_universities)
        return {
            'error': False
        }

    # MELHOR UNIVERSIDADE
    match = api.regex.match(r'(?i)^melhor faculdade (.+)$', text)
    if match:
        universities = api.mongodb.select(api, 'courses', {
            'name': {'$elemMatch':{'$eq': match.group(1)}}
        }, ['universities'])[0]['universities']
        sorted(universities, key=lambda u: u['score'])
        str_universities = ''
        str_universities += universities[0]['id']+ '\n'
        api.debug(str_universities)
        await api.bot.message(api, user_id, email, str_universities)
        return {
            'error': False
        }
        

    # AREA DE ATUACAO
    match = api.regex.match(r'(?i)^[aá]rea de atua[cç][ãa]o (.+)$', text)
    if match:
        ocupation_area = api.mongodb.select(api, 'courses', {
            'name':{'$elemMatch':{'$eq':match.group(1)}} #talvez nao seja 1
        }, ['ocupation_area'])[0]['']
        return {
            'error': False
        }
