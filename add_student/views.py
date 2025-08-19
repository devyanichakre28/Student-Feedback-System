from django.shortcuts import render

import mysql.connector

sn=''
sc=''
sd=''
sem=''
sid=''
spas=''

def signs (request):
    global sn,sc,sd,sem,sid,spas
    if request.method=="POST":
        m=mysql.connector.connect(host="localhost",user="root",password="",database="feedback_system")
        print(m)
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="sname":
                sn=value
            if key=="sclass":
                sc=value
            if key=="sdep":
                sd=value
            if key=="ssem":
                sem=value
            if key=="ID":
                sid=value
            if key=="PASS":
                spas=value

        c="insert into students Values('{}','{}','{}','{}','{}','{}')".format(sn,sc,sd,sem,sid,spas)
        cursor.execute(c)
        m.commit()

    return render(request,"add_student.html")            
