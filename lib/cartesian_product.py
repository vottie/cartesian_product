# coding: utf-8

from lib.logger import Logger

class CartesianProduct:
    def __init__(self):
        self.log = Logger(__name__)

    def extract(self, val, row):
        self.log.info("extract start")
        if isinstance(val, list):
            for v in val:
                row.append(v)
        else:
            row.append(val)

    def combi(self,x, y, result):
        self.log.info("combi start")
        row = []
        for i in x:
            for j in y:
                self.extract(i,row)
                row.append(j)
                self.log.info("row append val = ", j)
                result.append(row)
                row=[]
                # self.log.info("combi result = ", result)
    
    def execute(self,matrix,result):
        self.log.info("execute start")
        for idx, x in enumerate(matrix):
            if (idx == 0):
                self.log.info("0 times")
                self.combi(matrix[idx], matrix[idx+1], result)
                # self.log.info("execute result = ", result)
            elif (idx < len(matrix)-1):
                self.log.info("times: ", idx)
                tmp=[]
                self.combi(result, matrix[idx+1], tmp)
                result = tmp
                # self.log.info("execute result = ", result)
    
        return result
        #for r in result:
        #    print("result", r)

    def to_csv(self,result):
        for idx, r in enumerate(result):
            print(idx, ":", r)
            #print(idx, ":", split(r))
