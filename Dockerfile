FROM python:3.11
WORKDIR /edu
COPY . .
RUN pip install --upgrade setuptools
RUN pip install -r req.txt

