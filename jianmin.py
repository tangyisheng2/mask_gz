# !/usr/bin/env python
# coding=utf-8


import json
import logging
import random
import time
import requests


def autosubmit(auto_stop):
    url = "http://wechat.gzjmyy.com:8088/JmFMResrv/main/reser"

    person = {  # 自行抓包
        "PLACEPOINTID": "",
        "USERNAME": "", # 用户名除姓外其他使用**打码
        "MOBILE": "", # 完整手机
        "USERID": "", # 除前后4位外其他使用**打码
        "USERNAMEMD5": "", # 用户名算MD5
        "USERMOBILEMD5": "", # 手机算MD5
        "USERIDMD5": "" # 身份证算MD5
    }

    payload = json.dumps(person)
    headers = {
        'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, "
                      "like Gecko) Mobile/14G60 MicroMessenger/6.7.0 NetType/WIFI Language/zh_CN",
        'Content-Type': "application/json",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "19d245ad-342c-4cbb-97aa-f9c2fe4920f9,c630659f-dfec-4d6d-b355-2ba198d13d39",
        'Host': "wechat.gzjmyy.com:8088",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "288",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    count = 0
    while True:
        try:
            response = requests.request("POST", url, data=payload.encode(encoding='utf-8'), headers=headers,
                                        timeout=3.05)
            response.encoding = "utf-8"
        except:
            print(f"{'第'}{count}{'次运行-尝试预约'}{time.strftime('%Y-%m-%d %H:%M:%S : ', time.localtime(time.time()))}"
                  f"{'连接失败'}")
            count += 1
            continue
        print_output = f"{'第'}{count}{'次运行-尝试预约'}{time.strftime('%Y-%m-%d %H:%M:%S : ', time.localtime(time.time()))}" \
                       f"{response.content.decode('utf-8')} "
        print(print_output)
        logging.info(print_output)
        count += 1
        try:
            rc = json.loads(response.content)["RC"]
        except json.decoder.JSONDecodeError:
            continue
        if rc != 3 and rc != 1:
            push_notification(print_output)
            if check_success(count) == 1:
                break
        time.sleep(1 + 0.1 * random.randrange(-5, 10))


def check_success(count):
    url = "http://wechat.gzjmyy.com:8088/JmFMResrv/main/queryReservStatus"

    person = {  # 自行抓包
        "USERNAMEMD5": "",
        "USERMOBILEMD5": "",
        "USERIDMD5": ""
    }

    payload = json.dumps(person)
    headers = {
        'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, "
                      "like Gecko) Mobile/14G60 MicroMessenger/6.7.0 NetType/WIFI Language/zh_CN",
        'Content-Type': "application/json",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "19d245ad-342c-4cbb-97aa-f9c2fe4920f9,c630659f-dfec-4d6d-b355-2ba198d13d39",
        'Host': "wechat.gzjmyy.com:8088",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "288",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload.encode(encoding='utf-8'), headers=headers)
    response.encoding = "utf-8"
    json_encoded = json.loads(response.content)
    print_output = f"{'第'}{count}{'次运行-检查预约'}{time.strftime('%Y-%m-%d %H:%M:%S : ', time.localtime(time.time()))}" \
                   f"{json_encoded} "
    if json_encoded['RC'] == 1:
        print(print_output)
        push_notification(f"{'预约成功，预约号为下方PKID'}{print_output}")
    logging.info(print_output)
    return json_encoded['RC']


def push_notification(message):
    # url中SCU自行进行替换
    url = "https://sc.ftqq.com/SCU1.send"

    querystring = {"text": "健民口罩预约", "desp": message}

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
