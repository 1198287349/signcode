
import hashlib

body = {


    "appkey": "gl_rn_9bec6a1f78be",
    "uid": "21933733",
    "token": "R2vosCsJ2jBlYSFjvvF0Sg==",
    "client": "android",
    "deviceId": "05090a81-a1f9-3079-a2fd-69e54dbec519",
    "encrypt": "1",
    "timestamp": "1651892379007",
    "version": "2.4.0",
    "branchNo": "0",
    "fundAccount": "500443676",
}


def sort_map():
    a = ""
    for i in sorted(body):
        a = a + i + body[i]
    print(a)
    return a


def get_md5():
    str_data = sort_map()
    sort_string = "CBxxxxF5" + str_data + "CBxxxxF5"
    up_string = sort_string.upper()
    print(up_string)
    md5_string = hashlib.md5(up_string.encode(encoding='UTF-8')).hexdigest()
    print(md5_string.center(50, "-"))
    return md5_string


if __name__ == '__main__':
    get_md5()

