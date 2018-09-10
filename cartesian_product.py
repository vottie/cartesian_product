# coding: utf-8

class CartesianProduct:
    def extract(self,val,row):
        if isinstance(val, list):
            for v in val:
                row.append(v)
        else:
            row.append(val)

    def combi(self,x, y, result):
        #print("combi before",x,y,result)
        row = []
        for i in x:
            for j in y:
                self.extract(i,row)
                row.append(j)
                #print("row", row)
                result.append(row)
                row=[]
                #print("result", result)
    
    def execute(self,matrix,result):
        for idx, x in enumerate(matrix):
            if (idx == 0):
                #print("0 times")
                self.combi(matrix[idx], matrix[idx+1], result)
                #print("result=",result)
            elif (idx < len(matrix)-1):
                #print("{0} times", idx)
                tmp=[]
                self.combi(result, matrix[idx+1], tmp)
                #print("tmp=",tmp)
                result = tmp
                #print("exec() result=",result)
    
        return result
        #for r in result:
        #    print("result", r)

    def to_csv(self,result):
        for idx, r in enumerate(result):
            print(idx, ":", r)
            #print(idx, ":", split(r))
