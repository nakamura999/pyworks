# 単語並べ替えプログラム

import sys
# コマンドライン引数を使う為のモジュール

input_list = sys.argv[1:]
# １番目の要素を取り出して別のリストにする
input_list.sort()
# sort  新しく作ったリストを並べ替える
print(input_list)
