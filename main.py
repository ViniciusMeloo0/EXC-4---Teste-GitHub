import pandas as pd

def abrirArquivo(nomeArquivo):
  #lê a entrada
  return pd.DataFrame([linhas.strip().split() for linhas in open(nomeArquivo).readlines()])

def compararDataFrame(df1, df2):
  comp = df1.eq(df2)
  fat = []
  fibo = []
  for i in range(df1.shape[0]):
    if not comp.iloc[i].iat[1]:
     fat.append(i)

    if not comp.iloc[i].iat[2]:
     fibo.append(i)

  return fat,fibo

arq1 = abrirArquivo("arquivo-1.data")
arq2 = abrirArquivo("arquivo-2.data")
arqT = abrirArquivo("arquivo-teste.data")

print(">Primeira Comparação:")
fatorial1, fibonacci1 = compararDataFrame(arq1,arq2)
if fatorial1 == []:
  if fibonacci1 == []:
    print("Todos os valores estão certos")
  else:       
    print("Valor de Fibonacci está errado para a(s) linha(s):",fibonacci1)
    print("Valores de Fatorial estão certos") 
else:
  print("Valor de Fibonacci está errado para a(s) linha(s):",fatorial1)
  if fibonacci1 == []:
    print("Valores de Fibonacci estão certos")
  else:
    print("Valor de Fibonacci está errado para a(s) linha(s):",fibonacci1)
print()
print("Segunda Comparação:")
fatorial2, fibonacci2 = compararDataFrame(arq1,arqT)
if fatorial2 == []:
  if fibonacci2 == []:
    print("Todos os valores estão certos")
  else:       
    print("Valor de Fibonacci está errado para a(s) linha(s):",fibonacci2)
    print("Valores de Fatorial estão certos") 
else:
  print("Valor de Fibonacci está errado para a(s) linha(s):",fatorial2)
  if fibonacci2 == []:
    print("Valores de Fibonacci estão certos")
  else:
    print("Valor de Fibonacci está errado para a(s) linha(s):",fibonacci2)