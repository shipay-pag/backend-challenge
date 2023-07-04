# Documentação do Projeto API de Gerenciamento de Usuários

Este documento descreve como executar e implantar o projeto da API de Gerenciamento de Usuários que foi solicitado pela Shipay como parte de um Back-end Challenge.


## Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)
- PostgreSQL


## Configuração do Ambiente

Siga as etapas abaixo para configurar o ambiente local:

1. Clone ou baixe o repositório do projeto para sua máquina local.

```shell
git clone https://github.com/shipay-pag/backend-challenge.git
```
```

2. Crie e ative um ambiente virtual (recomendado).

```shell
python3 -m venv env
source venv/bin/activate  # Linux
```

3. Instale as dependências do projeto.

```shell
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente.

   - Renomeie o arquivo `.env.example` para `.env`.
   - Abra o arquivo `.env` em um editor de texto e configure as variáveis de acordo com seu ambiente.


## Executando o Projeto em Ambiente Local

Siga as etapas abaixo para executar o projeto em ambiente local:

1. Certifique-se de ter configurado corretamente as variáveis de ambiente no arquivo `.env`.

2. Crie um schema dentro de um banco de dados PostgreSQL.

3. Dentro do seu software cliente SQL de preferência (Dbeaver, DataGRIP), rode o Script SQL disponibilizado na raíz do projeto `1_create_database_ddl.sql`

4. Após a criação das tabelas dentro do seu Schema, foi disponibilizado um script de nome `populate_db.py` no caminho `api.database`, esse script irá popular as suas tabelas dinamicamente.

5. Inicie o servidor de desenvolvimento através do arquivo `main.py` que se encontra a pasta da `api`.

6. O servidor de desenvolvimento será iniciado em `http://localhost:8003`, ele está configurado para ser atualizado sempre que o código for utilizado.
Você pode acessar a documentação da API em `http://localhost:8003/docs` e testar os endpoints disponíveis.


## Implantação em Ambiente de Produção (AWS)

Assumindo que vamos utilizar a Amazon Web Services (AWS) para subir nossa aplicação em produção, seguiremos os seguintes passos:

1. Criar um banco de dados RDS (Relational Database Service) na AWS para armazenar os dados da aplicação.

2. Criar uma instância do Amazon ECS (Elastic Container Service) para implantar e executar a API de Gerenciamento de Usuários. Utilizaremos o ECS devido sua capacidade de escalabilidade através dos clusters.

3. Criar uma imagem Docker da aplicação para ser usada no ECS.

4. Faça o push da imagem Docker para um registro de container da AWS, como o Amazon Elastic Container Registry (ECR), para armazenar e gerenciar as imagens.

5. Criar um cluster no ECS e defina as tarefas (tasks) para executar a imagem Docker da aplicação. Importante configurar corretamente as opções de escalabilidade, como o número mínimo e máximo de instâncias, afim de evitar possíveis custos inesperados.

6. Configurar um load balancer, como o Elastic Load Balancer (ELB), para distribuir o tráfego entre as instâncias do ECS.

7. Associar o load balancer ao cluster do ECS e defina as regras de roteamento e balanceamento de carga necessárias.

8. Configurar um domínio personalizado para a API usando o serviço Route 53 da AWS.

9. Executar as migrações do banco de dados no RDS para criar as tabelas e estruturas necessárias para a aplicação.

10. Iniciar as tarefas do ECS no cluster e verifique se a API está sendo executada corretamente. Monitore os logs e métricas para garantir o bom funcionamento da aplicação.

11. Testar a API usando as rotas disponíveis e verifique se todos os endpoints estão funcionando corretamente.

12. Configurar os backups e as políticas de recuperação de desastres necessárias para o banco de dados RDS e os recursos do ECS.

13. Realizar testes de carga e estresse para verificar o desempenho e a escalabilidade da aplicação. Faça ajustes nas configurações do ECS e do banco de dados, se necessário, para melhorar o desempenho.

14. Por final podemos monitorar a aplicação (logs) e os recursos da AWS usando ferramentas como o Amazon CloudWatch. No CloudWatch é possível configurar alarmes e notificações para receber alertas em caso de problemas.


![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL Logo in a shields.io badge](https://img.shields.io/badge/PostgreSQL-gray.svg?logo=postgresql&style=for-the-badge&color=4169E1&logoColor=white)