FROM python:3.8

WORKDIR /app

COPY . /app
RUN echo "\
flask\n\
pymongo\n\
" > requirements.txt
RUN pip install -r requirements.txt

COPY ./templates/index.html ./templates/
