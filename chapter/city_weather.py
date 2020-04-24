import requests

class HeFeng():

  def __init__(self):
      self.url="https://cdn.heweather.com/china-city-list.txt"

  def get_weather(self,city_code):
      url="https://free-api.heweather.net/s6/weather/now?location="+city_code+"0c150bbb6b204fce9f15e8448ea2f559"
      info=requests.get(url)
      info.encoding='utf8'
      print(info.text)

  def get_city_code(self):
      cities=self.get_citys()
      for each in cities:
          yield each[2:13]

  def get_citys(self):
    html = requests.get(self.url)
    html.encoding = 'utf8'
    cities=html.text.split('\n')
    return cities[6:]



if __name__ == '__main__':
    hefeng=HeFeng()
    codes=hefeng.get_city_code()
    hefeng.get_weather(codes.__next__())
    #print(codes.__next__())
    #for each in hefeng.get_citys():
     #   print(each)

