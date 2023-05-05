import pymysql


class Connect:
    def __init__(self, host, port, user, password, database, charset):
        self.connect = pymysql.connect(host=host,
                                       port=port,
                                       user=user,
                                       password=password,
                                       database=database,
                                       charset=charset,
                                       cursorclass=pymysql.cursors.DictCursor)

    def function(self):
        with self.connect.cursor() as cur:
            self.connect.commit()
            pass
