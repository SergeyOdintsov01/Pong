# Используем конкретный Python-образ
FROM python:3.9-slim

# Создаем рабочую директорию
WORKDIR /Pong

# Копируем файл зависимостей отдельно (для использования кеша при сборке)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Указываем команду запуска
CMD ["python", "game.py"]
