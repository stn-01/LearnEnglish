FROM python:3-alpine
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt

ENV FLASK_APP=webapp
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

CMD ["flask", "run"]