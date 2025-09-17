import json
from ielts_agent import IELTSReadingAgent

# 示例数据
sample_passage = """The concept of artificial intelligence (AI) has evolved significantly since its inception in the 1950s. Early AI systems were rule-based and limited to specific domains, but modern AI, particularly machine learning, has revolutionized numerous industries. From healthcare diagnostics to autonomous vehicles, AI applications are becoming increasingly sophisticated and widespread.

However, this rapid advancement has sparked debates about the ethical implications of AI. Critics argue that AI systems may perpetuate biases present in their training data, leading to discriminatory outcomes in areas such as hiring, lending, and criminal justice. Additionally, there are concerns about job displacement as AI automation replaces human workers in various sectors.

Despite these challenges, many experts believe that AI, when properly regulated and developed, can bring tremendous benefits to society. Dr. Sarah Chen, a leading AI researcher at Stanford University, emphasizes that 'the key lies in developing AI systems that augment human capabilities rather than replace them entirely.' She advocates for transparent AI development processes and robust ethical frameworks to ensure that AI serves the greater good."""

sample_questions = [
    "What is the main difference between early AI systems and modern AI?",
    "According to the passage, what are two major concerns about AI development?",
    "What does Dr. Sarah Chen suggest as the key to beneficial AI development?",
    "Which of the following is NOT mentioned as an application of modern AI?",
    "What is the author's overall attitude toward AI development?"
]

sample_answers = ["B", "C", "A", "D", "C"]

def main():
    print("🎯 雅思阅读Agent助手 - 演示模式")
    print("=" * 50)
    
    # 注意：这里只是演示代码结构，实际运行需要配置API密钥
    print("📚 示例文章预览：")
    print(sample_passage[:200] + "...")
    print()
    
    print("❓ 示例题目：")
    for i, q in enumerate(sample_questions, 1):
        print(f"{i}. {q}")
    print()
    
    print("✅ 示例答案：")
    for i, a in enumerate(sample_answers, 1):
        print(f"{i}. {a}")
    print()
    
    print("🚀 使用说明：")
    print("1. 配置API密钥（获取免费API： https://platform.deepseek.com/）")
    print("2. 运行: streamlit run ielts_agent.py")
    print("3. 在Web界面中输入文章、题目和答案")
    print("4. 获得详细的题目解析和同义替换分析")
    print("5. 通过问答功能进行多轮交互学习")
    print()
    
    print("💡 支持的API提供商：")
    print("- DeepSeek: https://platform.deepseek.com/ (推荐，免费额度充足)")
    print("- Moonshot: https://platform.moonshot.cn/")
    print("- 其他OpenAI兼容API")

if __name__ == "__main__":
    main()