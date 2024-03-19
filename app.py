import xmltodict
import os
import pandas as pd



def pegar_infos(nome_arquivo, valores):
    #print(f'Pegou as informações {nome_arquivo}')
    with open(f'nfs/{nome_arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        
        if 'NFe' in dic_arquivo:
            info_nf = dic_arquivo["NFe"]["infNFe"]
        else:
            info_nf = dic_arquivo["nfeProc"]["NFe"]["infNFe"]
        numero_nota = info_nf["@Id"]
        empresa_emissora = info_nf["emit"]["xNome"]
        nome_cliente = info_nf["dest"]["xNome"]
        endereco = info_nf["dest"]["enderDest"]
        if 'vol' in info_nf["transp"]:
            peso = info_nf["transp"]["vol"]["pesoB"]
        else:
            peso = "nao informado"
        valores.append([numero_nota,empresa_emissora,nome_cliente,endereco,peso])
       
colunas = ['numero_nota','empresa_emissora','nome_cliente','endereco','peso']
valores = []
lista_arquivos = os.listdir('nfs')

for arquivo in lista_arquivos:
    pegar_infos(arquivo,valores)

tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel('NotasFiscais.xlsx', index=False)

    
