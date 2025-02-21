import json
import os
import tkinter as tk
from tkinter import messagebox

ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r") as arquivo:
            return json.load(arquivo)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def adicionar_tarefa():
    titulo = entrada_tarefa.get().strip()
    if titulo:
        tarefas = carregar_tarefas()
        tarefas.append({"titulo": titulo, "status": "Pendente"})
        salvar_tarefas(tarefas)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Digite um título para a tarefa.")

janela = tk.Tk()
janela.title("Gerenciador de Tarefas")

frame_topo = tk.Frame(janela)
frame_topo.pack(pady=10)

entrada_tarefa = tk.Entry(frame_topo, width=40)
entrada_tarefa.pack(side=tk.LEFT, padx=5)

botao_adicionar = tk.Button(frame_topo, text="Adicionar", command=adicionar_tarefa)
botao_adicionar.pack(side=tk.LEFT)

from gerenciador_arquivos import carregar_tarefas, salvar_tarefas

def adicionar_tarefa(titulo):
    """Adiciona uma nova tarefa."""
    if titulo.strip():
        tarefas = carregar_tarefas()
        tarefas.append({"titulo": titulo.strip(), "status": "Pendente"})
        salvar_tarefas(tarefas)
        return True
    return False

def marcar_como_concluida(indice, status):
    """Marca uma tarefa como concluída ou pendente."""
    tarefas = carregar_tarefas()
    tarefas[indice]["status"] = "Concluída" if status else "Pendente"
    salvar_tarefas(tarefas)

def excluir_concluidas():
    """Exclui todas as tarefas marcadas como concluídas."""
    tarefas = [tarefa for tarefa in carregar_tarefas() if tarefa["status"] != "Concluída"]
    salvar_tarefas(tarefas)

import tkinter as tk
from tkinter import messagebox
from tarefas import adicionar_tarefa, marcar_como_concluida, excluir_concluidas
from gerenciador_arquivos import carregar_tarefas

def atualizar_lista():
    """Atualiza a lista de tarefas exibida na interface."""
    for widget in frame_tarefas.winfo_children():
        widget.destroy()

    tarefas = carregar_tarefas()
    for idx, tarefa in enumerate(tarefas):
        var = tk.BooleanVar(value=tarefa["status"] == "Concluída")
        chk = tk.Checkbutton(frame_tarefas, text=tarefa['titulo'], variable=var, 
                             command=lambda i=idx, v=var: marcar_como_concluida(i, v.get()))
        chk.pack(anchor='w')

def adicionar_e_atualizar():
    """Adiciona uma tarefa e atualiza a interface."""
    if adicionar_tarefa(entrada_tarefa.get()):
        entrada_tarefa.delete(0, tk.END)
        atualizar_lista()
    else:
        messagebox.showwarning("Aviso", "Digite um título para a tarefa.")

def excluir_e_atualizar():
    """Exclui tarefas concluídas e atualiza a interface."""
    excluir_concluidas()
    atualizar_lista()

# Criando a janela principal
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")

frame_topo = tk.Frame(janela)
frame_topo.pack(pady=10)

entrada_tarefa = tk.Entry(frame_topo, width=40)
entrada_tarefa.pack(side=tk.LEFT, padx=5)

botao_adicionar = tk.Button(frame_topo, text="Adicionar", command=adicionar_e_atualizar)
botao_adicionar.pack(side=tk.LEFT)

frame_tarefas = tk.Frame(janela)
frame_tarefas.pack(pady=10)

botao_excluir = tk.Button(janela, text="Excluir Concluídas", command=excluir_e_atualizar)
botao_excluir.pack(pady=5)

atualizar_lista()
janela.mainloop()


janela.mainloop()
