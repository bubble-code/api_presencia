
# Imagen base
FROM python:3.12-slim

# Instalar dependencias para pyodbc y ODBC Driver
RUN apt-get update && apt-get install -y \
    curl gnupg apt-transport-https \
    unixodbc unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar ODBC Driver 18 para SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/12/prod.list -o /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY app ./app
COPY .env ./.env

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
