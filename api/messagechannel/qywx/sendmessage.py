import requests
import json
import os
class WeChatBot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={self.api_key}'
        self.upload_url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={self.api_key}'

    def send_message(self, data):
        response = requests.post(self.base_url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        return response.json()

    def upload_media(self, file_url, media_type):
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



# file_path = 'lishi.txt'
# media_type = 'file'  # Can be 'image', 'voice', 'video', or 'file'
# response = bot.upload_media(file_path, media_type)
# print(response)
# response = bot.send_media(media_type, response)

# file_path = '11_168153_d43157c29a981f4.png'
# media_type = 'image'  # Can be 'image', 'voice', 'video', or 'file'
# response = bot.upload_media(file_path, media_type)
# print(response)
# response = bot.send_media(media_type, response)


# file_path = '1.mp4'
# media_type = 'file'  # Can be 'image', 'voice', 'video', or 'file'
# response = bot.upload_media(file_path, media_type)
# print(response)
# media_type = 'file'
# response = bot.send_media(media_type, response)
# print(response)


# file_path = 'http://1.15.7.2:9000/album/1.mp4'
# media_type = 'file'  # Can be 'image', 'voice', 'video', or 'file'
# response = bot.upload_media(file_path, media_type)
# print(response)
# response = bot.send_media(media_type, response)
# print(response)