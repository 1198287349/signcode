# !/usr/bin/python3
# -*- coding:utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         guilv
# Author:       Android玄机
# Date:         2022/07/31‘


# -------------------------------------------------------------------------------

import hashlib

body = {

    "appkey": "xxx",
    "uid": "xxx",
    "token": "xxx",
    "client": "android",
    "deviceId": "xxx--xxxx--xxxx",
    "encrypt": "1",
    "timestamp": "xxx",
    "version": "3.0.0",
    "branchNo": "0",
    "fundAccount": "xxx",
}


def sort_map():
    a = ""
    for i in sorted(body):
        a = a + i + body[i]
  
    return a


def get_md5():
    str_data = sort_map()
    sort_string = "xxxkey联系1198287349" + str_data + "xxxkey联系1198287349"
    up_string = sort_string.upper()
 
    md5_string = hashlib.md5(up_string.encode(encoding='UTF-8')).hexdigest()
    print(md5_string.center(50, "-"))
    return md5_string

if __name__ == '__main__':
    get_md5()

