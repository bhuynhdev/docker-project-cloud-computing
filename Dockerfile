FROM python:3.7-alpine3.16
WORKDIR /home/data
COPY main.py main.py
CMD ["python3", "main.py"]