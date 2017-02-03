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

    # TESTES, TODO: REMOVER
    if api.regex.match(r'(Conte-me sobre a )?Unicamp', text):
        university = api.mongodb.select(api, 'universities', {'name': {'$elemMatch':{'$eq': 'Unicamp'}}}, ['description', 'public'])
        api.debug(university)
        await api.bot.message(api, user_id, email, university[0]['description'])

    elif api.regex.match(r'(Conte-me sobre a )?Usp', text):
        university = api.mongodb.select(api, 'universities', {'name': 'Usp'}, ['description', 'public'])
        api.bot.message(api, user_id, email, university[0]['description'])

    # MELHOR UNIVERSIDADE
    match = api.regex.match(r'(?i)^melhores faculdades (.+)$', text)
    elif match:
        courses = api.mongodb.select(api, 'courses', {'name': {'$elemMatch':{'$eq': match.group(1)}}}, ['universities'])
        universities = courses[0]['universities']
        sorted(universities, key=lambda u: u['score'])
        str_universities = ''
        for university in universities:
            str_universities += university['id'] + ': ' + str(university['score']) + '\n'
        api.debug(str_universities)
        # await api.bot.message(api, user_id, email, str_universities)

    match = api.regex.match(r'(?i)^melhor faculdade (.+)$', text)
    elif match:
        universities = api.mongodb.select(api, 'courses', {
            'name': {'$elemMatch':{'$eq': match.group(1)}}
        })[0]['universities']
        sorted(universities, key=lambda u: u['score'])
        str_universities = ''
        str_universities += universities[0]['x  id']+ '\n'
        api.debug(str_universities)
        # await api.bot.message(api, user_id, email, str_universities)

    match = api.regex.match(r'(?i)^[aá]rea de atua[cç][ãa]o (.+)$', text)
    elif match:
        ocupation_area = api.mongodb.select(api, 'courses', {
            'name':{'$elemMatch':{'$eq':match.group(1)}} #talvez nao seja 1
        }, ['ocupation_area'])[0]['']

    return {
        'error': False
    }
