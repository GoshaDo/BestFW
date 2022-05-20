FROM python:3.8-buster

RUN apt-get -y update

WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN pip install -U rook

# move relevant files
ADD main.py .
ADD database.py .
ADD CONF.py .
ADD api.py .
ADD utilities.py .

COPY database/ ./database
COPY templates/ ./templates
COPY static/ ./static

CMD ["python", "/app/main.py"]
