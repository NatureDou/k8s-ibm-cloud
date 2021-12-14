FROM python:3

RUN apt-get update && pip install --upgrade pip

WORKDIR /mnist_app


COPY * ./

RUN pip3 install -r requirements.txt


# RUN python3 train.py --epochs=1

EXPOSE 5000

ENTRYPOINT ["python3", "flask_server.py"]

# ENTRYPOINT ["python3", "flask_test.py"]