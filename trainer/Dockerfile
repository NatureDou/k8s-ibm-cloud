FROM pytorch/pytorch:1.0-cuda10.0-cudnn7-runtime

RUN pip install tensorboardX==1.6.0
WORKDIR /var
ADD train.py /var

ENTRYPOINT ["python", "/var/train.py"]
