from data.db import Database

class DesempenhoModel:
    def __init__(self, id, id_colaborador, id_gestor, nota_avaliacao, comentario):
        self.id = id
        self.id_colaborador = id_colaborador
        self.id_gestor = id_gestor
        self.nota_avaliacao = nota_avaliacao
        self.comentario = comentario

    def create_desempenho(self):
        db = Database()
        db.cursor.execute(f"""
            INSERT INTO engajamento (id_engajamento_pk, id_colaborador_fk, id_gestor_fk, nota_avaliacao, comentario)
            VALUES ('{self.id}', '{self.id_colaborador}', '{self.id_gestor}', '{self.nota_avaliacao}', '{self.comentario}');
        """)
        db.connection.commit()
        db.close_connection()
        return self.id
    
    # @staticmethod
    def get_all_desempenhos():
        db = Database()
        db.cursor.execute(f"""
            SELECT C.id_colaborador_pk, C.nome_colaborador, E.nota_avaliacao, E.comentario, G.nome_gestor, S.nome_setor, E.created_at FROM engajamento as E
                LEFT JOIN colaborador as C ON E.id_colaborador_fk = C.id_colaborador_pk
                LEFT JOIN setor as S ON C.id_setor_fk = S.id_setor_pk
                LEFT JOIN gestor as G ON E.id_gestor_fk = G.id_gestor_pk
            ORDER BY E.created_at ASC
        """)
        desempenhos = db.cursor.fetchall()
        db.close_connection()
        return desempenhos

    # Delete
    @staticmethod
    def delete_desempenho(id):
        db = Database()
        db.cursor.execute(f"""
            DELETE FROM engajamento WHERE id_engajamento_pk = '{id}';
        """)
        db.connection.commit()
        db.close_connection()
        return id
