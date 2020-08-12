from Common.func_logger import logger
from Common.func_option import conf
import requests
import json

def __set_headers_nmb(token=None):
    headers = {
        "Content-Type":"application/json"
    }
    if token:
        headers["Authorization"] = "JWT {}".format(token)
    return headers


def send_request(method, url, data=None, token=None):
    # global resp
    headers = __set_headers_nmb(token)
    logger.info("**********发送一次http请求**********")
    logger.info("请求头是：{}".format(headers))
    logger.info("请求数据：{}".format(data))

    url = __request_url(url)
    data = __request_data(data)
    method = method.upper()
    logger.info("请求方法：{}".format(method))
    logger.info("请求地址：{}".format(url))
    if method == "GET":
        resp = requests.get(url, data, headers=headers)
    elif method == "POST":
        resp = requests.post(url, json=data, headers=headers)

    logger.info("响应状态码为：{}".format(resp.status_code))
    logger.info("响应数据为：{}".format(resp.text))

    return resp


def __request_data(data):
    if data is not None and isinstance(data, str):
        return json.loads(data)
    else:
        return data

def __request_url(url):
    base_url = conf.get("server", "base_url")
    if url.startswith("/"):
        return base_url + url
    else:
        return base_url + "/" + url


if __name__ == '__main__':
    login_url = "user/register/"
    login_datas = {"username": "axmaki", "email":"23526624@qq.com", "password":"123456", "password_confirm":"123456"}
    resp = send_request("POST", login_url, data=login_datas)
    # token = resp.json()["data"]["token_info"]["token"]

    # recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
    # recharge_data = {"member_id": 200119, "amount": 2000}
    # resp = send_request("POST",recharge_url,recharge_data,token)
    print(resp.json())