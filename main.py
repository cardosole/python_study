#https://www.youtube.com/watch?v=GQpQha2Mfpg&list=PLpdAy0tYrnKznoeLzn06M-izJJpoEyzHC
# pandas - Integration python with excel
# openpyxl - Integration python with excel
# twilio - Integration python with sms
# ---------------------------------------------------
import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa714525d91f96dbb60ffd24e677d0479"
# Your Auth Token from twilio.com/console
auth_token  = "ca706d514da23a0d0066befa12e1f74f"
client = Client(account_sid, auth_token)

# Passo a passo de solução
# Abrir os 6 arquivos em Excel
## Dar nome para a lista de meses: VARIÁVEL. Toda lista no python fica em []
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
## Pra cada mês da lista_meses eu quero:
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 25000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 25000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 25000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5513991126977",
            from_="+19806002560",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

# Para cada arquivo:
# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
# Caso não seja maior do que 55.000 não quero fazer nada.
