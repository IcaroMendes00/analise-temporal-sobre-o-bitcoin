import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import BTC_FUNC_GRAFICOS

# Função para plotar gráfico entre halvings com o intervalo selecionado
def plota_grafico_entre_halvings():
    # Obter o valor do menu suspenso para o intervalo selecionado
    intervalo = intervalo_var.get()
    if intervalo:
        BTC_FUNC_GRAFICOS.plota_grafico_entre_halvings(int(intervalo))
    else:
        messagebox.showerror("Erro", "Por favor, selecione um intervalo antes de plotar o gráfico.")

# Criação da interface gráfica
root = tk.Tk()
root.title("Seleção de Função")

# Criar um estilo para personalizar o OptionMenu
style = ttk.Style(root)
style.theme_use("default")

# Alterar a cor de fundo do menu e o texto das opções
style.configure(
    "TMenubutton",
    background="black",  # Fundo preto para o menu
    foreground="white",  # Texto branco para o menu
    borderwidth=0,       # Remover bordas
    font=("Arial", 10, "bold"),  # Fonte para o texto
)

# Variável para armazenar o valor do menu suspenso
intervalo_var = tk.StringVar(root)
intervalo_var.set("1")  # Valor padrão

# Criar um frame para agrupar o menu suspenso e o botão correspondente
frame_halving = tk.Frame(root)
frame_halving.pack(pady=10, anchor="w")

# Criar o menu suspenso para selecionar o intervalo com estilo personalizado
intervalo_menu = ttk.OptionMenu(
    frame_halving,
    intervalo_var,
    "1 - 1° halving -> 2° halving",
    "1 - 1° halving -> 2° halving",
    "2 - 2° halving -> 3° halving",
    "3 - 3° halving -> 4° halving",
)
intervalo_menu.pack(side="left", padx=10)

# Criar o botão para plotar o gráfico entre halvings
btn2 = ttk.Button(frame_halving, text="Gráfico Entre Halvings", command=plota_grafico_entre_halvings)
btn2.pack(side="left", padx=10)

# Criar botões para outras funções com estilo ttk para manter consistência
btn1 = ttk.Button(root, text="Gráfico Separado por Halving", command=BTC_FUNC_GRAFICOS.plotar_grafico_separado_halving)
btn1.pack(pady=10, anchor="w")

btn3 = ttk.Button(root, text="Gráfico de Intervalos Sobrepostos", command=BTC_FUNC_GRAFICOS.plotar_grafico_intervalos_sobrepostos)
btn3.pack(pady=10, anchor="w")

btn4 = ttk.Button(root, text="Gráfico Candlestick", command=BTC_FUNC_GRAFICOS.plota_grafico_candlestick)
btn4.pack(pady=10, anchor="w")

btn5 = ttk.Button(root, text="Gráfico Candlestick Mensal", command=BTC_FUNC_GRAFICOS.plotar_grafico_candlestick_det_mes)
btn5.pack(pady=10, anchor="w")

btn6 = ttk.Button(root, text="Gráfico Candlestick Diário", command=BTC_FUNC_GRAFICOS.plotar_grafico_candlestick_det_dia)
btn6.pack(pady=10, anchor="w")

btn7 = ttk.Button(root, text="Gerar Página HTML", command=BTC_FUNC_GRAFICOS.gerar_pagina_html)
btn7.pack(pady=10, anchor="w")

# Executar a interface gráfica
root.mainloop()
