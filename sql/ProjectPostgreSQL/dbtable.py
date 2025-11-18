# Базовые действия с таблицами

from dbconnection import *

class DbTable:
    dbconn = None

    def __init__(self):
        return

    def table_name(self):
        return self.dbconn.prefix + "table"

    def columns(self):
        return {"test": ["integer", "PRIMARY KEY"]}

    def column_names(self):
        return sorted(self.columns().keys())

    def primary_key(self):
        return ['id']

    def column_names_without_id(self):
        res = sorted(self.columns().keys())
        if 'id' in res:
            res.remove('id')
        return res

    def table_constraints(self):
        return []

    def create(self):
        sql = "CREATE TABLE " + self.table_name() + "("
        arr = [k + " " + " ".join(v) for k, v in sorted(self.columns().items(), key = lambda x: x[0])]
        sql += ", ".join(arr + self.table_constraints())
        sql += ")"
        cur = self.dbconn.conn.cursor()
        cur.execute(sql)
        self.dbconn.conn.commit()
        return

    def drop(self):
        sql = "DROP TABLE IF EXISTS " + self.table_name() + " CASCADE"
        cur = self.dbconn.conn.cursor()
        cur.execute(sql)
        self.dbconn.conn.commit()
        return

    def insert_one(self, vals):
        sql_vals = []
        for val in vals:
            if val is None:
                sql_vals.append("NULL")  
            elif type(val) == str:
                sql_vals.append("'" + val + "'")
            else:
                sql_vals.append(str(val))
        
        sql = "INSERT INTO " + self.table_name() + "("
        sql += ", ".join(self.column_names_without_id()) + ") VALUES("
        sql += ", ".join(sql_vals) + ")"
        cur = self.dbconn.conn.cursor()
        cur.execute(sql)
        self.dbconn.conn.commit()
        return
    
    def update_by_id(self, record_id, updates):
        """Обновление записи по ID"""
        set_clause = []
        for col, val in updates.items():
            if val is None:
                set_clause.append(f"{col} = NULL")
            elif isinstance(val, str):
                set_clause.append(f"{col} = %s")
            else:
                set_clause.append(f"{col} = %s")
        
        pk_column = self.primary_key()[0]
        sql = f"UPDATE {self.table_name()} SET {', '.join(set_clause)} WHERE {pk_column} = %s"
        
        # Подготавливаем значения для параметризованного запроса
        values = [val for val in updates.values() if not isinstance(val, str) or val is not None]
        values.append(record_id)
        
        cur = self.dbconn.conn.cursor()
        cur.execute(sql, values)
        self.dbconn.conn.commit()
        return

    def delete_by_id(self, record_id):
        pk_column = self.primary_key()[0]
        sql = f"DELETE FROM {self.table_name()} WHERE {pk_column} = %s"
        cur = self.dbconn.conn.cursor()
        cur.execute(sql, (record_id,))
        self.dbconn.conn.commit()
        return

    def first(self):
        sql = "SELECT * FROM " + self.table_name()
        sql += " ORDER BY "
        sql += ", ".join(self.primary_key())
        cur = self.dbconn.conn.cursor()
        cur.execute(sql)
        return cur.fetchone()        

    def last(self):
        sql = "SELECT * FROM " + self.table_name()
        sql += " ORDER BY "
        sql += ", ".join([x + " DESC" for x in self.primary_key()])
        cur = self.dbconn.conn.cursor()
        cur.execute(sql)
        return cur.fetchone()

    def all(self):
        sql = "SELECT * FROM " + self.table_name()
        sql += " ORDER BY "
        sql += ", ".join(self.primary_key())
        cur = self.dbconn.conn.cursor()
        cur.execute(sql)
        return cur.fetchall()