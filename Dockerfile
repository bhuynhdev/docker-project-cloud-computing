FROM python:3.7-alpine3.16
COPY main.py .
CMD ["python3", "/main.py", "home/data"]