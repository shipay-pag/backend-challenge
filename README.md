# Shipay Back-end Challenge

***Nota: Utilizaremos os seguintes critérios para a avaliação: Desempenho, Testes, Manutenabilidade, Separação de responsabilidades e boas práticas de engenharia de software.***

1.- Tomando como base a estrutura do banco de dados fornecida (conforme diagrama [ER_diagram.png] e/ou script DDL [1_create_database_ddl.sql], disponibilizados no repositório do github): Construa uma consulta SQL que retorne o nome, e-mail, a descrição do papel e as descrições das permissões/claims que um usuário possui.

2.- Utilizando a mesma estrutura do banco de dados da questão anterior, rescreva a consulta anterior utilizando um ORM (Object Relational Mapping) de sua preferência utilizando a query language padrão do ORM adotado (ex.: Spring JOOQ, EEF LINQ, SQL Alchemy Expression Language, etc).

3.- Utilizando a mesma estrutura do banco de dados fornecida anteriormente, e a linguagem que desejar, construa uma API REST que irá listar o papel de um usuário pelo “Id” (role_id).

4.- Utilizando a mesma estrutura do banco de dados fornecida anteriormente, e a linguagem que desejar, construa uma API REST que irá criar um usuário. Os campos obrigatórios serão nome, e-mail e papel do usuário. A senha será um campo opcional, caso o usuário não informe uma senha o serviço da API deverá gerar essa senha automaticamente.

5.- Crie uma documentação que explique como executar seu projeto em ambiente local e também como deverá ser realizado o ‘deploy’ em ambiente produtivo.

***Para a próxima questão (a de número 6) apesar da 'stack trace' apresentada ser em Python, o erro é genérico e pode ocorrer com qualquer outra linguagem.***

6.- Nossos analistas de qualidade reportaram uma falha que só acontece em ambientes diferentes do local/desenvolvimento, os engenheiros responsáveis pelo ambiente de Homologação já descartaram problemas de infra-estrutura, temos que levantar o que está acontecendo.

Ao executar o comando para listar os logs (no stdio) do Pod de Jobs, capturei o seguinte registro de log:

[2020-07-06 20:24:49,781: INFO/ForkPoolWorker-2] [expire_orders] - Finishing job…

[2020-07-06 20:34:49,721: INFO/ForkPoolWorker-1] [renew_wallet_x_access_tokens] Starting task that renew Access Tokens from Wallet X about to expire

[2020-07-06 20:34:49,723: ERROR/ForkPoolWorker-1] Task tasks.wallet_oauth.renew_wallet_x_access_tokens[ee561a2e-e837-4d98-b771-07f4e2b5ec70] raised unexpected: AttributeError("module 'core.settings' has no attribute ‘WALLET_X_TOKEN_MAX_AGE'")
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/celery/app/trace.py", line 385, in trace_task
    R = retval = fun(args, kwargs)
  File "/usr/local/lib/python3.7/site-packages/celery/app/trace.py", line 650, in __protected_call__
    return self.run(args, kwargs)
  File "/opt/worker/src/tasks/wallet_oauth.py", line 15, in renew_wallet_x_access_tokens
    expire_at = now - settings.WALLET_X_TOKEN_MAX_AGE
AttributeError: module 'core.settings' has no attribute ‘WALLET_X_TOKEN_MAX_AGE'

[2020-07-06 20:34:49,799: INFO/ForkPoolWorker-2] [expire_orders] - Starting job…

[2020-07-66 20:34:49,801: INFO/ForkPoolWorker-2] [expire_orders] - Filtering pending operations older than 10 minutes ago.


***De acordo com o log capturado, o que pode estar originando a falha?***


7.- Ajude-nos fazendo o ‘Code Review’ do código de um robô/rotina que exporta os dados da tabela “users” de tempos em tempos. O código foi disponibilizado no mesmo repositório do git hub dentro da pasta “bot”. ***ATENÇÃO: Não é necessário implementar as revisões, basta apenas anota-las em um arquivo texto ou em forma de comentários no código.***

8.- Qual ou quais Padrões de Projeto/Design Patterns você utilizaria para normalizar serviços de terceiros (tornar múltiplas interfaces de diferentes fornecedores uniforme), por exemplo serviços de disparos de e-mails, ou então disparos de SMS. ***ATENÇÃO: Não é necessário implementar o Design Pattern, basta descrever qual você utilizaria e por quais motivos optou pelo mesmo.***

BOA SORTE!
