from data.db import Database

class ColaboradorModel:
    def __init__(self, id, nome, idade, gestor, alocacao, create_at):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.gestor = gestor
        self.alocacao = alocacao
        self.create_at = create_at

    # Create
    def create_colaborador(self):
        db = Database()
        db.cursor.execute(f"""
            INSERT INTO colaborador (id, nome, idade, gestor, alocacao, create_at)
            VALUES ('{self.id}', '{self.nome}', {self.idade}, '{self.gestor}', '{self.alocacao}', '{self.create_at}')
        """)
        db.connection.commit()
        db.close_connection()
        return self.id

    # Read
    @staticmethod
    def get_all_colaboradores():
        db = Database()
        db.cursor.execute(f"""
            SELECT * FROM colaborador
        """)
        colaboradores = db.cursor.fetchall()
        db.close_connection()
        return colaboradores
    
    @staticmethod
    def get_colaborador_by_id(id):
        db = Database()
        db.cursor.execute(f"""
            SELECT * FROM colaborador WHERE id = '{id}'
        """)
        colaborador = db.cursor.fetchone()
        db.close_connection()
        return colaborador

    # Update
    def update_colaborador(self):
        db = Database()
        db.cursor.execute(f"""
            UPDATE colaborador SET 
                nome = '{self.nome}',
                idade = {self.idade},
                gestor = '{self.gestor}',
                alocacao = '{self.alocacao}'
            WHERE id = '{self.id}'
        """)
        db.connection.commit()
        db.close_connection()
        return self.id
    
    # Delete
    @staticmethod
    def delete_colaborador(id):
        db = Database()
        db.cursor.execute(f"""
            DELETE FROM colaborador WHERE id = '{id}'
        """)
        db.connection.commit()
        db.close_connection()
        return id
