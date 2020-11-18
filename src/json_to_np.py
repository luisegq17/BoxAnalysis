import json
import numpy as np

# read file
json_file="hist_data_k_f.json"
with open(json_file,"r") as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

# process data
x_train=[]
y_train=[]
obj_len=len(obj)
for i in range(obj_len):
    # y_test
    tlytr=[]
    y_train_o=obj[i]["res"]
    tlytr.append(y_train_o)
    y_train.append(tlytr)
    #x_test
    tlxtr=[]
    x_train_o1=obj[i]["wfw"]
    tlxtr.append(x_train_o1)
    x_train_o2=obj[i]["lfw"]
    tlxtr.append(x_train_o2)
    x_train_o3=obj[i]["dw"]
    tlxtr.append(x_train_o3)
    x_train_o4=obj[i]["dw_w"]
    tlxtr.append(x_train_o4)
    x_train_o5=obj[i]["dw_l"]
    tlxtr.append(x_train_o5)
    x_train.append(tlxtr)

y_train=np.asarray(y_train)
x_train=np.asarray(x_train)

# variables to export
# x_train, y_train