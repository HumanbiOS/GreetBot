FROM python:3.8

RUN mkdir /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

CMD python /app/bot.py