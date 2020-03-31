import unittest
from post_youdao import *

class postyoudaotext(unittest.TestCase):
    def text_someing(self):
        self.assertEqual(True,True)

    def text_get_ts(self):
        import time
        ts=time.time()
        ts=str(int(round(ts*1000)))
        print(ts)
        get_ts=mock.Mock(return_value='1584684880395')
        self.assertEqual('1584684880395',get_ts())

if __name__ == '__main__':
    unittest.main()