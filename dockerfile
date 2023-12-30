FROM python:3.6
WORKDIR /jdxyzflask
COPY . /jdxyzflask
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD [ "run:app", "-c", "gunicorn.conf.py"]