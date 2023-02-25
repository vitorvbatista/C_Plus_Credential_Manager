# C+ Credential_Manager
Simple credential manager where you can insert password, get, update, delete and check expiry dates


[EN]
Purpose:
C+ Manager is a credential manager system that intends to create an easy way to store passwords and manage credential data. 
In a general way we're used to mobile applications, softwares and websites that require an account and then... passwords.
There are some credential managers available on the internet  (some of them are paid)
And there are some browser extensions that can store website password (but restricted to websites only)
C+ Manager can store passwords (and other credential data) in a individual database.

User guide:
In addition to packages required (available in the requirements.txt file)
it is necessary some additional informations that follows:

- To make your experience more pleasant I suggest to allocate .exe and
.pyw (and .py as well) in "C:\Program Files".

- Create a desktop shortcut

- Put a desktop icon if you want (I put an free exemple here)

- At first launch, Windows probably will show a message about protection before open this app. Infortunately I couldn't find a way
to get rid of it yet, so you have to continue if some kind of message is shown

- Another detail that I couldn't manage yet is about insert password. Command insert will only work if open this app as administrator
* For both cases above I'm open to receive all kinds of help 

Why was it important to develop this app:
CRUD (Create, Retrieve, Update and Delete) is a principle of 4 main operations of a system. Developers must understand this principle and know how 
to program it.
This project was born as an individual necessity at work. As a credential organizer I faced a challenge: our system can't offer a
credential manager that our developers can get password everytime they need, update and check expiry dates. So with this application 
we have a secure way to store our credentials (because all password are encoded) and easily manage all of them.
I know there's a lot of apps that have this features, but I tought it could be nice to create a personal app.

Enjoy it.




[PT]
Propósito:
C+ Manager é um sistema de gerenciamento de credenciais com o objetivo de criar uma maneira fácil de armazenar senhas e
outros tipos de dados de credenciais.
De uma forma resumida nós estamos acostumados com aplicativos mobile, programas desktop e sites que exigem uma conta pessoal
e portanto, senhas.
Exsitem alguns gerenciadores de credenciais disponíveis na internet (alguns são pagos) e também existem extensões de navegadores
que armazenam senhas de alguns sites (porém restrito a alguns sites)
C+ Manager pode armazenar senhas e outros tipos de dados de credenciais num database individual

Guia do usuário:

Além de todos os pacotes Python necessários (disponíveis no arquivo requirements.txt), são necessárias algumas informações adicionais:

- Para ter uma experiência melhor, sugiro alocar o arquivo .exe, .pyw e .py no diretório "C:\Program Files"

- Crie um atalho no desktop e coloque um ícone novo do seu interesse (coloquei um exemplo aqui no git)

- Na primeira abertura do aplicativo, provavelmente o Windows mostrará uma mensagem de proteção da sua máquina. Infelizmente
não consegui achar uma maneira de corrigir isso, portanto deve continuar sempre que o sistema lhe apresentar essa mensagem.

- Outro detalhe que não pude corrigir é na operação de insert. O comando insert só funcionará se o aplicativo for aberto como 
administrador.

*Para ambos os casos acima estou aberto para receber quaisquer tipos de dicas e ajudas para correção.

Por que foi importante desenvolver esse aplicativo:
O CRUD é um princípio das 4 operações básicas de um sistema/software. Desenvolvedores devem entender esse princípio e saber como
programá-lo. 
Esse projeto nasceu de uma necessidade individual no trabalho. Como sendo responsável por organizar as credenciais, encontrei um
desafio, nosso sistema não oferece um gerenciamento de credenciais em que os desenvolvedores poder realizar um "get" em qualquer
momento sem ter que abrir todo o sistema e debugar parte do código. Então, com o C+ nós temos uma maneira fácil e segura (pois 
as senhas são criptografadas no banco) de gerenciar as credenciais.
Sei bem que existem muitos aplicativos que possuem essas características, mas pensei que seria interessante e produtivo criar 
um aplicativo próprio.

Aproveite.
