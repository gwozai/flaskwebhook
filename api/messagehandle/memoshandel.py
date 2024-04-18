from api.messagechannel.qywx.qywxbot import WeChatBot
def push_to_app1(data):
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

def push_to_app2(data):
    print("Pushing to Application 2:", data)

def push_to_app3(data):
    print("Pushing to Application 3:", data)
