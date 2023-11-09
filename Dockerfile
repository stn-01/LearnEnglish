FROM python:3-alpine
WORKDIR /app
ENV FLASK_APP=webapp
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]