import streamlit as st
import openai
import os
from typing import List, Dict, Optional
import json
import re
from dotenv import load_dotenv

load_dotenv()

class IELTSReadingAgent:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.api_base = os.getenv('OPENAI_API_BASE', 'https://api.deepseek.com/v1')
        self.model_name = os.getenv('MODEL_NAME', 'deepseek-chat')
        
        if not self.api_key:
            raise ValueError("请设置OPENAI_API_KEY环境变量")
        
        self.client = openai.OpenAI(
            api_key=self.api_key,
            base_url=self.api_base
        )
        
        if "conversation_history" not in st.session_state:
            st.session_state.conversation_history = []
    
    def analyze_reading_passage(self, passage: str, questions: List[str], answers: List[str]) -> Dict:
        """分析阅读文章和题目"""
        prompt = f"""
        你是一个专业的雅思阅读老师。请分析以下雅思阅读文章和题目。

        文章：
        {passage}

        题目：
        {chr(10).join([f"{i+1}. {q}" for i, q in enumerate(questions)])}

        标准答案：
        {chr(10).join([f"{i+1}. {a}" for i, a in enumerate(answers)])}

        请为每道题提供详细解析，包括：
        1. 原文定位语句（精确到句子）
        2. 同义替换分析
        3. 解题思路和技巧
        4. 错误选项分析

        请以JSON格式输出，结构如下：
        {{
            "questions": [
                {{
                    "question_number": 1,
                    "correct_answer": "A",
                    "location_sentence": "原文中的定位句子",
                    "synonym_replacement": {{
                        "原文词汇": "题目中的同义替换",
                        "原文短语": "题目中的同义替换"
                    }},
                    "explanation": "详细的解题思路",
                    "wrong_options_analysis": "错误选项的分析"
                }}
            ]
        }}
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=8100
            )
            
            result = response.choices[0].message.content
            # 清理JSON响应
            result = re.sub(r'```json\n?', '', result)
            result = re.sub(r'\n?```', '', result)
            
            return json.loads(result)
        except Exception as e:
            st.error(f"分析失败: {str(e)}")
            return {"questions": []}
    
    def answer_question(self, question: str, context: str) -> str:
        """回答用户关于特定题目的疑问"""
        prompt = f"""
        你是一个专业的雅思阅读老师。基于之前的分析，请回答学生的问题。

        相关上下文：
        {context}

        学生问题：
        {question}

        请提供详细、清晰的解答，帮助学生理解。
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
                max_tokens=2000
            )
            
            return response.choices[0].message.content
        except Exception as e:
            return f"抱歉，回答问题时出现错误: {str(e)}"

def main():
    st.set_page_config(page_title="雅思阅读Agent助手", page_icon="📚", layout="wide")
    
    st.title("📚 雅思阅读Agent助手")
    st.markdown("---")
    
    # 初始化agent
    if "agent" not in st.session_state:
        try:
            st.session_state.agent = IELTSReadingAgent()
        except ValueError as e:
            st.error(str(e))
            st.info("请复制 `.env.example` 为 `.env` 并配置您的API密钥")
            return
    
    # 侧边栏 - 输入区域
    with st.sidebar:
        st.header("📝 输入阅读材料")
        
        passage = st.text_area("阅读文章", height=300, placeholder="请粘贴雅思阅读文章...")
        
        questions_input = st.text_area("题目（每题一行）", height=150, placeholder="1. What is the main idea of the passage?\n2. According to the passage, ...")
        
        answers_input = st.text_area("答案（每题一行）", height=150, placeholder="1. A\n2. B")
        
        analyze_button = st.button("🔍 开始分析", type="primary", use_container_width=True)
        
        if st.button("🗑️ 清空对话历史", use_container_width=True):
            st.session_state.conversation_history = []
            st.rerun()
    
    # 主内容区域
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📖 题目解析")
        
        if analyze_button and passage and questions_input and answers_input:
            with st.spinner("正在分析题目，请稍候..."):
                questions = [q.strip() for q in questions_input.strip().split('\n') if q.strip()]
                answers = [a.strip() for a in answers_input.strip().split('\n') if a.strip()]
                
                # if len(questions) != len(answers):
                #     st.error("题目数量和答案数量不匹配！")
                    # return
                
                # 分析阅读材料
                analysis_result = st.session_state.agent.analyze_reading_passage(passage, questions, answers)
                
                if analysis_result.get("questions"):
                    st.session_state.current_analysis = analysis_result
                    st.session_state.passage_text = passage
                    
                    # 显示解析结果
                    for q_data in analysis_result["questions"]:
                        with st.expander(f"第{q_data['question_number']}题解析", expanded=True):
                            st.markdown(f"**正确答案:** {q_data['correct_answer']}")
                            st.markdown(f"**原文定位:** {q_data['location_sentence']}")
                            
                            if q_data.get('synonym_replacement'):
                                st.markdown("**同义替换分析:**")
                                for original, replacement in q_data['synonym_replacement'].items():
                                    st.markdown(f"- `{original}` → `{replacement}`")
                            
                            st.markdown(f"**解题思路:** {q_data['explanation']}")
                            
                            if q_data.get('wrong_options_analysis'):
                                st.markdown(f"**错误选项分析:** {q_data['wrong_options_analysis']}")
                else:
                    st.error("分析失败，请检查输入内容或API配置")
        
        elif "current_analysis" in st.session_state:
            # 显示之前的分析结果
            for q_data in st.session_state.current_analysis["questions"]:
                with st.expander(f"第{q_data['question_number']}题解析", expanded=False):
                    st.markdown(f"**正确答案:** {q_data['correct_answer']}")
                    st.markdown(f"**原文定位:** {q_data['location_sentence']}")
                    
                    if q_data.get('synonym_replacement'):
                        st.markdown("**同义替换分析:**")
                        for original, replacement in q_data['synonym_replacement'].items():
                            st.markdown(f"- `{original}` → `{replacement}`")
                    
                    st.markdown(f"**解题思路:** {q_data['explanation']}")
                    
                    if q_data.get('wrong_options_analysis'):
                        st.markdown(f"**错误选项分析:** {q_data['wrong_options_analysis']}")
    
    with col2:
        st.header("💬 智能问答")
        
        # 显示对话历史
        if st.session_state.conversation_history:
            for msg in st.session_state.conversation_history:
                if msg["role"] == "user":
                    st.markdown(f"**你:** {msg['content']}")
                else:
                    st.markdown(f"**助手:** {msg['content']}")
                st.markdown("---")
        
        # 用户输入区域
        if "current_analysis" in st.session_state:
            user_question = st.text_input("对题目有疑问？在这里提问：", placeholder="例如：为什么第3题选A而不是B？")
            
            if st.button("发送问题", use_container_width=True):
                if user_question:
                    # 添加上下文
                    context = f"""
                    文章：{st.session_state.passage_text}
                    
                    当前分析结果：
                    {json.dumps(st.session_state.current_analysis, ensure_ascii=False, indent=2)}
                    """
                    
                    with st.spinner("正在思考回答..."):
                        answer = st.session_state.agent.answer_question(user_question, context)
                        
                        # 添加到对话历史
                        st.session_state.conversation_history.append({
                            "role": "user",
                            "content": user_question
                        })
                        st.session_state.conversation_history.append({
                            "role": "assistant", 
                            "content": answer
                        })
                        
                        st.rerun()
        else:
            st.info("请先分析阅读材料，然后可以在这里提问")

if __name__ == "__main__":
    main()