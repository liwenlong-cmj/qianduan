import unittest

from chapter.city_weather import HeFeng
from chapter.city_weather_db import HeFengdb


class MyTestCase(unittest.TestCase):
    def test_something(self):
        hefengDb = HeFengdb()
        hefengDb.save({"name": "liwenlong", "class": "qianduan"})
        hefengDb.show_all()
        results = hefengDb.find({"name": "liwenlong"})
        for each in results:
            self.assertEqual("liwenlong", each['name'])
            self.assertEqual("qianduan", each['class'])
        hefengDb.delete()
        # self.assertEqual(4,hefengDb.find_all())

    def test_save_all(self):
        hefeng = HeFeng()
        weathers=hefeng.get_all_weather(7)
        # codes=hefneg.get_citu_code()
        # for each in codes:
        #     print(next(codes))
        #each = hefeng.get_weather("CN101010200")
        #print(each)
        hefengdb = HeFengdb()
        hefengdb.save_all(weathers)
        print("show_all")
        hefengdb.show_all()
        self.assertEqual(7,hefengdb.count())
        hefengdb.delete()


if __name__ == '__main__':
    unittest.main()