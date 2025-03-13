import pymysql
def iud(qry,values):
    con=pymysql.connect(host='localhost',port=3306,user='root',password='',db='preschool')
    cmd=con.cursor()
    cmd.execute(qry,values)
    id=cmd.lastrowid
    con.commit()
    return id
def selectall(qry):
    con = pymysql.connect(host='localhost', port=3306, user='root', password='', db='preschool')
    cmd = con.cursor()
    cmd.execute(qry)
    res=cmd.fetchall()
    return res
def selectall2(qry,values):
    con = pymysql.connect(host='localhost', port=3306, user='root', password='', db='preschool')
    cmd = con.cursor()
    cmd.execute(qry, values)
    res=cmd.fetchall()
    return res
def selectone(qry,values):
    con = pymysql.connect(host='localhost', port=3306, user='root', password='', db='preschool')
    cmd = con.cursor()
    cmd.execute(qry, values)
    res=cmd.fetchone()
    return res

def selectonenew(qry):
    con = pymysql.connect(host='localhost', port=3306, user='root', password='', db='preschool')
    cmd = con.cursor()
    cmd.execute(qry)
    res=cmd.fetchone()
    return res


def androidselectall(q,val):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='preschool')
    cmd=con.cursor()
    cmd.execute(q,val)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data

def androidselectallnew(q):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='preschool')
    cmd=con.cursor()
    cmd.execute(q)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data
def androidselectallneww(q,v):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='preschool')
    cmd=con.cursor()
    cmd.execute(q,v)
    s=cmd.fetchall()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data
def andro(q,v):
    con=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='preschool')
    cmd=con.cursor()
    cmd.execute(q,v)
    s=cmd.fetchone()
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    print(json_data)
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return json_data