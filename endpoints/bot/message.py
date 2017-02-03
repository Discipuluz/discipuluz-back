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
    email_from = req.params['from']
    email_to = req.params['to']
    text = req.params['content']

    await api.bot.notify(api, user_id, email_from, email_to, 'accepted')

    api.debug(user_id + ') User ' + email_from + ' send text: ' + text)

    try :
        # MELHORES UNIVERSIDADES
        match = api.regex.search(r'(?i)melhores.+faculdades.+(.+)', text)
        if match:
            universities = api.mongodb.select(api, 'courses', {
                'name': {'$elemMatch':{'$eq': match.group(1)}}
            }, ['universities'])[0]['universities']
            sorted(universities, key=lambda u: u['score'])
            str_universities = ''
            for university in universities:
                str_universities += university['id'] + '\n'
            await api.bot.message(api, user_id, email_from, str_universities)
            return {
                'error': False
            }

        # MELHOR UNIVERSIDADE
        match = api.regex.search(r'(?i)melhor.+faculdade.+(.+)', text)
        if match:
            universities = api.mongodb.select(api, 'courses', {
                'name': {'$elemMatch':{'$eq': match.group(1)}}
            }, ['universities'])[0]['universities']
            sorted(universities, key=lambda u: u['score'])
            str_universities = ''
            str_universities += universities[0]['id']+ '\n'
            await api.bot.message(api, user_id, email_from, str_universities)
            return {
                'error': False
            }
            

        # AREA DE ATUACAO
        match = api.regex.search(r'(?i)[aá]rea.+atua[cç][ãa]o (.+)', text)
        if match:
            ocupation_area = api.mongodb.select(api, 'courses', {
                'name':{'$elemMatch':{'$eq':match.group(1)}} #talvez nao seja 1
            }, ['ocupation_area'])[0]['']
            return {
                'error': False
            }
    except Exception as error:
        await api.bot.notify(api, user_id, email_from, email_to, 'failed', {
            'code': 500,
            'description': str(error)
        })
