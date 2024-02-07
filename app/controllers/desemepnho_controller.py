from models.desempenho_model import DesempenhoModel
import uuid
import pandas as pd

class DesempenhoController:
    def __init__(self):
        self.desempenho_model = DesempenhoModel

    def create_desempenho(self, id_colaborador, id_gestor, nota_avaliacao, comentario):
        id = uuid.uuid4().int & (1<<10)-1
        desempenho = self.desempenho_model(id, id_colaborador, id_gestor, nota_avaliacao, comentario)
        return desempenho.create_desempenho()
    
    def get_all_desempenhos():
        desempenhos = DesempenhoModel.get_all_desempenhos()
        desempenhos = pd.DataFrame(desempenhos, columns=['nome_colaborador', 'nota_avaliacao', 'comentario', 'nome_gestor', 'nome_setor', 'created_at'])
        desempenhos['created_at'] = pd.to_datetime(desempenhos['created_at']).dt.strftime('%d/%m/%Y')
        return desempenhos
    
    def delete_desempenho(self, id):
        return self.desempenho_model.delete_desempenho(id)
    
# Path: app/controllers/desempenho_controller.py

    