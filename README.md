# TPO Ingeniería de Datos 2

## Instalación de dependencias:

```bash
pip install uvicorn
pip install fastapi
pip install bcrypt
```

## Para conectar a base de datos

Crear un archivo llamado **.env** en la raíz del proyecto y colocarle lo siguiente:

```bash
MYSQL_HOST=<MYSQL_HOST>
MYSQL_PORT=<MYSQL_PORT>
MYSQL_USER=<MYSQL_USER>
MYSQL_PASS=<MYSQL_PASS>
MYSQL_DB_NAME=<MYSQL_DB_NAME>

MONGODB_SERVICE=<MONGODB_SERVICE>
MONGODB_URI=<MONGODB_URI>
MONGODB_DBNAME=<MONGODB_DBNAME>
MONGODB_USERNAME=<MONGODB_USERNAME>
MONGODB_PASSWORD=<MONGODB_PASSWORD>
MONGODB_COLLECTION=<MONGODB_COLLECTION>

NEO4J_URI=<NEO4J_URI>
NEO4J_USERNAME=<NEO4J_USERNAME>
NEO4J_PASSWORD=<NEO4J_PASSWORD>
AURA_INSTANCEID=<AURA_INSTANCEID>
AURA_INSTANCENAME=<AURA_INSTANCENAME>

JWT_SECRET=<UUID_V4>
JWT_EXP_MINUTES="10"
```

## Iniciar server

```bash
python main.py
```

## Ver Swagger

http://localhost:8081/docs
