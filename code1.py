import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval
path="C:/Users/uwhub/PycharmProjects/movie recommendation"
credits_df = pd.read_csv(path + "/tmdb_5000_credits.csv")
movies_df = pd.read_csv(path + "/tmdb_5000_credits.csv")
movies_df.head()
credits_df.head()

credits_df.columns = ['id', 'title','cast','crew']
movies_df = movies_df.merge(credits_df, on=["title"])


movies_df.head()
