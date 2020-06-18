from chapter.city_weather import HeFeng
from chapter.city_weather_db import HeFengdb

def save_all_weather():
    hefeng = HeFeng()
    weathers = hefeng.get_all_weather(100)
    hefengdb = HeFengdb()
    hefengdb.save_all(weathers)
    hefengdb.show_all()

if __name__ == '__main__':
    #save_all_weather()
    hefengdb=HeFengdb()
    #hefengdb.show_all()
    for each in hefengdb.find({'HeWeather6.basic.parent_city':'北京'}):
        print(each)
    print('=========================================晴天=============================================')
    for each in hefengdb.find({'HeWeather6.now.cond_txt':'晴'}):
        print(each['HeWeather6'][0]['basic']['location'])
    print('======================================温度大于26度=========================================')
    for each in hefengdb.find({'HeWeather6.now.tmp':{'$gte':'26'}}):
        print(each)
