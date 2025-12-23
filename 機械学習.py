import numpy as np
import matplotlib.pyplot as plt

# 関数を定義
def f(x):
    return (x - 2) * x * (x + 2)     # 関数ｆの定義

def f2(x):
    return (x -1) * x * (x + 2)      # 関数ｆ2の定義

# x の範囲を定義
x = np.linspace(-3, 3, 100)          # xを100個準備

# グラフを描写
plt.plot(x, f(x), "black", label="$f$")    # fのグラフ
plt.plot(x, f2(x), "cornflowerblue", label="$f_2$")  #f2のグラフ
plt.legend(loc="upper left")         # 凡例表示
plt.title("comparison of $f$ and $f_2$")  # タイトル
plt.xlabel("x")                    # x軸ラベル
plt.ylabel("y")                    # y軸ラベル
plt.xlim(-3, 3)                    # x軸の範囲
plt.ylim(-15, 15)                  # y軸の範囲
plt.grid()                         # グリッド
plt.show()


