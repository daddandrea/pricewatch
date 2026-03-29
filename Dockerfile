FROM python:3.13-slim
RUN adduser --disabled-password --gecos '' appuser
RUN mkdir /app
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
RUN mkdir -p /app/data /app/celerybeat && chmod 777 /app/data /app/celerybeat
EXPOSE 8000
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
USER appuser
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
