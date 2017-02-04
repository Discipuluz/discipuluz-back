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
        match = api.regex.search(r'(?i)melhores.+(faculdades|universidades) +de +([^!?.,]+)', text)
        api.debug(match)
        if match:
            api.debug(match.group(2).lower())
            universities = api.mongodb.select(api, 'courses', {
                'name': {'$elemMatch':{'$eq': match.group(2).lower()}}
            }, ['universities'])[0]['universities']
            sorted(universities, key=lambda u: u['score'])
            str_universities = 'Eai tá pensando em fazer med mas quer as melhores né? Podexá que eu te falo. As melhores são: \n'
            for university in universities:
                str_universities += university['id'] + '\n'
            await api.bot.message(api, user_id, email_from, email_to, str_universities)
            return {
                'error': False
            }

        # MELHOR UNIVERSIDADE
        match = api.regex.search(r'(?i)melhor.+(faculdade|universidade) +de +([^!?.,]+)', text)
        if match:
            universities = api.mongodb.select(api, 'courses', {
                'name': {'$elemMatch':{'$eq': match.group(2).lower()}}
            }, ['universities'])[0]['universities']
            sorted(universities, key=lambda u: u['score'])
            str_universities = 'Boa! Quando se trata do nosso futuro a gente busca sempre a melhor, no curso ' + match.group(2).lower() + ' a melhor Universidade é a ' + universities[0]['id']
            await api.bot.message(api, user_id, email_from, email_from, str_universities)
            return {
                'error': False
            }

        # AREA DE ATUACAO
        match = api.regex.search(r'(?i)[aá]rea +de +atua[cç][ãa]o +d[aeo] +([^!?.,]+)', text)
        if match:
            ocupations = api.mongodb.select(api, 'courses', {
                'name':{'$elemMatch':{'$eq':match.group(1)}}
            }, ['ocupation_area'])[0]['ocupation_area']
            str_ocupations = 'Deixa eu te falar um pouquinho mais das Áreas de Ocupação da "medicina". Dentre elas estão: \n'
            for ocupation in ocupations:
                str_ocupations += ocupation + '\n'
            await api.bot.message(api, user_id, email_from, email_to, str_ocupations)
            return {
                'error': False
            }

        api.error('Message not implemented: ' + text)

        await api.bot.message(api, user_id, email_from, email_to, 
            'Eita, não entendi .-. , você poderia me perguntar de uma forma diferente ? Nós ovelhas temos um vocabulário limitado.')

        await api.bot.notify(api, user_id, email_from, email_to, 'failed', {
            'code': 404,
            'description': 'Message not implemented'
        })
    except Exception as error:
        api.error(str(error))
        await api.bot.notify(api, user_id, email_from, email_to, 'failed', {
            'code': 500,
            'description': str(error)
        })

    return {
        'error': True
    }
