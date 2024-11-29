# Simulado da Plataforma Gran - TSE Unificado - Programação de sistemas

def extrair_respostas(texto):
    lista_respostas=[]
    for palavra in texto:
        if palavra!="G" and palavra!="I":
            if palavra.isupper():
                lista_respostas.append(palavra)
    return lista_respostas

def extrair_meu_gabarito(texto):
    respostas = []
    texto.sort(key=lambda linha: int(linha.split("-")[0].strip()))
    for linha in texto:
        respostas.append(linha.split("-")[1])
    return respostas

with open("texto_gabarito_gran_nao_processado.txt", "r") as f:
    conteudo_gab = f.read()

with open("gabarito_simulado1TSE_nao_ordenado.txt","r") as f:
    conteudo_respostas = f.read().splitlines()

gabarito = extrair_respostas(conteudo_gab)

respostas = extrair_meu_gabarito(conteudo_respostas)

respostas = list(map(str.strip,respostas))

pontuacao = 0
qtd_acertos_basicos = 0
qtd_erros_basicos = 0
qtd_acertos_especificos = 0
qtd_erros_especificos = 0
questoes_erradas_basicos = []
questoes_erradas_especificos = []

for i in range(0,51):
    if respostas[i] == 'Branco':
        continue 
    if respostas[i] == gabarito[i]:
        pontuacao += 1  
        qtd_acertos_basicos +=1
    else:
        pontuacao -= 1  
        qtd_erros_basicos +=1
        questoes_erradas_basicos.append(i+1)

for i in range(51, 120):
   if respostas[i] == 'Branco':
       continue  
   if respostas[i] == gabarito[i]:
       pontuacao += 2  
       qtd_acertos_especificos+=1
   else:
       pontuacao -= 2 
       qtd_erros_especificos+=1
       questoes_erradas_especificos.append(i+1)

print(f"Acertos em conhecimentos básicos: {qtd_acertos_basicos}")
print(f"Erros em conhecimentos básicos: {qtd_erros_basicos}")
print(f"Acertos em conhecimentos específicos: {qtd_acertos_especificos}")
print(f"Erros em conhecimentos específicos: {qtd_erros_especificos}")
print(f"Questões incorretas de conhecimentos básicos {questoes_erradas_basicos}")
print(f"Questões incorretas de conhecimentos específicos {questoes_erradas_especificos}")
print(f"A pontuação total foi de {pontuacao}, \
o que corresponde a um aproveitamento de {(pontuacao/190)*100:.1f}%")



