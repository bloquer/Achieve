import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'tmvjswl@2877',
    database = 'hw3'
)

mycursor = mydb.cursor()

make_db = 'create database hw3'
st_table = 'create table student (id int not null, pw varchar(64) not null, name varchar(64) not null' \
           ', phone varchar(64), email varchar(128), adviser int not null, dept int not null, primary key(id)' \
           ', foreign key (adviser) references professor(id), foreign key (dept) references department(id))'
prof_table = 'create table professor (id int not null, name varchar(64) not null, phone varchar(64)' \
             ', email varchar(128), dept int not null, primary key (id), foreign key (dept)' \
             'references department(id))'
dept_table = 'create table department (id int not null, name varchar(64) not null, location varchar(32) not null, primary key (id))'


stu_data = 'insert into student (id, pw, name, phone, email, adviser, dept) values (%s, %s, %s, %s, %s, %s, %s)'
stu_val = [
    (201400, "what", "Jocker", "010-5924-5940", "wefn2@gmail.com", 10010, 41),
    (201401, "are", "Bruce", "010-5890-2149", "eijy56@gmail.com", 10010, 41),
    (201402, "you", "Wayne", "010-1670-1769", "bnxcm99@gmail.com", 10012, 41),
    (201403, "doing", "Queen", "010-1073-1055", "gekr@gmail.com", 10011, 41),
    (201404, "here", "Penguin", "010-9581-9412", "iuoiu245@gmail.com", 10016, 21),
    (201405, "there", "Poison", "010-1860-7819", 'hoijxb@gmail.com', 10015, 21),
    (201406, "are", "Robin", "010-1546-1749", "3598gn@gmail.com", 10017, 58),
    (201407, "so", "Talia", "010-4172-6197", "enig58@gmail.com", 10018, 58),
    (201408, "many", "Hugo", "010-8093-0187", "oeiguoiw@gmail.com", 10014, 43),
    (201409, "books", "Harvey", "010-0751-1643", 'onijvoi@gmail.com', 10013, 43)
]

prof_data = 'insert into professor (id, name, phone, email, dept) values (%s, %s, %s, %s, %s)'
prof_val = [
    (10010, "Aziz", "043-261-3597", "aziz@chungbuk.ac.kr", 41),
    (10011, "KwanHeeYoo", "043-261-2788", "khyoo@chungbuk.ac.kr", 41),
    (10012, "JangEuiHong", "043-261-2261", "jehong@chungbuk.ac.kr", 41),
    (10013, "OkHyeonKim", "043-261-2447", "ohkim@chungbuk.ac.kr", 43),
    (10014, "SeokHoLee", "043-261-2444", "rhi@chungbuk.ac.kr", 43),
    (10015, "HeuiJaeKang", "", "hjkang@chungbuk.ac.kr", 21),
    (10016, "DongHyeonKim", "043-261-2268", "dhkim73@chungbuk.ac.kr", 21),
    (10017, "ChangSeokKang", "043-261-2097", "cskang@chungbuk.ac.kr", 58),
    (10018, "HangBumJo", "043-261-2099", "bum2099@chungbuk.ac.kr", 58)
]

dept_data = 'insert into department (id, name, location) values (%s, %s, %s)'
dept_val = [
    (41, "Software", "S1-4"),
    (43, "Mechanical", "E8-7"),
    (21, "Physics", "S1-1"),
    (58, "Korean", "N16")
]
sql_stu = 'select st.id, st.name, st.phone, st.email, ' \
              'prof.name from student as st join professor as prof' \
              ' on st.adviser = prof.id where st.id=201400'
sql_dept = 'select dept.name, dept.location from department as dept join student as st ' \
               'on dept.id = st.dept where st.id=201400 or st.id=201401'
sql_prof = 'select prof.* from professor as prof join department as dept ' \
               'on dept.id = prof.dept where dept.id = (select dept from student ' \
               'where id=201400)'
mycursor.execute(sql_dept)

list = mycursor.fetchall()

print(list)