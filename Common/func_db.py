import pymysql
from Common.func_option import conf


class ConnDB:

    def __init__(self):
        self.conn = pymysql.connect(
            host=conf.get("db_server", "host"),
            user=conf.get("db_server", "user"),
            port=conf.getint("db_server", "port"),
            database=conf.get("db_server", "database"),
            password=conf.get("db_server", "password"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    def select_one(self, sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def select_all(self, sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def update(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def get_acount(self, sql):
        self.conn.commit()
        return self.cur.execute(sql)

    def close_db(self):
        self.cur.close()
        self.conn.close()


# class ENV:
#     pass
# db = ConnDB()
#
# ss = db.select_one("SELECT username FROM auth_user WHERE id=1")
# for key, value in ss.items():
#     setattr(ENV, key, value)
# clear_EnvData()
# print(ENV.__dict__)