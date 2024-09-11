"""
Britez Tobias 

Ejercicio 8:
Genere un segundo módulo en el cual existan las funciones necesarias para la gestión del
equipo de recursos humanos de la empresa.
En el mismo debe existir una primera función que calcule el valor del salario de cada
empleado. El valor del mismo es la cantidad de horas trabajadas multiplicadas por 10 y un
incremento del 3% por cada año de antigüedad.
También debe haber una segunda función que calcule la productividad del empleado. La
misma se calcula como la cantidad de artefactos producidos, dividido por la cantidad de
horas de trabajo.
En tercer lugar debe haber una función que reporte toda la información del empleado
incluyendo la calculada en las dos funciones anteriores, nombre y edad.
"""

def calcular_salario(cantidad_horas_trabajadas:float, años_antiguedad:int) -> float:
    total_salario = cantidad_horas_trabajadas * 10 * (1 + (años_antiguedad * 3/100))
    return total_salario

def calcular_productividad_empleado(cantidad_artefactos_producidos:int, cantidad_horas_trabajadas: float) -> float:
    productividad_empleado = cantidad_artefactos_producidos / cantidad_horas_trabajadas
    return productividad_empleado 

def mostrar_informacion (nombre: str, edad:int, total_salario:float, productividad_empleado:float) -> None:

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Salario Total: ${total_salario}")
print(f"Productividad del empleo: {productividad_empleado} artefactos/hora")