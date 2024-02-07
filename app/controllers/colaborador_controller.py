from models.colaborador_model import ColaboradorModel
import pandas as pd
import uuid

class ColaboradorController:
    def __init__(self):
        self.colaborador_model = ColaboradorModel

    def create_colaborador(self, nome, idade, id_gestor, id_setor):
        # Gerar id de inteiros aleatórios que aceitam até 10 dígitos
        id = uuid.uuid4().int & (1<<10)-1
        colaborador = self.colaborador_model(id, nome, idade, id_gestor, id_setor)
        colaborador_id = colaborador.create_colaborador()
        return colaborador_id

    def get_all_colaboradores():
        colaboradores = ColaboradorModel.get_all_colaboradores()
        colaboradores_df = pd.DataFrame(colaboradores, columns=['id', 'nome', 'idade', 'id_gestor', 'gestor', 'id_setor', 'setor', 'created_at'])
        colaboradores_df['created_at'] = pd.to_datetime(colaboradores_df['created_at']).dt.strftime('%d/%m/%Y')
        return colaboradores_df

    def get_colaborador_by_id(id):
        colaborador = ColaboradorModel.get_colaborador_by_id(id)
        colaborador_df = pd.DataFrame([colaborador], columns=['id', 'nome', 'idade', 'id_gestor', 'gestor', 'id_setor', 'setor', 'create_at'])
        colaborador_df['create_at'] = pd.to_datetime(colaborador_df['create_at']).dt.strftime('%d/%m/%Y')
        return colaborador_df

    def get_all_gestores():
        gestores = ColaboradorModel.get_all_gestores()
        gestores_lista = [(gestor[0], gestor[1]) for gestor in gestores]
        return gestores_lista
    
    def get_all_setores():
        setores = ColaboradorModel.get_all_setores()
        setores_lista = [(setor[0], setor[1]) for setor in setores]
        return setores_lista

    def get_all_avaliacoes():
        avaliacoes = ColaboradorModel.get_all_avaliacoes()
        avaliacoes_lista = pd.DataFrame(avaliacoes, columns=['id', 'nome', 'gestor', 'setor', 'nota_produtividade', 'atingiu_meta', 'nota_engajamento'])
        return avaliacoes_lista

    def get_colaborador_by_setor(id_setor):
        colaboradores = ColaboradorModel.get_colaborador_by_setor(id_setor)
        colaboradores_df = pd.DataFrame(colaboradores, columns=['id', 'nome', 'idade', 'id_gestor', 'gestor', 'id_setor', 'setor', 'created_at'])
        colaboradores_df['created_at'] = pd.to_datetime(colaboradores_df['created_at']).dt.strftime('%d/%m/%Y')
        return colaboradores_df

    def update_colaborador(self, id, nome, idade, id_gestor, id_setor):
        colaborador = self.colaborador_model(id, nome, idade, id_gestor, id_setor)
        colaborador_id = colaborador.update_colaborador()
        return colaborador_id

    def delete_colaborador(id):
        colaborador_id = ColaboradorModel.delete_colaborador(id)
        return colaborador_id

# Path: app/controllers/feedback_controller.py