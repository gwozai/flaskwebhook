from api import app
from api.messagechannel.qywx.qywxbot import WeChatBot
# 没有走main方法，获取app直接就运行了
try:
    bot = WeChatBot('4e35a96d-134b-45fa-9c5a-f3d4f65670f6')
    bot.send_text('消息通知 启动！')
except Exception as e:
    pass

if __name__ == '__main__':

    app.run()