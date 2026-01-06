# リスト4-4-(1)
import numpy as np

# リスト4-4-(2)
a = np.array([2, 1])
print(a)

# リスト4-4-(3)
type(a)

# リスト4-4-(4)　縦ベクトル
c = np.array([[1, 2], [3, 4]])
print(c)

# リスト4-4-(5)
d = np.array([[1], [2]])
print(d)

# リスト4-4-(6)　転置を表す(ベクトルの方向を反対にする)
print(d.T)  # Tは大文字
print(d.T.T)

# リスト4-4-(7)　ベクトルの足し算
a = np.array([2, 1])
b = np.array([1, 3])
print(a + b)

# リスト4-4-(8)　ベクトルの引き算
a = np.array([2, 1])
b = np.array([1, 3])
print(a - b)

# リスト4-4-(9)　ベクトルとスカラーの掛け算
a = np.array([2,1])
print(2 * a)

# リスト4-4-(10)　ベクトルの内積
b = np.array([1, 3])
c = np.array([4, 2])
print(b @ c)

# リスト4-4-(11)　ベクトルの大きさを確かめる
