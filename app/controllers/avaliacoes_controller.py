from models.avaliacoes_model import AvaliacaoModel
import pandas as pd


class AvaliacaoController:
    def create_avaliacao(self, id_colaborador, id_engajamento, id_produtividade):
        return AvaliacaoModel().create_avaliacao(id_colaborador, id_engajamento, id_produtividade)
    
    def avaliacoes(self):
        avaliacoes = AvaliacaoModel.avaliacoes()
        avaliacoes_df = pd.DataFrame(avaliacoes, columns=['Id Colaborador', 'Colaborador', 'Id engajamento', 'Engajamento', 'Comentário eng.', 'Id produtividade', 'Produtividade', 'Comentário prod.', 'Meta', 'Setor', 'Gestor'])
        return avaliacoes_df
