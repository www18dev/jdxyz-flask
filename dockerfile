FROM python:3.6
WORKDIR /jdxyzflask/
COPY requirements.txt /jdxyzflask/
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY ./root/jdxyzflask/ /jdxyzflask/
CMD [ "run:app", "-c", "gunicorn.conf.py"]

sudo docker build -t 'jdxyz_flask' .

sudo docker run -it --rm -p 5000:80 jdxyz_flask:latest
sudo docker run -d -p 5000:80 --name jdxyz_flask jdxyz_flask:latest