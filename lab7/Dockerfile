FROM python:3.7-alpine

COPY requirements.txt /tmp/

RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

COPY . /app

WORKDIR /app

ENTRYPOINT ["python3"]

CMD ["site.py"]