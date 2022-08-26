FROM python:3.8-slim

WORKDIR /app

COPY . .

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
