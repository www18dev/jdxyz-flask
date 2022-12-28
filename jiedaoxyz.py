# coding: UTF-8


#import os
from shapely.geometry import shape, Point
import geojson
import CoordinatesConverter as cc

#SOURCE_PATH = os.path.dirname(os.path.abspath(__file__))
#GEO_JSON    = SOURCE_PATH + "/芝罘区.json"

#判定任意位置信息属于哪个街道的方法

def belong(GEO_JSON, lat, lon):
  point = Point(lon, lat)
  for feature in GEO_JSON['features']:
    polygon = shape(feature['geometry'])
    

    if polygon.contains(point):
        return feature['properties']['name'] # 街道名称
  return None

### main
#if __name__ == '__main__':


def jiedao(GEO_JSON,lon,lat):
  '''
  :param GEO_JSON边界文件:
  :param 经度坐标:
  :param 纬度坐标:
  :return 所属街道:
  '''
  with open(GEO_JSON, encoding='utf-8-sig') as f:
    GEO_JSON = geojson.load(f)

  # 处理芝罘区
  #lon,lat = input().split('	')
  lon,lat = float(lon),float(lat)
 
  lon,lat = cc.wgs84togcj02(lon,lat)
  city = belong(GEO_JSON,lat,lon)
  print(city)
  return city

#jiedao(GEO_JSON,lon,lat)