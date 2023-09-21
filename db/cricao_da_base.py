# Recriando a função de inicialização da base de dados
import sqlite3

def initialize_database_v2():
    conn = sqlite3.connect("e_magic_shop_v2.db")
    cursor = conn.cursor()

    # Criando tabelas
    cursor.execute("DROP TABLE IF EXISTS Usuarios")
    cursor.execute("DROP TABLE IF EXISTS Produtos")
    cursor.execute("DROP TABLE IF EXISTS Classificacoes")

    cursor.execute("""
    CREATE TABLE Usuarios(
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cpf TEXT NOT NULL,
        endereco TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE Produtos(
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        descricao TEXT NOT NULL,
        categoria TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE Classificacoes(
        id_usuario INTEGER,
        id_produto INTEGER,
        comentario TEXT NOT NULL,
        FOREIGN KEY(id_usuario) REFERENCES Usuarios(id),
        FOREIGN KEY(id_produto) REFERENCES Produtos(id)
    )
    """)

    # Inserindo valores padrão
    usuarios = [
        (1, "Alice", 28, "12345678901", "Rua das Maravilhas, 10", "alice@wonderland.com"),
        (2, "Bob", 35, "23456789012", "Rua dos Construtores, 5", "bob@builder.com"),
        (3, "Charlie", 40, "34567890123", "Praça dos Chocolate, 7", "charlie@chocolate.com"),
        (4, "Diana", 29, "45678901234", "Avenida das Caçadoras, 15", "diana@amazon.com"),
        (5, "Eduardo", 50, "56789012345", "Beco dos Economistas, 20", "ed@economy.com")
    ]

    produtos = [
        (1, "Varinha Mágica", "Varinha feita de madeira de carvalho", "Magia", 99.90, 10),
        (2, "Teclado Mecânico", "RGB com switches blue", "Eletrônicos", 150.00, 20),
        (3, "Pó de Fada", "Pó mágico que concede voo temporário", "Magia", 200.00, 5),
        (4, "Headset Gamer", "7.1 canais com microfone", "Eletrônicos", 80.00, 15),
        (5, "Pergaminho Encantado", "Pergaminho que revela segredos", "Magia", 50.00, 8),
        (6, "Mouse Gamer", "RGB com DPI ajustável", "Eletrônicos", 40.00, 25),
        (7, "Elixir da Longevidade", "Bebida mágica que prolonga a vida", "Magia", 500.00, 3)
    ]

    cursor.executemany("INSERT INTO Usuarios VALUES (?, ?, ?, ?, ?, ?)", usuarios)
    cursor.executemany("INSERT INTO Produtos VALUES (?, ?, ?, ?, ?, ?)", produtos)
    cursor.execute("INSERT INTO Classificacoes VALUES (4, 2, 'Ótimo teclado!')")

    conn.commit()
    conn.close()

# Chamando a função para inicializar o banco de dados
initialize_database_v2()
