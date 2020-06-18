import unittest

from chapter.city_weather import HeFeng


class cityweathertest(unittest.TestCase):
    def test_get_city_code(self):
        hefeng=HeFeng()
        codes=hefeng.get_city_code()
        print(codes)
        count=0
        for each in codes:
            print(next(codes))
            count+=1
        print("count=",count)
        self.assertEqual(1620, count)

    def test_get_all_weather(self):
        hefeng=HeFeng()
        results=hefeng.get_all_weather(7)
        #print(results)
        for each in results:
            print(each)
        self.assertEqual(7,len(results))


if __name__ == '__main__':
    unittest.main()
