from django.shortcuts import render,redirect
import mysql.connector as sql
from django.http import HttpResponse, HttpResponseRedirect

tn=''
ts=''
tss=''
q1=''
q2=''
q3=''
q4=''
q5=''
q6=''
q7=''


def data(request):
    global tn,ts,tss,q1,q2,q3,q4,q5,q6,q7
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="",database='feedback_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="tname":
                tn=value
            if key=="subject":
                ts=value
            if key=="sem":
                tss=value
            if key=="Marking1":
                q1=value
            if key=="Marking2":
                q2=value
            if key=="Marking3":
                q3=value
            if key=="Marking4":
                q4=value
            if key=="Marking5":
                q5=value
            if key=="Marking6":
                q6=value
            if key=="comment":
                q7=value
        c="insert into feedback Values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(tn,ts,tss,q1,q2,q3,q4,q5,q6,q7)
        cursor.execute(c)
        m.commit()
    
    return redirect("/feed_form")