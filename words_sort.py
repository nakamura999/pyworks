# 単語並べ替えプログラム
# （例）ターミナルで　python word_sort.py 単語 単語 単語

import sys
# コマンドライン引数を使う為のモジュール

input_list = sys.argv[1:]
# １番目の要素を取り出して別のリストにする
input_list.sort()
# sort  新しく作ったリストを並べ替える
print(input_list)
