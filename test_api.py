import os
import openai
from dotenv import load_dotenv

load_dotenv()

def test_api():
    """测试API配置是否正确"""
    api_key = os.getenv('OPENAI_API_KEY')
    api_base = os.getenv('OPENAI_API_BASE', 'https://api.deepseek.com/v1')
    model_name = os.getenv('MODEL_NAME', 'deepseek-chat')
    
    if not api_key or api_key == 'your_api_key_here':
        print("❌ 错误: API密钥未配置")
        print("请编辑 .env 文件，设置 OPENAI_API_KEY")
        return False
    
    try:
        client = openai.OpenAI(
            api_key=api_key,
            base_url=api_base
        )
        
        # 发送简单测试请求
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": "Hello, this is a test."}],
            max_tokens=10
        )
        
        print("✅ API配置正确！")
        print(f"使用模型: {model_name}")
        print(f"API端点: {api_base}")
        print(f"响应: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ API测试失败: {str(e)}")
        print("请检查:")
        print("1. API密钥是否正确")
        print("2. 网络连接是否正常")
        print("3. API余额是否充足")
        return False

if __name__ == "__main__":
    test_api()