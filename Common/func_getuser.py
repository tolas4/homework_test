import random
from Common.func_db import ConnDB
from Common.func_option import conf
from Common.func_requests import send_request


def get_username():
    global username
    db = ConnDB()
    count = 1
    while count != 0:
        username = __new_name()
        count = db.get_acount("SELECT * FROM auth_user WHERE username='{}'".format(username))
    db.close_db()
    return username


def get_email():
    global email
    db = ConnDB()
    count = 1
    while count != 0:
        email = __new_email()
        count = db.get_acount("SELECT * FROM auth_user WHERE username='{}'".format(email))
    db.close_db()
    return email


def __new_name():
    name = ""
    for i in range(6):
        a = random.randint(97, 122)
        a = chr(a)
        name += a
    return name


def __new_email():
    email = ""
    for i in range(8):
        a = random.randint(1, 9)
        email += str(a)
    email += "@qq.com"
    return email


def new_password():
    pwd = "123456"
    return pwd


def get_proname():
    db = ConnDB()
    count = 1
    while count != 0:
        proname = __new_name()
        proname = "这是一个{}的项目".format(proname)
        count = db.get_acount("SELECT * FROM tb_projects WHERE name='{}'".format(proname))
    db.close_db()
    return proname



# ss = get_username()
# print(ss)
# aa = get_email()
# print(aa)
# db = ConnDB()
# count = db.get_acount("SELECT * FROM auth_user WHERE username='lemin123'")
# print(count)
