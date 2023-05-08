FROM python:3.10.2-slim-bullseye


ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /hi_app

COPY ./requirements.txt /hi_app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x ./hi.sh

RUN ./hi.sh  
