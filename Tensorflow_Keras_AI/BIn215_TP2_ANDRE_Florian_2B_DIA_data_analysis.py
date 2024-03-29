#Florian ANDRE
#2B DIA
#BIn215 TP2 : Text Data Analysis

# Code 1 : import libraries
import pandas as pd
import os
import nltk #C'est la bibliotheque Natural Language Toolkit pour le Natural Language Processing
#nltk.download("all")
from nltk.sentiment.vader import SentimentIntensityAnalyzer #
from nltk.corpus import stopwords #Sert à lire les corpus et à retirer les mots n'apportant pas de valeur à l'analyse du texte
from nltk.tokenize import word_tokenize #Sert à diviser une phrase en plusieurs mots distincts
from nltk.stem import WordNetLemmatizer #Regroupe les mots ayant la même racine syntaxique


# Code 2 : Load the amazon review dataset
os.chdir("C:\\Users\\flori\\Documents") #Navigue vers le dossier où se trouve le fichier .csv
df = pd.read_csv('data.csv', sep=';')
print(df)
#Cette partie du programme renvoie les avis ainsi que leur numéro sous ce format "numéro (ordinal integer) avis (nominal string)"
#L'analyse permettrait d'afficher et classer les différents éléments du fichier .csv. Le numéro de l'avis est la variable indépendante dans le fichier

# Code 3 : create preprocess_text function (fonction exécutée par appel ou avec apply(preprocess_text))
def preprocess_text(text):
    tokens = word_tokenize(text.lower()) #Les jetons correspondent à la décomposition des mots dans la chaîne de caractère
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')] #Retire les mots ne figurant pas dans la langue anglaise
    lemmatizer = WordNetLemmatizer() #Renvoie le mot obtenu même s'il ne figure pas dans le WordNet
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    processed_text = ' '.join(lemmatized_tokens) #Concatene les mots existants et inexistants dans 1 chaine de caractères
    return processed_text #Renvoie le texte obtenu

# Code 4 : apply the function df
df['reviewText'] = df['reviewText'].apply(preprocess_text) #Applique aux phrases de la colonne 'reviewText' du fichier .csv la fonction preprocess_text()
print(df['reviewText']) #Renvoie le texte après prepprocess_text()

# Code 5 : initialize NLTK sentiment analyzer 
analyzer = SentimentIntensityAnalyzer() #Sert à analyser le sentiment de l'utilisateur en s'appuyant sur une banque de mots liée aux sentiments humains

# Code 6 : create get_sentiment function (fonction exécutée par appel ou avec apply.(get_sentiment)
def get_sentiment(text): 
    scores = analyzer.polarity_scores(text) 
    sentiment = 1 if scores['pos'] > 0 else 0 
    return sentiment #renvoie le sentiment en tant que premier mot

# Code 7 : apply get_sentiment function (applique la fonction get_sentiment au texte). Ne génère pas de nouvelles colonnes
df['sentiment'] = df['reviewText'].apply(get_sentiment)

# Code 8 :
from sklearn.metrics import confusion_matrix #Permet de déterminer a quel point un certain modèle peut être confus dans ses prédictions
print(confusion_matrix(df['Positive'], df['sentiment']))
#La matrice renvoyée est [4]

# Code 9 :
from sklearn.metrics import classification_report 
print(classification_report(df['Positive'], df['sentiment'])) 
#Rapport de classement : renvoie la précision, la moyenne simple, la moyenne pondérée
#Renvoie le rapport de classement sous forme d'un tableau

