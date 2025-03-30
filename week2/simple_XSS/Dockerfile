FROM python:3.10.12-alpine3.18@sha256:5d1dafb473686c5435faed90387956d6f1fdd919e4ced85eb2aa5ac45d29a98c

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r requirements.txt

RUN apt install curl -y

RUN curl -LO https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN rm google-chrome-stable_current_amd64.deb

RUN useradd web
COPY ./ /home/web
WORKDIR /home/web/app

CMD ["python3", "-u", "app.py"]