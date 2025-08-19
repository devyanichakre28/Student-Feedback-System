from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import mysql.connector as sql
import matplotlib.pyplot as plt
import io
import base64

def homepage(request):
    global id , pas, sem
    if request.method == "POST":
        id = request.POST.get("ID")
        pas = request.POST.get("PASS")
        sem = request.POST.get("SEM")

        conn = sql.connect(
            host="localhost",
            user="root",
            password="",
            database="feedback_system"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, password FROM students WHERE user_id = %s AND password = %s AND s_sem = %s", (id, pas, sem))
        rows = cursor.fetchall()
        conn.close()
        if rows:
            return HttpResponseRedirect("/feed_form" )
    
    return render(request, "index.html")

def a_login(request):
    try:
        if request.method=="POST":
            a=["shri","shripad","shree","admin","anjali"]
            n1=(request.POST.get("ID"))
            n2=(request.POST.get("PASS"))
        
            for n in a:
                if n1==n and n2=="s123" or n1==n and n2=="a123":
                    return HttpResponseRedirect("/add_student/")
    except:
        pass 
    
    return render(request,"adminlogin.html")

def a_panel(request):
    return render(request,"admin_panel.html")

def  add_stud(request):
    return render(request,"add_student.html")

def add_teacher(request):
    return render(request,"add_teacher.html")

def del_teacher(request):
    try:
        if request.method=="POST":
            
            n1=(request.POST.get("tname"))
            n2=(request.POST.get("tsub"))
            n3=(request.POST.get("tdep"))
            n4=(request.POST.get("tsem"))

            conn = sql.connect(
            host="localhost",
            user="root",
            password="",
            database="feedback_system"
            )
            cursor = conn.cursor()
            cursor.execute("DELETE FROM teacher WHERE teacher_name = %s AND teaching_subject = %s AND teaching_department = %s AND teaching_sem = %s",(n1, n2, n3, n4))
            conn.close()
    except:
        pass 

    return render(request,"delet_teacher.html")


def stud_feedback(request):
    dep = []
    sem = []
    ssub = []
    feedbacks_q1 = []
    feedbacks_q2 = []
    feedbacks_q3 = []
    feedbacks_q4 = []
    feedbacks_q5 = []
    feedbacks_q6 = []
    verybad_q1, poor_q1, good_q1, better_q1, excellent_q1 = [], [], [], [], []
    verybad_q2, poor_q2, good_q2, better_q2, excellent_q2 = [], [], [], [], []
    verybad_q3, poor_q3, good_q3, better_q3, excellent_q3 = [], [], [], [], []
    verybad_q4, poor_q4, good_q4, better_q4, excellent_q4 = [], [], [], [], []
    verybad_q5, poor_q5, good_q5, better_q5, excellent_q5 = [], [], [], [], []
    verybad_q6, poor_q6, good_q6, better_q6, excellent_q6 = [], [], [], [], []

    conn = sql.connect(
        host="localhost",
        user="root",
        password="",
        database="feedback_system"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT teaching_department FROM teacher")
    rowdep = cursor.fetchall()
    for item in rowdep:
        dep.append(item[0])

    cursor.execute("SELECT DISTINCT teaching_sem FROM teacher")
    rowsem = cursor.fetchall()
    for item in rowsem:
        sem.append(item[0])

    if request.method == 'GET' and 'Marking1' in request.GET and 'Marking2' in request.GET:
        selected_department = request.GET.get('Marking1')
        selected_semester = request.GET.get('Marking2')

        cursor.execute("SELECT teacher_name FROM teacher WHERE teaching_department = %s AND teaching_sem = %s", 
                       (selected_department, selected_semester))
        rowteachers = cursor.fetchall()
        for item in rowteachers:
            ssub.append(item[0])

        if 'teacher_select' in request.GET:
            selected_teacher = request.GET.get('teacher_select')
            cursor.execute("SELECT q1, q2, q3, q4, q5, q6 FROM feedback WHERE teaching_sem = %s AND teacher_name = %s", 
                           (selected_semester, selected_teacher))
            feedbacks = cursor.fetchall()

            for item in feedbacks:
                # Question 1 feedbacks
                if item[0] == 1:
                    verybad_q1.append(item[0])
                elif item[0] == 2:
                    poor_q1.append(item[0])
                elif item[0] == 3:
                    good_q1.append(item[0])
                elif item[0] == 4:
                    better_q1.append(item[0])
                elif item[0] == 5:
                    excellent_q1.append(item[0])
                
                # Question 2 feedbacks
                if item[1] == 1:
                    verybad_q2.append(item[1])
                elif item[1] == 2:
                    poor_q2.append(item[1])
                elif item[1] == 3:
                    good_q2.append(item[1])
                elif item[1] == 4:
                    better_q2.append(item[1])
                elif item[1] == 5:
                    excellent_q2.append(item[1])
                
                # Question 3 feedbacks
                if item[2] == 1:
                    verybad_q3.append(item[2])
                elif item[2] == 2:
                    poor_q3.append(item[2])
                elif item[2] == 3:
                    good_q3.append(item[2])
                elif item[2] == 4:
                    better_q3.append(item[2])
                elif item[2] == 5:
                    excellent_q3.append(item[2])
                
                # Question 4 feedbacks
                if item[3] == 1:
                    verybad_q4.append(item[3])
                elif item[3] == 2:
                    poor_q4.append(item[3])
                elif item[3] == 3:
                    good_q4.append(item[3])
                elif item[3] == 4:
                    better_q4.append(item[3])
                elif item[3] == 5:
                    excellent_q4.append(item[3])
                
                # Question 5 feedbacks
                if item[4] == 1:
                    verybad_q5.append(item[4])
                elif item[4] == 2:
                    poor_q5.append(item[4])
                elif item[4] == 3:
                    good_q5.append(item[4])
                elif item[4] == 4:
                    better_q5.append(item[4])
                elif item[4] == 5:
                    excellent_q5.append(item[4])
                
                # Question 6 feedbacks
                if item[5] == 1:
                    verybad_q6.append(item[5])
                elif item[5] == 2:
                    poor_q6.append(item[5])
                elif item[5] == 3:
                    good_q6.append(item[5])
                elif item[5] == 4:
                    better_q6.append(item[5])
                elif item[5] == 5:
                    excellent_q6.append(item[5])

    def generate_bar_plot(verybad, poor, good, better, excellent, title):
        categories = ['Very Bad', 'Poor', 'Good', 'Better', 'Excellent']
        values = [len(verybad), len(poor), len(good), len(better), len(excellent)]
        total = sum(values)

        fig, ax = plt.subplots()
        ax.bar(categories, values, color=['red', 'orange', 'yellow', 'green', 'blue'])
        ax.set_xlabel('Feedback Category')
        ax.set_ylabel('Number of People')
        ax.set_title(title)
        ax.text(0.5, 0.95, f'Total People: {total}', 
                transform=ax.transAxes, ha='center', va='center', fontsize=12, color='black')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()
        return image_base64

    bar_plot_image_q1 = generate_bar_plot(verybad_q1, poor_q1, good_q1, better_q1, excellent_q1, 'Communication and Presentation Skills')
    bar_plot_image_q2 = generate_bar_plot(verybad_q2, poor_q2, good_q2, better_q2, excellent_q2, 'Explanation with practical examples to understand the subject')
    bar_plot_image_q3 = generate_bar_plot(verybad_q3, poor_q3, good_q3, better_q3, excellent_q3, 'Well Prepared for the lectures with notes referring to renowned books?')
    bar_plot_image_q4 = generate_bar_plot(verybad_q4, poor_q4, good_q4, better_q4, excellent_q4, ' Syllabus completion and exam preparation')
    bar_plot_image_q5 = generate_bar_plot(verybad_q5, poor_q5, good_q5, better_q5, excellent_q5, 'Effective use of teaching tools and blackboard')
    bar_plot_image_q6 = generate_bar_plot(verybad_q6, poor_q6, good_q6, better_q6, excellent_q6, 'Overall Satisfaction')

    conn.close()
    return render(request, "feedback.html", {
        'dep': dep, 'sem': sem, 'ssub': ssub,
        'bar_plot_image_q1': bar_plot_image_q1,
        'bar_plot_image_q2': bar_plot_image_q2,
        'bar_plot_image_q3': bar_plot_image_q3,
        'bar_plot_image_q4': bar_plot_image_q4,
        'bar_plot_image_q5': bar_plot_image_q5,
        'bar_plot_image_q6': bar_plot_image_q6
    })

def feed_form(request):
    global id,pas,sem
    sname = None
    conn = sql.connect(
            host="localhost",
            user="root",
            password="",
            database="feedback_system"
        )
    cursor = conn.cursor()
    cursor.execute("SELECT studnet_name,s_dep FROM students WHERE user_id = %s AND password = %s AND s_sem = %s", (id, pas, sem))
    sname = cursor.fetchone()
    s_dep=sname[1]
    cursor.execute("select teacher_name , teaching_subject from teacher where teaching_sem=%s and teaching_department=%s",(sem,s_dep))
    dep=cursor.fetchall()
    cursor.execute("select teaching_sem from teacher where teaching_sem=%s and teaching_department=%s",(sem,s_dep))
    s_sem=cursor.fetchone()
    ssem=s_sem[0]
    dep1=[]

    result_list = []
    list1=[]
    list2=[]
    for item in dep:
        list1.append(item[0])
        list2.append(item[1])
    
    if sname:
            sname = sname[0]

    conn.close()
    return render(request, "form.html", {'sname': sname,'tname':list1,'ssub':list2,'ssem':ssem})