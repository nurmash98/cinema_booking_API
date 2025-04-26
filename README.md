# 🎬 Cinema Booking API

API-проект для управления фильмами, пользователями и бронированиями в кинотеатре.  
Реализован на **Django**, **Django REST Framework**, с использованием **Poetry** и **PostgreSQL**.

## 🚀 Технологии проекта

- Python 3.13
- Django 5.2
- Django REST Framework
- PostgreSQL
- Poetry
- Pytest + Coverage
- Makefile

## 📦 Локальная установка

```bash
git clone https://github.com/nurmash98/cinema_booking_api.git
cd cinema_booking_api
poetry install
```

Создайте файл `.env`:

```dotenv
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=127.0.0.1,localhost
DB_NAME=cinema
DB_USER=cinema_user
DB_PASSWORD=booking
DB_HOST=localhost
DB_PORT=5432
```

Примените миграции и запустите сервер:

```bash
make migrate
make run
```

## 🧪 Тестирование

Создайте базу данных `test_cinema_booking`, затем:

```bash
make test
```
или

```bash
DJANGO_ENV=test PYTHONPATH=src poetry run pytest --cov=apps --cov-report=term-missing
```



## 🛠 ️ Команды Makefile

| Команда | Описание |
|:---|:---|
| `make run` | Запустить сервер |
| `make migrate` | Применить миграции |
| `make makemigrations` | Создать новые миграции |
| `make test` | Запустить тесты |
| `make createsuperuser` | Создать администратора |

