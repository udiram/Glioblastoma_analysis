from pyDeepInsight import ImageTransformer, LogScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
import math
import autokeras as ak
import keras as k
from sklearn.manifold import TSNE

X_trainCCLER = pd.read_csv('C:/Research/CCLEFullExpression/ccle_rnaseq_234568.csv', index_col=0)
X_trainCCLES = pd.read_csv('C:/Research/CCLEFullExpression/ccle_rnaseq_234568_structured.csv', index_col=0)
X_trainCCLEY = pd.read_csv('C:/Research/CCLEFullExpression/ccle_rnaseq_234568_SForY.csv', index_col=0)
X_trainAffy = pd.read_csv('C:/Research//CCLEFullExpression/ccle_affy_234568.csv', index_col=0)
X_trainAffRNAS = pd.read_csv('C:/Research/CCLEFullExpression/ccle_affyRNA_234568_structured.csv', index_col=0)
Y_trainAffRNA = pd.read_csv('C:/Research/CCLEFullExpression/ccle_affyRNA_234568_SForY.csv', index_col=0)

X_trainAffy.columns = X_trainAffy.columns.astype(float)
X_trainAffy.columns = X_trainAffy.columns.astype(int)
X_trainAffy.columns = X_trainAffy.columns.astype(str)

ln = LogScaler()
X_train = X_trainAffy.fillna(0)
X_train_norm = ln.fit_transform(X_train)

ln = LogScaler()
X_trainR = X_trainCCLER.fillna(0)
X_train_normR = ln.fit_transform(X_trainR)

X_train_norm[np.isnan(X_train_norm)] = 0
X_train_normR[np.isnan(X_train_normR)] = 0

tsne = TSNE(n_components=2, perplexity=100, learning_rate=1000,
            random_state=1701, n_jobs=-1)

it = ImageTransformer(feature_extractor=tsne,
                      pixels=150, random_state=7,
                      n_jobs=-1)


X_train_img = it.fit_transform(X_train_norm)
X_train_imgR = it.fit_transform(X_train_normR)
xcombined = np.concatenate((X_train_img, X_train_imgR), axis=0)
print(xcombined.shape)

# x training = xcombined  X structured = X_trianAffRNAS  y = Y_trainAffRNA