FROM python:latest

ADD game.py /Pong

WORKDIR /Pong/

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "game.py"]
