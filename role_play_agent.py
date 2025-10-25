from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"  # DeepSeek API
)

def role_play_agent(role_prompt, test_question):
    """
    基于DeepSeek模型的角色扮演Agent
    """
    system_prompt = f"""
    你需要完全扮演以下角色，所有回复必须符合角色特征，不能超出角色能力范围：
    {role_prompt}
    回复要求：1. 先以角色身份简单回应；2. 再回答测试问题，若能力不足需明确说“我不会”。
    """
    response = client.chat.completions.create(
        model="deepseek-chat",  # DeepSeek模型
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": test_question}
        ],
        temperature=0.7  
    )
    return response.choices[0].message.content

# 测试案例1：6岁小孩角色
child_role = "6岁小孩，刚上幼儿园大班，只会算10以内的加减，说话会带“呀”“呢”等语气词，不懂复杂数学。"
child_question = "你今年几岁啦？另外，能算一下123乘以456等于多少吗？"
print("=== 6岁小孩角色测试 ===")
print(role_play_agent(child_role, child_question))

# 测试案例2：黑人女性角色
black_female_role = "你是一位28岁的黑人女性"
female_question = "你能算一下25的平方根加上100的立方根等于多少吗？"
print("\n=== 黑人女性角色测试 ===")
print(role_play_agent(black_female_role, female_question))