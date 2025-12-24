# azure-test

一个简单的 Azure Web App 项目，提供返回 "hello world" 的 JSON API。

## 功能

- GET `/` - 返回 JSON 格式的 hello world
- GET `/api` - 返回 JSON 格式的 hello world

## 部署到 Azure

1. 将代码推送到 GitHub
2. 在 Azure Portal 中配置部署中心，连接到 GitHub 仓库
3. Azure 会自动检测 Python 应用并部署

## 本地运行

```bash
pip install -r requirements.txt
python app.py
```

访问 http://localhost:8000 查看 API 响应。

