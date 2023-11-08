FROM python:3-alpine
WORKDIR /app/LearnEnglish
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod +x /start.sh
CMD ["/start.sh"]
