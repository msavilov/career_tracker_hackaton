# 'Хакатон Карьерный трекер х Практикум октябрь’23 Команда 4'

## Описание
Cоздание сервиса, который предоставит возможность партнерам работать с базой заинтересованных кандидатов Карьерного трекера Яндекс.Практикума.


## Команда
[Максим Савилов - developer](https://github.com/msavilov)


### Технологии
- _[Python 3.11](https://docs.python.org/3/)_
- _[Django 4.2.4](https://www.djangoproject.com/download/)_
- _[Django REST framework 3.12.4](https://www.django-rest-framework.org/)_
- _[Postgresql](https://hub.docker.com/_/postgres)-Docker-образ_
- _[Docker and docker-compose](https://www.docker.com/get-started/)_
- _[drf-yasq](https://drf-yasg.readthedocs.io/en/stable/readme.html)_
- _[celery](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#installing-celery)_
- _[redis](https://redis.io/download/#redis-downloads)_


### Установка

1. Клонировать репозиторий (открыть терминал в нужной папке, вставить эту строчку,
   и нажать "ENTER", в директории появится папка с названием проекта):

   ```python
   git clone https://github.com/msavilov/career_tracker_hackaton.git
   ```
2. Перейти в ветку develop:

   ```python
   cd career_tracker_hackaton && git checkout develop
   ```

3. Установить виртуальное окружение для проекта (там же набираешь одну из этих команд
   и нажимаешь "ENTER", в директории появится папка env):

   ```python
   # для OS Lunix и MacOS
   python3 -m venv venv

   # для OS Windows и MacOS
   python -m venv venv
   ```

4. Активировать виртуальное окружение для проекта (там же набираешь одну из этих команд
   и нажимаешь "ENTER", в терминал слева появится (venv)):

   ```python
   # для OS Lunix и MacOS
   source venv/bin/activate

   # для OS Windows
   source venv/Scripts/activate
   ```

5. Установить зависимости:

      ```python
   # для OS Lunix и MacOS
   python3 -m pip install --upgrade pip && pip install -r backend/requirements.txt

   # для OS Windows
   python -m pip install --upgrade pip && pip install -r backend/requirements.txt
   ```

6. Cоздайте файл `.env` в директории `/backend/`:

   ```python
   cd backend && nano .env

   В открывшийся редактор вставьте ключи ниже и после закройте командой "Ctrl + X"

   SECRET_KEY=любой_секретный_ключ_на_ваш_выбор
   DEBUG=''
   ALLOWED_HOSTS='*' (или,ваши,хосты,через,запятые,без,пробелов)

   Для работы 
   ```
7. В зависимости от того, запускаете вы проект в Docker или нет,
   выбрать ALLOWED_HOSTS в settings.py

### Для запуска вне Docker.

1. Выполнить миграции на уровне проекта из директории `/backend/`
   (если не вы перешли на нее предыдущей комнаде cd backend,
   то выполните команду cd backend):

   ```python
   # для OS Lunix и MacOS
   python3 manage.py makemigrations candidates
   python3 manage.py makemigrations vacancies
   python3 manage.py migrate

   # для OS Windows
   python manage.py makemigrations candidates
   python manage.py makemigrations vacancies
   python manage.py migrate
   ```
2. Создание суперпользователя: ввести команду 'python manage.py createsuperuser'

   ```python
   # для OS Lunix и MacOS
   python3 manage.py createsuperuser

   # для OS Windows
   python manage.py createsuperuser
   ```
3. Запустить проект локально:

   ```python
   # для OS Lunix и MacOS
   python3 manage.py runserver

   # для OS Windows
   python manage.py runserver
   ```
### Для запуска в Docker

1. Запустить контейнеры
   
   ```python
   docker compose up --build
   ```
2. Сделать миграции и собрать статику
   
   ```python
   docker compose exec backend python manage.py migrate

   docker compose exec backend python manage.py collectstatic

   docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
   ```

### Вход на главную страницу (не работает)
- [Index](http://127.0.0.1:8000/) со своим почтой и паролем

### Вход в админку
- [Admin](http://127.0.0.1:8000/admin) со своим почтой и паролем

### Работа с документацией и Postman после запуска проекта
- [Swagger](http://127.0.0.1:8000/api/swagger/)
