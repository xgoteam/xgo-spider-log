### 介绍

本项目主要功能为发送钉钉通知使用

### 安装

```
pipenv install -e git+ssh://https://github.com/cielpy/hiii-dingding-notify.git#egg=hiii-dingding-notify
```

### 使用

```python
from spider_log import spider_start, spider_stop, queue_remaining, crawl_content, general_log

spider_start()
crawl_content('ahh', 1)
queue_remaining('ahh', 1)
general_log({'ahh': 111})
spider_stop()
```