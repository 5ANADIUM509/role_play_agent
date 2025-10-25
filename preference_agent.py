from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()  
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),  
    base_url="https://api.deepseek.com/v1"  # DeepSeek的API地址
)

def preference_agent(shopping_info):
    system_prompt = """
    你是一位购物偏好分析师，需要：
    1. 从用户提供的购物信息中，提炼3-5个核心偏好（如品牌、品类、价格区间、风格）；
    2. 基于偏好，给出1-2个后续购物推荐（要具体，比如“推荐某品牌的某品类”）；
    3. 语言要简洁，分点说明，不要冗余。
    """
    response = client.chat.completions.create(
        model="deepseek-chat",  # 使用DeepSeek的模型
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"我的购物信息：{shopping_info}"}
        ],
        temperature=0.5
    )
    return response.choices[0].message.content

# 测试案例
user_shopping_info = """
1. 上月买了2件优衣库的纯棉T恤（白色、浅灰色，每件99元）；
2. 收藏了3款北面的冲锋衣（黑色、藏青色，价格在800-1200元）；
3. 过去半年买过4双Nike跑鞋（都是飞马系列，价格500-700元）；
4. 每次购物都会筛选“可机洗”“纯棉/透气面料”的商品。
"""
print("=== 用户购物偏好分析 ===")
print(preference_agent(user_shopping_info))