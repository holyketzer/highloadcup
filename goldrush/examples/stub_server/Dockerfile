FROM python:3.6-slim

RUN apt-get update --fix-missing -y \
    && apt-get install -y --no-install-recommends \
        curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8000

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]

HEALTHCHECK --interval=5s --timeout=3s --start-period=15s \
  CMD curl -f http://localhost:8000/health-check || exit 1