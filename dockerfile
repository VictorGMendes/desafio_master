# Use uma imagem base oficial do Python
FROM python:3.12

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o diretório de trabalho
COPY . .

# Define a variável de ambiente para o host do PostgreSQL
ENV DATABASE_URL=postgresql://<usuario>:<senha>@<host>:<porta>/<nome_do_banco>

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
