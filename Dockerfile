FROM python:3.11-slim
WORKDIR /app

RUN pip install --no-cache-dir telethon
COPY main.py /app

CMD ["python", "main.py"]