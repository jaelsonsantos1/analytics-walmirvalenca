from models.produtividade_model import ProdutividadeModel
import uuid
import pandas as pd

class ProdutividadeController:
    def __init__(self):
        self.produtividade_model = ProdutividadeModel
    
    def create_produtividade(self, id_colaborador, id_gestor, nota_avaliacao, comentario, atingiu_meta):
        id = uuid.uuid4().int & (1<<20)-1
        self.produtividade_model(id, id_colaborador, id_gestor, nota_avaliacao, comentario, atingiu_meta).create_produtividade()
        return id
    
    def get_all_produtividades():
        produtividades = ProdutividadeModel.get_all_produtividades()
        produtividades = pd.DataFrame(produtividades, columns=['id', 'nome_colaborador', 'nota_avaliacao', 'comentario', 'nome_gestor', 'nome_setor', 'atingiu_meta', 'created_at'])
        produtividades['created_at'] = pd.to_datetime(produtividades['created_at']).dt.strftime('%d/%m/%Y')
        return produtividades

    def delete_produtividade(self, id):
        return self.produtividade_model.delete_produtividade(id)

# Path: app/controllers/produtividade_controller.py

    