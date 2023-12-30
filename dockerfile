FROM python:3.6
WORKDIR /jdxyzflask/
COPY requirements.txt /jdxyzflask/
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . /jdxyzflask/
CMD [ "run:app", "-c", "gunicorn.conf.py"]