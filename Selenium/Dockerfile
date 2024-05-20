FROM --platform=amd64 python:3.9.6 

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt 

RUN apt-get update && nstall -y wget unzip && \
    wget https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/linux64/chrome-headless-shell-linux64.zip && \
    unzip chrome-headless-shell-linux64.zip && \
    rm chrome-headless-shell-linux64.zip && \
    apt-get clean

CMD [ "python","scrape.py" ]