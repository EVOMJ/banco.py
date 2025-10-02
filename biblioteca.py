import sqlite3

# Conexão 
conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()


# 1 
cursor.execute("""
CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nacionalidade TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    ano INTEGER,
    id_autor INTEGER,
    FOREIGN KEY (id_autor) REFERENCES autores(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_livro INTEGER,
    nome_aluno TEXT,
    data_emprestimo TEXT,
    data_devolucao TEXT,
    FOREIGN KEY (id_livro) REFERENCES livros(id)
)
""")




