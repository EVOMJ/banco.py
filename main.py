import sqlite3 

# Autores
# banco = sqlite3.connect('biblioteca.db')
# cursor = banco.cursor()

# cursor.execute("INSERT INTO autores (nome, nacionalidade) VALUES (?, ?)", ("lucas", "Santana de Parnaiba"))


# banco.commit()


# cursor.execute("SELECT * FROM autores")
# print(cursor.fetchall())

# banco.close()




# banco = sqlite3.connect("biblioteca.db")
# cursor = banco.cursor()


# cursor.execute("""
# INSERT INTO emprestimos (id_livro, nome_aluno, data_emprestimo, data_devolucao)
# VALUES (?, ?, ?, ?)
# """, (3, "Marcos Jesus ", "2025-10-20", "2025-11-02")) 

# banco.commit()
# banco.close()



# # delete teste em emprestimos
# banco = sqlite3.connect("biblioteca.db")
# cursor = banco.cursor()


# cursor.execute("DELETE FROM emprestimos  WHERE id = ?", (1,))

# banco.commit()
# banco.close()


# # livros
# banco = sqlite3.connect("biblioteca.db")
# cursor = banco.cursor()


# cursor.execute("""
# INSERT INTO livros (id,titulo , ano, id_autor)
# VALUES (?, ?, ?, ?)
# """, (4, "Escola de HipHop", "2004-09-02", 3)) 



# banco.commit()
# banco.close()

# # Atualizar um dade de DEVOLUCAO
# banco = sqlite3.connect("biblioteca.db")
# cursor = banco.cursor()

# cursor.execute("""
#  UPDATE emprestimos SET data_devolucao = '2025-10-20'  WHERE id = 4  """)

 
# banco.commit()
# banco.close()









