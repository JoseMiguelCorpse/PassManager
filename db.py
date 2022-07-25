import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS PASSWORD (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Titulo text,
        Usuario text, 
        Email text, 
        Categoria text,
        Password text,
        Url text)
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, mititulo, miUsuario, miEmail, miCategoria, miPassword, miUrl):
        self.cur.execute("insert into PASSWORD values (NULL,?,?,?,?,?,?)",
                         (mititulo, miUsuario, miEmail, miCategoria, miPassword, miUrl))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from PASSWORD")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, Usuario):
        self.cur.execute("delete from PASSWORD where Usuario=?", (Usuario,))
        self.con.commit()

    # Update a Record in DB
    def update(self, ID, Titulo, Usuario, Email, Categoria, Password, Url):
        self.cur.execute(
            "update PASSWORD set Titulo=?, Usuario=?, Email=?, Categoria=?, Password=?, Url=? where ID=?",
            ((Titulo, Usuario, Email, Categoria, Password, Url, ID)))
        self.con.commit()