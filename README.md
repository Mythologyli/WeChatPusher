# WeChatPusher

企业微信应用消息推送

## 功能

+ 发送文本卡片消息

## 测试方法

+ 使用 config.json.templ 文件为模版创建 config.json 文件，填写企业ID、企业应用ID、应用的凭证密钥
+ 运行 ``python3 test.py``

## 使用方法

+ ``from wechatpusher import WeChatPusher``
+ 创建实例 ``WeChatPusher(corpid, agentid, corpsecret)``
+ 使用 push 方法发送文本卡片消息
  
  必选参数：
  + title: 标题，不超过 128 个字节，超过会自动截断
  
  可选参数有：
  + description: 描述，不超过 512 个字节，超过会自动截断。默认与标题一致
  + url: 点击后跳转的链接。最长 2048 字节，请确保包含了协议头(http/https)。默认为 https://github.com/Mythologyli/WeChat-Push
  + btntxt: 按钮文字。默认为“详情”，不超过 4 个文字，超过自动截断
  + user: 成员ID列表（消息接收者，多个接收者用‘|’分隔，最多支持 1000 个）。特殊情况：指定为 @all，则向关注该企业应用的全部成员发送。默认为 @all