# !/usr/bin/env python
# coding=utf-8
import requests
import time
import random
import json
import logging


def autosubmit(auto_stop):
    url = "http://mina2.hbbyun.com/HBBAPI/GetData"

    # payload 贴上抓包的内容
    payload = ""

    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, "
                      "like Gecko) Mobile/15E148 MicroMessenger/7.0.10(0x17000a21) NetType/WIFI Languag",
        'Accept': "*/*",
        'Host': "mina2.hbbyun.com",
        'Referer': 'https://servicewechat.com/wxb455dc8601ea1ac2/16/page-frame.html',
        'Accept-Language': 'en-us'
    }
    count = 0
    while True:
        response = requests.request("POST", url, data=payload.encode(encoding='utf-8'), headers=headers)
        response.encoding = "utf-8"
        print_output = f"{'第'}{count}{'次运行-'}{time.strftime('%Y-%m-%d %H:%M:%S : ', time.localtime(time.time()))}" \
                       f"{response.content.decode('utf-8')} "
        print(print_output)
        logging.info(print_output)
        time.sleep(1 + 0.1 * random.randrange(-5, 10))
        count += 1
        try:
            err_code = json.loads(response.content)["errcode"]
        except json.decoder.JSONDecodeError:
            continue
        if err_code != "10008" and err_code != "69007":
            push_notification(print_output)
            break
        if count == 50000 and auto_stop:
            break


def push_notification(message):
    import requests

    # url中SCU自行进行替换
    url = "https://sc.ftqq.com/.send"

    querystring = {"text": "%E9%87%87%E8%8A%9D%E6%9E%97%E6%8E%A8%E9%80%81", "desp": message}

    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "PostmanRuntime/7.19.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "10707869-0be2-408f-9f2f-0d4b0e51edbf,f2022aca-d631-42e3-a564-893d4a79fc2b",
        'Host': "sc.ftqq.com",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "PHPSESSID=e36b1a41d2b34ee746319b82e166fce0",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


if __name__ == "__main__":
    logging.basicConfig(filename=f"{__file__}{'.log'}", filemode="w", level=logging.INFO)
    autosubmit(0)
