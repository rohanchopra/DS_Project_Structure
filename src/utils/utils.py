import matplotlib
import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
import logging as logger
matplotlib.use('Agg')


def test_logger(text):
    logger.info(text)
    logger.warning(text)
    logger.error(text)


def save_object(obj, filename):
    file = open(filename, 'wb')
    pickle.dump(obj, file)


def read_object(filename):
    return pickle.load(open(filename, 'rb'))


def save_csv(obj, filename, save_index=False):
    obj.to_csv(filename, index=save_index)


def read_data(filename):
    # TODO: Implement read function
    pass


def plot_precision_recall_vs_threshold(precisions, recalls, thresholds):

    plt.figure(figsize=(8, 8))
    plt.title("Precision and Recall Scores as a function of the \
               Decision Threshold")
    plt.plot(thresholds, precisions[:-1], "b--", label="Precision")
    plt.plot(thresholds, recalls[:-1], "g--", label="Recall")
    plt.ylabel("Score")
    plt.xlabel("Decision Threshold")
    plt.legend(loc='best')
    plt.ylim([0, 1])
    return plt


def plot_roc_curve(y_val_splt, predicted_prob):

    fpr, tpr, thresholds = roc_curve(y_val_splt, predicted_prob)
    plt.plot(fpr, tpr)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.rcParams['font.size'] = 12
    plt.plot([0, 1], [0, 1], color='red',  linestyle='--')
    plt.title('ROC curve')
    plt.xlabel('False Positive Rate (1 - Specificity)')
    plt.ylabel('True Positive Rate (Sensitivity)')
    plt.grid(True)
    return plt
