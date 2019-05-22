from spider_log import spider_start, spider_stop, queue_remaining, crawl_content, general_log

spider_start()
crawl_content('ahh', 1)
queue_remaining('ahh', 1)
general_log({'ahh': 111})
spider_stop()