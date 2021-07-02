# 날짜 구하기
from datetime import *
_today_ = datetime.now()
print("-- 날짜 구하기 --")
print("-> 형식: yyyy-mm-dd <-")
any_date = str(input("날짜: "))
_date = ''
_date += any_date[:4]
_date += any_date[5:7]
_date += any_date[8:10]
_date_ = datetime.strptime(_date, "%Y%m%d")
diff = _date_ - _today_
print("-> {}년 {}월 {}일 까지 {}일 남았어요 <-".format(_date[:4], _date[4:6], _date[6:8], diff.days))