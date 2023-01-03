FROM python:3.8
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ./ ./
EXPOSE 8080
CMD ["python","app.py"]