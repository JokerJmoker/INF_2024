# точно такой же файл, как и в 3_1
FROM python:3.8

WORKDIR /app

COPY . /app

RUN echo "\
flask\n\
pymongo\n\
" > requirements.txt

RUN pip install -r requirements.txt


