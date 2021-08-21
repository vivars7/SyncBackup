import yaml


with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    #print(config.get('directories'))

    def data_sync(source, target):
        print(source)
        print(target)
'''

    [data_sync(source, target) for d in config.get('directories') for source, target in d.items()]
    #[data_sync(source, target) for source, target in config.get('directories')]
    #dirs = [{k:v for d in config.get('directories') for k, v in d.items()}]
    #print(config)
    #print(dirs)

'''
for d in config.get('directories'):
    print(d)
    print(d['source'])
