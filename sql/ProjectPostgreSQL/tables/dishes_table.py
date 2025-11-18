# Таблица блюд и особые действия с ней.

from dbtable import *

class DishesTable(DbTable):
    def table_name(self):
        return self.dbconn.prefix + "dishes"

    def columns(self):
        return {
            "id": ["serial", "PRIMARY KEY"],
            "name": ["varchar(64)", "NOT NULL", "UNIQUE"],
            "category_id": ["integer", "NOT NULL", "REFERENCES categories(id) ON DELETE CASCADE"],
            "image_id": ["integer", "REFERENCES images(id)"],  # Убрал NOT NULL
            "time": ["integer", "NOT NULL"],
            "description": ["text", "NOT NULL"],
            "technic": ["text", "NOT NULL"]
        }
    
    def primary_key(self):
        return ['id']

    def table_constraints(self):
        return [] 

    def all_by_category_id(self, cid):
        sql = "SELECT * FROM " + self.table_name()
        sql += " WHERE category_id = %s"
        sql += " ORDER BY "
        sql += ", ".join(self.primary_key())
        cur = self.dbconn.conn.cursor()
        cur.execute(sql, (cid,)) 
        return cur.fetchall()