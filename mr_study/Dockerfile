FROM python
WORKDIR /app
COPY requirements.txt /app
RUN apt-get update && apt-get install -y nano mc htop
RUN pip install -r requirements.txt
RUN mkdir logs
COPY . .