# 📚 Library Management System

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-19.03.12-blue?logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-2.28.0-blue?logo=git&logoColor=white)

Добро пожаловать в систему управления библиотекой! Это консольное приложение позволяет легко управлять книгами, добавлять новые, удалять существующие, искать и отображать их. 📖✨

# 🚀 Функционал

1. **Добавление книги**: 📚 Пользователь вводит `title`, `author` и `year`, после чего книга добавляется в библиотеку с уникальным `id` и статусом “в наличии”.
2. **Удаление книги**: 🗑️ Пользователь вводит `id` книги, которую нужно удалить.
3. **Поиск книги**: 🔍 Пользователь может искать книги по `title`, `author` или `year`.
4. **Отображение всех книг**: 📜 Приложение выводит список всех книг с их `id`, `title`, `author`, `year` и `status`.
5. **Изменение статуса книги**: 🔄 Пользователь вводит `id` книги и новый статус (“в наличии” или “выдана”).

# 🛠 Установка и запуск

## Клонирование репозитория
```bash
git clone https://github.com/nazarijbeketovv/library_management.git
cd library_management
```



## Запуск без Docker
1. **Убедитесь, что у вас установлена версия Python 3.12.x**
2.
```bash
python3 main.py
```

## Запуск с использованием Docker
1. Убедитесь, что у вас установлен Docker.
2. Сборка Docker-образа:
```bash
docker build -t library_management .
docker run -it --rm library_management

```

# 🧪 Тестирование

## Для запуска тестов используйте команду:

```bash
python -m unittest discover tests
```

# 📜 Требования

1. **Python 3.12**
2. **Docker (опционально)**


