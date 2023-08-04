# Blog-API
A simple API for a blog site

## 📖 Description
A simple API for a blog site with user authorization, verification by mail, user roles, creating and receiving articles, likes and dislikes, comments on articles.

## 💻 Technologies
- 🐍 Python - FastAPI
- 🗄️ PosgreSQL
- ⛓️ Bearer + JWT
- 🙋‍♂️ FastAPI-Users
- 📄 Alembic, SQLalchemy
- 🚀 Uvicorn

# ⚙️ User manual
1. ⬇️ Installing and downloading dependencies
   Creating a virtual environment and activating it
   ```
   python -m venv/venv
   source venv/bin/activete
   ```
   Downloading dependencies
   ```
   pip install fastapi[all] sqlalchemy[asyncio] alembic pydantic uvicorn asyncpg fastapi-users[sqlalchemy]
   ```
2. 👷‍♂️ Create a new database with PostgreSQL
   Create a new database with PostgreSQL, once created, open 'Query tool' and add a table 'alembic_version'
   ```
   CREATE TABLE public.alembic_version
   (
     version_num character varying(32) NOT NULL,
     PRIMARY KEY (version_num)
   );
   ```
4. 📂 Creating an .env file
   In the main directory, create a .env file with the following fields
   ```
   DB_NAME = localhost
   DB_HOST = localhost
   DB_PORT = 5467
   DB_PASS = postgres
   DB_USER = postgres

   JWT_SECRET = seCreT
   
   EMAIL_SEND = example@gmail.com
   EMAIL_PASS = password
   ```
   In the fields with the DB_ prefix, enter values about your database. The JWT_SECRET field is the secret key with the help of which
   tokens will be generated. EMAIL_SEND and EMAIL_PASS fields are the mail from which verification letters will be sent and the password       that your mail account gave you
6. 🏗️ Creating tables in the database
   If you connected your database correctly, now it's time to create tables in it, go to the project console (make sure that your virtual      environment is active and you are in the project root directory) and run the following commands:
   ```
   alembic revision --autogenerate -m 'Init'
   alembic upgrade head
   ```
7. 📎 Creating user roles
   If point 5 is passed successfully, then tables will be added to your database: article, user, comment, role, verify. To add user roles      open the 'Query tool' and enter the following query:
   ```
   INSERT INTO role
   VALUES
   (1, 'user', 'read'),
   (2, 'admin', 'read/whrite')
   ```
7. 🏁 Server start
   If you have successfully completed all the previous points, then you are already a great fellow and it remains only to start our local      server, go to the project console and run the following commands:
   ```
   cd src
   uvicorn mail:app --reload
   ```
   After which the server will be launched, you can follow the link http://127.0.0.1:8000/docs where you will have access to the full          documentation on methods and requests

**The best gratitude for my work will be your star 🌟, it's not difficult for you, but I'm pleased 🙃**
