import sqlite3

class Client:
    
    def __init__(self, phone, info = None):
        self.id = phone
        self.info = info

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect('base.sql')
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE clients(\
                id str not null,\
                info str,\
                PRIMARY KEY (id)\
            )"
        )
    
    @classmethod
    def select_by_id(cls, id):
        conn = sqlite3.connect('base.sql')
        scalar = False if isinstance(id, list) else True
        result = []
        if scalar:
            id = [ id ]
        if not len(id):
            return result

        with  conn.cursor() as cursor:
            in_list = ','.join( list(map (lambda i: '%s', id)) )
            cursor.execute('SELECT from client WHER id IN (%s)' % in_list, id)
            result = list(map lambda item: Client(item[0], item[1]), cursor.fetchall())
        
        return result
    
    def insert(self):
        conn = sqlite3.connect('base.sql')

        with  conn.cursor() as cursor:
            cursor.execute('INSERT INTO clients )
            result = list(map lambda item: Client(item[0], item[1]), cursor.fetchall())
        
        return result
        

