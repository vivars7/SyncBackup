#-*- coding:utf-8 -*-
import asyncio
from dirsync import sync
import os
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

    sync(data['source'], data['target'], 'sync', purge=config.get('purge'))

async def main_async():
    await asyncio.wait([data_sync(d) for d in config.get('directories')])

asyncio.run(main_async())