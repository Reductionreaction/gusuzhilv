import pandas as pd

# 读取Excel文件
df = pd.read_excel('cao.xlsx', engine='openpyxl')

# 遍历answer列，提取名词并构造问题
for index, row in df.iterrows():
    # 分割字符串，提取名词
    noun = row['answer'].split(':',1)[0]
    # 构造问题并填入question列
    df['question'] = df['question'].astype(str)

    df.at[index, 'question'] = f'请解释一下{noun}的意思'

# 将修改后的DataFrame保存回Excel文件
df.to_excel('牛牛牛牛.xlsx', index=False)
