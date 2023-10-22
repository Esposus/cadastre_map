# Кадастронавигатор

Описание проекта
===================
Проект включает в себя два сервиса, первый принимает запрос с указанием кадастрового номера, широты и долготы и эмулирует отправку запроса на внешний сервер. Второй сервис принимает и  обрабатывает запрос до 60 секунд и отдает результат запроса. Считается, что внешний сервер может ответить `true` или `false`. Данные запроса на сервер и ответ с сохраняются в базу данных. 
Функционал обоих сервисов протестирован с помощью pytest. Каждый сервис завернут в докер-контейнер.

***Сервис содержит следующие эндпоинты:***

```
"/query" - для получения запроса
"/result" - для отправки результата
"/ping" - проверка, что сервер запустился
"/history" - для получения истории запросов
"/history/<cadastre_number: int>" - для получения истории запросов
"/admin" - панель администратора
"/docs" или "/redoc" - документация к сервису
```

Сервис будет запущен и доступен по следующим адресам:
--------------------------------------------------------

- http://127.0.0.1:8000/docs - автоматически сгенерированная документация Swagger для первого сервиса
- http://127.0.0.1:8003/docs - автоматически сгенерированная документация Swagger для второго сервиса

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

1. Клонируйте репозиторий и перейдите в него в командной строке:
```bash
git clone git@github.com:Esposus/cadastre_map.git
```
```bash
cd cadastre_map
```
3. Заполните ```.env``` файл с переменными окружения по примеру:
```bash 
echo DATABASE_URL=sqlite:///./cadastre.db >> app/.env
```
4. Установите и запустите приложения в контейнерах:
```bash 
docker-compose build & docker-compose up
```
 
## Автор 
[Дмитрий Морозов](https://github.com/Esposus "GitHub аккаунт")
*telegram: @Vanadoo*