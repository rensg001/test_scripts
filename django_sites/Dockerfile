FROM python:2.7-slim
COPY ./src/requirements.txt /code/requirements.txt
COPY ./src/jessie-sources.list /etc/apt/sources.list

# install libs
RUN apt-get update \
    && apt-get -y --no-install-recommends install \
                              ca-certificates \
                              curl \
                              build-essential \
                              libpq-dev \
                              gettext \
                              git \
                              libffi-dev \
                              libjpeg-dev \
                              libpng-dev \
                              apt-utils \
    && pip install -r /code/requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com \
    && apt-get purge -y build-essential git \
    && apt-get autoremove -y \
    && apt-get remove -y libpq-dev libffi-dev libjpeg-dev libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# setup env
ENV SERVICE_PORT 8000
EXPOSE $SERVICE_PORT

ENV LOCAL_USER_ID 1001
ENV LOCAL_GROUP_ID 1001

ADD ./src /code
RUN chown -R $LOCAL_USER_ID:$LOCAL_GROUP_ID /code

USER $LOCAL_USER_ID:$LOCAL_GROUP_ID
WORKDIR /code