from models.feedback_model import FeedbackModel
import uuid
from datetime import datetime
import pandas as pd

class FeedbackController:
    def __init__(self):
        self.feedback_model = FeedbackModel

    def create_feedback(self, avaliador, avaliado, feedback, comentario):
        id = str(uuid.uuid4())
        create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        feedback = self.feedback_model(id, avaliador, avaliado, feedback, comentario, create_at)
        feedback_id = feedback.create_feedback()
        return feedback_id

    @staticmethod
    def get_all_feedbacks():
        feedbacks = FeedbackModel.get_all_feedbacks()
        df = pd.DataFrame(feedbacks, columns=['id', 'nome', 'gestor', 'feedback', 'comentario', 'alocacao', 'create_at'])
        return df
    
    @staticmethod
    def delete_feedback(id):
        feedback_id = FeedbackModel.delete_feedback(id)
        return feedback_id
