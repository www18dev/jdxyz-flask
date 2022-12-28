# coding: UTF-8


#import os
from shapely.geometry import shape, Point
import geojson
import CoordinatesConverter as cc

#SOURCE_PATH = os.path.dirname(os.path.abspath(__file__))
#GEO_JSON    = SOURCE_PATH + "/芝罘区.json"

#判定任意位置信息属于哪个街道的方法

def belong(geo_json, lat, lon):
  point = Point(lon, lat)
  for feature in geo_json['features']:
    polygon = shape(feature['geometry'])
    

    if polygon.contains(point):
        return feature['properties']['name'] # 街道名称
  return None

### main
#if __name__ == '__main__':
def jiedao(GEO_JSON,lon,lat):
  with open(GEO_JSON,encoding='utf-8-sig') as f:
    geo_json = geojson.load(f)

  # 处理芝罘区
  #lon,lat = input().split('	')
  lon,lat = float(lon),float(lat)
 
  lon,lat = cc.wgs84togcj02(lon,lat)
  city = belong(geo_json,lat,lon)
  print(city)
  return city

#jiedao(GEO_JSON,lon,lat)