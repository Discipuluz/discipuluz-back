# DISCIPULUZ BACK
Back End usado para o site e o bot da discipuluz!

## LINGUAGEM
[Python 3.5+](https://docs.python.org/3/tutorial/index.html)

## BIBLIOTECAS
* [apys](https://github.com/seijihirao/apys)

## BANCO DE DADOS
[MongoDB](https://www.mongodb.com/) - [Python-lib](https://api.mongodb.com/python/current/)

---

## INSTALAÇÃO
 1. Instale o python 3.5+
     * Windows - [Link](https://www.python.org/)
     * Ubuntu - `sudo apt-get install python2`
     * Fedora - `sudo yum install python2`
     * Arch - `sudo pacman -S python2`
 2. Instale o PIP - gerenciador de bibliotcas do python
     * Windows - [Link](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip)
     * Ubuntu - `sudo apt-get install pip`
     * Fedora - `sudo yum install pip`
     * Arch - `sudo pacman -S pip`
 3. Instale a(s) biblioteca(s) usando o PIP
     * `pip install -r requirements.txt`
     
---

## Desenvolvimento

### Config

```javascript
{
    server: {
        port: 'Porta de acesso, (padrão=8888)'
    },
    mongodb: {
        host: 'Mudar para localhost:27017, (padrão="db:27017")',
        database: 'Banco de Dados, (padrão="discipuluz")'
    },
}
```

### Endpoints

    web/ - pasta com endpoints acessados pelo site
    bot/ - pasta com endpoints acessados pelos bots
    infra/ - pasta com endpoints para auxílio no servidor (como popular bancos)

## BRANCHING

* Prod - Branch de produção, apenas versão final

* Dev - Branch de desenvolvimento, versões prontas para irem para produção, beta

* Outras branches - Criá-las para realizar alterações, alpha 

---

## EXECUÇÃO

Execute `apys -s` pelo terminal na pasta raiz do seu projeto

---

## AGRADECIMENTOS

https://youtu.be/NooZO2UeNjI