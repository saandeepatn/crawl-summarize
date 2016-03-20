__author__ = 'saandeepa'

import networkx as nx
import numpy as np
import SciPy

from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

def textrank(document):
    sentence_tokenizer = PunktSentenceTokenizer()
    sentences = sentence_tokenizer.tokenize(document)

    bow_matrix = CountVectorizer().fit_transform(sentences)
    normalized = TfidfTransformer().fit_transform(bow_matrix)

    similarity_graph = normalized * normalized.T

    nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
    scores = nx.pagerank(nx_graph)
    return sorted(((scores[i],s) for i,s in enumerate(sentences)),
                  reverse=True)

def main():
    document="""Established in 1963 with three engineering branches namely Civil, Mechanical and Electrical, today RVCE offers 12 Under Graduate Engineering programmes, 16 Master Degree programmes and Doctoral Studies.Located 13 km from the heart of Bangalore City – the Silicon Valley of India, on Mysore Road.Sprawling campus spread over an area of 52 acres set in sylvan surroundings.Provides an ideal ambience to stimulate the teaching-learning process, helping in bringing out skilled and disciplined Engineers. Rated one amongst the top ten self-financing Engineering Institutions in the country. Current annual student intake for Undergraduate Programmes & Post Graduate Programmes in Engineering is in excess of 1200. Highly qualified and dedicated faculty. Utilizes its expertise in various disciplines to conduct Research and Development for Industry and Defense establishments in the country."""
    textrank(document)
