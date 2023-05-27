from data.apartamentos import apartamento1,apartamento2
import pandas as pd
from helpers.crearTablasHTML import crearTabla

#1. Crear el DATAFRAME

tabla1 = pd.DataFrame(apartamento1,columns=['Edades'])
tabla2 = pd.DataFrame(apartamento2,columns=['Edades'])
tabla3 = pd.read_csv("./data/empleados.csv")

# print(tabla1)
# print(tabla2)

# estadisticasAPTO1 = tabla1.describe()
# estadisticasAPTO2 = tabla2.describe()
# estadisticasEMPLEADOS = tabla3.describe()

# print(estadisticasAPTO1)
# print("\n")
# print(estadisticasAPTO2)
# print("\n")
# print(estadisticasEMPLEADOS)

#Efectuando filtros con python

#1 Definir una condicion logica

filtro=tabla3.query('edad<28 and cargo=="analista1"')
empleadosSalarioBajo=tabla3.query('salario<5000000 and cargo=="analista2"')
empladoADespedir=tabla3.query('edad>=50')

#2 crearmos la tabla HTML con dataFrame

crearTabla(filtro,"tablaJovenes")
crearTabla(empleadosSalarioBajo,"tablaEmpleadosSalarioBajo")
crearTabla(empladoADespedir,"tablaOportunidadMejora")
