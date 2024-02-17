from data.db import Database

class AvaliacaoModel:
    def create_avaliacao(self, id_colaborador, id_engajamento, id_produtividade):
        db = Database()
        db.cursor.execute(f"""
            INSERT INTO avaliacoes (id_colaborador_fk, id_engajamento_fk, id_produtividade_fk)
            VALUES ('{id_colaborador}', '{id_engajamento}', '{id_produtividade}')
        """)
        db.connection.commit()
        db.close_connection()
    
    def avaliacoes():
        db = Database()
        db.cursor.execute(f"""
            SELECT * FROM avaliacoes_colaboradores;
        """)
        avaliacoes = db.cursor.fetchall()
        db.close_connection()
        return avaliacoes