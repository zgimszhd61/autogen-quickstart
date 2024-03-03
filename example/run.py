!pip install pyautogen~=0.1.0 -q -U

import autogen

# 配置LLM和API密钥
config_list = [{
    'model': 'gpt-3.5-turbo',  # 或者您可以使用其他模型，如gpt-4
    'api_key': ""  # 替换为您的API密钥
}]
llm_config = {
    "timeout": 600,
    "config_list": config_list,
    "temperature": 0.7
}

# 创建代理
user_proxy = autogen.UserProxyAgent(name="user_proxy")
financial_analyst = autogen.AssistantAgent(name="Financial_Analyst", llm_config=llm_config)
software_engineer = autogen.AssistantAgent(name="Software_Engineer", llm_config=llm_config)
ui_designer = autogen.AssistantAgent(name="UI_Designer", llm_config=llm_config)

# 创建群聊管理器
groupchat = autogen.GroupChat(agents=[user_proxy, financial_analyst, software_engineer, ui_designer], messages=[], max_round=2)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# 发起对话
message = "Analyze stock price for GRAB for the last 30 days and create a chart."
user_proxy.initiate_chat(manager, clear_history=True, message=message)
