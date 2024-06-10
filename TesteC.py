import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess

# Função para calcular o MDC em Python usando o algoritmo de Euclides
def calcularMDC(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Função para executar o programa C com os argumentos fornecidos e retornar a saída
def run_program(executable, num1, num2):
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
        messagebox.showerror("Erro", "Por favor, selecione o arquivo executável.")
        return
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    expected_output = str(calcularMDC(num1, num2))
    output = run_program(executable_path, num1, num2)
    result = f"Números: {num1}, {num2} - "
    if expected_output in output:
        result += f"Passou - MDC: {expected_output}"
    else:
        result += f"Falhou - Saída esperada: {expected_output}, Saída recebida: {output}"
    result += "\n"
    results_text.insert(tk.END, result)
    mdc_result_label.config(text=f"MDC: {expected_output}")
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    entry_num1.focus_set()  # Coloca o foco de volta no campo do primeiro número

# Função para selecionar o arquivo executável
def select_executable():
    global executable_path
    executable_path = filedialog.askopenfilename(
        title="Selecione o arquivo executável",
        filetypes=[("Executáveis", "*.exe"), ("Todos os arquivos", "*.*")]
    )
    if executable_path:
        executable_label.config(text=f"Executável selecionado: {executable_path}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Teste de MDC")

executable_path = ""

# Botão para selecionar o arquivo executável
select_button = tk.Button(root, text="Selecionar Executável", command=select_executable)
select_button.pack(pady=10)

# Label para mostrar o caminho do executável selecionado
executable_label = tk.Label(root, text="Nenhum executável selecionado")
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

# Label para exibir o resultado do MDC
mdc_result_label = tk.Label(root, text="MDC: ")
mdc_result_label.pack(pady=10)

root.mainloop()
