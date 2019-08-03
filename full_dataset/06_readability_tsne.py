import pandas as pd 
from sklearn.manifold import TSNE

import plotly.offline as py
import plotly.graph_objs as go

if __name__ == '__main__':

    columns = ['FS_index', 'FH_read', 'GP_com', 'MM_read', 'CA_sch', 'source']

    nacion = pd.read_csv('./full_dataset/news_csv/nacion_unida_readability.csv')
    nacion = nacion[columns]

    heraldo = pd.read_csv('./full_dataset/news_csv/heraldo_readability.csv')
    heraldo = heraldo[columns]

    all_sources = pd.read_csv('./full_dataset/news_csv/all_sources_readability.csv')
    all_sources = all_sources[columns]

    data = pd.concat([nacion, heraldo, all_sources])

    X = data.drop(['source'], 1)
    y = data[['source']]
    
    X_array = X.values
    y_array = y.values

    tsne = TSNE(n_components=2, verbose=1, perplexity=1000, n_iter=500)

    tsne_results = tsne.fit_transform(X)

    df_tsne = data.copy()
    df_tsne['x-tsne'] = tsne_results[:,0]
    df_tsne['y-tsne'] = tsne_results[:,1]

    population = sorted(list(df_tsne['source'].unique()))

    print('\n------------ Visual -------------')
    
    data = []
    for p in population:

        space = df_tsne[df_tsne['source'] == p]

        x_tsne = space['x-tsne'].tolist()
        y_tsne = space['y-tsne'].tolist()

        trace = go.Scatter(
            x = x_tsne,
            y = y_tsne,
            mode = 'markers',
            name = p
        )

        data.append(trace)

    py.plot(data, filename='scatter-mode')