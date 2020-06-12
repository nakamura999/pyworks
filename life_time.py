# 自分が何日生きているのか調べるプログラム
import datetime

today = datetime.date.today()
birthday = datetime.date(1989,10,10)
# 上記に生年月日記入
life = today - birthday
print(life.days)