import pymongo

class HeFengdb():
    def __init__(self):
        self.client=pymongo.MongoClient('localhost',27017)
        self.book_weather=self.client['weather']
        self.sheet_weather=self.book_weather['sheet_weather_3']

    def save(self,data):
        self.sheet_weather.insert_one(data)

    def show_all(self):
        all=self.sheet_weather.find()
        for each in all:
            print(each)

    def find(self,condition):
        return self.sheet_weather.find(condition)

    def delete(self):
        self.sheet_weather.delete_many({})

    def save_all(self, weathers):
        for each in weathers:
            self.save(each)

    def count(self):
        all = self.sheet_weather.find()
        nums=0
        for each in all:
            nums=nums+1
        print(nums)



if __name__ == '__main__':
    hefengdb=HeFengdb()
    hefengdb.show_all()
    hefengdb.save({"name":"liwenlong","class":"qianduan"})