import funciones as func

print('En esta función se va a calcular la cantidad de calorías recomendadas que una personas debe consumir a diario, en caso de que desee adelgazar')
peso = float(input('Ingrese el peso de la persona (En Kilogramos): '))
altura = float(input('Ingrese la altura de la persona (En metros): '))
alturacm = altura * 100
edad = int(input('Ingrese la edad de la persona (en años): '))
valor_genero = float(input('Ingrese el valor 5 en caso de ser hombre y -161 en caso de ser mujer: '))
valor_actividad = float(input('Ingrese el valor de actividad de la persona: '))
# Funciones
imc = round(func.calcular_IMC(peso, altura),2)
porcentaje_grasa = round(func.calcular_porcentaje_grasa(peso, altura, edad, valor_genero), 2)
calorias_reposo = round(func.calcular_calorias_reposo(peso, alturacm, edad, valor_genero), 2)
calorias_actividad = round(func.calcular_calorias_en_actividad(peso, alturacm, edad, valor_genero, valor_actividad), 2)
consumo_recomendado = func.consumo_calorias_recomendado_para_adelgazar(peso, alturacm, edad, valor_genero)
print('-------------------------------------------------------------------------------------')
print(f'El valor del imc: {imc}')
print(f'El calculo del porcentaje de grasa es: {porcentaje_grasa} %')
print(f'El calculo de calorias en resposo es: {calorias_reposo} cal')
print(f'El calculo de calorias en actividad es: {calorias_actividad} cal')
print(consumo_recomendado)