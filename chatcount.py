from konlpy.tag import *
from konlpy import jvm
from matplotlib import pyplot as plt
import numpy as np




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
def countchat4(f_name,sec):
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
    countparticle=0
    countlen=0
    countspace=0
    countnoun=0
    okt=Okt()
    print("전체구간의 30초당 평균 채팅 수 = ",avgchat)
    
    for line in lines:
        timesec=(int(line[1])*10+int(line[2]))*3600+(int(line[4])*10+int(line[5]))*60+int(line[7])*10+int(line[8])
        chattable.append(timesec)
        text=line[11:-1]
        textlen=len(text)
        countlen+=textlen
        #textword=text.split(" ")
        textlist=okt.pos(text)
        
        countspace+=len(textlist)
        for t in textlist:
            #t2=preprocessing(t)
            if t[1] == 'KoreanParticle':
                countparticle+=1
                break
        for t in textlist:
            #t2=preprocessing(t)
            if t[1] == 'Noun':
                countnoun+=1
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
    avgparticle=countparticle/countline
    avgspace=countspace/countline
    avgnoun=countnoun/countline
    print("전체구간의 채팅 평균 길이 = ",avglen)
    print("전체구간의 한글낱자 수 = ",avgparticle)
    print("전체구간의 형태소 분리후 갯수 =",avgspace)
    print("전체구간의 평균 명사 갯수 = ",avgnoun)
    result=[] 
    #print(highlights)
    for k in highlights:
        for i in range(k+1,k+30):
            if i in highlights:
                highlights.remove(i)
            
    

    print(highlights)
    
    f.close()
    return highlights
def countchat5(f_name,sec):
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
    countparticle=0
    countlen=0
    countspace=0
    countnoun=0
    okt=Okt()
    print("전체구간의 10초당 평균 채팅 수 = ",avgchat)
    
    for line in lines:
        timesec=(int(line[1])*10+int(line[2]))*3600+(int(line[4])*10+int(line[5]))*60+int(line[7])*10+int(line[8])
        chattable.append(timesec)
        text=line[11:-1]
        textlen=len(text)
        countlen+=textlen
        #textword=text.split(" ")
        textlist=okt.pos(text)
        
        countspace+=len(textlist)
        for t in textlist:
            #t2=preprocessing(t)
            if t[1] == 'KoreanParticle':
                countparticle+=1
                break
        for t in textlist:
            #t2=preprocessing(t)
            if t[1] == 'Noun':
                countnoun+=1
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
    avgparticle=countparticle/countline
    avgspace=countspace/countline
    avgnoun=countnoun/countline
    print("전체구간의 채팅 평균 길이 = ",avglen)
    print("전체구간의 한글낱자 수 = ",avgparticle)
    print("전체구간의 형태소 분리후 갯수 =",avgspace)
    print("전체구간의 명사 분리후 갯수 =",avgnoun)
    result=[] 
    #print(highlights)
    starttime=highlights[0]
    temp=highlights[0]
    highlights2=[]
    for i in highlights:
        if starttime==0:
            starttime=i
            temp=i
        else:
            if i > temp+10:
                endtime=temp
                highlights2.append((starttime,endtime))
                starttime=0
            else:
                temp=i
        
            
    dellist=[]
    for k in highlights2:
        #print(k)
        if k[1]-k[0] < 9 :
            #print(k)
            dellist.append(k)
            #highlights2.remove(k)
    for k in dellist:
        highlights2.remove(k)
    print(highlights2)
    print(len(highlights2))
    f.close()
    return highlights2
def countchat6(f_name,sec):
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
    countparticle=0
    countlen=0
    countspace=0
    okt=Okt()
    print("전체구간의 10초당 평균 채팅 수 = ",avgchat)
    delsec=[]
    tempchat=[]
    presec=0
    
    deltempsec=[]
    for line in lines:
        timesec=(int(line[1])*10+int(line[2]))*3600+(int(line[4])*10+int(line[5]))*60+int(line[7])*10+int(line[8])
        chattable.append(timesec)
        tempchat.append(timesec)
        text=line[11:-1]
        textlen=len(text)
        countlen+=textlen
        #textword=text.split(" ")
        textlist=okt.pos(text)
        delsec.clear()
        countspace+=len(textlist)
        for t in textlist:
            #t2=preprocessing(t)
            if t[1] == 'KoreanParticle':
                countparticle+=1
                break
        for i in chattable:
            if timesec > i+sec :
                delsec.append(i)

        for second in delsec:
            chattable.remove(second)
        for i in tempchat:
            if timesec-i > 3600:
                deltempsec.append(i)
        for i in deltempsec:
            if i in tempchat:
                tempchat.remove(i)
        avgtemp=len(tempchat)/3600*sec
        if timesec<3600:
            if ( len(chattable) >= avgchat*3.5) :
                if (timesec not in highlights):
                    highlights.append(timesec)
        else:
            if(len(chattable) >= avgtemp*3.5):
                if (timesec not in highlights):
                    highlights.append(timesec)
        
    checkcount=0
    checknum=0
    avglen=countlen/countline
    avgparticle=countparticle/countline
    avgspace=countspace/countline
    print("전체구간의 채팅 평균 길이 = ",avglen)
    print("전체구간의 한글낱자 수 = ",avgparticle)
    print("전체구간의 형태소 분리후 갯수 =",avgspace)
    result=[] 
    #print(highlights)
    starttime=highlights[0]
    temp=highlights[0]
    highlights2=[]
    for i in highlights:
        if starttime==0:
            starttime=i
            temp=i
        else:
            if i > temp+10:
                endtime=temp
                highlights2.append((starttime,endtime))
                starttime=0
            else:
                temp=i
        
            
    dellist=[]
    for k in highlights2:
        #print(k)
        if k[1]-k[0] < 9 :
            #print(k)
            dellist.append(k)
            #highlights2.remove(k)
    for k in dellist:
        highlights2.remove(k)
    print(highlights2)
    print(len(highlights2))
    f.close()
    return highlights2
def countchat7(f_name,sec):
    filename=f_name
    f=open(str(f_name)+".txt",'rt',encoding="utf-8")
    lines=f.readlines()
    countline=len(lines)
    #print("전체 구간의 채팅 수 = ",countline)
    #print(lines[-1])
    totaltime_h=int(lines[-1][1])*10+int(lines[-1][2])
    totaltime_m=int(lines[-1][4])*10+int(lines[-1][5])
    totaltime_s=int(lines[-1][7])*10+int(lines[-1][8])
    totalsec=3600*totaltime_h+60*totaltime_m+totaltime_s
    chattable=[]
    highlights=[]
    avgchat=(countline/int(totalsec))
    dic=['ㅋ']
    countparticle=0
    countlen=0
    countspace=0
    okt=Okt()
    #print("전체구간의 초당 평균 채팅 수 = ",avgchat)
    delsec=[]
    tempchat=[]
    countnoun=0
    deltempsec=[]
    counttotalpart=0
    countnounchat=0
    for line in lines:
        timesec=(int(line[1])*10+int(line[2]))*3600+(int(line[4])*10+int(line[5]))*60+int(line[7])*10+int(line[8])
        #chattable.append(timesec)
        #tempchat.append(timesec)
        text=line[11:-1]
        textlen=len(text)
        countlen+=textlen
        #textword=text.split(" ")
        textlist=okt.pos(text)
        delsec.clear()
        countspace+=len(textlist)
        for t in textlist:
            #t2=preprocessing(t)
            if t[1] == 'KoreanParticle':
                countparticle+=1
                break
        for t in textlist:
            #t2=preprocessing(t)
            if t[1] == 'Noun':
                countnoun+=1
        for t in textlist:
            #t2=preprocessing(t)
            if t[1] == 'KoreanParticle':
                counttotalpart+=1
        for t in textlist:
            #t2=preprocessing(t)
            if t[1] == 'Noun':
                countnounchat+=1
                break
        
        
        
    checkcount=0
    checknum=0
    avglen=countlen/countline
    avgparticle=countparticle/countline
    avgspace=countspace/countline
    avgnoun=countnoun/countline
    print("전체구간의 채팅 평균 길이 = ",avglen)
    print("전체구간의 평균 한글낱자포함 채팅 수 = ",avgparticle)
    print("전체구간의 평균 명사포함 채팅 수 = ",countnounchat/countline)
    print("전체구간의 채팅 수 = ",countline)
    print("전체구간의 형태소 분리후 갯수 =",avgspace)
    print("전체구간의 채팅당 평균 명사 갯수 =",avgnoun)
    print("전체구간의 채팅당 평균 한글낱자 갯수 =",counttotalpart/countline)
    print("전체구간의 총 길이 = ",totalsec)
    print("전체구간의 평균 초당 채팅 수 = ",avgchat)
    result=[] 
    #print(highlights)
    
            


def preprocessing(string):
    text=string
    if len(text) > 2:
        if text[0]==text[1] and text[1]==text[2]:
            return text[0]+text[1]

    if len(text) > 3:
        if text[0]+text[1] == text[2]+text[3]:
            return text[0]+text[1]

    return string
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


def analyzeh2(f_name,seclist,sec):
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
    countparticle=0
    countspace=0
    countnoun=0
    dic=['ㅋ']
    okt=Okt()
    for line in lines:
        
        timesec=(int(line[1])*10+int(line[2]))*3600+(int(line[4])*10+int(line[5]))*60+int(line[7])*10+int(line[8])
        if ((timesec in seclist) or timecheck >0 ) :
            text=line[11:-1]
            #print(text)
            countline+=1
            textlen=len(text)
            countlen+=textlen
            textlist=okt.pos(text)
            #textword=text.split(" ")
            countspace+=len(textlist)
            #print(textword)
            #for index in textword:
            for word in textlist:
                #word2=preprocessing(word)
                word2=preprocessing(word[0])
                if word2 in word_list:
                    word_list[word2] = word_list[word2]+1

                else:
                    word_list[word[0]] = 1
            for t in textlist:
                
                if t[1] =='KoreanParticle':
                    countparticle+=1
                    break
            for t in textlist:
                
                if t[1] =='Noun':
                    countnoun+=1
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
    avgparticle=countparticle/countline
    avgnoun=countnoun/countline
    print("하이라이트 구간 average length = ",avglen)
    print("하이라이트 구간 평균 한글낱말 갯수 = ",avgparticle)
    print("하이라이트 구간 전체 라인 수 = ",countline)
    print("하이라이트 구간 형태소분리후의 갯수 = ",avgspace)
    print("하이라이트 구간 평균 명사갯수 = ",avgnoun)
    
    f.close()

def analyzeh3(f_name,seclist,sec):
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
    countparticle=0
    countspace=0
    countnoun=0
    dic=['ㅋ']
    okt=Okt()
    print(seclist[list_index][1])
    for line in lines:
        if list_index >= len(seclist):
            break
        timesec=(int(line[1])*10+int(line[2]))*3600+(int(line[4])*10+int(line[5]))*60+int(line[7])*10+int(line[8])
        if timesec > seclist[list_index][1]:
            list_index+=1
            word_list2={key: value for key,value in word_list.items() if value > 1}
            word_list2=sorted(word_list2.items(), key=lambda x:x[1], reverse=True)
            #print(word_list2)
            word_list={}
        else:
            
            if (seclist[list_index][0] <=timesec and seclist[list_index][1] >= timesec ) :
                text=line[11:-1]
                #print(text)
                countline+=1
                textlen=len(text)
                countlen+=textlen
                textlist=okt.pos(text)
                #textword=text.split(" ")
                countspace+=len(textlist)
                #print(textword)
                #for index in textword:
                for word in textlist:
                    #word2=preprocessing(word)
                    word2=preprocessing(word[0])
                    if word2 in word_list:
                        word_list[word2] = word_list[word2]+1

                    else:
                        word_list[word[0]] = 1
                for t in textlist:
                    
                    if t[1] =='KoreanParticle':
                        countparticle+=1
                        break
                for t in textlist:
                    
                    if t[1] =='Noun':
                        countnoun+=1
                        break
            

        

        
    avglen=countlen/countline
    avgspace=countspace/countline
    avgparticle=countparticle/countline
    avgnoun=countnoun/countline
    print("하이라이트 구간 average length = ",avglen)
    print("하이라이트 구간 평균 한글낱말 갯수 = ",avgparticle)
    print("하이라이트 구간 전체 라인 수 = ",countline)
    print("하이라이트 구간 형태소분리후의 갯수 = ",avgspace)
    print("하이라이트 구간 평균 명사갯수 = ",avgnoun)
    
    f.close()

def analyzeh4(f_name,seclist,sec):
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
    countparticle=0
    countspace=0
    countnoun=0
    countsec=0
    countnounchat=0
    counttotalpart=0
    dic=['ㅋ']
    okt=Okt()
    #print(seclist[list_index][1])
    for i in seclist:
        countsec+=i[1]-i[0]+1
    countsec+=len(seclist)*10
    for line in lines:
        if list_index >= len(seclist):
            break
        timesec=(int(line[1])*10+int(line[2]))*3600+(int(line[4])*10+int(line[5]))*60+int(line[7])*10+int(line[8])
        if timesec > seclist[list_index][1]+10:
            list_index+=1
            #word_list2={key: value for key,value in word_list.items() if value > 1}
            #word_list2=sorted(word_list2.items(), key=lambda x:x[1], reverse=True)
            #print(word_list2)
            #word_list={}
        else:
            
            if (seclist[list_index][0] <=timesec and seclist[list_index][1]+10 >= timesec ) :
                text=line[11:-1]
                #print(text)
                countline+=1
                textlen=len(text)
                countlen+=textlen
                textlist=okt.pos(text)
                #textword=text.split(" ")
                countspace+=len(textlist)
                #print(textword)
                #for index in textword:
                '''
                for word in textlist:
                    #word2=preprocessing(word)
                    word2=preprocessing(word[0])
                    if word2 in word_list:
                        word_list[word2] = word_list[word2]+1

                    else:
                        word_list[word[0]] = 1
                '''
                for t in textlist:
                    
                    if t[1] =='KoreanParticle':
                        countparticle+=1
                        break
                for t in textlist:
                    
                    if t[1] =='Noun':
                        countnoun+=1
                        
                for t in textlist:
                    
                    if t[1] =='KoreanParticle':
                        counttotalpart+=1
                        
            
                for t in textlist:
                    
                    if t[1] =='Noun':
                        countnounchat+=1
                        break
        

    
    avglen=countlen/countline
    avgspace=countspace/countline
    avgparticle=countparticle/countline
    avgnoun=countnoun/countline
    print("하이라이트 구간 average length = ",avglen)
    print("하이라이트 구간 한글낱자 포함한 채팅 갯수 = ",avgparticle)
    print("하이라이트 구간 명사 포함한 채팅 갯수 = ",countnounchat/countline)
    print("하이라이트 구간 전체 라인 수 = ",countline)
    print("하이라이트 구간 형태소분리후의 갯수 = ",avgspace)
    print("하이라이트 구간 채팅당 평균 명사 갯수 = ",avgnoun)
    print("하이라이트 구간 채팅당 평균 한글낱자 갯수 =",counttotalpart/countline)
    print("하이라이트 구간 총 길이 = ",countsec)
    print("하이라이트 구간 초당 평균 채팅 수 = ",countline/countsec)
    f.close()

def findhigh(line,seclist):
    timesec=(int(line[0])*10+int(line[1]))*3600+(int(line[3])*10+int(line[4]))*60+int(line[6])*10+int(line[7])
    newlist=[]
    
    for i in seclist:
        left=(int(i[0][0])*10+int(i[0][1]))*60+(int(i[0][3])*10+int(i[0][4]))+timesec
        right=(int(i[1][0])*10+int(i[1][1]))*60+(int(i[1][3])*10+int(i[1][4]))+timesec
        newlist.append((left,right))
    return newlist

def findhigh2(f_name,sec,h,p,n,c,l,stime):
    filename=f_name
    f=open(str(f_name)+".txt",'rt',encoding="utf-8")
    lines=f.readlines()
    countline=len(lines)
    #print(countline)
    #print(lines[-1])
    totaltime_h=int(lines[-1][1])*10+int(lines[-1][2])
    totaltime_m=int(lines[-1][4])*10+int(lines[-1][5])
    totaltime_s=int(lines[-1][7])*10+int(lines[-1][8])
    totalsec=3600*totaltime_h+60*totaltime_m+totaltime_s
    chattable=[]
    highlights=[]
    avgchat=(countline/int(totalsec))*int(sec)
    dic=['ㅋ']
    countparticle=0
    countlen=0
    counth=0
    countnoun=0
    okt=Okt()
    #print("전체구간의 10초당 평균 채팅 수 = ",avgchat)
    delsec=[]
    tempchat=[]
    presec=0
    hlist=[0]*(totalsec+1)
    plist=[0]*(totalsec+1)
    nlist=[0]*(totalsec+1)
    clist=[0]*(totalsec+1)
    llist=[0]*(totalsec+1)
    deltempsec=[]
    for line in lines:
        
        timesec=(int(line[1])*10+int(line[2]))*3600+(int(line[4])*10+int(line[5]))*60+int(line[7])*10+int(line[8])
        
        if timesec<9:
            continue
        
        text=line[11:-1]
        textlen=len(text)
        countlen+=textlen
        #textword=text.split(" ")
        textlist=okt.pos(text)
        counth+=len(textlist)
        for i in range(0,sec):
            hlist[timesec-i]+=len(textlist)
            clist[timesec-i]+=1
            llist[timesec-i]+=textlen
        for t in textlist:
            if t[1]=='KoreanParticle':
                countparticle+=1
                for i in range(0,sec):
                    plist[timesec-i]+=1
                break
        for t in textlist:
            if t[1]=='Noun':
                countnoun+=1
                for i in range(0,sec):
                    nlist[timesec-i]+=1
                break
        
        
    avg_l=countlen/countline
    avg_p=countparticle/countline
    avg_n=countnoun/countline
    avg_h=counth/countline
    avg_c=countline/totalsec*sec
    hscore=[0]*(totalsec+1)
    #for i in range(0,totalsec+1):
    #for i in range(7550,7600):
        #print(clist[i],hlist[i]/clist[i],plist[i]/clist[i],nlist[i]/clist[i])
    '''    
    for i in range(0,totalsec+1):
        score=0
        if clist[i]>= c*1.0*avg_c:
        #if clist[i]!=0 and hlist[i]!=0 and clist[i]!=0 and nlist[i]!=0:
            score+=clist[i]/avg_c/c+avg_h/hlist[i]/clist[i]*h+avg_n/nlist[i]/clist[i]*n+plist[i]/clist[i]/avg_p/p
            #score+=clist[i]
            hscore[i]=score

    #print(max(hscore))
    #for i in range(0,15):
    #    print(hscore[2695+i])
    hlist=[]
    for i in range(0,totalsec+1):
        if hscore[i]>=2.0:
            hlist.append(i)
'''
    
    #print(clist[20])
    #print(avg_c*c)
    highlist=[0]*(totalsec+1)
    normallist=[0]*(totalsec+1)
    for i in range(stime,totalsec+1):
        index=0
        index2=0
        if clist[i]==0:
            continue
        if (clist[i]>=avg_c*c*1.00):
            index2+=1
            
            normallist.append(i)
        if (hlist[i]/clist[i]<=avg_h*h*1.00):
            index+=1
        if (plist[i]/clist[i]>=avg_p*p*1.00):
            index+=1
        if(nlist[i]/clist[i]<=avg_n*n*1.00):
            index+=1
        if(llist[i]/clist[i]<=avg_l*l*1.00):
            index+=1
        if (index>=2 and index2>=1 or clist[i]>=avg_c*c*1.15) :
            highlist.append(i)

    #print(hlist)
    #for i in range(0,totalsec+1):
    #    if clist[i]>= 1.1*c*avg_c:
    #        hlist.append(i)
    
    starttime=highlist[0]
    temp=highlist[0]
    hlist2=[]
    for i in highlist:
        if starttime==0:
            starttime=i
            temp=i
        else:
            if i > temp+10:
                endtime=temp
                hlist2.append((starttime,endtime))
                starttime=0
            else:
                temp=i
    normallist2=[]
    starttime=normallist[0]
    temp=normallist[0]

    '''
    x=np.arange(16230,16300)
    y=clist[16230:16300]
    y2=[0]*(totalsec+1)
    for i in range(0,totalsec+1):
        if clist[i]!=0:
            y2[i]=hlist[i]/clist[i]
    y3=[0]*19810
    for i in range(0,19810):
        if clist[i]!=0:
            y3[i]=plist[i]/clist[i]
    plt.plot(x,y)
    
    #plt.plot(x,y2,'r')
    #plt.plot(x,y3[19750:19810],'b')
    plt.axvline(16244, 0, 1, color='gray', linewidth='1')
    plt.axvline(16284, 0, 1, color='gray', linewidth='1')
    #plt.show()
    localmax=[]
    print(clist[2625])
    for i in range(stime,totalsec+1-10):
        now=clist[i]
        #now2=hlist[i]/clist[i]
        index=0
        index2=0
        if clist[i]<avg_c*c:
            continue
        for k in range(1,16):
            pre=clist[i-k]
            next=clist[i+k]
            if pre<=now and next<now:
                
                index+=1
            pre=hlist[i-k]
            next=hlist[i+k]
        if index==15:
            localmax.append(i)

    print(localmax)
    '''
    for i in normallist:
        if starttime==0:
            starttime=i
            temp=i
        else:
            if i > temp+10:
                endtime=temp
                normallist2.append((starttime,endtime))
                starttime=0
            else:
                temp=i
    dellist=[]
    for k in hlist2:
        #print(k)
        if k[1]-k[0] < 5 :
            #print(k)
            dellist.append(k)
            #highlights2.remove(k)
    for k in dellist:
        hlist2.remove(k)
    dellist=[]
    for k in normallist2:
        #print(k)
        if k[1]-k[0] < 5 :
            #print(k)
            dellist.append(k)
            #highlights2.remove(k)
    for k in dellist:
        normallist2.remove(k)
    countsec=0
    print(hlist2)
    for i in hlist2:
        countsec+=i[1]-i[0]+1
    print(countsec)
    countsec=0
    for i in normallist2:
        countsec+=i[1]-i[0]+1
    print(normallist2)
    print(countsec)
    f.close()
    
    return (hlist2,normallist2)

def calresultratio(testlist,reallist):
    reallen=len(reallist)
    count=0
    for i in reallist:
        for k in testlist:
            if k[0]<=i[1] and k[1]>=i[0]:
                count+=1
                break

    print(count/reallen)
    return count/reallen

def calpreratio(testlist,reallist):
    testlen=len(testlist)
    count=0
    for i in testlist:
        for k in reallist:
            if k[0]<=i[1] and k[1]>=i[0]:
                count+=1
                break
    print(count/testlen)
    return count/testlen
    
if __name__ == "__main__":
    #highlist=countchat5(953697152,10)
    #analyzeh3(953697152,highlist,10)
    #high=[(3283, 3308), (3460, 3477), (3657, 3680), (3775, 3785), (4143, 4162), (4499, 4529), (4814, 4864), (5158, 5268), (5283, 5288), (5325, 5357), (7226, 7236), (7445, 7474), (7845, 7890), (8088, 8128), (8201, 8246), (8343, 8955), (8608, 8663), (8760, 8832), (10594, 10634), (10792, 10807), (11121, 11147), (11307, 11328), (11349, 11377), (11462, 11474), (11837, 11885), (11942, 11952), (12011, 12039), (12202, 12277)]
    #high1=findhigh('00:36:21',[('03:22','03:42'),('05:10','05:17'),('05:27','05:45'),('06:20','06:37'),('09:37','09:52'),('17:40','18:04'),('23:30','24:04'),('26:50','27:08'),('28:58','29:21'),('33:55','34:58'),('38:00','38:30'),('38:40','39:05')])
    #high2=findhigh('01:40:21',[('05:29','05:43'),('08:37','08:55'),('11:10','11:36'),('18:18','18:40'),('21:40','22:42'),('24:32','24:50'),('25:08','25:16'),('30:21','31:08'),('32:57','33:26'),('34:55','35:20'),('35:40','36:20'),('39:40','40:24')])
    #high3=findhigh('03:27:44',[('10:55','11:12'),('12:08','12:21'),('14:16','14:26'),('16:20','16:30'),('18:21','18:46'),('21:54','22:40'),('24:00','24:20'),('24:35','25:16'),('26:40','26:54'),('28:20','28:46'),('30:24','30:44'),('31:05','31:16'),('31:44','32:05'),('33:07','34:42')])
    #high4=findhigh('04:29:05',[('03:02','03:15'),('06:35','07:23'),('08:36','08:44'),('12:54','13:27'),('16:18','17:20'),('19:00','19:21'),('19:44','20:02'),('20:38','21:09'),('21:20','21:44'),('22:44','22:54'),('23:48','24:33'),('27:01','27:33'),('28:46','29:40')])
    #print(high1+high2+high3+high4)
    #countchat7(953697152,10)
    #analyzeh4(974896147,high,10)
    '''
    testlist=findhigh2(892382049,10,0.809,1.104,0.915,1.945,0.819,2537)
    #testlist=[(2362, 2374), (3139, 3150), (3248, 3259), (3509, 3540), (4097, 4145), (4195, 4239), (4253, 4289), (4400, 4410), (5379, 5392), (5709, 5733), (6117, 6132), (6197, 6215), (6356, 6378), (6631, 6646), (6823, 6844), (6945, 6960), (7042, 7067), (7126, 7145), (7184, 7194), (7309, 7324), (7422, 7450), (7492, 7503), (7548, 7565), (7644, 7685), (7701, 7740), (8169, 8182), (9591, 9619), (10136, 10179), (10338, 10392), (10952, 10978), (11041, 11054), (11093, 11150), (11164, 11189), (11209, 11329), (11558, 11570), (12356, 12368)]
    reallist=[(2383, 2403), (2491, 2498), (2508, 2526), (2561, 2578), (2758, 2773), (3241, 3265), (3591, 3625), (3791, 3809), (3919, 3942), (4216, 4279), (4461, 4491), (4501, 4526), (6350, 6364), (6538, 6556), (6691, 6717), (7119, 7141), (7321, 7383), (7493, 7511), (7529, 7537), (7842, 7889), (7998, 8027), (8116, 8141), (8161, 8201), (8401, 8445), (13119, 13136), (13192, 13205), (13320, 13330), (13444, 13454), (13565, 13590), (13778, 13824), (13904, 13924), (13939, 13980), (14064, 14078), (14164, 14190), (14288, 14308), (14329, 14340), (14368, 14389), (14451, 14546), (16327, 16340), (16540, 16588), (16661, 16669), (16919, 16952), (17123, 17185), (17285, 17306), (17329, 17347), (17383, 17414), (17425, 17449), (17509, 17519), (17573, 17618), (17766, 17798), (17871, 17925)]
    calresultratio(testlist[0],reallist)
    calpreratio(testlist[0],reallist)
    calresultratio(testlist[1],reallist)
    calpreratio(testlist[1],reallist)
    '''
    #okt=Okt()
    #print(okt.pos("지나갑니다 ㅋㅋㅋㅋㅋ"))
    high1=[(2383, 2403), (2491, 2498), (2508, 2526), (2561, 2578), (2758, 2773), (3241, 3265), (3591, 3625), (3791, 3809), (3919, 3942), (4216, 4279), (4461, 4491), (4501, 4526), (6350, 6364), (6538, 6556), (6691, 6717), (7119, 7141), (7321, 7383), (7493, 7511), (7529, 7537), (7842, 7889), (7998, 8027), (8116, 8141), (8161, 8201), (8401, 8445), (13119, 13136), (13192, 13205), (13320, 13330), (13444, 13454), (13565, 13590), (13778, 13824), (13904, 13924), (13939, 13980), (14064, 14078), (14164, 14190), (14288, 14308), (14329, 14340), (14368, 14389), (14451, 14546), (16327, 16340), (16540, 16588), (16661, 16669), (16919, 16952), (17123, 17185), (17285, 17306), (17329, 17347), (17383, 17414), (17425, 17449), (17509, 17519), (17573, 17618), (17766, 17798), (17871, 17925)]
    high2=[(2762, 2778), (2948, 2980), (3073, 3083), (3186, 3203), (3478, 3548), (3628, 3642), (3868, 3929), (3963, 4013), (4091, 4118), (4179, 4220), (4378, 4448), (6106, 6116), (6196, 6216), (6336, 6366), (6707, 6741), (7036, 7114), (7286, 7298), (7411, 7456), (9173, 9192), (9401, 9419), (9435, 9459), (9531, 9565), (9977, 10025), (10415, 11022), (10675, 10775), (10835, 10842), (10895, 10945), (15314, 15349), (15604, 15619), (15759, 15775), (15851, 15863), (16119, 16173), (16244, 16284), (16429, 16453), (16571, 16656), (16754, 16767), (16789, 16799), (16964, 17006), (17049, 17083), (17107, 17206), (17264, 17374), (19132, 19166), (19183, 19204), (19278, 19288), (19408, 19423), (19476, 19488), (19664, 19688), (19703, 19725), (19763, 19796), (19868, 19883), (20183, 20198), (20245, 20284), (20344, 20366), (20495, 20551), (20595, 20661), (20796, 20890)]
    high3=[(2387, 2416), (2461, 2481), (2566, 2579), (2619, 2639), (2919, 2953), (3091, 3143), (3161, 3171), (3344, 3371), (3471, 3496), (3641, 3684), (3836, 3855), (3941, 3980), (4096, 4133), (6026, 6049), (6102, 6117), (6131, 6150), (6237, 6249), (6275, 6296), (6435, 6449), (6532, 6579), (6637, 6702), (6797, 6867), (7025, 7115), (7257, 7892), (7377, 7462), (7552, 7586), (7607, 7614), (7777, 7834), (9727, 9746), (9764, 9782), (10004, 10030), (10074, 10094), (10199, 10217), (10375, 10409), (10589, 10607), (10649, 10671), (10724, 10804), (10874, 10917), (11094, 11117), (11135, 11147), (11277, 11289), (11309, 11352), (15796, 15810), (15865, 15915), (15997, 16044), (16232, 16269), (16392, 16413), (16731, 16754), (17065, 17142), (18984, 19001), (19011, 19026), (19217, 19256), (19476, 19520), (19621, 19680), (19696, 19704), (19858, 19895), (19974, 19984), (20014, 20021), (20041, 20082), (20193, 20298)]
    high4=[(2695, 2708), (2880, 2910), (3237, 3245), (3488, 3528), (4072, 4123), (4177, 4210), (4237, 4266), (6149, 6202), (6347, 6355), (6520, 6547), (6617, 6631), (6787, 6857), (6937, 6951), (7027, 7050), (7110, 7135), (7152, 7172), (7303, 7312), (7535, 7582), (7612, 7703), (9579, 9607), (9705, 9725), (9904, 9922), (9983, 10013), (10125, 10157), (10325, 10375), (10690, 10755), (10934, 10995), (11075, 11140), (11170, 11180), (11200, 11260)]
    high5=[(2123, 2131), (2191, 2215), (2393, 2408), (2706, 2724), (2736, 2756), (2796, 2811), (2911, 2946), (3036, 3081), (3319, 3364), (3437, 3485), (3683, 3778), (3813, 3833), (4100, 4152), (4246, 4287), (6296, 6364), (6840, 6858), (7021, 7030), (7061, 7077), (7186, 7208), (7232, 7273), (7385, 7418), (7475, 7497), (7508, 7522), (7685, 7707), (7885, 7956), (12280, 12287), (12487, 12501), (12582, 12605), (12740, 12755), (12838, 12847), (13038, 13076), (13157, 13165), (13396, 13427), (13476, 13514), (13770, 13794), (14107, 14141), (14239, 14257), (14274, 14312), (14404, 14452), (16337, 16362), (16476, 16511), (16578, 16591), (16609, 16620), (16787, 16807), (16886, 16894), (16950, 16970), (17367, 17394), (17504, 17535), (17600, 17693)]
    high6=[(2256, 2270), (2465, 2477), (2625, 2643), (2774, 2798), (2838, 2848), (2929, 2938), (3258, 3280), (3511, 3547), (3694, 3734), (3864, 3924), (3935, 3948), (4054, 4091), (4201, 4240), (6409, 6423), (6441, 6466), (6712, 6721), (6844, 6864), (6941, 6984), (7003, 7070), (7199, 7279), (7376, 7398), (7424, 7463), (7717, 7777), (12065, 12091), (12143, 12159), (12595, 12621), (12720, 12750), (12765, 12774), (12785, 12804), (12819, 12834), (12898, 12927), (13007, 13040), (13107, 13130), (13185, 13229), (15043, 15058), (15162, 15180), (15375, 15434), (15471, 15479), (15549, 15619), (15742, 15749), (15778, 15835), (15947, 15976), (16158, 16170), (16309, 16337), (16352, 16370), (16488, 16528), (16652, 16735)]
    high7=[(2568, 2600), (2883, 2899), (3025, 3041), (3225, 3265), (3417, 3439), (3551, 3595), (3727, 3743), (3866, 3933), (4067, 4119), (4214, 4275), (5990, 6008), (6059, 6073), (6183, 6208), (6338, 6364), (6440, 6475), (6525, 6541), (7070, 7113), (7391, 7418), (7546, 7554), (7808, 7879), (9508, 9531), (9907, 9936), (10203, 10221), (10469, 10517), (10671, 10704), (11113, 11178), (11286, 11370), (15709, 15742), (15846, 15862), (16262, 16271), (16321, 16359), (16486, 16503), (16535, 16553), (16831, 16905), (17184, 17229), (17334, 17354), (17383, 17450), (17503, 17558), (19211, 19271), (19298, 19327), (19531, 19559), (19583, 19602), (19669, 19702), (19861, 19867), (19877, 19911), (20032, 20167), (20240, 20254), (20353, 20368), (20505, 20520), (20920, 21000), (21058, 21098), (22770, 22800), (22838, 22858), (23091, 23105), (23446, 23457), (23591, 23639), (23726, 23740), (23767, 23785), (23988, 24010), (24199, 24233), (24253, 24267), (24282, 24321), (24361, 24375), (24432, 24518)]
    high8=[(2330, 2355), (2377, 2394), (2459, 2469), (2498, 2504), (2583, 2595), (2974, 3024), (3147, 3167), (3326, 3350), (3483, 3531), (3727, 3757), (3832, 3884), (3927, 3968), (4177, 4197), (4337, 4369), (6123, 6143), (6470, 6502), (6681, 6756), (6776, 6896), (6964, 6984), (7099, 7160), (7289, 7338), (7372, 7382), (7437, 7445), (7499, 7561), (11922, 11939), (12048, 12092), (12235, 12272), (13245, 13272), (13384, 13439), (13674, 13715), (16141, 16163), (16388, 16440), (16782, 16801), (16898, 16939), (17162, 17183), (17249, 17266), (17303, 17319), (17623, 17679), (17893, 17953), (18048, 18092), (18272, 18283), (18342, 18349), (18398, 18451)]
    high9=[(2430, 2467), (2477, 2506), (2623, 2638), (2738, 2757), (2863, 2883), (2993, 3024), (3259, 3271), (3288, 3300), (3410, 3422), (3567, 3586), (3594, 3613), (3634, 3660), (3710, 3743), (4009, 4021), (4030, 4038), (4058, 4066), (4127, 4148), (4188, 4248), (6052, 6061), (6210, 6260), (6405, 6450), (6643, 6653), (6695, 6707), (6757, 6767), (6817, 6855), (6932, 6959), (7063, 7140), (7284, 7409), (11687, 11704), (11958, 11989), (12065, 12075), (12473, 12538), (13243, 13316), (13389, 13477), (13597, 13655), (13720, 13769), (15459, 15494), (15551, 15563), (15614, 15632), (15670, 15682), (15776, 15821), (16161, 16180), (16272, 16350), (16523, 16569), (16671, 16731)]
    high10=[(3283, 3308), (3460, 3477), (3657, 3680), (3775, 3785), (4143, 4162), (4499, 4529), (4814, 4864), (5158, 5268), (5283, 5288), (5325, 5357), (7226, 7236), (7445, 7474), (7845, 7890), (8088, 8128), (8201, 8246), (8343, 8955), (8608, 8663), (8760, 8832), (10594, 10634), (10792, 10807), (11121, 11147), (11307, 11328), (11349, 11377), (11462, 11474), (11837, 11885), (11942, 11952), (12011, 12039), (12202, 12277)]
    print(len(high1))
    print(len(high2))
    print(len(high3))
    print(len(high4))
    print(len(high5))
    print(len(high6))
    print(len(high7))
    print(len(high8))
    print(len(high9))
    print(len(high10))
