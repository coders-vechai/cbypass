# bypass

绕过cloudflare TLS指纹校验的Http代理

### Python用法

```shell
# Clone
git clone https://github.com/gngpp/cbypass.git && cd cbypass

# Install
wget https://github.com/gngpp/cbypass/releases/download/0.1/bypass-latest-x86_64-unknown-linux-musl.tar.gz
tar -xf bypass-latest-x86_64-unknown-linux-musl.tar.gz
nohup ./bypass run &

python3 -m venv venv
source venv/bin
pip install requests

python3 python.py
```
