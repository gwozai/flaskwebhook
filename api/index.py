from api import app
from api.messagechannel.qywx.qywxbot import WeChatBot

if __name__ == '__main__':
    try:
        bot = WeChatBot('4e35a96d-134b-45fa-9c5a-f3d4f65670f6')
        bot.send_text('pushed 启动！')
    except Exception as e:
        pass
    app.run()