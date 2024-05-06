FROM python:3.8

WORKDIR /app 

RUN echo "\
flask\n\
pymongo\n\
" > req.txt

RUN pip install -r req.txt

COPY app_test.py .

CMD ["python", "create_db.py"]

CMD ["python", "app_test.py"]

