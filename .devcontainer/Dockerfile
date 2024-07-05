FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Instalar PostgreSQL
RUN apt-get update && apt-get install -y postgresql postgresql-contrib libpq-dev

# Crear directorio para el volumen de datos
RUN mkdir -p /var/lib/postgresql/data
VOLUME /var/lib/postgresql/data

# Configurar PostgreSQL
USER postgres
RUN service postgresql start &&\
    psql --command "CREATE USER vscode WITH SUPERUSER PASSWORD 'password';" &&\
    createdb -O vscode vscode &&\
    echo "listen_addresses='*'" >> /etc/postgresql/12/main/postgresql.conf &&\
    echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/12/main/pg_hba.conf &&\
    echo "host all  all    ::1/128  md5" >> /etc/postgresql/12/main/pg_hba.conf

# Exponer el puerto 5432
EXPOSE 5432

USER vscode
