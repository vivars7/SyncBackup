#-*- coding:utf-8 -*-
import asyncio
from dirsync import sync
import logger
import os
import sys
import yaml

log = logger.getLogger()

def load_config():
    with open('config.yaml', encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.FullLoader)

async def data_sync(data, purge=False):
    if not os.path.exists(data['source']):
        log.error('source directory not found - source : ' + data['source'])
        exit()

    if not os.path.exists(data['target']):
        os.makedirs(data['target'])

    sync(data['source'], data['target'], 'sync', logger=log, purge=purge)

def genData(args):
        result = {}
        if len(args) >= 2:
            arr = []
            for arg in args:
                if ('purge=' in arg) or (',' in arg):
                    if 'purge=' in arg:
                        result['purge'] = True if arg.split('purge=')[1].lower() == 'true' else False
                    else:
                        s = arg.split(',')
                        if len(s) >= 2:
                            temp = {}
                            temp['source'] = s[0]
                            temp['target'] = s[1]
                            arr.append(temp)
            result['directories'] = arr
        return result

async def main_async(args):
    if len(args) >= 2:
        data = genData(args)
        await asyncio.wait([data_sync(d, data['purge'] if 'purge' in data else False) for d in data['directories']])
    else:
        data = load_config()
        await asyncio.wait([data_sync(d, data.get('purge')) for d in data.get('directories')])

if __name__ == '__main__':
    asyncio.run(main_async(sys.argv))