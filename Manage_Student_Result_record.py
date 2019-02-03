dic={}
subject={}
marks=[]
ans=input('To Continue y/n.. ')
while ans=='y':
    ch=input('press\n 1 add name \n 2 shlow \n 3 Update \n 4 Exit ')
    if ch=='1':  
        name=input('student name')
        for i in range(3):
            a=input('inte subject name')
            b=input('enter marks')
            subject[a]=b
            dic[name]=subject
    elif ch=='2':
            print(dic)
    elif ch=='3':
        print('what you want to update\n 1 name \n 2 subjict \n  ')
        ch=''
        ans='y'
        while ans=='y':
            ch=input('enter your choice')
            if ch=='1':
                name=input('update name')
                dic.clear()
                dic[name]=subject
                break
            elif ch=='2':
                for x in range(3):
                    sub=input('update subject')
                    mrk=input('udate marks')
                    subject[sub]=mrk
                    dic[name]=subject
                break
    elif ch=='4':
          exit(0)      
    else:
        ans=input('To continue press y... ')
