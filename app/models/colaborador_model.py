from data.db import Database

class ColaboradorModel:
    def __init__(self, id, nome, idade, id_gestor, id_setor):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.id_gestor = id_gestor
        self.id_setor = id_setor

    # Create
    def create_colaborador(self):
        db = Database()
        db.cursor.execute(f"""
            INSERT INTO colaborador (id_colaborador_pk, nome_colaborador, idade, id_gestor_fk, id_setor_fk)
            VALUES ({self.id}, '{self.nome}', {self.idade}, '{self.id_gestor}', '{self.id_setor}')
        """)
        db.connection.commit()
        db.close_connection()
        return self.id
    
    # Read
    @staticmethod
    def get_all_colaboradores(page, page_size):
        try:
            db = Database()

            offset = (page - 1) * page_size

            query = f"SELECT * FROM colaboradores LIMIT {page_size} OFFSET {offset};"
            db.cursor.execute(query)

            colaboradores = db.cursor.fetchall()
            db.close_connection()

            return colaboradores
        except Exception as e:
            return e
    
    @staticmethod
    def get_colaborador_by_id(id):
        db = Database()
        db.cursor.execute(f"""
            SELECT C.id_colaborador_pk, C.nome_colaborador, C.idade, C.id_gestor_fk, G.nome_gestor, C.id_setor_fk, S.nome_setor, C.created_at FROM colaborador C
                LEFT JOIN gestor G ON C.id_gestor_fk = G.id_gestor_pk
                LEFT JOIN setor S ON C.id_setor_fk = S.id_setor_pk
            WHERE id_colaborador_pk = '{id}'
        """)
        colaborador = db.cursor.fetchone()
        db.close_connection()
        return colaborador

    @staticmethod
    def get_colaborador_by_setor(id_setor):
        db = Database()
        db.cursor.execute(f"""
            SELECT C.id_colaborador_pk, C.nome_colaborador, C.idade, C.id_gestor_fk, G.nome_gestor, C.id_setor_fk, S.nome_setor, C.created_at FROM colaborador C
                LEFT JOIN gestor G ON C.id_gestor_fk = G.id_gestor_pk
                LEFT JOIN setor S ON C.id_setor_fk = S.id_setor_pk
            WHERE id_setor_fk = '{id_setor}'
        """)
        colaborador = db.cursor.fetchall()
        db.close_connection()
        return colaborador
    
    @staticmethod
    def get_all_gestores():
        db = Database()
        db.cursor.execute(f"""
            SELECT * FROM gestores;
        """)
        gestores = db.cursor.fetchall()
        db.close_connection()
        return gestores

    @staticmethod
    def get_all_setores():
        db = Database()
        db.cursor.execute(f"""
            SELECT * FROM setores;
        """)
        setores = db.cursor.fetchall()
        db.close_connection()
        return setores

    @staticmethod
    def get_all_avaliacoes():
        db = Database()
        db.cursor.execute(f"""
            SELECT * FROM avaliacoes;
        """)
        avaliacoes = db.cursor.fetchall()
        db.close_connection()
        return avaliacoes

    # Update
    def update_colaborador(self):
        db = Database()
        db.cursor.execute(f"""
            UPDATE colaborador SET 
                nome_colaborador = '{self.nome}',
                idade = {self.idade},
                id_gestor_fk = '{self.id_gestor}',
                id_setor_fk = '{self.id_setor}'
            WHERE id_colaborador_pk = '{self.id}'
        """)
        db.connection.commit()
        db.close_connection()
        return self.id
    
    # Delete
    @staticmethod
    def delete_colaborador(id):
        db = Database()
        db.cursor.execute(f"""
            DELETE FROM colaborador WHERE id_colaborador_pk = '{id}'
        """)
        db.connection.commit()
        db.close_connection()
        return id
    
# Path: app/models/engajamento_model.py