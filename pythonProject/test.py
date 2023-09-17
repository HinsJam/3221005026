import unittest
from main import main

class TestArticle(unittest.TestCase):
    def setUp(self):
        print("-----------------------------")
        print("测试单元")
    def testadd(self):
        print("测试文本add")
        main("D:\\PyCharm\\PyCharm 2022.1.3\\pythonProject\\orig.txt","D:\\PyCharm\\PyCharm 2022.1.3\\pythonProject\\orig_0.8_add.txt")
    def testdel(self):
        print("测试文本del")
        main("D:\\PyCharm\\PyCharm 2022.1.3\\pythonProject\\orig.txt","D:\\PyCharm\\PyCharm 2022.1.3\\pythonProject\\orig_0.8_del.txt")
    def testdis1(self):
        print("测试文本dis1")
        main("D:\\PyCharm\\PyCharm 2022.1.3\\pythonProject\\orig.txt","D:\\PyCharm\\PyCharm 2022.1.3\\pythonProject\\orig_0.8_dis_1.txt")
    def testdis10(self):
        print("测试文本dis10")
        main("D:\\PyCharm\\PyCharm 2022.1.3\\pythonProject\\orig.txt","D:\\PyCharm\\PyCharm 2022.1.3\\pythonProject\\orig_0.8_dis_10.txt")
    def testdis15(self):
        print("测试文本dis15")
        main("D:\\PyCharm\\PyCharm 2022.1.3\\pythonProject\\orig.txt","D:\\PyCharm\\PyCharm 2022.1.3\\pythonProject\\orig_0.8_dis_15.txt")


if __name__ == '__main__':
    unittest.main()