# Back-End Developer Engineer Challenge - Shipay

**Candidato:** Wesley Gurgel Marcelino de Oliveira

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/wesleygurgel/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](https://mail.google.com/mail/?view=cm&to=wesleygurgel27@gmail.com)

## Questão 1
```sql
SELECT name, email, r.description AS role_description, c.description AS claim_description
from users
INNER JOIN roles r on users.role_id = r.id
INNER JOIN user_claims uc on users.id = uc.user_id
INNER JOIN claims c on c.id = uc.claim_id;

```
## Questão 2
```python
query = session.query(User.name, User.email, Role.description.label('role_description'), Claim.description.label('claim_description')) \
    .join(Role, User.role_id == Role.id) \
    .join(UserClaim, User.id == UserClaim.user_id) \
    .join(Claim, Claim.id == UserClaim.claim_id)

results = query.all()
```
## Questão 3
A resposta da questão 3, está dentro do código que foi disponiblizado via Pull Request ou ZIP.
Os arquivos que compõem a resposta são:
`api/main.py`
`api/routers/users.py`
`api/repositories/user_repository.py`

Para melhor entendimento, solicito que analise via código, porém deixarei aqui um trecho que faz referência a resposta.
```python
# Questão 3
@router.get('/{user_id}/role')
def get_user_role(user_id: int):
    user_role = UserRepository().get_user_role(user_id)

    if not user_role:
        raise HTTPException(status_code=404, detail='User not found')

    return {'role_description': user_role.get('description')}
```

## Questão 4
A resposta da questão 4, está dentro do código que foi disponiblizado via Pull Request ou ZIP..
Os arquivos que compõem a resposta são:
`api/main.py`
`api/routers/users.py`
`api/repositories/user_repository.py`
`api/helpers/password.py`

Para melhor entendimento, solicito que analise via código, porém deixarei aqui um trecho que faz referência a resposta.
```python
# Questão 4
@router.post('/')
def create_user(user_data: UserCreate):
    existing_user = UserRepository().get_user_by_email(user_data.email)

    if existing_user:
        raise HTTPException(status_code=400, detail='Email already registered')

    # Gera uma senha aleatória se não for fornecida
    if not user_data.password:
        user_data.password = generate_random_password()

    # Criptografa a senha
    hashed_password = hash_password(user_data.password)

    UserRepository().create_user(user_data, hashed_password)

    return {'message': 'User created successfully'}
```

## Questão 5
Para responder essa questão foi criado um Markdown com nome de `README.md` dentro da pasta da nossa `api`.
Você poderá encontrar esse arquivo seguindo o caminho:
`api/README.md`

## Questão 6
De acordo com o log capturado, parece que a falha foi causada por um atributo inexistente no módulo `core.settings`. O erro está sendo representado pela seguinte linha:

```shell
AttributeError("module 'core.settings' has no attribute ‘WALLET_X_TOKEN_MAX_AGE'")
```
O atributo `WALLET_X_TOKEN_MAX_AGE` é usado em:
```shell
expire_at = now - settings.WALLET_X_TOKEN_MAX_AGE”
```
Apesar de ser referenciado dentro do código, esas referência não pode ser encontrada no módulo `core.settings`. Como resultado, o código não consegue encontrar esse atributo, ocasionando um `AttributeError`.

Possível solução do problema seria ir em `core.settings` e verificar se o atributo `WALLET_X_TOKEN_MAX_AGE` foi configurado corretamente. Assegurando que o nome do atributo esteja correto e que ele foi importado corretamente no módulo `wallet_oauth` e o método `renew_wallet_x_access_tokens` tenha o devido acesso a esse elemento.


## Questão 7
Alguns pontos que percebi que são interessantes como melhoria:

### Documentação
Adicionar uma documentação breve sobre a funcionalidade da aplicação e o que é necessário (passo-a-passo) para executar a funcionalidade. Assim quem clonar o projeto poderá rodar localmente sem mais dificuldades. Importante ressaltar que além dessa documentação que seria um README.md, também é uma boa prática adicionar documentação para os métodos dentro do nosso bot, para facilitar o entendimento do código em uma primeira visualização.

### Variáveis de Ambiente
Seria interessante adicionar o uso de variáveis de ambiente ao projeto, colocarmos de forma exposta a URI de acesso ao banco, pode ser perigoso.
```shell
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/shipay'
```

### Melhoria de Código
Na linha 30, temos um problema. observe que a função `task1(db)` é chamada diretamente ao adicionar o job ao nosso scheduler:
```python
task1_instance = scheduler.add_job(task1(db), 'interval', id='task1_job', minutes=var1)
```
Para que a função `task1(db)` seja executada corretamente com o scheduler, precisamos passar a própria função `task1` como argumento e não o resultado da chamada da função `task1(db)`. Passando o nome que faz referência a função podemos passar nossos argumentos através da opção `args`.
```python
task1_instance = scheduler.add_job(task1, 'interval', id='task1_job', minutes=var1, args=[app, db])
```

De combo com essa alteração, é possível perceber que também está sendo passado o argumento `app`. Esse argumento é de fundamental importância, pois sem ele não conseguiremos criar um contexto da nossa aplicação Flask para execução de métodos na nossa instância do db.

Uma possível solução seria deixar dessa forma:
```python
def task1(app, db):
    with app.app_context():
```

---
Algumas sugestões de melhoria para o método `task1`:
Em relação ao código abaixo, utilizar a consulta SQL diretamente como uma string pode ocasionar vulnerabilidade no código para ataques de Injeção de SQL.
```python
orders = db.session.execute('SELECT * FROM users;')
```
O próprio SQLAlchemy fornece uma forma mais segura de construir consultas SQL através de parâmetros por marcadores. No caso em específico não estamos usando nenhum parâmetro. 
Mas um exemplo da prática seria assim:
```python
qs = text('SELECT * FROM users WHERE id = :user_id')
orders = db.session.execute(qs, {'user_id': 30})
```
O método `text()` é importado diretamente da library `sqlalchemy`.
```shell
from sqlalchemy import text
```

---

Uma outra ocasião de melhoria, seria deixar esse trecho de código de forma dinâmica.
```python
    worksheet.write('A{0}'.format(index),'Id')
    worksheet.write('B{0}'.format(index),'Name')
    worksheet.write('C{0}'.format(index),'Email')
    worksheet.write('D{0}'.format(index),'Password')
    worksheet.write('E{0}'.format(index),'Role Id')
    worksheet.write('F{0}'.format(index),'Created At')
    worksheet.write('G{0}'.format(index),'Updated At')

    for order in orders:
        index = index + 1

        print('Id: {0}'.format(order[0]))
        worksheet.write('A{0}'.format(index),order[0])
        print('Name: {0}'.format(order[1]))
        worksheet.write('B{0}'.format(index),order[1])
        print('Email: {0}'.format(order[2]))
        worksheet.write('C{0}'.format(index),order[2])
        print('Password: {0}'.format(order[3]))
        worksheet.write('D{0}'.format(index),order[3])
        print('Role Id: {0}'.format(order[4]))
        worksheet.write('E{0}'.format(index),order[4])
        print('Created At: {0}'.format(order[5]))
        worksheet.write('F{0}'.format(index),order[5])
        print('Updated At: {0}'.format(order[6]))
        worksheet.write('G{0}'.format(index),order[6])

    workbook.close()
    print('job executed!')
```

Analisando, podemos perceber muita repetição de código e basicamente o que altera de linha para linha é apenas o index. 
Uma sugestão de melhoria seria deixarmos o código assim, até mesmo para melhor adaptação em caso de surgirem novas colunas na tabela:
```python
    column_names = ['ID', 'Name', 'Email', 'Password', 'Role Id', 'Created At', 'Updated At']
    for i, column_name in enumerate(column_names):
        cell = '{0}{1}'.format(chr(65 + i), index)
        worksheet.write(cell, column_name)

    for index, order in enumerate(orders, start=2):
        print('--------------------NEW ROW--------------------------')
        for i, value in enumerate(order):
            cell = '{0}{1}'.format(chr(65 + i), index)
            worksheet.write(cell, value)
            print('{0}: {1}'.format(column_names[i], value))
        print('--------------------END ROW---------------------------')
        print('--------------------xxxxxxx---------------------------')

    workbook.close()
    print('job executed!')
```
O funcionamento continua sendo o mesmo, porém agora estamos criando a referência para a célula do excel de forma dinâmica através do index.

---
Algumas outras sugestões mais simples porém que também são vistas com bons olhos.

- O fechamento do nosso  `workbook` seria interessante colocar dentro de uma cláusula `try-finnaly`, pois em qualquer exceção que aconteça em nossa execução teremos o problema de que o workbook não terá liberado os recursos relacionado a aquela escrita de arquivo.

- No seguinte trecho de código seria interessante adicionar algum tratamento para caso essa exceção venha a acontecer, pode ser um simples logging caso não necessite de tratamento específico. 
```python
try:
    scheduler.start()
except(KeyboardInterrupt, SystemExit):
    pass
```

- O nosso método `main`está sendo poluído com configurações referentes a aplicação que poderiam ser externas. Todo esse trecho de código faz referência a configurações da aplicação em si. Então seria uma boa prática fazer essa configuração de forma separada ao main da aplicação.
```python
app = Flask(__name__)
handler = RotatingFileHandler('bot.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/shipay'

db = SQLAlchemy(app)

config = configparser.ConfigParser()
config.read('settings/config.ini')
```

- Nas importações podemos ver que temos librarys que estão sendo importadas e não são usadas, seria uma boa prática removê-las.
![image](https://github.com/wesleygurgel/hooks/assets/39765254/ccc1c467-eb89-4229-a2e5-b773439a8243)

## Questão 8

Quando pensamos em uma forma de normalizar diferentes interfaces em uma saída uniforme, de cara pensamos em algum `Structural Design Patterns`.

Dois caras que podem ser muito úteis para o que precisamos são os Designers `Adapter` e o `Proxy`.

### Adapter Pattern (Também conhecido como: Adaptador, Wrapper):
https://refactoring.guru/pt-br/design-patterns/adapter

O Adapter é um padrão de projeto estrutural que permite objetos com interfaces incompatíveis colaborarem entre si.
O exemplo do mundo real no site do Guru é perfeito, o nome em si já diz tudo, quando você pega diferentes interfaces (Cabo de carregador de notebook) e você está indo para a Europa, você irá precisar de um Adaptador para plugar na tomada, ou seja você implementou uma interface comum que é desejada.

### Proxy Pattern
https://refactoring.guru/pt-br/design-patterns/proxy

A diferença entre eles é que no Proxy iremos manter o estado atual do objeto e apenas faremos o controle do acesso ao objeto. Ele será responsável para que a comunicação entre as duas pontas ocorra de forma correta, atuando como um intermediário entre a nossa aplicação e o nosso fornecedor.
