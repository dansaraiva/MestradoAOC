import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os

# Função para calcular o MDC em Python usando o algoritmo de Euclides
def calcularMDC(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Função para compilar o programa C
def compile_program(c_file):
    executable = c_file.rsplit('.', 1)[0]
    compile_command = f"gcc {c_file} -o {executable}"
    compile_process = subprocess.run(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if compile_process.returncode != 0:
        raise Exception(f"Erro na compilação: {compile_process.stderr.decode()}")
    return executable

# Função para executar o programa compilado com os argumentos fornecidos e retornar a saída
def run_program(executable, num1, num2):
    if not os.path.isfile(executable):
        raise FileNotFoundError(f"Executable '{executable}' not found.")
    process = subprocess.Popen([executable], 
                                stdin=subprocess.PIPE, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE, 
                                universal_newlines=True)
    stdout, _ = process.communicate(f"{num1}\n{num2}\n")
    return stdout.strip()

# Função para executar os testes e exibir os resultados na interface gráfica
def run_test():
    if not executable_path:
        messagebox.showerror("Erro", "Por favor, selecione o arquivo .c.")
        return

    try:
        executable = compile_program(executable_path)
    except Exception as e:
        messagebox.showerror("Erro na compilação", str(e))
        return

    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
    except ValueError:
        messagebox.showerror("Erro de entrada", "Por favor, insira números inteiros válidos.")
        return

    expected_output = str(calcularMDC(num1, num2))
    try:
        output = run_program(executable, num1, num2)
    except Exception as e:
        messagebox.showerror("Erro na execução", str(e))
        return

    result = f"Números: {num1}, {num2} - "
    if expected_output in output:
        result += f"Passou - MDC: {expected_output}"
    else:
        result += f"Falhou - Saída esperada: {expected_output}, Saída recebida: {output}"
    result += "\n"
    results_text.insert(tk.END, result)
  
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    entry_num1.focus_set()  # Coloca o foco de volta no campo do primeiro número

# Função para selecionar o arquivo .c
def select_executable():
    global executable_path
    executable_path = filedialog.askopenfilename(
        title="Selecione o arquivo .c",
        filetypes=[("Arquivos C", "*.c"), ("Todos os arquivos", "*.*")]
    )
    if executable_path:
        executable_label.config(text=f"Arquivo .c selecionado: {executable_path}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Teste de MDC")

# Definindo o tamanho da janela
root.geometry("800x600")

# Carregar o ícone
icon_image = tk.PhotoImage(file="./univali.png")

# Configurar o ícone da janela
root.iconphoto(True, icon_image)

executable_path = ""

# Botão para selecionar o arquivo .c
select_button = tk.Button(root, text="Selecionar Arquivo .c", command=select_executable)
select_button.pack(pady=10)

# Label para mostrar o caminho do arquivo .c selecionado
executable_label = tk.Label(root, text="Nenhum arquivo .c selecionado")
executable_label.pack(pady=10)

# Entrada para o primeiro número
label_num1 = tk.Label(root, text="Digite o primeiro número:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

# Entrada para o segundo número
label_num2 = tk.Label(root, text="Digite o segundo número:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Botão para executar os testes
run_button = tk.Button(root, text="Executar Teste", command=run_test)
run_button.pack(pady=10)

# Área de resultados
results_text = tk.Text(root, height=10, width=50)
results_text.pack()

# Frame para o botão Fechar
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Botão Fechar
close_button = tk.Button(bottom_frame, text="Fechar", command=root.quit)
close_button.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()
