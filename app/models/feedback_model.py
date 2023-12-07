from data.db import Database

class FeedbackModel:
    def __init__(self, id, avaliador, avaliado, feedback, comentario, create_at):
        self.id = id
        self.avaliador = avaliador
        self.avaliado = avaliado
        self.feedback = feedback
        self.comentario = comentario
        self.create_at = create_at

    def create_feedback(self):
        db = Database()
        db.cursor.execute(f"""
            INSERT INTO feedback (id, avaliador, avaliado, feedback, comentario, create_at)
            VALUES ('{self.id}', '{self.avaliador}', '{self.avaliado}', '{self.feedback}', '{self.comentario}', '{self.create_at}')
        """)
        db.connection.commit()
        db.close_connection()
        return self.id

    # @staticmethod
    def get_all_feedbacks():
        db = Database()
        db.cursor.execute(f"""
            SELECT F.id, C.nome, C.gestor, F.feedback, F.comentario, C.alocacao, F.create_at  FROM feedback AS F
            INNER JOIN colaborador AS C
            ON F.avaliado = C.nome;
        """)
        feedbacks = db.cursor.fetchall()
        db.close_connection()
        return feedbacks

    # Delete
    @staticmethod
    def delete_feedback(id):
        db = Database()
        db.cursor.execute(f"""
            DELETE FROM feedback WHERE id = '{id}';
        """)
        db.connection.commit()
        db.close_connection()
        return id
