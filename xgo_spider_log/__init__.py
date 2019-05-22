import logging
import logging.handlers
import socket
import os
import json

delimiter = '|'

name = 'xgo_spider_log'


def create_logger(log_level=logging.DEBUG):
    """
    create monitor logger
    :param log_level logging log level
    :return: logging object
    """

    debug = (os.getenv('PROD') != '1')

    hostname = socket.gethostname()
    project_name = os.getenv('PROJECT_NAME')

    # create logger
    logger = logging.getLogger(project_name)
    logger.setLevel(log_level)

    class ContextFilter(logging.Filter):
        """
        This is a filter which injects contextual information into the log.
        """
        def filter(self, record):
            record.project_name = project_name
            record.delimiter = delimiter
            record.program = project_name
            return True
    logger.addFilter(ContextFilter())
    formatter = logging.Formatter('%(program)s %(project_name)s%(delimiter)s%(name)s%(delimiter)s%(asctime)s%(delimiter)s%(levelname)s%(delimiter)s%(message)s', "%Y-%m-%d %H:%M:%S")


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


monitor_logger = create_logger(logging.DEBUG)

def spider_start():
    msg = {
        'type': 'event',
        'content': '抓取开始'
    }
    monitor_logger.info(json.dumps(msg, ensure_ascii=False))

def spider_stop():
    msg = {
        'type': 'event',
        'content': '抓取结束'
    }
    monitor_logger.info(json.dumps(msg, ensure_ascii=False))

def spider_aborting():
    msg = {
        'type': 'event',
        'content': '异常结束'
    }
    monitor_logger.info(json.dumps(msg, ensure_ascii=False))

def spider_node_start():
    msg = {
        'type': 'event',
        'content': '节点抓取开始'
    }
    monitor_logger.info(json.dumps(msg, ensure_ascii=False))

def spider_node_stop():
    msg = {
        'type': 'event',
        'content': '节点抓取结束'
    }
    monitor_logger.info(json.dumps(msg, ensure_ascii=False))

def spider_node_aborting():
    msg = {
        'type': 'event',
        'content': '节点异常结束'
    }
    monitor_logger.info(json.dumps(msg, ensure_ascii=False))

def crawl_content(type, count):
    msg = {
        'type': 'count',
        'content_type': type,
        'count': count
    }
    monitor_logger.info(json.dumps(msg, ensure_ascii=False))

def queue_remaining(type, count):
    msg = {
        'type': 'count',
        'content_type': f'{type}-剩余',
        'count': count
    }
    monitor_logger.info(json.dumps(msg, ensure_ascii=False))

def general_log(log_dict):
    msg = {
        'type': 'general'
    }
    msg.update(log_dict)

    monitor_logger.info(json.dumps(msg, ensure_ascii=False))

def general_log_info(info):
    general_log({'info': info})
    

if __name__ == "__main__":
    spider_start()
    crawl_content('ahh', 1)
    queue_remaining('ahh', 1)