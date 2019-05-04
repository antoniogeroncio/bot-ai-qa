FROM python:3.6.3-jessie
COPY requirements.txt requirements.txt
COPY server.py server.py
RUN pip install -r requirements.txt

EXPOSE 5000

CMD python server.py

