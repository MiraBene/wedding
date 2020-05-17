FROM python:alpine3.8

WORKDIR /app
copy app/ /app

# RUN apk update
# RUN apk add make automake gcc g++ subversion python3-dev

RUN pip --no-cache-dir install flask

CMD ["python", "app.py"]
# CMD ["sh"]
