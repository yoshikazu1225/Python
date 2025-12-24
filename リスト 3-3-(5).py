import numpy as np
import matplotlib.pyplot as plt

# 関数f3を定義
def f3(x0, x1):
    ans = (2 * x0 ** 2 + x1 ** 2) * np.exp(-(2 * x0 ** 2 + x1 ** 2))
    return ans

# 各 x0, x1　でf3を計算ん
x0_n, x1_n = 9, 9
x0 = np.linspace(-2, 2, x0_n)    # x0を準備 
x1 = np.linspace(-2, 2, x1_n)    # x1を準備
y = np.zeros((x1_n, x0_n))       # 計算悔過を入れるyを準備
for i0 in range(x0_n):
    for i1 in range (x1_n):
        y[i1, i0] = f3(x0[i0], x1[i1])   # f3を求めyに入れる

xx0, xx1 = np.meshgrid(x0, x1)    # グリッド座標の作成

plt.figure(figsize=(5, 3.5))
ax = plt.subplot(projection="3d")    # 3Dグラフの準備
ax.plot_surface(
    xx0,                    # x 座標のデータ
    xx1,                    # y 座標のデータ
    y,                      # z 座標のデータ
    rstride=1,              # 何行おきに線を引くか
    cstride=1,              # 何列おきに線を引くのか
    alpha=0.3,              # 面の透明度
    color="blue",           # 面の色
    edgecolor="black",      # 線の色
    )
ax.set_zticks(((0, 0.2)))   # z 軸のメモリの指定
ax.view_init(40, -30)       # グラフの向きの指定 (仰角, 方位角)
plt.show()