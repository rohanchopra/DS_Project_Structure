from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import roc_auc_score, accuracy_score
import logging as logger

from processing.train_test_split import tt_split
from utils.utils import save_object, plot_precision_recall_vs_threshold


def train(data, config):

    logger.info('Starting classification training.')

    X = data.copy()
    y = X.pop('target')

    X_train, X_val, y_train, y_val = tt_split(X, y)

    clf = RandomForestClassifier(n_estimators=100,
                                 max_depth=10,
                                 random_state=0,
                                 class_weight={0: 1, 1: 10})
    clf.fit(X_train, y_train)
    predicted = clf.predict(X_val)

    logger.info("Recall: {}".format(recall_score(y_val, predicted)))
    logger.info("Accuracy: {}".format(accuracy_score(y_val, predicted)))
    logger.info("Precision: {}".format(precision_score(y_val, predicted)))
    logger.info("AUC: {}".format(roc_auc_score(y_val, predicted)))

    predicted_prob = clf.predict_proba(X_val)[:, 1]

    p, r, thresholds = precision_recall_curve(y_val, predicted_prob)
    plot_precision_recall_vs_threshold(p, r, thresholds)

    filename = config.get('MODELS', 'PATH') + config.get('MODELS', 'NPTB')
    save_object(clf, filename)
    logger.info('Classification training complete. Model saved.')
