import base64
import hashlib
import hmac
import json
import threading
import time
from urllib.request import urlopen
import urllib.parse

from . import constant

dict = {
    "msgtype": "markdown",
    "markdown": {"title": "",
                 "text": ""
                 },
    "at": {
        "isAtAll": True
    }
}


def sendDingMsg(url, sendDatas, header):
    request = urllib.request.Request(url, data=sendDatas, headers=header)
    opener = urllib.request.urlopen(request)
    return opener


def getTimestamp():
    return str(round(time.time() * 1000))


def getSign(secret):
    secret_enc = secret.encode('utf-8')
    get_string_to_sign_enc = '{}\n{}'.format(getTimestamp(), secret).encode('utf-8')
    get_hmac_code = hmac.new(secret_enc, get_string_to_sign_enc, digestmod=hashlib.sha256).digest()
    return urllib.parse.quote_plus(base64.b64encode(get_hmac_code))


lock = threading.RLock()


def genDingTalkMsg(ding_url, secret, title, msg, isAtAll=False):
    lock.acquire()
    # get_sign = getSign(secret)
    # dongtai_ding_final_url = f'{ding_url}&timestamp={getTimestamp()}&sign={get_sign}'

    # 把文案内容写入请求格式中
    dict["markdown"]["title"] = f'{constant.constant.get_app_name()}:{title}'
    dict["markdown"]["text"] = f'{constant.constant.get_app_name()}:{msg}'
    dict["at"]["isAtAll"] = isAtAll
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    sendData = json.dumps(dict)
    sendDatas = sendData.encode("utf-8")
    opener = None
    times = 5
    while times > 0:
        time.sleep(3)
        try:
            opener = sendDingMsg(f'{ding_url}&timestamp={getTimestamp()}&sign={getSign(secret)}', sendDatas, header)
            result = opener.read()
            object = json.loads(result)
            if object["errcode"] == 0:
                break

            print(
                f'{constant.constant.is_release_version()} genDingTalkMsg{ding_url} errcode ：{object["errcode"]}')
        except BaseException as e:
            print(f'{constant.constant.is_release_version()} genDingTalkMsg{ding_url} 报错 ： {e}')
        finally:
            times -= 1

    lock.release()
    return opener


def getDingAccount():
    if constant.constant.is_release():
        return constant.constant.get_release_ding_url(), constant.constant.get_release_ding_secret()
    else:
        return constant.constant.get_dev_ding_url(), constant.constant.get_dev_ding_secret()


def unimportantMsg(title, msg):
    return genDingTalkMsg(getDingAccount()[0], getDingAccount()[1], title, msg, False)


def importantMsg(title, msg):
    return genDingTalkMsg(getDingAccount()[0], getDingAccount()[1], title, msg, True)
