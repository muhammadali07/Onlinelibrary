FROM python:3.9-alpine3.13

WORKDIR /app

ENV PYTHONPATH=/app \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  INSTALL_DEV=true

ADD requirements.txt .
RUN pip install -r requirements.txt


# Set Timezone
RUN apk add tzdata
ENV TZ=Asia/Jakarta

COPY ./start.sh /start.sh
RUN chmod +x /start.sh


COPY . /app

CMD ["/start.sh"]