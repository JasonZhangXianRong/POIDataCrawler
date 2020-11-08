# -*- coding: utf-8 -*-
import json
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

class format(object):
    def __init__(self):
        pass
    def format_2(self):
        file_in = "D:\\primary\\2.json"
        file_out = "baidu1.json"
        fout = open(file_out, "w", encoding="utf8")
        with open(file_in, 'r', encoding="utf8") as fin:
            for line in fin.readlines():
                json_data = json.loads(line)
                item = {}
                item["province"] = ""
                item["city"] = json_data["city"]
                item["county"] = json_data["county"]
                item["name"] = json_data["name"]
                item["adress"] = json_data["address"]
                item["class1"] = u"生活服务"
                item["class2"] = u"便利店"
                item["longitude"] = json_data["lng"]
                item["latitude"] = json_data["lat"]
                dataline = json.dumps(item, ensure_ascii=False) + "\n"
                fout.write(dataline)
                print(dataline)
        fout.close()

    def format_3(self):
        file_in = "D:\\primary\\3.json"
        file_out = "baidu2.json"
        fout = open(file_out, "w", encoding="utf8")
        with open(file_in, 'rb') as fin:
            for line in fin.readlines():
                json_data = json.loads(line)
                item = {}
                item["province"] = ""
                item["city"] = json_data["city"]
                item["county"] = json_data["county"]
                item["name"] = json_data["name"]
                item["adress"] = json_data["address"]
                item["class1"] = u"生活服务"
                item["class2"] = u"便利店"
                item["longitude"] = json_data["lng"]
                item["latitude"] = json_data["lat"]
                dataline = json.dumps(item, ensure_ascii=False) + "\n"
                fout.write(dataline)
                print(dataline)
        fout.close()
    def format_4(self):
            file_in = "D:\\primary\\ABCCHINA.json"
            file_out = "baidu3.json"
            fout = open(file_out, "w", encoding="utf8")
            with open(file_in, 'r', encoding="utf8") as fin:
                for line in fin.readlines():
                    print(line)
                    json_data = json.loads(line)
                    item = {}
                    item["province"] = json_data["Province"]
                    item["city"] = json_data["City"]
                    item["county"] = json_data["Borough"]
                    item["name"] = json_data["Name"]
                    item["adress"] = json_data["FullAddress"]
                    item["class1"] = u"生活服务"
                    item["class2"] = u"银行"
                    item["longitude"] = json_data["Longitude"]
                    item["latitude"] = json_data["Latitude"]
                    dataline = json.dumps(item, ensure_ascii=False) + "\n"
                    fout.write(dataline)
                    print(dataline)
            fout.close()
    def format_5(self):
            file_in = "D:\\primary\\CCB_ATM.json"
            file_out = "baidu4.json"
            fout = open(file_out, "w", encoding="utf8")
            with open(file_in, 'r', encoding="utf8") as fin:
                for line in fin.readlines():
                    print(line)
                    json_data = json.loads(line)
                    item = {}
                    item["province"] = json_data["Province"]
                    item["city"] = json_data["cityName"]
                    item["county"] = json_data["countyName"]
                    item["name"] = json_data["NET_NAME"]
                    item["adress"] = json_data["NET_AREA"]
                    item["class1"] = u"生活服务"
                    item["class2"] = u"银行"
                    item["longitude"] = json_data["X_COORDINATE"]
                    item["latitude"] = json_data["Y_COORDINATE"]
                    dataline = json.dumps(item, ensure_ascii=False) + "\n"
                    fout.write(dataline)
                    print(dataline)
            fout.close()

    def format_6(self):
        file_in = "D:\\primary\\CCBCHINA.json"
        file_out = "baidu5.json"
        fout = open(file_out, "w", encoding="utf8")
        with open(file_in, 'r', encoding="utf8") as fin:
            for line in fin.readlines():
                print(line)
                json_data = json.loads(line)
                item = {}
                item["province"] = json_data["Province"]
                item["city"] = json_data["cityName"]
                item["county"] = json_data["countyName"]
                item["name"] = json_data["NET_NAME"]
                item["adress"] = json_data["NET_AREA"]
                item["class1"] = u"生活服务"
                item["class2"] = u"银行"
                item["longitude"] = json_data["X_COORDINATE"]
                item["latitude"] = json_data["Y_COORDINATE"]
                dataline = json.dumps(item, ensure_ascii=False) + "\n"
                fout.write(dataline)
                print(dataline)
        fout.close()





if __name__ == "__main__":
    format().format_6()




