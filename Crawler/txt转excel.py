import pandas as pd

# 读取txt文件，每行以":"分割为名词和解释
data = []
with open('被洗过的牛.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data.append(line)
      #  noun, definition = line.strip().split(':',1)
      #  data.append([noun.strip(), definition.strip()])


# 创建DataFrame
df = pd.DataFrame(data)

# 将DataFrame写入Excel文件
df.to_excel('洗过的牛.xlsx', index=False)
