import requests
import json
import os

class WeChatBot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={self.api_key}'
        self.headers = {'Content-Type': 'application/json'}
        self.upload_url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={self.api_key}'
    def send_message(self, data):
        response = requests.post(self.base_url, headers=self.headers, data=json.dumps(data))
        return response.json()

    def send_text(self, content, mentioned_list=None, mentioned_mobile_list=None):
        data = {
            "msgtype": "text",
            "text": {
                "content": content,
                "mentioned_list": mentioned_list if mentioned_list else [],
                "mentioned_mobile_list": mentioned_mobile_list if mentioned_mobile_list else []
            }
        }
        return self.send_message(data)

    def send_markdown(self, content):
        data = {
            "msgtype": "markdown",
            "markdown": {"content": content}
        }
        return self.send_message(data)

    def send_image(self, base64_data, md5):
        data = {
            "msgtype": "image",
            "image": {
                "base64": base64_data,
                "md5": md5
            }
        }
        return self.send_message(data)

    # 发送图文类型的
    def send_news(self, articles):
        data = {
            "msgtype": "news",
            "news": {
                "articles": articles
            }
        }
        return self.send_message(data)



    def upload_media(self, file_path, media_type):
        url = f"{self.upload_url}&type={media_type}"
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        with open(file_path, 'rb') as file:
            files = {'media': (file_name, file, 'application/octet-stream', {'filename': file_name, 'filelength': file_size, 'Content-Type': 'application/octet-stream'})}
            response = requests.post(url, files=files)
            return response.json()

    def upload_media_fromurl(self, file_url, media_type):
        url = f"{self.upload_url}&type={media_type}"
        response = requests.get(file_url)  # 获取网络文件的响应
        if response.status_code == 200:
            file_content = response.content  # 文件内容
            file_name = os.path.basename(file_url)  # 从URL提取文件名
            file_size = len(file_content)  # 文件大小，通过内容长度获取
            files = {
                'media': (
                    file_name,
                    file_content,
                    'application/octet-stream',
                    {'filename': file_name, 'filelength': file_size, 'Content-Type': 'application/octet-stream'}
                )
            }
            response = requests.post(url, files=files)
            return response.json()
        else:
            return {'error': 'Failed to download file', 'status_code': response.status_code}

    def send_media(self, media_type, response):
        if response.get("media_id"):
            data = {
                "msgtype": media_type,
                media_type: {"media_id": response["media_id"]}
            }
            return self.send_message(data)
        else:
            return response


bot = WeChatBot('4e35a96d-134b-45fa-9c5a-f3d4f65670f6')
# 发送网络文件
# file_path = 'http://1.15.7.2:9000/album/1.mp4'
# media_type = 'file'  # Can be 'image', 'voice', 'video', or 'file'
# response = bot.upload_media_fromurl(file_path, media_type)
# print(response)
# response = bot.send_media(media_type, response)
# print(response)


# 发送文件
# file_path = '../../../static/1.mp3'
# media_type = 'file'  # Can be 'image', 'voice', 'video', or 'file'
# response = bot.upload_media(file_path, media_type)
# print(response)
# response = bot.send_media(media_type, response)
# print(response)


# bot = WeChatBot('4e35a96d-134b-45fa-9c5a-f3d4f65670f6')

# 发送图文类型的
# articles = [
#     {
#         "title": "中秋节礼品领取",
#         "description": "今年中秋节公司有豪礼相送",
#         "url": "www.qq.com",
#         "picurl": "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
#     }
# ]
# news_response = bot.send_news(articles)
# print(news_response)


# 发送网络图片
# url = 'http://1.15.7.2:9000/picshow/imfree/202404180158353.png'
# base64_data, md5 = fetch_and_encode_image(url)
# print("Base64 Data:", base64_data)
# print("MD5 Hash:", md5)
# image_response = bot.send_image(base64_data, md5)
# print(image_response)


# base64_data, md5 = encode_image_to_base64('11_168153_d43157c29a981f4.png')
# print("Base64 Data:", base64_data)
# print("MD5 Hash:", md5)

# image_response = bot.send_image(base64_data, md5)
# print(image_response)

# text_response = bot.send_text('Hello world', mentioned_list=["userid1", "userid2"],
#                               mentioned_mobile_list=["12345678901", "10987654321"])
# text_response = bot.send_text('Hello world')
# print(text_response)
# markdown_content = """# Daily Weather Forecast
#
# **Location:** Springfield
# **Date:** April 18, 2024
#
# **Overview:**
# Partly cloudy with a chance of afternoon showers.
# **Temperature:** High of 75°F (24°C), Low of 52°F (11°C)
# **Humidity:** 78%
# **Wind:** South at 10 to 15 mph
#
# ## Hourly Forecast:
# - **06:00 AM:** 54°F, Mostly cloudy
# - **09:00 AM:** 64°F, Partly sunny
# - **12:00 PM:** 72°F, Cloudy
# - **03:00 PM:** 75°F, Light showers
# - **06:00 PM:** 70°F, Clearing skies
#
# ## Safety Tips:
# - Carry an umbrella or raincoat.
# - Stay hydrated and apply sunscreen during sunny intervals.
#
# For more details, visit [Weather Channel](http://www.weather.com)."""
# markdown_response = bot.send_markdown(markdown_content)
#
# print(markdown_response)