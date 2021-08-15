import logging.config
import yaml
import os

def get_last_index(s):
    idx1 = 0
    idx2 = 0
    try:
        idx1 = s.rindex('\\')
    except ValueError:
        idx1 = 0
    try:
        idx2 = s.rindex('/')
    except ValueError:
        idx2 = 0

    print(idx1)
    print(idx2)

    return idx1 if idx1 > idx2 else idx2

logging_config_path = 'logging.yaml'
if os.path.exists(logging_config_path):
    with open(logging_config_path) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        logfile_path = config.get('handlers').get('file').get('filename')
        logdir_path = logfile_path[:get_last_index(logfile_path)]
        if not os.path.exists(logdir_path):
            os.makedirs(logdir_path)
        try:
            logging.config.dictConfig(config)
        except Exception as e:
            print(e)
else:
    logging.basicConfig(level=logging.INFO)

logging.getLogger(__name__)

logging.info("AAAAA")