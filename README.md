=============================
🧳 API DE GESTÃO DE MILHAS - FLASK
=============================

Autor: Acalu  
E-mail: acalusereno@hotmail.com  

------------------------------------------------------------
📘 SOBRE O PROJETO
------------------------------------------------------------
Esta API foi desenvolvida em Python com Flask para gerenciar clientes e seus saldos de milhas aéreas.

Ela permite:
- Listar todos os clientes  
- Buscar cliente por ID  
- Adicionar novos clientes  
- Atualizar dados de clientes  
- Deletar clientes  
- Adicionar milhas ao saldo de um cliente  

------------------------------------------------------------
⚙️ TECNOLOGIAS UTILIZADAS
------------------------------------------------------------
- Python 3.11+
- Flask (framework web)
- MySQL (banco de dados)
- mysql-connector-python (driver para conexão)

------------------------------------------------------------
📁 ESTRUTURA DO PROJETO
------------------------------------------------------------

API_MILHAS/
│
├── app.py                   -> Arquivo principal (inicia o servidor Flask)
├── conn.py                  -> Conexão com o banco MySQL
├── DATA_BASE.sql            -> Script SQL de exemplo com estrutura e dados
├── README.txt               -> Instruções e documentação
├── requirements.txt         -> Dependências Python
│
├── routes/                  -> Rotas da API
│   └── usuario_route.py
│
└── services/                -> Lógica e acesso ao banco
    └── usuario_service.py

------------------------------------------------------------
⚙️ CONFIGURAÇÃO RÁPIDA
------------------------------------------------------------

1️⃣ Instale o Python 3.11 (ou superior) e o MySQL.  
2️⃣ Instale as dependências do projeto:

pip install -r requirements.txt

(Se o arquivo não existir, crie um com o conteúdo abaixo:)
--------------------------------
flask  
mysql-connector-python  
--------------------------------

3️⃣ Crie o banco de dados executando o script `DATA_BASE.sql` no MySQL.  
   Ele cria o banco `DBMILHAS` e adiciona exemplos de clientes.

4️⃣ Execute a aplicação Flask:

python app.py

A API ficará disponível em:
👉 http://127.0.0.1:5000/

------------------------------------------------------------
🔗 COMO USAR OS ENDPOINTS
------------------------------------------------------------

### 1️⃣ Testar se a API está online
**GET /**
http://127.0.0.1:5000/



✅ Resposta:
Tudo OK!



---

### 2️⃣ Listar todos os clientes
**GET /clientes**
http://127.0.0.1:5000/clientes



✅ Retorna todos os clientes cadastrados no banco.

Exemplo de resposta:

[
  {
    "id_cliente": 1,
    "nome": "Ana Clara Souza",
    "email": "ana.souza@email.com",
    "saldo_milhas": 35000,
    "destino_desejado": "Paris"
  },
  {
    "id_cliente": 2,
    "nome": "Bruno Henrique Lima",
    "email": "bruno.lima@email.com",
    "saldo_milhas": 12000,
    "destino_desejado": "Rio de Janeiro"
  }
]
3️⃣ Buscar cliente por ID
GET /clientes/<id_cliente>



http://127.0.0.1:5000/clientes/1
✅ Retorna os dados do cliente com o ID informado.

Exemplo de resposta:



{
  "id_cliente": 1,
  "nome": "Ana Clara Souza",
  "email": "ana.souza@email.com",
  "saldo_milhas": 35000,
  "destino_desejado": "Paris"
}
4️⃣ Adicionar novo cliente
POST /clientes



http://127.0.0.1:5000/clientes
📤 Corpo (JSON):



{
  "nome": "Lucas Santos",
  "email": "lucas@email.com",
  "cartao": "9999-8888-7777-6666",
  "saldo_milhas": 5000,
  "destino_desejado": "Lisboa"
}
✅ Resposta:



{
  "id_cliente": 21,
  "mensagem": "Cliente adicionado com sucesso!"
}
5️⃣ Atualizar cliente existente
PUT /clientes/<id_cliente>



http://127.0.0.1:5000/clientes/3
📤 Corpo (JSON):



{
  "nome": "Carla Menezes",
  "email": "carla.menezes@email.com",
  "cartao": "3456-7890-1234-5678",
  "saldo_milhas": 85000,
  "destino_desejado": "Nova York"
}
✅ Resposta:



{
  "mensagem": "Cliente atualizado com sucesso!"
}
6️⃣ Deletar um cliente
DELETE /clientes/<id_cliente>



http://127.0.0.1:5000/clientes/3
✅ Resposta:



{
  "mensagem": "Cliente deletado com sucesso!"
}
7️⃣ Adicionar milhas a um cliente
POST /clientes/<id_cliente>/adicionar-milhas

bash

http://127.0.0.1:5000/clientes/1/adicionar-milhas
📤 Corpo (JSON):



{
  "milhas": 2000
}
✅ Resposta:



{
  "mensagem": "2000 milhas adicionadas ao cliente 1"
}
🧠 DECISÕES DE DESIGN
Separação entre camadas:
• routes/ → define endpoints da API
• services/ → contém a lógica e consultas SQL
• conn.py → cuida da conexão com o banco MySQL

Utilização de SQL direto (sem ORM) para fins didáticos.

Validações implementadas:

Campos obrigatórios

E-mail único

Impede saldo negativo

👨‍💻 AUTOR
Desenvolvido por: Acalu
E-mail: acalusereno@hotmail.com