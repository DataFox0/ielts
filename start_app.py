import os
import subprocess

# 设置环境变量避免Streamlit询问邮箱
os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'

# 启动Streamlit应用
subprocess.run(['streamlit', 'run', 'ielts_agent.py', '--server.port=8501', '--server.address=localhost'])