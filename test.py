from xgo_spider_log import spider_start, spider_stop, spider_aborting

from xgo_spider_log import spider_node_start, spider_node_stop, spider_node_aborting

from xgo_spider_log import queue_remaining, crawl_content, general_log, general_log_info

spider_start()
crawl_content('酒店详情')
crawl_content('酒店详情', 10)
queue_remaining('酒店详情', 1)
spider_aborting()
general_log({'ahh': 111})
xxx = 'j@xgo.one'
general_log_info(f"账号{xxx}登录失败")
general_log_info(f"账号{xxx}无订单")
spider_stop()

spider_node_start()
spider_node_stop()
spider_node_aborting()