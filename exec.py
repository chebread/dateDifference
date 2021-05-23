# 날짜 구하기
from datetime import *
_today_ = datetime.now()
print("-- 날짜 구하기 --")
print("-> 형식: yyyymmdd <-")
any_date = str(input("날짜: "))
_date_ = datetime.strptime(any_date, "%Y%m%d")
diff = _date_ - _today_
print("-- {}년 {}월 {}일 까지 {}일 남았어요 --".format(any_date[:4], any_date[4:6], any_date[6:8], diff.days))