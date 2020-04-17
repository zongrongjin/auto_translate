from event import ctrl_a, ctrl_v, ctrl_x, send_text, get_text, set_text, tap_enter
import keyboard
import requests
import time
import hashlib

def MD5(s):
    md = hashlib.md5()
    md.update(s.encode('utf-8'))
    return md.hexdigest()

def trans(string):
    sign = MD5('你的百度翻译api的appid' + string + '1435660288你的百度翻译api密钥')
    api = f'http://api.fanyi.baidu.com/api/trans/vip/translate?q={string}&from=zh&to=en&appid=20200417000422755&salt=1435660288&sign={sign}'
    res = requests.get(api)
    return res.json()['trans_result'][0]['dst']

def main():
    ctrl_a()
    ctrl_x()
    cn = get_text()
    en = trans(cn)
    set_text(en)
    ctrl_v()
    tap_enter()

if __name__ == "__main__":
    while 1:
        keyboard.add_hotkey('ctrl+s', main)
        keyboard.wait()