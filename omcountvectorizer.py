# -*- coding: utf-8 -*-
"""omCountVectorizer

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X5DY-wKArVb1H-VzaGgeayxyQVDtKXOa
"""

class CountVectorizer():
  def __init__(self):
    self._unique_words = []
  '''
  класс, предназначенный для анализа текстов
  '''
  def fit_transform(self, data):
    '''
    метод, прнимающий список слов, разделённых пробелами
    и возвращающий терм-документную матрицу
    '''
    assert type(data) is list, 'Данные должны быть переданы списком!'
    all_words = []
    for row in data:
      assert type(row) is str, 'Предложения должны быть строками!'
      all_words += [word.lower() for word in row.split()]
    self._unique_words = list(set(all_words))
    n, m = len(data), len(self._unique_words)
    count_matrix = [[0] * m for _ in range(n)]
    for ind, row in enumerate(data):
      for word in row.split():
        word = word.lower()
        number = self._unique_words.index(word)
        count_matrix[ind][number] += 1
    return count_matrix

  def get_feature_names(self):
    '''
    метод, возвращающий список слов
    '''
    if self._unique_words:
      return self._unique_words
    else:
      print('сначала вызовите метод "fit_transform"')