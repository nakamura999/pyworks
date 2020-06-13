import sys

try:
	a = float(sys.argv[1])
	b = float(sys.argv[2])
	print(a+b)
except:
	print('Error')

print('end')

# float 少数型に変更
# 最初の一番目と２番目の値のみ足算するプログラム
# 計算できない場合errorを出力する