  <h1>Cadastro de Livros - API com FastAPI</h1>
  <p>Este projeto implementa uma API simples para o cadastro de livros, utilizando FastAPI e SQLite. A API permite realizar operações básicas de CRUD (Criar, Ler, Atualizar e Excluir) em uma tabela de livros, com as colunas <strong>id</strong>, <strong>nome</strong>, <strong>autor</strong> e <strong>páginas</strong>.</p>

  <h2>Funcionalidades</h2>
  <ul>
      <li><strong>Criar</strong> um novo livro.</li>
      <li><strong>Listar</strong> todos os livros cadastrados.</li>
      <li><strong>Obter</strong> detalhes de um livro pelo seu <code>id</code>.</li>
      <li><strong>Atualizar</strong> informações de um livro existente.</li>
      <li><strong>Excluir</strong> um livro.</li>
  </ul>

  <h2>Tecnologias Utilizadas</h2>
  <ul>
      <li><strong>FastAPI</strong>: Framework para criação da API.</li>
      <li><strong>Uvicorn</strong>: Servidor ASGI para rodar a aplicação.</li>
      <li><strong>SQLAlchemy</strong>: ORM para comunicação com o banco de dados SQLite.</li>
      <li><strong>Pydantic</strong>: Para validação e serialização dos dados.</li>
      <li><strong>SQLite</strong>: Banco de dados leve, utilizado para armazenar as informações dos livros.</li>
  </ul>

  <h2>Instalação</h2>
  <ol>
      <li><strong>Clone o repositório</strong>:
          <pre><code>git clone https://github.com/VictorGMendes/projeto_livro.git
cd cadastro-livros</code></pre>
      </li>
      <li><strong>Instale as dependências</strong>:
          <pre><code>pip install -r requirements.txt</code></pre>
      </li>
      <li><strong>Criação do Banco de Dados</strong>: O banco de dados SQLite será automaticamente criado ao executar a aplicação. As tabelas serão geradas quando você rodar o servidor pela primeira vez.</li>
  </ol>

  <h2>Como Rodar o Projeto</h2>
  <ol>
      <li><strong>Execute a API com o Uvicorn</strong>:
          <pre><code>uvicorn main:app --reload</code></pre>
          A API estará disponível em <code>http://127.0.0.1:8000</code>.
      </li>
      <li>O FastAPI gera automaticamente uma documentação interativa para a API. Acesse em:
          <pre><code>http://127.0.0.1:8000/docs</code></pre>
          Você poderá testar os endpoints diretamente pela interface.
      </li>
  </ol>

  <h2>Endpoints da API</h2>

  <h3>1. Criar um novo livro</h3>
  <ul>
      <li><strong>Método</strong>: <code>POST</code></li>
      <li><strong>URL</strong>: <code>/livros/</code></li>
      <li><strong>Body</strong>:
          <pre><code>{
  "nome": "Nome do Livro",
  "autor": "Nome do Autor",
  "paginas": 200
}</code></pre>
      </li>
  </ul>

  <h3>2. Listar todos os livros</h3>
  <ul>
      <li><strong>Método</strong>: <code>GET</code></li>
      <li><strong>URL</strong>: <code>/livros/</code></li>
      <li><strong>Resposta</strong>:
          <pre><code>[
  {
      "id": 1,
      "nome": "Nome do Livro",
      "autor": "Nome do Autor",
      "paginas": 200
  },
  ...
]</code></pre>
      </li>
  </ul>

  <h3>3. Obter um livro pelo ID</h3>
  <ul>
      <li><strong>Método</strong>: <code>GET</code></li>
      <li><strong>URL</strong>: <code>/livros/{livro_id}</code></li>
      <li><strong>Resposta</strong>:
          <pre><code>{
  "id": 1,
  "nome": "Nome do Livro",
  "autor": "Nome do Autor",
  "paginas": 200
}</code></pre>
      </li>
  </ul>

  <h3>4. Atualizar informações de um livro</h3>
  <ul>
      <li><strong>Método</strong>: <code>PUT</code></li>
      <li><strong>URL</strong>: <code>/livros/{livro_id}</code></li>
      <li><strong>Body</strong>:
          <pre><code>{
  "nome": "Novo Nome do Livro",
  "autor": "Novo Nome do Autor",
  "paginas": 250
}</code></pre>
      </li>
  </ul>

  <h3>5. Excluir um livro</h3>
  <ul>
      <li><strong>Método</strong>: <code>DELETE</code></li>
      <li><strong>URL</strong>: <code>/livros/{livro_id}</code></li>
      <li><strong>Resposta</strong>:
          <pre><code>{
  "message": "Livro excluído com sucesso"
}</code></pre>
      </li>
  </ul>

![dev_capivara (1)](https://github.com/user-attachments/assets/8cbe7f74-e4ac-485b-9cad-9ff48867fa95)
