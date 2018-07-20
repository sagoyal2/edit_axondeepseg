FROM python:2.7
ADD . /app
WORKDIR /app

RUN pip install -e .

RUN pip install -r requirements.txt

RUN chmod 777 -R /app

CMD ["python", "application.py"]