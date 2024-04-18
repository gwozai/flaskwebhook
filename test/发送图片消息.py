import requests

def send_data_to_webhook():
    url = 'https://memoswebhook.gwozai.com/webhook'  # 替换成你的Webhook URL
    headers = {'Content-Type': 'application/json'}
    data = {
        "type": "image",
        "content": "https://file.ertuba.com/2023/0128/eff35cb25cfbd1b05ebaff35465d153c.jpg"
    }

    # 发送POST请求
    response = requests.post(url, json=data, headers=headers)

    # 打印响应信息
    print("状态码:", response.status_code)
    print("响应内容:", response.json())

if __name__ == "__main__":
    send_data_to_webhook()
