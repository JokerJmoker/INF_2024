FROM python:3.8

WORKDIR /app

COPY upload.txt .
# сначала копируем зависимсоти(для удобства), затем запускаем их "применение "
RUN pip install -r upload.txt
#копируем исходный код
COPY . .
# запускаем через терминал приложение
CMD ["python", "app_2.py"]

