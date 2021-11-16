import logging

def initializeLogger(name):
    logFormat = '[%(asctime)s] -> %(name)s -> [%(levelname)s]: %(message)s'
    dateFormat = '%d-%b-%y %H:%M'
    logging.basicConfig(level=logging.DEBUG,
                        format=logFormat,
                        datefmt=dateFormat,
                        filename='app.log',
                        filemode='a')
    logging.getLogger("urllib3").setLevel(logging.CRITICAL)
    return logging.getLogger(name)