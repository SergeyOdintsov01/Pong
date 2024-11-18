FROM python:latest

ADD game.py /Pong/

WORKDIR /Pong/

CMD ["python", "game.py"]
