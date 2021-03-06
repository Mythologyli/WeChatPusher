import os
import json

from wechatpusher import WeChatPusher


def main():
    # 读取配置文件
    if os.path.exists('./config.json'):
        configs = json.loads(open('./config.json', 'r').read())
        corpid = configs["corpid"]
        agentid = configs["agentid"]
        corpsecret = configs["corpsecret"]
    else:
        print('配置文件 config.json 不存在！')
        return

    push = WeChatPusher(corpid, agentid, corpsecret)

    res = push.send('发送消息测试')
    if res == 0:
        print('发送消息成功！')
    else:
        print('发送消息失败！错误代码:', res)


if __name__ == "__main__":
    main()
