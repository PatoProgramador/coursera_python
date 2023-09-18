def calcular_IMC(peso, altura) :
  imc = peso / (altura**2)
  return imc

def calcular_porcentaje_grasa(peso, altura, edad, valor_genero) :
  gC = 1.2 * calcular_IMC(peso, altura) + 0.23 * edad - 5.4 - valor_genero
  return gC

def calcular_calorias_reposo(peso, altura, edad, valor_genero) :
  tMb = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
  return tMb

def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
  tMbAct = calcular_calorias_reposo(peso, altura, edad, valor_genero) * valor_actividad
  return tMbAct

def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
  valorMenor = (calcular_calorias_reposo(peso,altura, edad, valor_genero) * 80) / 100 
  valorMayor = (calcular_calorias_reposo(peso,altura, edad, valor_genero) * 85) / 100
  messag = 'Para adelgazar es recomendado que consumas entre: ' + str(round(valorMenor, 2)) + ' y ' + str(round(valorMayor,2)) + ' calorías al día.' 
  return messag
