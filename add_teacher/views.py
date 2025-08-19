from django.shortcuts import render

import mysql.connector as sql
tn=''
cl=''
dep=''
sem=''
su=''
# Create your views here.
def sign(request):
    global tn,cl,dep,sem,su
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="",database='feedback_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="tname":
                tn=value

            if key=="tclass":
                cl=value

            if key=="tdep":
                dep=value

            if key=="tsem":
                sem=value

            if key=="tsub":
                su=value    
        
        c="insert into teacher Values('{}','{}','{}','{}','{}')".format(tn,su,dep,sem,cl)
        cursor.execute(c)
        m.commit()

    return render(request,'add_teacher.html')