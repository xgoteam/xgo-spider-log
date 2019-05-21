import logging
import logging.handlers
import socket
import os

delimiter = '|'


def create_logger(logger_type, log_level=logging.DEBUG):
    """
    create monitor logger
    :param log_level logging log level
    :return: logging object
    """

    debug = (os.getenv('PROD') != '1')

    hostname = socket.gethostname()
    project_name = os.getenv('PROJECT_NAME')

    # create logger
    logger = logging.getLogger(project_name + '-' + logger_type)
    logger.setLevel(log_level)

    class ContextFilter(logging.Filter):
        """
        This is a filter which injects contextual information into the log.
        """
        def filter(self, record):
            record.hostname = hostname
            record.project_name = project_name
            record.logger_type = logger_type
            record.delimiter = delimiter
            return True
    logger.addFilter(ContextFilter())
    formatter = logging.Formatter('%(hostname)s%(delimiter)s%(project_name)s%(delimiter)s%(name)s%(delimiter)s%(asctime)s%(delimiter)s%(levelname)s%(delimiter)s%(logger_type)s%(delimiter)s%(message)s')


    if debug:
        # create stream logger handler
        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    else:
        # create syslog logger handler
        sh = logging.handlers.SysLogHandler(address='/var/log/spider.sock')
        sh.setLevel(log_level)
        sh.setFormatter(formatter)
        logger.addHandler(sh)

    return logger


count_monitor_logger = create_logger('count')
info_monitor_logger = create_logger('info')

def spider_start():
    msg = {
        'info': '抓取开始'
    }
    info_monitor_logger.info(json.dumps(msg))

def spider_stop():
    msg = {
        'info': '抓取结束'
    }
    info_monitor_logger.info(json.dumps(msg))

def crawl_content(type, count):
    msg = {
        'type': type,
        'count': count
    }
    count_monitor_logger.info(json.dumps(msg))

def queue_remaining(type, count):
    count_monitor_logger.info(delimiter.join([f'{type}-剩余', str(count)]))
    

if __name__ == "__main__":
    spider_start()
    crawl_content('ahh', 1)
    queue_remaining('ahh', 1)