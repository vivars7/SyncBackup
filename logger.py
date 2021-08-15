"""Create Logger

Functions:
    getLogger(logger_name)
"""
import logging.config
import yaml
import os

def getLogger(logger_name=None):    
    def get_last_index(s):
        idx1 = s.rfind('\\')
        idx2 = s.rfind('/')
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

    if logger_name == None:
       logger_name = 'backuplog'
    
    if len([s for s in config.get('loggers') if s == logger_name]) == 0:
        logging.config = logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger(logger_name)

    return logger