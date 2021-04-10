FROM python:3.7

WORKDIR /..

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5500

ENTRYPOINT ["python", "app.py"]