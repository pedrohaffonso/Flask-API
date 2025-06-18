Gerenciador de Contatos Simples.

Um aplicativo web simples desenvolvido com Flask para gerenciamento de contatos. Permite adicionar novos contatos, visualizar uma lista de contatos existentes e realizar pesquisas básicas por nome.

🚀 Tecnologias Utilizadas
Python: Linguagem de programação principal.
Flask: Microframework web para Python.
Flask-SQLAlchemy: Extensão Flask para facilitar o uso do SQLAlchemy (ORM para bancos de dados).
SQLite: Banco de dados padrão utilizado para desenvolvimento (pode ser configurado para outros SGBDs).
HTML/CSS: Para a estrutura e estilização das páginas web.
Bootstrap: Framework CSS e HTML para desenvolvimento de interfaces responsivas.

✨ Funcionalidades
Página Inicial (/): Exibe uma mensagem de boas-vindas com informações básicas (usuário e idade, configuráveis).
Formulário de Contato (/contato/): Permite adicionar novos contatos ao banco de dados com campos como nome, e-mail, etc. (presumindo que ContatoForm e Contato têm esses campos).
Listagem de Contatos (/contato/lista): Exibe todos os contatos cadastrados.
Pesquisa de Contatos: Permite pesquisar contatos por nome na página de listagem.
