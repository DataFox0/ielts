# 雅思阅读Agent助手

一个基于AI的雅思阅读题目分析工具，支持多轮交互问答，帮助考生深入理解题目解析和同义替换。

## 功能特点

- 🎯 **智能题目分析**: 自动分析每道题的正确答案、原文定位、同义替换
- 🔍 **详细解析**: 提供解题思路、错误选项分析
- 💬 **多轮交互**: 支持用户就特定题目进行提问和追问
- 🆓 **免费API支持**: 支持DeepSeek、Moonshot等免费或低价API
- 📱 **友好界面**: 基于Streamlit的现代化Web界面

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置API

复制环境变量模板：
```bash
cp .env.example .env
```

编辑 `.env` 文件，填入你的API密钥：
```
OPENAI_API_KEY=your_api_key_here
OPENAI_API_BASE=https://api.deepseek.com/v1
MODEL_NAME=deepseek-chat
```

### 3. 获取免费API密钥

- **DeepSeek**: 访问 [https://platform.deepseek.com/](https://platform.deepseek.com/) 注册获取免费API密钥
- **Moonshot**: 访问 [https://platform.moonshot.cn/](https://platform.moonshot.cn/) 注册获取免费API密钥

### 4. 运行应用

```bash
streamlit run ielts_agent.py
```

## 使用方法

### 输入格式

1. **阅读文章**: 直接粘贴雅思阅读文章原文
2. **题目**: 每题一行，格式如：
   ```
   1. What is the main idea of the passage?
   2. According to the passage, what caused the problem?
   3. Which of the following is NOT mentioned in the passage?
   ```
3. **答案**: 每题一行，格式如：
   ```
   1. A
   2. C
   3. B
   ```

### 使用流程

1. 在左侧输入区域填写文章、题目和答案
2. 点击"开始分析"按钮
3. 查看每道题的详细解析
4. 在右侧问答区域提出疑问
5. 进行多轮交互直到完全理解

### 示例数据

你可以使用以下示例数据测试：

**文章**:
```
The rise of social media has fundamentally changed how people communicate and share information. Platforms like Facebook, Twitter, and Instagram have become integral parts of daily life for billions of users worldwide. While these platforms offer unprecedented connectivity, they also raise concerns about privacy, mental health, and the spread of misinformation.

Research conducted by the University of California found that excessive social media use can lead to increased anxiety and depression, particularly among young adults. The constant comparison with others' curated lives creates unrealistic expectations and feelings of inadequacy. However, the same study also revealed that moderate use of social media can strengthen social bonds and provide emotional support during difficult times.
```

**题目**:
```
1. What is the main idea of the passage?
2. According to the research, what is a negative effect of excessive social media use?
3. What positive aspect of social media is mentioned in the passage?
```

**答案**:
```
1. C
2. A
3. B
```

## 技术架构

- **前端**: Streamlit - 现代化的Python Web框架
- **后端**: OpenAI API兼容接口
- **AI模型**: 支持DeepSeek、Moonshot等模型
- **语言**: Python 3.7+

## 注意事项

- 确保API密钥的安全性，不要提交到代码仓库
- 免费API通常有调用次数限制，请合理使用
- 分析结果基于AI模型，建议结合人工判断
- 支持中英文混合输入和输出

## 更新日志

- v1.0.0: 基础功能实现，支持题目分析和问答交互

## 许可证

MIT License