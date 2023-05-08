import pandas as pd

import plotly.graph_objects as go
# 数据预处理
# df = pd.read_fwf('./1.txt') # pandas 读取txt的方法今天才知道quq
# df.to_csv('1.csv', index=False)

data = pd.read_csv('C:/Users/Administrator.DESKTOP-31VSLBG/PycharmProjects/pythonProject/venv/2.csv')
size = data['size']
data = data.drop(columns='size', axis=1)
# print(data)
#绘图
fig = go.Figure(data=[go.Surface(z=data.values, x=data.columns, y=size)])

fig.update_layout(title='My memory mountain', autosize=False,
                  width=800, height=800,
                  margin=dict(l=65, r=50, b=65, t=90))
# fig.write_html('1.html') # 保存HTML
fig.show()
