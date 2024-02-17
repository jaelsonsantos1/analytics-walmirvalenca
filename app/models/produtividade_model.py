from data.db import Database

class ProdutividadeModel:
    def __init__(self, id, id_colaborador, id_gestor, nota_avaliacao, comentario, atingiu_meta):
        self.id = id
        self.id_colaborador = id_colaborador
        self.id_gestor = id_gestor
        self.nota_avaliacao = nota_avaliacao
        self.comentario = comentario
        self.atingiu_meta = atingiu_meta

    def create_produtividade(self):
        db = Database()
        db.cursor.execute(f"""
            INSERT INTO produtividade (id_produtividade_pk, id_colaborador_fk, id_gestor_fk, nota_avaliacao, comentario, atingiu_meta)
            VALUES ('{self.id}', '{self.id_colaborador}', '{self.id_gestor}', '{self.nota_avaliacao}', '{self.comentario}', '{self.atingiu_meta}');
        """)
        db.connection.commit()
        db.close_connection()
        return self.id

    # @staticmethod
    def get_all_produtividades():
        db = Database()
        db.cursor.execute(f"""
            SELECT C.id_colaborador_pk, C.nome_colaborador, P.nota_avaliacao, P.comentario, G.nome_gestor, S.nome_setor, P.atingiu_meta, P.created_at FROM produtividade as P
                LEFT JOIN colaborador as C ON P.id_colaborador_fk = C.id_colaborador_pk
                LEFT JOIN setor as S ON C.id_setor_fk = S.id_setor_pk
                LEFT JOIN gestor as G ON P.id_gestor_fk = G.id_gestor_pk
            ORDER BY P.created_at ASC
        """)
        produtividades = db.cursor.fetchall()
        db.close_connection()
        return produtividades

    # Delete
    @staticmethod
    def delete_produtividade(id):
        db = Database()
        db.cursor.execute(f"""
            DELETE FROM produtividade WHERE id_produtividade_pk = '{id}';
        """)
        db.connection.commit()
        db.close_connection()
        return id