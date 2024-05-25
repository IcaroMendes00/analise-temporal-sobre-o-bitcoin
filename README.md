# Analise do bitcoin com Python
Código desenvolvido com o objetivo de me ajudar a entender o comportamento e variações do bitcoin de acordo com o tempo, principalmente o ganho médio mês a mês e o ganho total no período selecionado.

Gráficos BTC - v1.0 19/04/2024 E.V. (Bloco:839927)
Arquivo com funções geradoras de gráficos do valor do bitcoin em relação ao Dólar (Dólar é mais estável que Real)
Autor: Icaro Mendes
Referências: https://github.com/hugoplm/bitcoin-candlestick/tree/main

# ATENÇÃO 

Antes de rodar qualquer função garanta que possui as bibliotecas necessárias. 
O arquivo bib_externas.txt te ajuda fazer isso. Para instalar as bibliotecas necessárias:

0 - Copie e cole o comando: 'pip install --upgrade pip setuptools' no seu terminal na pasta do projeto e pressione Enter

1 - Execute o arquivo install_bib.py da pasta instalador de bibliotecas e aguarde ele instalar todas as bibliotecas

2 - HODL!


# FUNÇÕES
        
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
    
    
# Melhorias futuras: 

1 - o yahoo finance só possui dados a partir de 01/01/2014, como inserir as informações anteriores no grafico? ou acessar um banco de dados melhor?

2 - implementar grade de calor de variação onde no eixo y temos os anos e no eixo x os meses

3 - integrar tudo em uma pagina web
