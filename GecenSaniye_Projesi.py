import datetime
import time
while 1:
    tarih = datetime.datetime.now()
    tarih.second
    print(tarih.ctime())
    print("saniye:{}".format(tarih.second))
    if tarih.second%10==0:
        print("\n{}. saniye icerisindesiniz.............".format(tarih.second))
    time.sleep(1)