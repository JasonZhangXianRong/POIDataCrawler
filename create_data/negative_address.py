# -*- coding: utf-8 -*-
import json
import pandas as pd
class NegAddr(object):
    def __init__(self):
        pass
    def read_data(self):
        addL1 = []
        addL2 = []
        i = 0
        j = 0
        f1 = "D:\\CLUEDatasetSearch-master\\POIDataCrawler\\baidu_out.json"
        f2 = "D:\\CLUEDatasetSearch-master\\POIDataCrawler\\poilist.json"
        with open(f1, "r", encoding="utf8") as f_1:
            for line in f_1.readlines():
                if i > 96500:
                    break
                item = json.loads(line)
                addL1.append(item["province"]+item["city"]+item["county"]+item["adress"])
                i = i + 1
        with open(f2, "r", encoding="gbk") as f_2:
            for line in f_2.readlines():
                if j > 96500:
                    break
                item = json.loads(line)
                addL2.append(item["province"]+item["city"]+item["county"]+item["address"])
                j = j + 1
        dataframe = pd.DataFrame({"baidu":addL1, "poiList": addL2, "tag":0})
        dataframe.to_csv("negative_address.csv", index=False, sep=",")
if __name__ =="__main__":
    NegAddr().read_data()



