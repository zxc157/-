def countchat(f_name,sec):
    filename=f_name
    f=open(str(f_name)+".txt",'rt',encoding="utf-8")
    lines=f.readlines()
    countline=len(lines)
    print(countline)
    print(lines[-1])
    totaltime_h=int(lines[-1][1])*10+int(lines[-1][2])
    totaltime_m=int(lines[-1][4])*10+int(lines[-1][5])
    totaltime_s=int(lines[-1][7])*10+int(lines[-1][8])
    totalsec=3600*totaltime_h+60*totaltime_m+totaltime_s
    
    print(totaltime_h)
    print(totaltime_m)
    print(totaltime_s)
    avgchat=(countline/int(totalsec))*int(sec)

    print(avgchat)
        
        



if __name__ == "__main__":
    countchat(739935451,30)
    
    
