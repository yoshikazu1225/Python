import numpy as np
import matplotlib.pyplot as plt

#データ生成
np.random.seed(seed=1) # 乱数を固定
x = np.arange(10) # x を作成
y = np.random.rand(10) # y を作成

#グラフ描写
plt.plot(x, y) # 折れ線グラフを登録
plt.show() # グラフ表示

