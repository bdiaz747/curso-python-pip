# python app/charts.py
# matplotlib = 
# https://matplotlib.org/stable/plot_types/index.html

import matplotlib.pyplot as plt

def generater_bar_chart(name, labels,values):
  fig, ax = plt.subplots()
  ax.bar(labels, values) 
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generater_pie_chart(labels,values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.savefig('chart_pie_final.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a','b','c']
  values = [50, 100, 150]
  #generater_bar_chart(labels, values)
  #generater_pie_chart(labels, values)

