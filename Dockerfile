FROM python:3.12

WORKDIR /app
RUN pip install django

COPY . .

CMD ./run.sh