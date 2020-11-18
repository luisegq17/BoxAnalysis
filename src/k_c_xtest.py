import numpy as np
s=200
m=220
e=240
j=1
x_test=[]
for i in range(s,e+1,j):
    tl=[]
    d=m-i
    wf1=i #wf1
    wf2=m+d #wf2
    dw=wf1-wf2 #dw
    drf1=dw/wf1 #drf1
    drf2=dw/wf2 #drf2
    tl.append(wf1)
    tl.append(wf2)
    tl.append(dw)
    tl.append(drf1)
    tl.append(drf2)
    x_test.append(tl)
x_test=np.asarray(x_test)