# Таблица категорий и особые действия с ней

from dbtable import *

class CategoriesTable(DbTable):
    def table_name(self):
        return self.dbconn.prefix + "categories"

    def columns(self):
        return {
            "id": ["serial", "PRIMARY KEY"],
            "name": ["varchar(64)", "NOT NULL", "UNIQUE"],
            "parent_id": ["integer", "REFERENCES categories(id)"]
        }

    def find_by_position(self, num):
        if num <= 0:
            return None
        sql = "SELECT * FROM " + self.table_name()
        sql += " ORDER BY "
        sql += ", ".join(self.primary_key())
        sql += " LIMIT 1 OFFSET %(offset)s"
        cur = self.dbconn.conn.cursor()
        cur.execute(sql, {"offset": num - 1})
        return cur.fetchone()

    def find_by_id(self, category_id):
        sql = "SELECT * FROM " + self.table_name() + " WHERE id = %s"
        cur = self.dbconn.conn.cursor()
        cur.execute(sql, (category_id,))
        return cur.fetchone()