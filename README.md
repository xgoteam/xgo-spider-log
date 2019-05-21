### 介绍

本项目主要功能为发送钉钉通知使用

### 安装

```
pipenv install -e git+ssh://https://github.com/cielpy/hiii-dingding-notify.git#egg=hiii-dingding-notify
```

### 使用

```python
from dingding_notify.dingding_notify import send_message

send('通知内容', ['token'])
```