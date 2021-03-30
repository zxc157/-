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
    chattable=[]
    highlights=[]
    avgchat=(countline/int(totalsec))*int(sec)

    print(avgchat)
    for line in lines:
        timesec=(int(line[1])*10+int(line[2]))*3600+(int(line[4])*10+int(line[5]))*60+int(line[7])*10+int(line[8])
        chattable.append(timesec)

        for i in chattable:
            if timesec > i+sec :
                chattable.remove(i)

        if ( len(chattable) >= avgchat*3.5) :
            if (timesec not in highlights):
                highlights.append(timesec)
        
    checkcount=0
    checknum=0
    result=[]
    #print(highlights)
    for k in highlights:
        for i in range(k+1,k+30):
            if i in highlights:
                highlights.remove(i)
            
    

    print(highlights)

    f.close()
    return highlights
def preprocessing(string):
    
def analyzeh(f_name,seclist,sec):
    filename=f_name
    f=open(str(f_name)+".txt",'rt',encoding="utf-8")
    lines=f.readlines()
    word_list={}
    timecheck=0
    data=[]
    list_index=0
    pasttime=0
    for line in lines:
        
        timesec=(int(line[1])*10+int(line[2]))*3600+(int(line[4])*10+int(line[5]))*60+int(line[7])*10+int(line[8])
        if ((timesec in seclist) or timecheck >0 ) :
            text=line[11:-1]
            #print(text)
            textword=text.split(" ")
            #print(textword)
            #for index in textword:
            for word in textword:
                if word in word_list:
                    word_list[word] = word_list[word]+1

                else:
                    word_list[word] = 1
            if timesec in seclist:
                pasttime=timesec
                timecheck+=1
            else:
                if timesec != pasttime:
                    timecheck+=1
                    pasttime=timesec

        if timecheck >= sec :
            print(timesec)
            word_list=sorted(word_list.items(), key=lambda x:x[1], reverse=True)
            print(word_list)
            timecheck=0
            word_list={}
            list_index+=1

        


    f.close()
                
if __name__ == "__main__":
    highlist=countchat(739935451,30)
    analyzeh(739935451,highlist,30)
    
