import sqlite3

class Client:
    
    def __init__(self, phone, info = None, created = None):
        self.phone = phone
        self.info = info
        self.created = created

    def dump(self):
        print(self.phone, self.info, self.created)

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect('base.sql')
        cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE clients(\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                phone STRING not null,\
                info STRING,\
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP\
            );'
        )
        cursor.execute('CREATE INDEX phone_idx ON clients (phone);')
        cursor.close()

    @classmethod
    def select_by_phone(cls, phones):
        conn = sqlite3.connect('base.sql')
        scalar = False if isinstance(phones, list) else True
        result = []
        if scalar:
            phones = [ phones ]
        if not len(phones):
            return result
        cursor = conn.cursor()
        in_list = ','.join( list(map (lambda i: i, phones)) )
        cursor.execute('SELECT phone, info, created from clients WHERE phone IN (%s) order by created' % in_list)
        result = list(map( lambda item: Client(item[0], item[1], item[2]), cursor.fetchall()))
        cursor.close()
        
        return result

    @classmethod
    def insert(cls, obj):
        conn = sqlite3.connect('base.sql')
        cursor = conn.cursor()
        scalar = False if isinstance(obj, list) else True
        if scalar:
            obj = [ obj ]

        try:
            value_str = ','.join( list(map (lambda o: "({}, '{}')".format(o.phone, o.info or ''), obj)))
            cursor.execute('INSERT INTO clients (phone, info) VALUES %s' % value_str)
            cursor.close()
        except Exception as e:
            print(e)
            return False

        conn.commit()
        return True
        

