import tkinter as tk
from tkinter import messagebox
import subprocess

def install_dependencies(requirements_file):
    with open(requirements_file, 'r') as file:
        dependencies = file.readlines()

    total_dependencies = len(dependencies)
    progress_label.config(text=f'0 / {total_dependencies} bibliotecas instaladas')

    for index, dependency in enumerate(dependencies, start=1):
        dependency = dependency.strip()
        progress_label.config(text=f'{index} / {total_dependencies} - Instalando {dependency}...')
        window.update()

        result = subprocess.run(['pip', 'install', dependency], capture_output=True)
        if result.returncode == 0:
            progress_label.config(text=f'{index} / {total_dependencies} - {dependency} instalado com sucesso!')
        else:
            progress_label.config(text=f'{index} / {total_dependencies} - Erro ao instalar {dependency}')
            messagebox.showerror('Erro', f'Erro ao instalar {dependency}:\n{result.stderr.decode("utf-8")}')

    messagebox.showinfo('Concluído', 'Processo de instalação concluído!')

if __name__ == '__main__':
    requirements_file = 'bib_externas.txt'

    window = tk.Tk()
    window.title('Instalador de Bibliotecas')

    progress_label = tk.Label(window, text='')
    progress_label.pack(padx=10, pady=10)

    install_dependencies(requirements_file)

    window.mainloop()
