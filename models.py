import pickle
import pandas as pd

from easydict import EasyDict as edict

#Importa a classe de preparação de dados
from prepare_data import PegaBotTools

class BotProbability():
    def __init__(self):
        self.id = id
        self.total = 0
        self.friends = 0
        self.network = 0
        self.temporal = 0
        self.sentiment = 0

    def predict(self, users_data, timeline_data, path_input_model="pegabot-model-02.pbm"):
        
        #Carrega o modelo do disco
        loaded_model = pickle.load(open(path_input_model, 'rb'))

        #Prepara os dados do usuário para a aplicação do modelo
        tools = PegaBotTools()
        x_data = tools.prepare_data(users_data, timeline_data, apply = True)

        #Aplica o modelo para predição e retorna a predição {[0] Não é Bot, [1] é Bot}
        #predicted = loaded_model.predict(x_data)

        #Aplica o modelo para retorno dentro da faixa de [0, 1] para as classes [não bot | bot]
        predicted_proba = loaded_model.predict_proba(x_data)

        return predicted_proba

    def botProbability(self, handle, twitterTimeline, twitterUserData):
        #try:
        df_timeline = pd.DataFrame.from_dict(twitterTimeline)
        df_user_data = pd.DataFrame.from_dict(twitterUserData)

        df_timeline.to_csv("twitterTimeline", sep='\t')
        df_user_data.to_csv("twitterUserData", sep='\t')

        analise = self.predict(df_user_data, df_timeline)
        self.total = round(analise[0][1]*100, 2)
        #except:
        #    self.total = -1

        return edict({
            'pegabot_version': 'version-2.0',
            'handle': handle,
            'total': self.total
        })
