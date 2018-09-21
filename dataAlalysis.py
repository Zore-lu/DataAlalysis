#!/usr/bin/env python
#!-*-coding:utf-8-*-
#!@Time :9/21/18 10:01 AM
#!@Author   :qiyu
#!@File :.py

import pandas as pd
import numpy as np

class DataAlalysis():
    def __init__(self):
        pass

    def readData(self):
        data1 = pd.read_csv('./births1.csv')
        data2 = pd.read_csv('./births2.csv')
        datas = pd.concat([data1,data2])
        return datas

    def handleData(self,datas):
        # 筛选出指定字段的数据
        reDatas1 = datas.reindex(columns = ['year','month','births'])
        # 查找某个值对应的数据
        reDatas2 = datas.loc[datas['month'] == 1]
        # 删除重复的数据
        reDatas = reDatas1.drop_duplicates()

        return reDatas

    def saveData(self,reDatas):
        return reDatas.to_csv('./reData.csv')


def main():
    alalysiser = DataAlalysis()
    datas = alalysiser.readData()
    reDatas = alalysiser.handleData(datas)
    alalysiser.saveData(reDatas)
    print(reDatas)


if __name__ == "__main__":

    main()

