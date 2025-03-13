from flask import *
from src.dbconnection import *
obj=Flask(__name__)
obj.secret_key="preschool"

@obj.route('/')
def main():
    return render_template('Admin Login.html')

@obj.route('/login',methods=['post'])
def login():
    uname=request.form['textfield']
    password=request.form['textfield2']
    qry="select *from login where username=%s and password=%s"
    val=(uname,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("Invalid user");window.location="/"</script>'''
    else:
        return render_template("Admin Home.html")

@obj.route('/add_lessons')
def add_lessons():
    return render_template('Add Lessons.html')

@obj.route('/add_teacher')
def add_teacher():
    return render_template('Add Teacher.html')


@obj.route('/insert_teacher',methods=['post'])
def insert_teacher():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    gender=request.form['RadioGroup1']
    dob=request.form['textfield8']
    qualification=request.form['textfield4']
    email=request.form['textfield7']
    phone=request.form['textfield3']
    uname=request.form['textfield5']
    password=request.form['textfield6']
    qry="INSERT INTO login VALUES(NULL,%s,%s,'teacher')"
    val=(uname,password)
    lid=iud(qry,val)
    qry1="INSERT INTO teacher VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(fname,lname,gender,email,phone,str(lid),dob,qualification)
    iud(qry1,val1)
    return '''<script>alert("Registration Success!!!");window.location="/manage_teachers"</script>'''


@obj.route('/allocate_students')
def allocate_students():
    return render_template('Allocate Students.html')

@obj.route('/approve_parent')
def approve_parent():
    qry="SELECT * FROM `parent table` JOIN `login` ON `login`.id=`parent table`.`lid` WHERE `login`.`type`!='parent'"
    res=selectall(qry)
    return render_template('Approve Parent.html',val=res)

@obj.route('/approval',methods=['get'])
def approval():
    id = request.args.get('id')
    print(id)
    qry="update login set type='parent' where id=%s"
    val=(str(id))
    iud(qry,val)
    return '''<script>alert("Approval Success!!!");window.location="/approve_parent"</script>'''

@obj.route('/reject',methods=['get'])
def reject():
    id = request.args.get('id')
    qry = "delete from `parent table` where lid=%s"
    val = (str(id))
    iud(qry,val)
    qry1 = "delete from login where id=%s"
    print(id)
    val1 = (str(id))
    iud(qry1,val1)
    return '''<script>alert("Rejection Success!!!");window.location="/approve_parent"</script>'''


@obj.route('/chat_with_parent')
def chat_with_parent():
    return render_template('Chat With Parent')

@obj.route('/complants_and_reply')
def complants_and_reply():
    qry="SELECT `complaint`.*,`parent table`.`first_name`,`last_name` FROM `parent table` JOIN `complaint` ON `complaint`.`pid`=`parent table`.`lid`"
    res=selectall(qry)
    return render_template('Complants And Reply.html',val=res)

@obj.route('/manage_lessons')
def manage_lessons():
    return render_template('Manage Lessons.html')

@obj.route('/manage_teachers')
def manage_teachers():
    qry="select * from teacher"
    res=selectall(qry)
    return render_template('Manage Teachers.html',val=res)

@obj.route('/update_teacher',methods=['post'])
def update_teacher():
    lid=session['lid']
    fname = request.form['textfield']
    lname = request.form['textfield2']
    gender = request.form['RadioGroup1']
    dob = request.form['textfield8']
    qualification = request.form['textfield4']
    email = request.form['textfield7']
    phone = request.form['textfield3']
    qry1="update teacher set first_name=%s,last_name=%s,gender=%s,dob=%s,qualification=%s,email=%s,phone=%s where lid=%s"
    val1=(fname,lname,gender,dob,qualification,email,phone,str(lid))
    iud(qry1,val1)
    return '''<script>alert("Updation Success!!!");window.location="/manage_teachers"</script>'''

@obj.route('/edit_teacher')
def edit_teacher():
    id = request.args.get('id')
    session['lid']=id
    qry = "select * from teacher where lid=%s"
    val=(str(id))
    res = selectone(qry,val)

    return render_template('Edit Teacher.html',val=res)

@obj.route('/delete_teacher')
def delete_teacher():
    id=request.args.get('id')
    qry="delete from teacher where teacher.lid=%s"
    val=(str(id))
    iud(qry,val)
    return '''<script>alert("Deletion Success!!!");window.location="/manage_teachers"</script>'''

@obj.route('/send_reply',methods=['get'])
def send_reply():
    id=request.args.get('id')
    session['id']=id
    return render_template('Send reply.html')


@obj.route('/send_reply2',methods=['post'])
def send_reply2():
    id=session['id']
    reply=request.form['textfield']
    qry="update complaint set reply=%s where pid=%s"
    val=(reply,str(id))
    iud(qry,val)
    return '''<script>alert("Success!!!");window.location="/complants_and_reply"</script>'''


@obj.route('/student_allocation')
def student_allocation():
    return render_template('Student Allocation.html')

@obj.route('/student_work')
def student_work():
    return render_template('Student Work.html')

@obj.route('/teacher_home')
def teacher_home():
    return render_template('Teacher Home.html')

@obj.route('/upload_activity')
def upload_activity():
    return render_template('Upload Activity.html')

@obj.route('/view_parent')
def view_parent():
    qry = "SELECT * FROM `parent table` JOIN `login` ON `login`.id=`parent table`.`lid` WHERE `login`.`type`='parent'"
    res = selectall(qry)
    return render_template('View Parent.html',val=res)

@obj.route('/view_photo_and_video')
def view_photo_and_video():
    return render_template('View Photo And Video.html')

@obj.route('/view_rating')
def view_rating():
    return render_template('View Rating.html')

@obj.route('/view_work')
def view_work():
    return render_template('View Work.html')




obj.run(debug=True)