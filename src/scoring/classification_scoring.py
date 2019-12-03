import pandas as pd
from utils.utils import read_object, save_csv


def score(data, config, path, logging):

    logging.info('Starting Mobile NPTB scoring.')
    X = data.copy()
    ID = X.pop('ID')

    filename = path + config.get('MODELS', 'PATH')\
        + config.get('MODELS', 'CLASSIFICATION')
    model = read_object(filename)

    scores = model.predict(X)
    score_prob = model.predict_proba(X)

    score_df = pd.concat([ID,
                          pd.DataFrame(scores),
                          pd.DataFrame(score_prob[:, 1])
                          ], axis=1)
    score_df.columns = ['ID', 'Prediction', 'Probability']

    filename = path + config.get('DATA', 'PATH')\
        + config.get('DATA', 'CLASSIFICATION_SCORES')
    save_csv(score_df, filename)
    logging.info('Classification scoring done.')
