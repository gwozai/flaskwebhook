from api.messagechannel.qywx.qywxbot import WeChatBot
from api.messagechannel.qywx.utils import fetch_and_encode_image


def push_to_app1(data):
    try:
        activity_type = data['activityType']
        # print("activityType:", activity_type)

        # Only process if the activity type is not memo deletion
        if activity_type != "memos.memo.deleted":
            bot = WeChatBot('4e35a96d-134b-45fa-9c5a-f3d4f65670f6')

            # Process creation or updates only
            if activity_type in ["memos.memo.created", "memos.memo.updated"]:
                memo_content = data['memo']['content']
                # print("Processing memo:", memo_content)
                bot.send_text(memo_content)
                # Optionally, you can use send_markdown if needed
                # bot.send_markdown(memo_content)
        else:
            print("Memo deletion event, no action taken")
    except Exception as e:
        bot = WeChatBot('4e35a96d-134b-45fa-9c5a-f3d4f65670f6')
        bot.send_text(e)


def push_to_app2(data):
    try:
        bot = WeChatBot('4e35a96d-134b-45fa-9c5a-f3d4f65670f6')
        if data.get('type') == 'image':
            # 这里可以添加处理图像的代码
            url = data.get('content')
            base64_data, md5 = fetch_and_encode_image(url)
            bot.send_image(base64_data, md5)

        elif data.get('type') == 'text':
            # 这里可以添加处理文本的代码
            bot.send_text(data['content'])

        else:
            pass
    except Exception as e:
        bot = WeChatBot('4e35a96d-134b-45fa-9c5a-f3d4f65670f6')
        bot.send_text(e)

def push_to_app3(data):
    print("Pushing to Application 3:", data)
