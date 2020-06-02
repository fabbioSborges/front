import streamlit as st
import pandas as pd
import numpy as np
from bokeh.plotting import figure
import matplotlib.pyplot as plt
#import plotly.figure_factory as ff


uploaded_file = st.sidebar.file_uploader("Choose a xlsx file", type="xlsx")
if uploaded_file is not None:
  df = pd.read_excel(uploaded_file, index_col=0)
  #st.write(data)

  #df = pd.read_excel('cev1.xlsx', index_col=0) 

  df = df.drop(columns=['Número de identificação', 'Sobrenome','Instituição', 'Departamento', 'Endereço de email', 'Último download realizado neste curso.'])
  #df['combined']=df.apply(lambda x:'%s_%s' % (x['Sobrenome'],x['Instituição']),axis=1)'''
  [lin, col] = df.shape

  st.title('Dashboard Quiz')
  st.write('Quantidade de Quizz na Disciplina: ', col)
  st.write('Número de Alunos ', lin)

  #x1 = np.random.randn(200) - 2
  #x2 = np.random.randn(200)
  #x3 = np.random.randn(200) + 2
  #hist_data = [x1, x2, x3]
  #group_labels = ['Group 1', 'Group 2', 'Group 3']
  #fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
  #st.plotly_chart(fig, use_container_width=True)

  st.header('Nota Quiz Arquitetura')
  st.write(df)

  #df1_transposed = df.T
  df1_transposed = df.reset_index()

  coluna = df.columns
  x = st.selectbox('Escolha o Quiz',coluna)  # 👈 this is a widget

  #st.line_chart(df[x])

  [lin, col] = df.shape
  index = np.arange(lin)
  plt.bar(index, df[x])
  plt.xlabel('Aluno', fontsize=5)
  plt.ylabel('Nota Quiz', fontsize=5)
  plt.xticks(index, df.index, fontsize=5, rotation=30)
  plt.title(x)

  st.pyplot()

  vetor = []
  for i in df.index:
    vetor = [vetor, i];


  options = st.multiselect('Escolha o Alunos', df1_transposed['Nome'])

  for i in options:
    plt.plot(np.arange(col), df.loc[i].T)
  plt.xlabel('QUIZ')
  plt.ylabel('NOTA')
  plt.legend(loc='best')
  st.pyplot()

