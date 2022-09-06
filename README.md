# Unicheck Backend

Unicheck é um sistema web voltado para gerenciamento escolar, onde uma escola e seus professores podem gerenciar notas, presenças e horários de suas disciplinas e turmas.


## Ferramentas
- [Postgres 12](): Banco de dados utilizado para armazenar dados do sistema.
- [Python 3.9](): Linguagem de programação utilizada.
- [Docker](): Ferramenta para a criação de containers.
- [Keycloack](): Ferramenta de autenticação do sistema.
- [Swagger](): Ferramenta utilizada para documentação das APIs


## Estrutura do Projeto
```
API
└ database
└ integrations
└ resources
└ requirements.txt
└ server.py
```

- **API**: Pastas localizadas na raiz do projeto, cada pasta é uma API, cada API é um micro-serviço.

- **database**: Cada API possui uma pasta 'database', esta é utilizada como módulo de comunicação com o banco de dados.

- **integrations**: Uma API pode possuir uma pasta 'integrations', a mesma é utilizada para armazenar funções de integração com outras APIs do próprio sistema ou integração com sistemas externos.

- **resources**: Cada API possui uma pasta 'resources', a mesma é utilizada para armazenar funções internas do sistema (ex.: CRUDs).

- **server.py**: Cada API possui uma pasta 'server.py', a mesma deverá ser utilizada para armazenar a classe/função de comunicação com as APIs.