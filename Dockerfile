FROM python:3.9-slim
WORKDIR /app
COPY app/ /app
RUN pip install -r /app/requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]
