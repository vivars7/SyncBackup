def test1():
    return {'aaa':'111','bbb':[1,2,3,4,5]}

if __name__ == '__main__':
    print(test1()['bbb'][2])