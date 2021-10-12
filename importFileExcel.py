import pandas as pd
filePath = 'sampleData.xlsx'

# Importo e uso la prima colonna come indice del dataframe e la elimino
# successivamente
def importaFile(f):
  dati = pd.read_excel(f)
  dati.index = dati.iloc[:, 0].values
  dati = dati.drop(labels='Lotto',axis=1)
  return dati

df = importaFile(filePath)
