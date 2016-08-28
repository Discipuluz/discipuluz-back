# DISCIPULUZ BACK
Back End usado para o site e o bot da discipuluz!

## LINGUAGEM
[Python 2.7](https://docs.python.org/2/tutorial/index.html)

## BIBLIOTECAS
* [pypolyback](https://github.com/seijihirao/pypolyback)

## BANCO DE DADOS
[SQLite](https://www.sqlite.org/) - [Python-lib](https://docs.python.org/2.6/library/sqlite3.html)

---

## INSTALAÇÃO
 1. Instale o python 2.7
     * Windows - [Link](https://www.python.org/download/releases/2.7/)
     * Ubuntu - `sudo apt-get install python2`
     * Fedora - `sudo yum install python2`
     * Arch - `sudo pacman -S python2`
 2. Instale o PIP - gerenciador de bibliotcas do python
     * Windows - [Link](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip)
     * Ubuntu - `sudo apt-get install pip2`
     * Fedora - `sudo yum install pip2`
     * Arch - `sudo pacman -S pip2`
 3. Instale a(s) biblioteca(s) usando o PIP
     * `pip2 install pypolyback`
     
---

## Desenvolvimento

### Config

```javascript
{
    server: {
        port: 'Porta de acesso, (padrão=8888)'
    },
    url: {
        bot: 'endereço para os endpoints do bot',
        site: 'endereço para os endpoints do site'
    }
}
```

### Endpoints

    site/ - pasta com endpoints acessados pelo site
    bot/ - pasta com endpoints acessados pelo bot

## BRANCHING

* Prod - Branch de produção, apenas versão final

* Dev - Branch de desenvolvimento, versões prontas para irem para produção, beta

* Outras branches - Criá-las para realizar alterações, alpha 

---

## EXECUÇÃO

Execute `pypolyback` pelo terminal na pasta raizdo seu projeto

---

## AGRADECIMENTOS

https://youtu.be/NooZO2UeNjI