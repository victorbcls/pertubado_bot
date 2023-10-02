
FROM python:3.8
RUN apt-get -y update
RUN apt-get install -y ffmpeg

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
CMD [ "python3","-u", "app/bot.py"]