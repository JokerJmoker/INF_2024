FROM python:3.8

WORKDIR /app

RUN echo "flask" > req.txt

RUN pip install -r req.txt

COPY app_1.py .

CMD ["python", "app_1.py"]

