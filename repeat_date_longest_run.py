days=0
month=1
year=2026
days_iteration=31
date_list=[]
temp=0
startdate=""
lastdate=""
count=0
confirm_start_date=False
found_repeat=False
swap=True
length_inbetween=[]
startdatelist=[]
enddatelist=[]

while days!=31 and month!=12 and year!=2099:
    for i in range(12):
        if month==4 or month==6 or month==9 or month==11:
            days_iteration=30
        elif month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 ==0):
                days_iteration=29
            else:
                days_iteration=28
        else:
            days_iteration=31
        for j in range(days_iteration):
            days=int(days)+1
            if len(str(days))==1:
                days="0"+str(days)
            else:
                days=str(days)
            if len(str(month))==1:
                month="0"+str(month)
            else:
                month=str(month)
            date=days+month+str(year)[-2]+str(year)[-1]
            for k in range(len(date)):
                date_list.append(date[k])
            top=len(date_list)-1
            while swap and top>0:
                for index in range(top):
                    if date_list[index]>date_list[index+1]:
                        temp=date_list[index]
                        date_list[index]=date_list[index+1]
                        date_list[index+1]=temp
                        swap=True
                top=top-1
                
            for r in range(len(date_list)-1):
                if date_list[r]==date_list[r+1]:
                    if confirm_start_date==False:
                        confirm_start_date=True
                        found_repeat=True
                        count=count+1
                        break
                    else:
                        count=count+1
                        found_repeat=True
                        break
                else:
                    found_repeat=False
                                           
            if found_repeat==False:
                lastdate=date
                if count>0:
                    print(startdate+"\n"+str(count)+"\n"+lastdate)
                    length_inbetween.append(count)
                    startdatelist.append(startdate)
                    enddatelist.append(lastdate)

                count=0
                confirm_start_date=False
                startdate=date
            date_list=[]
        days=0
        month=int(month)+1
    month=1
    year=int(year)+1

max_length=length_inbetween[:]
swap1=True
top1=len(max_length)-1
while swap1 and top1>0:
    for index in range(top1):
        if max_length[index]>max_length[index+1]:
            temp=max_length[index]
            max_length[index]=max_length[index+1]
            max_length[index+1]=temp
            swap1=True
    top1=top1-1

print(max_length[-1])

for y in range(len(length_inbetween)):
    if length_inbetween[y]==max_length[-1]:
        print(startdatelist[y], enddatelist[y])
print(max_length[-2])
for y in range(len(length_inbetween)):
    if length_inbetween[y]==max_length[-2]:
        print(startdatelist[y], enddatelist[y])