import random
from fake_useragent import UserAgent

def generate_fake_headers(Cookie):
    # 初始化随机 User-Agent
    ua = UserAgent()

    # 随机生成 headers
    headers = {
        "User-Agent": ua.random,  # 随机 User-Agent
        "Accept": random.choice([
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "application/json, text/javascript, */*; q=0.01"
        ]),
        "Accept-Language": random.choice([
            "zh-CN,zh;q=0.9",
            "zh-TW,zh;q=0.8,en-US;q=0.7,en;q=0.6"
        ]),
         "Accept-Encoding": random.choice([
            "gzip, deflate, br",  # 常见的组合，支持 Brotli
            "gzip, deflate",      # 不支持 Brotli
            "gzip",               # 仅支持 gzip
            "deflate",            # 仅支持 deflate
            "*",                  # 表示支持所有压缩方式
            ""                    # 不支持任何压缩方式
        ]),
        "Connection": "keep-alive",
        "Referer": random.choice([
            "https://www.baidu.com/",
            "https://index.baidu.com/"
        ]),
        "Cookie": Cookie,  
        "Host": "index.baidu.com",  # 目标站点的 Host
        "Sec-Fetch-Dest": random.choice(["empty", "document", "script", "image"]),
        "Sec-Fetch-Mode": random.choice(["cors", "no-cors", "same-origin", "navigate"]),
        "Sec-Fetch-Site": random.choice(["same-origin", "same-site", "cross-site"]),
    }
    return headers
