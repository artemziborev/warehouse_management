
FROM python:3.12-slim


WORKDIR /app


COPY requirements.txt dev-requirements.txt ./


RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r dev-requirements.txt


COPY . .


CMD ["python", "app/main.py"]
