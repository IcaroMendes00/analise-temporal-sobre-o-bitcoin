"""

    Gráficos BTC - v1.0 19/04/2024 (Bloco:839927)
    Arquivo com funções geradoras de gráficos do valor do bitcoin em relação ao Dólar (Dólar é mais estável que Real)
    Autor: Icaro Mendes
    Referências: https://github.com/hugoplm/bitcoin-candlestick/tree/main

    *********************************************** ATENÇÃO ***********************************************
        Antes de rodar qualquer função garanta que possui as bibliotecas necessárias. 
        O arquivo bib_externas.txt te ajuda fazer isso. Para instalar as bibliotecas necessárias:
         0 - Copie e cole o comando: 'pip install --upgrade pip setuptools' no seu terminal na pasta do projeto e pressione Enter
         1 - Execute o arquivo install_bib.py da pasta instalador de bibliotecas e aguarde ele instalar todas as bibliotecas
         2 - HODL!
    *******************************************************************************************************

    *********************************************** FUNÇÕES ***********************************************
        plotar_grafico_separado_halving() - OK!
        plota_grafico_entre_halvings(intervalo) - Como o yfinance não possui dados até 01/01/2014 ele não plota nada até essa data
        plotar_grafico_intervalos_sobrepostos() - É preciso corrigir a informação até o segundo halving "linha verde" 
        plota_grafico_candlestick() - OK!
        calcular_variacao_percentual(df) - OK!
        plotar_grafico_candlestick_det_mes() - OK!
        plotar_grafico_candlestick_det_dia() - OK!
        calcular_ganhos_percentuais_halving(halving) - por enquanto tratei apenas dos perios a partir do segundo e terceiro halving, pois
            existem alguns problemas que ainda não tratei, o primeiro problema: o periodo inicial do bitcoin, não achei nenhum banco de dados 
            para isso, ou não procurei o suficiente? esse periodo em questão é 03/2009 até 31/12/2013. portanto analises sobre o periodo do 
            inicio até o 1° halving e do primeiro halving até o segundo halving e o segundo problema: tatar os intervalos de tem de acordo 
            com a data atual a partir do quarto halving
    *******************************************************************************************************
    
    Melhorias futuras: 1 - o yahoo finance só possui dados a partir de 01/01/2014, como inserir as informações anteriores no grafico? ou acessar um banco de dados melhor?
                       2 - implementar grade de calor de variação onde no eixo y temos os anos e no eixo x os meses
                       3 - integrar tudo em uma pagina web

"""

# bibliotecas
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
import plotly.offline as py
from datetime import datetime
import matplotlib.pyplot as plt
import webbrowser

# periodos de analise
DATA_INICIO = '2014-01-01' # o registro mais antido do bitcoin ans bases do yahoo finance
data_atual = datetime.now()
DATA_HOJE = data_atual.strftime('%Y-%m-%d')

# baixa os dados do yahoo finance para o BTC-USD
DF_BTC = yf.download('BTC-USD', start=DATA_INICIO, end=DATA_HOJE)

# DATAS HALVING
DATA_HALVING_4 = pd.to_datetime('2024-04-19')
DATA_HALVING_3 = pd.to_datetime('2020-05-11')
DATA_HALVING_2 = pd.to_datetime('2016-07-09')
DATA_HALVING_1 = pd.to_datetime('2012-11-28')

############################################################################################################################################
# plota grafico do valor do bitcoin separado por halving
def plotar_grafico_separado_halving():
    # intervalo entre 01/01/2014 e o segundo halving
    df_inicio_halving_2 = DF_BTC.loc['2014-01-01':DATA_HALVING_2]
    # intervalo entre o segundo e o terceiro halving
    df_halving_2_3 = DF_BTC.loc[DATA_HALVING_2:DATA_HALVING_3]
    # intervalo após o terceiro halving
    df_halving_3 = DF_BTC.loc[DATA_HALVING_3:]

    # plota o grafico
    plt.figure(figsize=(10, 6))
    plt.plot(df_halving_3.index, df_halving_3['Close'], label='Após o 3º halving', color='red')                  # vermelho
    plt.plot(df_halving_2_3.index, df_halving_2_3['Close'], label='Entre o 2º e o 3º halving', color='blue')     # azul
    plt.plot(df_inicio_halving_2.index, df_inicio_halving_2['Close'], label='Até o 2º halving', color='green')   # verde

    # adiciona marcacao dos halvings
    plt.axvline(x=DATA_HALVING_4, color='black', linestyle='--', label='4º Halving - 19/04/2024')
    plt.axvline(x=DATA_HALVING_3, color='black', linestyle='--', label='3º Halving - 11/05/2020')
    plt.axvline(x=DATA_HALVING_2, color='black', linestyle='--', label='2º Halving - 09/07/2016')
    plt.axvline(x=DATA_HALVING_1, color='black', linestyle='--', label='1º Halving - 28/11/2012')

    plt.title('Preço do bitcoin entre os halvings')
    plt.xlabel('Data')
    plt.ylabel('Preço do Bitcoin em USD')
    plt.legend()
    plt.grid(True)
    plt.show()

############################################################################################################################################
# plota os graficos de cada halving isolado
def plota_grafico_entre_halvings(intervalo):
    if intervalo == 0:
        inicio = datetime.strptime('2009-01-01', '%Y-%m-%d')
        fim = DATA_HALVING_1
    elif intervalo == 1:
        inicio = DATA_HALVING_1
        fim = DATA_HALVING_2    
    elif intervalo == 2:
        inicio = DATA_HALVING_2
        fim = DATA_HALVING_3
    elif intervalo == 3:
        inicio = DATA_HALVING_3
        fim = DATA_HALVING_4
    #elif intervalo == 4:
    #    inicio = DATA_HALVING_4
    #    fim = DATA_HOJE
    
    # intervalo desejado
    df_intervalo = DF_BTC.loc[inicio:fim]
    
    # plota o grafico
    plt.figure(figsize=(10, 6))
    plt.plot(df_intervalo['Close'], color='blue', label='Preço')

    # plota as marcacoes das datas do halving
    if intervalo == 0:
        plt.axvline(x=inicio, color='#c72626', linestyle='--', label='INICIO - 01/01/2009')
        plt.axvline(x=fim, color='#a13838', linestyle='--', label='Halving 1 - 28/11/2012')
    elif intervalo == 1:
        plt.axvline(x=inicio, color='#c72626', linestyle='--', label='Halving 1 - 28/11/2012')
        plt.axvline(x=fim, color='#a13838', linestyle='--', label='Halving 2 - 09/07/2016')
    elif intervalo == 2:
        plt.axvline(x=inicio, color='#c72626', linestyle='--', label='Halving 2 - 09/07/2016')
        plt.axvline(x=fim, color='#a13838', linestyle='--', label='Halving 3 - 11/05/2020')
    elif intervalo == 3:
        plt.axvline(x=inicio, color='#c72626', linestyle='--', label='Halving 3 - 11/05/2020')
        plt.axvline(x=fim, color='#a13838', linestyle='--', label=f'Halving 4 - 19/04/2024')
    #elif intervalo == 4:
    #    plt.axvline(x=inicio, color='#c72626', linestyle='--', label='Halving 4 - 19/04/2024')
    #    plt.axvline(x=fim, color='#a13838', linestyle='--', label=f'Data de hoje')

    plt.title(f'Preço do Bitcoin do Intervalo {intervalo}')
    plt.xlabel('Data')
    plt.ylabel('Preço em USD')
    plt.legend()
    plt.grid(True)
    plt.show()

############################################################################################################################################
# plota os graficos dos periodos entre halvings sobrepostos
def plotar_grafico_intervalos_sobrepostos():
    # intervalo entre o primeiro e o segundo halving
    df_halving_1_2 = DF_BTC.loc[DATA_HALVING_1:DATA_HALVING_2]
    # intervalo entre o segundo e o terceiro halving
    df_halving_2_3 = DF_BTC.loc[DATA_HALVING_2:DATA_HALVING_3]
    # intervalo do terceiro halving ate hoje
    df_halving_3_atual = DF_BTC.loc[DATA_HALVING_3:DATA_HOJE]

    # quantidade de dias apos o início do gráfico para cada intervalo
    dias_halving_1_2 = (df_halving_1_2.index - df_halving_1_2.index[0]).days +400 # yfinance so possui dados de 400 dias apos o primeiro halving
    dias_halving_2_3 = (df_halving_2_3.index - df_halving_2_3.index[0]).days
    dias_halving_3_atual = (df_halving_3_atual.index - df_halving_3_atual.index[0]).days

    #  grafico
    plt.figure(figsize=(10, 6))
    plt.plot(dias_halving_1_2, df_halving_1_2['Close'], label='Entre o 1º e o 2º halving', color='green')
    plt.plot(dias_halving_2_3, df_halving_2_3['Close'], label='Entre o 2º e o 3º halving', color='blue')       # vermelho
    plt.plot(dias_halving_3_atual, df_halving_3_atual['Close'], label='Do 3º halving até hoje', color='red')   # azul

    plt.title('Preço do bitcoin entre dos halvings')
    plt.xlabel('Dias após o halving anterior')
    plt.ylabel('Preço do Bitcoin em USD')
    plt.legend()
    plt.grid(True)
    plt.show()

############################################################################################################################################
# grafico de candlestick com ajustes disponiveis
def plota_grafico_candlestick():
    candlestick = go.Candlestick(x=DF_BTC.index,
                                open=DF_BTC['Open'],
                                high=DF_BTC['High'],
                                low=DF_BTC['Low'],
                                close=DF_BTC['Close'])

    # Calculando o intervalo total com base na data de início
    intervalo_total = (DF_BTC.index[-1] - DF_BTC.index[0]).days

    # botoes de intervalo de tempo
    rangeselector_buttons = [{'count': intervalo_total, 'label': 'Total', 'step': 'all'},
                            {'count': 2, 'label': 'Diário (ùltimos dois dias)', 'step': 'day', 'stepmode': 'backward'},
                            {'count': 7, 'label': 'Semanal', 'step': 'day', 'stepmode': 'backward'},
                            {'count': 1, 'label': 'Mensal', 'step': 'month', 'stepmode': 'backward'},
                            {'count': 3, 'label': 'Trimestral', 'step': 'month', 'stepmode': 'backward'},
                            {'count': 6, 'label': 'Semestral', 'step': 'month', 'stepmode': 'backward'},
                            {'count': 1, 'label': 'Anual', 'step': 'year', 'stepmode': 'backward'}]

    # layout do grafico com os seletores de intervalo de tempo
    layout = go.Layout(title='Gráfico do Bitcoin (Candlestick)',
                    xaxis={'rangeslider': {'visible': True},
                            'rangeselector': {'buttons': rangeselector_buttons}})

    # figura do grafico
    fig = go.Figure(data=[candlestick], layout=layout)

    # grafico
    py.iplot(fig, filename='bitcoin_candlestick')

    py.plot(fig, filename='bitcoin_candlestick.html', auto_open=True)

#############################################################################################################################################
def calcular_variacao_percentual(df):
    # Calcula variação percentual diária
    df['Variacao_Percentual_Diaria'] = (df['Close'] - df['Open']) / df['Open'] * 100
    
    # Calcula variação percentual mensal
    df_monthly = df.resample('ME').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'})
    df_monthly['Variacao_Percentual_Mensal'] = (df_monthly['Close'] - df_monthly['Open']) / df_monthly['Open'] * 100
    
    # Combina os resultados de volta ao DataFrame original
    df = pd.merge(df, df_monthly[['Variacao_Percentual_Mensal']], how='left', left_index=True, right_index=True)
    
    return df

#############################################################################################################################################
# candlesticks com detalhes - Mês
def plotar_grafico_candlestick_det_mes():
    df = calcular_variacao_percentual(DF_BTC)

    # intervalo mensal
    df_monthly = df.resample('M').agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'})

    # grafico para os dados mensais
    fig = go.Figure(data=[go.Candlestick(x=df_monthly.index,
                                         open=df_monthly['Open'],
                                         high=df_monthly['High'],
                                         low=df_monthly['Low'],
                                         close=df_monthly['Close'])])

    # ganhos percentuais mensais e totais
    ganho_percentual_mensal_medio = df['Variacao_Percentual_Mensal'].mean()
    ganho_percentual_diario_medio = df['Variacao_Percentual_Diaria'].mean()
    ganho_percentual_total = (df.iloc[-1]['Close'] - df.iloc[0]['Open']) / df.iloc[0]['Open'] * 100
    
    # titulo do gráfico
    titulo = "Gráfico do Bitcoin (Candlestick) Mês a mês\nGanho Diário Médio: {:.2f}%, Ganho Mensal Médio: {:.2f}%, Ganho Total: {:.2f}%".format(ganho_percentual_diario_medio, ganho_percentual_mensal_medio, ganho_percentual_total)
    fig.update_layout(title_text=titulo)

    # plota o grafico na janela
    py.plot(fig, filename='bitcoin_plot.html', auto_open=True)

############################################################################################################################################
# candlesticks com detalhes - Dia
def plotar_grafico_candlestick_det_dia():
    df = calcular_variacao_percentual(DF_BTC)

    # grafico para os dados diarios
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])

    # ganhos percentuais mensais e totais
    ganho_percentual_mensal_medio = df['Variacao_Percentual_Mensal'].mean()
    ganho_percentual_diario_medio = df['Variacao_Percentual_Diaria'].mean()
    ganho_percentual_total = (df.iloc[-1]['Close'] - df.iloc[0]['Open']) / df.iloc[0]['Open'] * 100

    # titulo do gráfico
    titulo = "Gráfico do Bitcoin (Candlestick) Mês a mês\nGanho Diário Médio: {:.2f}%, Ganho Mensal Médio: {:.2f}%, Ganho Total: {:.2f}%".format(ganho_percentual_diario_medio, ganho_percentual_mensal_medio, ganho_percentual_total)
    fig.update_layout(title_text=titulo)

    # grafico na janela
    py.plot(fig, filename='bitcoin_plot.html', auto_open=True)

##############################################################################################################################################
# gera informações percentuais sobre cada periodo de halving**
def calcular_ganhos_percentuais_halving(halving):
    # por enquanto tratei apenas dos periodos a partir do segundo e terceiro halving
    if halving != 2 and halving != 3:
        return "Halving deve ser 2 ou 3."
    
    if halving == 2:
        data_halving = DATA_HALVING_2
    else:
        data_halving = DATA_HALVING_3

    resultados = {}

    # periodos de analise em dias
    #          dois meses, tres meses, seis meses, um ano, dois anos, tres anos
    periodos = [60,        90,         180,        365,    730,       1095]  

    # ganhos percentuais para cada periodo
    for periodo in periodos:
        # dados do periodo apos o halving
        data_inicio = data_halving + pd.DateOffset(days=1)
        data_fim = data_inicio + pd.DateOffset(days=periodo)
        df_periodo = DF_BTC.loc[data_inicio:data_fim]

        # ganhos percentuais mensais
        ganhos_mensais = ((df_periodo['Close'] - df_periodo['Open']) / df_periodo['Open']) * 100
        ganho_percentual_mensal_medio = ganhos_mensais.mean()

        # ganhos percentuais diarios
        ganho_percentual_diario_medio = ((df_periodo['Close'].iloc[-1] - df_periodo['Open'].iloc[0]) / df_periodo['Open'].iloc[0]) * (100 / periodo)  # Média diária

        # ganho percentual em relacao ao valor inicial apos o halving (ganho pos halving)
        ganho_percentual_valor_inicial = ((df_periodo['Close'].iloc[-1] - df_periodo['Open'].iloc[0]) / df_periodo['Open'].iloc[0]) * 100

        # adiciona resultados ao dicionário
        resultados[f'{periodo} Dias após o halving'] = {
            'Ganho Percentual Diário Médio': ganho_percentual_diario_medio,
            'Ganho Percentual Mensal Médio': ganho_percentual_mensal_medio,
            'Ganho Percentual em Relação ao Valor Inicial': ganho_percentual_valor_inicial
        }

    return resultados

#####################################################################################################################################################
# gera a pagina html para mostrar os resultados percentuais do halving
def gerar_pagina_html():
    # abre arquivo HTML
    with open("ganhos_percentuais_halving.html", "w") as file:
        # cabecalho HTML
        file.write("<html>\n<head>\n<title>Ganhos Percentuais após Halving</title>\n</head>\n<body>\n")

        # halvings
        for halving in [2, 3]:
            resultados = calcular_ganhos_percentuais_halving(halving)

            # ititulo do halving
            file.write(f"<h2>Halving {halving}</h2>\n")

            # resultados
            for periodo, info in resultados.items():
                file.write("<p>\n")
                file.write(f"<strong>Periodo {periodo}:</strong><br>\n")
                file.write(f"Ganho percentual em relação ao valor inicial após o halving: {info['Ganho Percentual em Relação ao Valor Inicial']:.2f}%<br>\n")
                file.write(f"Ganho percentual mensal médio: {info['Ganho Percentual Mensal Médio']:.2f}%<br>\n")
                file.write(f"Ganho percentual diário médio: {info['Ganho Percentual Diário Médio']:.2f}%<br>\n")
                file.write("</p>\n")

        # fecha arquivo HTML
        file.write("</body>\n</html>")

    # abre o arquivo HTML automaticamente no navegador padrao
    webbrowser.open_new_tab("ganhos_percentuais_halving.html")