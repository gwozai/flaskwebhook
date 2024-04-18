import requests

def send_data_to_webhook():
    url = 'http://127.0.0.1:5000/webhook'  # 替换成你的Webhook URL
    headers = {'Content-Type': 'application/json'}
    data = {
        "type": "text",
        "content": "这是一条测试消息"
    }

    # 发送POST请求
    response = requests.post(url, json=data, headers=headers)

    # 打印响应信息
    print("状态码:", response.status_code)
    print("响应内容:", response.json())

if __name__ == "__main__":
    send_data_to_webhook()
