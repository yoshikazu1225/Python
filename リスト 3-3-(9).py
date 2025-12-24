import numpy as np
import matplotlib.pyplot as plt

# 関数f3を定義
def f3(x0, x1):
    ans = (2 * x0 ** 2 + x1 ** 2) *np.exp(-(2 * x0 ** 2 + x1 ** 2))
    return ans

# 各x0, x1 でf3を計算
x0_n, X1_n = 50, 50
x0 = np.linspace(-2, 2, x0_n)    # x0を準備
x1 = np.linspace(-2, 2, X1_n)    # x1を準備
xx0, xx1 = np.meshgrid(x0, x1)   # グリッド座標の作成
y = f3(xx0, xx1)                 # グリッド座標に対するyを求める

# グラフ描写
plt.figure(figsize=(4, 4))   #グラフの大きさを指定
cont = plt.contour(    # 等高線プロット
    xx0, xx1, y,       # データ
    levels=3,
    colors="black",    #等高線の色
)
cont.clabel(fmt="%.2f", fontsize=8)   #等高線に数値を入れる
plt.xlabel("$x_0$", fontsize=14)
plt.ylabel("$x_1$", fontsize=14)
plt.show()