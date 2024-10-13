import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Datos
datos = [5434, 4948, 4521, 4570, 4990, 5702, 5241, 5112, 5015, 4659, 4806, 4637, 
         5670, 4381, 4820, 5043, 4886, 4599, 5288, 5299, 4848, 5378, 5260, 5055, 
         5828, 5218, 4859, 4780, 5027, 5008, 4609, 4772, 5133, 5095, 4618, 4848, 
         5089, 5518, 5333, 5164, 5342, 5069, 4755, 4925, 5001, 4803, 4951, 5679, 
         5256, 5207, 5621, 4918, 5138, 4786, 4500, 5461, 5049, 4974, 4592, 4173, 
         5296, 4965, 5170, 4740, 5173, 4568, 5653, 5078, 4900, 4968, 5248, 5245, 
         4723, 5275, 5419, 5205, 4452, 5227, 5555, 5388, 5498, 4681, 5076, 4774, 
         4931, 4493, 5309, 5582, 4308, 4823, 4417, 5364, 5640, 5069, 5188, 5764, 
         5273, 5042, 5189, 4986]

# Crear tabla de frecuencias
df = pd.DataFrame(datos, columns=['Datos'])
df['Frecuencia'] = pd.cut(df['Datos'], bins=10)
tabla_frecuencias = df['Frecuencia'].value_counts().reset_index().sort_values(by='index')

# Crear histograma
plt.hist(datos, bins=10, edgecolor='black', alpha=0.7)
plt.title('Histograma de Frecuencia Relativa')
plt.xlabel('Resistencia al esfuerzo cortante (lb)')
plt.ylabel('Frecuencia')
plt.show()

# Calcular MTC, MD y MP
media = np.mean(datos)
mediana = np.median(datos)

print(f'Media (MD): {media}')
print(f'Mediana (MP): {mediana}')
