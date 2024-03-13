import requests

# 代理设置
proxies = {
  "http": "http://localhost:8000",
  "https": "http://localhost:8000",
}

# HTTPS根证书路径
cert_path = "/Users/gngpp/VSCode/bypass-target/ca/cert.crt"

# 发送请求
response = requests.get("https://chat.openai.com/api/auth/csrf", proxies=proxies, verify=cert_path)

# 打印响应内容
print(response.text)