FROM python:3.8

WORKDIR /contactscrapper

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY contactscrapper/ .

CMD [ "python", "./run.py" ]