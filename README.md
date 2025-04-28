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

## 🛠 ️ Команды Makefile

| Команда | Описание |
|:---|:---|
| `make run` | Запустить сервер |
| `make migrate` | Применить миграции |
| `make makemigrations` | Создать новые миграции |
| `make test` | Запустить тесты |
| `make createsuperuser` | Создать администратора |

