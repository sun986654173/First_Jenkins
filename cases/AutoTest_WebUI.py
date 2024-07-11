from lib.Webui import webui
from lib.cfg import *
import time

# 使用上下文管理器管理 WebDriver 的生命周期
with webui() as driver:
    # 创建 WebUI 实例
    web_ui = webui()
    web_ui.driver = driver

    # 打开百度网站
    web_ui.open_website(target_url)

    # 在搜索框中输入关键字并搜索
    web_ui.search('kw', 'byhy')

    # 等待一段时间以便查看搜索结果
    time.sleep(5)
