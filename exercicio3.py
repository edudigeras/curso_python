def verificar_idade(nome, idade):

  if idade >= 18:
    return f"{nome}! Você é maior de idade."
  else:
    return f"{nome}! Você é menor de idade."

nome = "ygor"
idade = 15
print(verificar_idade(nome, idade))