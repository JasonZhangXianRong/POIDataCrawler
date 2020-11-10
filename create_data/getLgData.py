# -*- coding: utf-8 -*-
import json
import os, sys
class format(object):
    def __init__(self):
        self.project_path =os.path.abspath(os.path.join(os.getcwd(), "../"))
        # 获取当前文件路径的上一级目录
        #D:\CLUEDatasetSearch-master\POIDataCrawler
    def marData(self):
        f1 = os.path.join(self.project_path, 'primaryData', 'market1.json')
        fo = os.path.join(self.project_path, 'data', 'market.json')
        fout = open(fo, "w", encoding="utf8")
        listdata = []
        with open(f1, 'rb') as f:
            for line in f.readlines():
                json_data = json.loads(line)
                item = {}
                item["province"] = ""
                item["city"] = json_data["city"]
                item["county"] = json_data["county"]
                item["name"] = json_data["name"]
                item["adress"] = json_data["address"]
                item["class1"] = u"生活服务"
                item["class2"] = u"超市"
                item["longitude"] = json_data["lng"]
                item["latitude"] = json_data["lat"]
                dataline = json.dumps(item, ensure_ascii=False) + "\n"
                print(dataline)
                fout.write(dataline)
        fout.close()
    def govData(self):
        f1 = os.path.join(self.project_path, 'primaryData', 'BeiJing.json')
        f2 = os.path.join(self.project_path, 'primaryData', 'GuangZhou.json')
        f3 = os.path.join(self.project_path, 'primaryData', 'ShangHai.json')
        f4 = os.path.join(self.project_path, 'primaryData', 'ShenZhen.json')
        fo = os.path.join(self.project_path, 'data', 'government.json')
        fout = open(fo, "w", encoding="utf8")
        listdata = []
        with open(f2, 'r', encoding="utf8") as f:
            for line in f.readlines():
                json_data = json.loads(line)
                item = {}
                item["province"] = json_data["province"]
                item["city"] = json_data["city"]
                item["county"] = ""
                item["name"] = json_data["name"]
                item["adress"] = json_data["address"] + json_data["govern"]
                item["class1"] = u"政府"
                item["class2"] = u"社保"
                item["longitude"] = ""
                item["latitude"] = ""
                dataline = json.dumps(item, ensure_ascii=False) + "\n"
                listdata.append(dataline)
        with open(f1, 'rb') as f:
            for line in f.readlines():
                json_data = json.loads(line)
                item = {}
                item["province"] = u"北京"
                item["city"] = u"北京"
                item["county"] = ""
                item["name"] = json_data["name"]
                item["adress"] = json_data["address"]
                item["class1"] = u"政府"
                item["class2"] = json_data["categoryName1"]
                item["longitude"] = json_data["lon"]
                item["latitude"] = json_data["lat"]
                dataline = json.dumps(item, ensure_ascii=False) + "\n"
                listdata.append(dataline)
        with open(f4, 'rb') as f:
            for line in f.readlines():
                json_data = json.loads(line)
                item = {}
                item["province"] = u"广东省"
                item["city"] = u"深圳市"
                item["county"] = ""
                item["name"] = json_data["name"]
                item["adress"] = item["province"] + item["county"]+ json_data["address"]
                item["class1"] = u"政府"
                item["class2"] = u"社区"
                item["longitude"] = ""
                item["latitude"] = ""
                dataline = json.dumps(item, ensure_ascii=False) + "\n"
                listdata.append(dataline)
        for item in listdata:
            fout.write(item)
        fout.close()
    def lgData(self):
        fiList = ["primaryData/lg_BJBC.json", "primaryData/lg_BJXD.json",
                  "primaryData/lg_CAFT.json", "primaryData/lg_DFBT.json",
                  "primaryData/lg_DFRC.json", "primaryData/lg_GQBT.json",
                  "primaryData/lg_meizuRepair.json", "primaryData/lg_meizuSell.json",
                  "primaryData/lg_QRQC.json", "primaryData/lg_SHTYWL.json",
                  "primaryData/lg_YQDZ.json", "primaryData/lgData_ABCCHINA.json",
                  "primaryData/lgData_BCCHINA.json", "primaryData/lgData_CCBCHINA.json"]
        fo = os.path.join(self.project_path, 'data', 'lg.json')
        fout = open(fo, "w", encoding="utf8")
        for name in fiList:
            na = name.replace("primaryData/", "")
            f1 = os.path.join(self.project_path, 'primaryData', na)
            listdata = []
            with open(f1, 'rb') as f:
                for line in f.readlines():
                    json_data = json.loads(line)
                    item = {}
                    item["province"] = json_data["province"]
                    item["city"] = json_data["city"]
                    item["county"] = ""
                    item["name"] = json_data["name"]
                    item["adress"] = json_data["address"]
                    item["class1"] = u"生活服务"
                    item["class2"] = u"手机"
                    item["longitude"] = json_data["longitude"]
                    item["latitude"] = json_data["latitude"]
                    dataline = json.dumps(item, ensure_ascii=False) + "\n"
                    print(dataline)
                    fout.write(dataline)
        fout.close()
    def oppo(self):
        f1 = os.path.join(self.project_path, 'primaryData', 'OPPOSHOPS.json')
        fo = os.path.join(self.project_path, 'data', 'oppo.json')
        fout = open(fo, "w", encoding="utf8")
        listdata = []
        with open(f1, 'rb') as f:
            for line in f.readlines():
                json_data = json.loads(line)
                item = {}
                item["province"] = json_data["pro_name"]
                item["city"] = json_data["city_name"]
                item["county"] = json_data["district_name"]
                item["name"] = json_data["name"]
                item["adress"] = json_data["address"]
                item["class1"] = u"生活服务"
                item["class2"] = u"手机专卖"
                item["longitude"] = json_data["longitude"]
                item["latitude"] = json_data["latitude"]
                dataline = json.dumps(item, ensure_ascii=False) + "\n"
                print(dataline)
                fout.write(dataline)
        fout.close()



if __name__ == "__main__":
    format().oppo()



