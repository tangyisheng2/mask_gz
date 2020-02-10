# !/usr/bin/env python
# coding=utf-8
import requests
import time
import random
import json


def autosubmit():
    person = {
        "mobile": "",  # 手机号
        "name": "",  # 姓名
        "category": "普通防护口罩",
        "commodity_id": "100003",
        "number": 10,
        "changeable": "yes",
        "time_code": "0",
        "wxmsg": 2,
        "identity": "",  # 身份证号码
        "mail_address": "",  # 留空
        "identityType": "身份证",
        "zone": "广州市",
        "shop_id": "GZ0001",
        "idcard": "身份证,44010xxxxx"  # 把44010xxxxx替换成自己的身份证
    }

    url = "http://wyjgzyy.govcloud.tencent.com/preorder/add"

    payload = json.dumps(person)

    headers = {
        "sessionid": "9a2575f7-44cf-458f-ba73-3f33487115f1",  # 这里的session id要自己抓包
        "Content-Type": "application/json",
        "Accept-Language": "en-us",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, "
                      "like Gecko) "
                      "Mobile/15E148 MicroMessenger/7.0.10(0x17000a21) NetType/WIFI Language/en",
        "Referer": "https://servicewechat.com/wx2ac2313767a99df9/24/page-frame.html",
        "appid": "microService-GUANGZHOU",
        "Content-Length": "311"
    }

    while True:
        response = requests.request("POST", url, data=payload.encode(encoding='utf-8'), headers=headers)
        response.encoding = "utf-8"
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S : ', time.localtime(time.time()))}{response.content.decode('utf-8')}")
        time.sleep(1 + 0.1 * random.randrange(-5, 10))


if __name__ == "__main__":
    autosubmit()
