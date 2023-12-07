from models.colaborador_model import ColaboradorModel
from datetime import datetime
import pandas as pd
import uuid

class ColaboradorController:
    def __init__(self):
        self.colaborador_model = ColaboradorModel

    def create_colaborador(self, nome, idade, gestor, alocacao):
        id = str(uuid.uuid4())
        create_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        colaborador = self.colaborador_model(id, nome, idade, gestor, alocacao, create_at)
        colaborador_id = colaborador.create_colaborador()
        return colaborador_id

    def get_all_colaboradores():
        colaboradores = ColaboradorModel.get_all_colaboradores()
        colaboradores_df = pd.DataFrame(colaboradores, columns=['id', 'nome', 'idade', 'gestor', 'alocacao', 'create_at'])
        return colaboradores_df

    def get_colaborador_by_id(id):
        colaborador = ColaboradorModel.get_colaborador_by_id(id)
        colaborador_df = pd.DataFrame([colaborador], columns=['id', 'nome', 'idade', 'gestor', 'alocacao', 'create_at'])
        return colaborador_df

    def update_colaborador(self, id, nome, idade, gestor, alocacao):
        create_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        colaborador = self.colaborador_model(id, nome, idade, gestor, alocacao, create_at)
        colaborador_id = colaborador.update_colaborador()
        return colaborador_id

    def delete_colaborador(id):
        colaborador_id = ColaboradorModel.delete_colaborador(id)
        return colaborador_id

