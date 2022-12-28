# 经纬度坐标确定归属街道
此程序实现了从大地坐标系转换火星坐标系，并确定此坐标所属街道，最终通过docker实现网络调用。

## jiedaoxyz.py
通过geojson边界文件，shapely模块绘制各街道边界，以火星坐标系经纬坐标确定位于哪个街道

## run.py
通过flask实现网络接口调用

## CoordinatesConverter.py
大地坐标系转火星坐标系

**参考资料**：[坐标系转换](https://github.com/ni1o1/CoordinatesConverter.git)

## 用法

1. docker安装
```sh
sudo docker run -d -p 5000:80 --name jdxyz_flask www18/jdxyz_flask:latest
```

https://hub.docker.com/r/www18/jdxyz_flask

- **Request**：GET http://服务器ip:5000/user/print?p1=经度&p2=纬度
- **Response**：XX街道

2. Excel调用
```
=WEBSERVICE("http://服务器ip:5000/user/print?"&"p1="&经度&"&"&"p2="&纬度)
```