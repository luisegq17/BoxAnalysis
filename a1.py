#"https://boxrec.com/en/date?date=2011-01-07&sport=proboxing"
s0="-"
s1="https://boxrec.com/en/date?date="
s2="&sport=proboxing"
url_list=[]
sy=2000
fy=2018

for y in range(sy,fy+1):
    for m in range(1,9+1):
        for d in range(10,28+1):
            sy=str(y)
            sm="0"+str(m)
            sd=str(d)
            urlm=s1+sy+s0+sm+s0+sd+s2
            url_list.append(urlm)

print(url_list)