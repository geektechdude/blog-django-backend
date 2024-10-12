FROM python:3.13.0

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

RUN chmod +x ./docker-script.sh

ENTRYPOINT ["./docker-script.sh"]