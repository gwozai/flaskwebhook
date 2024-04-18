import requests

def send_data_to_webhook():
    url = 'https://memoswebhook.gwozai.com/webhook'  # 替换成你的Webhook URL
    headers = {'Content-Type': 'application/json'}
    data = {
        "type": "file",
        "content": "http://1.15.7.2:9000/album/1.mp4"
    }

    # 发送POST请求
    response = requests.post(url, json=data, headers=headers)

    # 打印响应信息
    print("状态码:", response.status_code)
    print("响应内容:", response.json())

if __name__ == "__main__":
    send_data_to_webhook()
