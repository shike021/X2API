# 使用官方的Python基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /work

# 复制requirements.txt到容器中并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码到容器中
COPY . .

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 暴露端口
EXPOSE 8864

# 使用gunicorn启动应用
# 注意：在生产环境中，建议设置更多的gunicorn配置选项
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8864", "app.main:app"]