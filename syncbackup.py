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

async def data_sync(data):
    '''
    target 경로가 존재하지 않으면 생성.
    '''
    check_target_path(data['target'])

    sync(data['source'], data['target'], 'sync', logger=logger.getLogger(), purge=config.get('purge'))


async def main_async(args):
    def genData(args):
        data = {}
        data['source'].append(1)
        print(data)
        for i in range(len(args)):
            if i % 2 == 1:
                data = data + 'source'
            else:
                print(args[i])

    print('::::::')
    print(genData(args))
    print('::::::')
    print(config.get('directories'))
    await asyncio.wait([data_sync(d) for d in config.get('directories')])

if __name__ == '__main__':
    print(len(sys.argv))
    asyncio.run(main_async(sys.argv))