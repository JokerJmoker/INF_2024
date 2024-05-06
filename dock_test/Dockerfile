FROM python:3.8

WORKDIR /app

COPY app.py .
RUN echo "\
flask\n\
pymongo\n\
" > req.txt
RUN pip install -r req.txt

COPY ./templates/index.html ./templates/


COPY create_db.py .
RUN python create_db.py

CMD ["python", "app.py"]