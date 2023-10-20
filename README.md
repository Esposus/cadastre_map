#Кадастронавигатор

Описание проекта
===================
Проект включает в себя два сервиса, первый принимает запрос с указанием кадастрового номера, широты и долготы и эмулирует отправку запроса на внешний сервер. Второй сервис принимает и  обрабатывает запрос до 60 секунд и отдает результат запроса. Считается, что внешний сервер может ответить `true` или `false`. Данные запроса на сервер и ответ с сохраняются в базу данных. 

Сервис содержит следующие эндпоинты:
"/query" - для получения запроса
“/result" - для отправки результата
"/ping" - проверка, что  сервер запустился
“/history” - для получения истории запросов
“/history/<cadastre_number: int>” - для получения истории запросов
"/admin" - панель администратора
"/docs" - документация к сервису

Функционал обоих сервисов протестирован с помощью pytest. Каждый сервис завернут в докер-контейнер.

Будет плюсом!
Документация к сервису
Тесты функционала


Стек технологий
----------
* Python 3.11
* FastAPI
* Docker
* SQLAlchemy
* Alembic
* GitHub Actions (CI)


Установка проекта из репозитория
----------

1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git@github.com:Esposus/cadastre_map.git

```

2. Cоздать в папке app файл ```.env``` с переменными окружения:
```bash 
touch app/.env
```

3. Заполнить ```.env``` файл с переменными окружения по примеру:
```bash 
echo DATABASE_URL=sqlite:///./cadastre.db >> app/.env-dev
```

4. Установка и запуск приложения в контейнерах:
```bash 
docker-compose build & docker-compose up
```
