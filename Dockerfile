FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

COPY . .

RUN chmod +x /app/init.sh
RUN chmod +x /app/run.sh

CMD [ "sh", "-c", "/app/init.sh && /app/run.sh" ]
