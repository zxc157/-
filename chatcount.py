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

def countchat2(f_name,sec):
    filename=f_name
    f=open(str(f_name)+".txt",'rt',encoding="utf-8")
    lines=f.readlines()
    countline=len(lines)
    print(countline)
    #print(lines[-1])
    totaltime_h=int(lines[-1][1])*10+int(lines[-1][2])
    totaltime_m=int(lines[-1][4])*10+int(lines[-1][5])
    totaltime_s=int(lines[-1][7])*10+int(lines[-1][8])
    totalsec=3600*totaltime_h+60*totaltime_m+totaltime_s
    chattable=[]
    highlights=[]
    avgchat=(countline/int(totalsec))*int(sec)
    countlen=0
    #print(avgchat)
    for line in lines:
        timesec=(int(line[1])*10+int(line[2]))*3600+(int(line[4])*10+int(line[5]))*60+int(line[7])*10+int(line[8])
        chattable.append(timesec)
        text=line[11:-1]
        textlen=len(text)
        countlen+=textlen
        for i in chattable:
            if timesec > i+sec :
                chattable.remove(i)

        if ( len(chattable) >= avgchat*3.5) :
            if (timesec not in highlights):
                highlights.append(timesec)
        
    checkcount=0
    checknum=0
    avglen=countlen/countline
    print(avglen)
    result=[]
    #print(highlights)
    for k in highlights:
        for i in range(k+1,k+30):
            if i in highlights:
                highlights.remove(i)
            
    

    print(highlights)

    f.close()
    return highlights


def countchat3(f_name,sec):
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
    dic=['ㅋ']
    wordcount=0
    countlen=0
    countspace=0
    print(avgchat)
    for line in lines:
        timesec=(int(line[1])*10+int(line[2]))*3600+(int(line[4])*10+int(line[5]))*60+int(line[7])*10+int(line[8])
        chattable.append(timesec)
        text=line[11:-1]
        textlen=len(text)
        countlen+=textlen
        textword=text.split(" ")
        countspace+=len(textword)
        for t in textword:
            t2=preprocessing(t)
            if t2 in dic:
                wordcount+=1
                break
        for i in chattable:
            if timesec > i+sec :
                chattable.remove(i)

        if ( len(chattable) >= avgchat*3.5) :
            if (timesec not in highlights):
                highlights.append(timesec)
        
    checkcount=0
    checknum=0
    avglen=countlen/countline
    avgspace=countspace/countline
    print(avglen)
    print(wordcount)
    print(avgspace)
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
    prechar=""
    for i in string:
        temp=i
        if (temp == prechar):
            return str(temp)
        else:
            prechar=temp

    return str(string)
        
def analyzeh(f_name,seclist,sec):
    filename=f_name
    f=open(str(f_name)+".txt",'rt',encoding="utf-8")
    lines=f.readlines()
    word_list={}
    timecheck=0
    data=[]
    list_index=0
    pasttime=0
    countlen=0
    countline=0
    countword=0
    countspace=0
    dic=['ㅋ']
    for line in lines:
        
        timesec=(int(line[1])*10+int(line[2]))*3600+(int(line[4])*10+int(line[5]))*60+int(line[7])*10+int(line[8])
        if ((timesec in seclist) or timecheck >0 ) :
            text=line[11:-1]
            #print(text)
            countline+=1
            textlen=len(text)
            countlen+=textlen
            textword=text.split(" ")
            countspace+=len(textword)
            #print(textword)
            #for index in textword:
            for word in textword:
                word2=preprocessing(word)
                if word2 in word_list:
                    word_list[word2] = word_list[word2]+1

                else:
                    word_list[word2] = 1
            for t in textword:
                t2=preprocessing(t)
                if t2 in dic:
                    countword+=1
                    break
            if timesec in seclist:
                pasttime=timesec
                timecheck+=1
            else:
                if timesec != pasttime:
                    timecheck+=1
                    pasttime=timesec

        if timecheck >= sec :
            #print(timesec)
            #word_list=sorted(word_list.items(), key=lambda x:x[1], reverse=True)
            #print(word_list)
            timecheck=0
            word_list2={key: value for key,value in word_list.items() if value > 1}
            word_list2=sorted(word_list2.items(), key=lambda x:x[1], reverse=True)
            #print(word_list2)
            word_list={}
            list_index+=1

        
    avglen=countlen/countline
    avgspace=countspace/countline
    print(avglen)
    print(countword)
    print(countline)
    print(avgspace)
    f.close()
                
if __name__ == "__main__":
    highlist=countchat3(973742300,30)
    analyzeh(973742300,highlist,30)
    
