#-*- coding:utf-8 -*-
import asyncio
from dirsync import sync
import logger
import os
import sys
import yaml

with open('config.yaml', encoding='utf-8') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

def check_target_path(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print('Error: Create Target Directory. ' + path)

async def data_sync(data, purge=False):
    # target 경로가 존재하지 않으면 생성.
    check_target_path(data['target'])

    sync(data['source'], data['target'], 'sync', logger=logger.getLogger(), purge=purge)


async def main_async(args):
    def genData(args):
        data = {}
        if len(args) >= 2:
            for arg in args:
                if 'purge=' in arg:
                    data['purge'] = True if arg.split('purge=')[1] == 'true' else False
                else:
                    arr = []
                    s = arg.split(',')
                    if len(s) >= 2:
                        temp = {}
                        temp['source'] = s[0]
                        temp['target'] = s[1]
                        arr.append(temp)
                    data['data'] = arr
        return data

    argsData = genData(args)['data'] if 'data' in genData(args) else ''
    purge = genData(args)['purge'] if 'purge' in genData(args) else config.get('purge')
    data = argsData if not len(argsData) == 0 else config.get('directories')
    print('****************')
    print(data)
    print('****************')
    await asyncio.wait([data_sync(d, purge) for d in data])

if __name__ == '__main__':
    asyncio.run(main_async(sys.argv))