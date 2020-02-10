# !/usr/bin/env python
# coding=utf-8
import requests
import time
import json
import logging


def autosubmit(auto_stop):
    url = "http://mina.hbbyun.com/HBBAPI/GetData"

    payload = 'HBBWSType=1&strKeyName=Goods_GoodsBaseStockGet_V3_Get&strJsonData=%7B%22tableData%22%3A%5B%7B%22EntID' \
              '%22%3A%22881350672161%22%2C%22UserID%22%3A%22888420198324%22%2C%22ShopID%22%3A%22889089848428%22%2C' \
              '%22GoodsID%22%3A%22886284008218%22%2C%22AppID%22%3A%22%40AppID%22%2C%22Secret%22%3A%22%40Secret%22%2C' \
              '%22BSN%22%3A%22%40BSN%22%2C%22SourceType%22%3A%22Shop%22%2C%22IsSale%22%3A%222%22%2C%22IsGetSku%22%3A' \
              '%221%22%7D%5D%7D&strAuthorizationCode=hbb&IsRSA=0 '
    headers = {

        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,deflate,br",
        "Connection": "keep-alive",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, "
                      "like Gecko) Mobile/14G60 MicroMessenger/6.7.0 NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxb455dc8601ea1ac2/16/page-frame.html",
        "Content-Length": "2797"
    }
    count = 0
    while True:
        count += 1
        response = requests.request("POST", url, data=payload.encode(encoding='utf-8'), headers=headers)
        response.encoding = "utf-8"
        try:
            table_0_bal = json.loads(response.content)['data']['table1'][0]['BalQua']
            table_1_bal = json.loads(response.content)['data']['table2'][0]['BalQua']
        except KeyError:
            continue
        if table_0_bal != "0.0000" or table_1_bal != "0.0000":
            print_output = f"{'第'}{count}{'次运行-有货！'}{time.strftime('%Y-%m-%d %H:%M:%S : ', time.localtime(time.time()))}" \
                           f"{response.content.decode('utf-8')} "
            push_notification(print_output)
        else:
            print_output = f"{'第'}{count}{'次运行-无货！'}{time.strftime('%Y-%m-%d %H:%M:%S : ', time.localtime(time.time()))}" \
                           f"{response.content.decode('utf-8')} "
        print(print_output)
        logging.info(print_output)
        time.sleep(1)


def push_notification(message):
    # url中SCU自行进行替换
    url = "https://sc.ftqq.com/SCUID.send"

    querystring = {"text": "采芝林口罩有货啦！", "desp": message}

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
