import customtkinter as ctk
import random
import json
from tkinter import messagebox

# Função para carregar a lista de campeões e lanes a partir do arquivo 'champions.json'
def carregar_campeoes():
    try:
        with open("champions.json", "r") as file:
            champions = json.load(file)
        return champions
    except FileNotFoundError:
        return {"Campeão1": ["Top", "Mid"], "Campeão2": ["Jungle"], "Campeão3": ["Support"]}

# Carrega os campeões e as lanes permitidas
champions_data = carregar_campeoes()

# Classe para o aplicativo de sorteio
class SorteioApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sorteio de Lanes e Campeões para League of Legends")
        self.geometry("600x500")
        ctk.set_appearance_mode("dark")  # Opções: "light", "dark"
        ctk.set_default_color_theme("blue")  # Cores: "blue", "green", "dark-blue"
        self.init_ui()

    def init_ui(self):
        # Título principal
        title = ctk.CTkLabel(self, text="Sorteio de Campeões e Lanes", font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=15)

        # Frame para os campos de entrada
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(pady=10, padx=20, fill="x")

        # Campos de entrada para os jogadores
        self.inputs = []
        for i in range(5):
            label = ctk.CTkLabel(input_frame, text=f"Player {i + 1}:", font=ctk.CTkFont(size=12))
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            input_field = ctk.CTkEntry(input_frame, font=ctk.CTkFont(size=12))
            input_field.grid(row=i, column=1, padx=10, pady=5)
            self.inputs.append(input_field)

        # Frame para os botões, ajustado para alinhamento e tamanho
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=15)

        # Botão para Sortear
        sort_button = ctk.CTkButton(button_frame, text="Sortear", command=self.sortear, width=120)
        sort_button.grid(row=0, column=0, padx=5, pady=5)

        # Botão para Limpar Campos
        clear_button = ctk.CTkButton(button_frame, text="Limpar", command=self.limpar_campos, width=120)
        clear_button.grid(row=0, column=1, padx=5, pady=5)

        # Resultados
        result_frame = ctk.CTkFrame(self)
        result_frame.pack(pady=10, padx=20, fill="x")

        self.result_labels = [ctk.CTkLabel(result_frame, text="", font=ctk.CTkFont(size=12)) for _ in range(5)]
        for i, label in enumerate(self.result_labels):
            label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

    def sortear(self):
        if any(not input_field.get().strip() for input_field in self.inputs):
            messagebox.showwarning("Atenção", "Por favor, insira o nome de todos os jogadores.")
            return

        # Define as lanes e embaralha a ordem para cada sorteio
        lanes = ["Top", "Jungle", "Mid", "ADC", "Support"]
        random.shuffle(lanes)  # Embaralha as lanes para cada sorteio

        # Seleciona campeões aleatórios para as lanes
        selected_champions = []
        for lane in lanes:
            champions_for_lane = [champ for champ, champ_lanes in champions_data.items() if lane in champ_lanes]
            champion = random.choice(champions_for_lane) if champions_for_lane else "N/A"
            selected_champions.append(champion)

        # Exibe o resultado com as lanes e campeões embaralhados
        for i, lane in enumerate(lanes):
            player_name = self.inputs[i].get()
            champion_name = selected_champions[i]
            self.result_labels[i].configure(text=f"{lane}: {player_name} jogará de {champion_name}")

    def limpar_campos(self):
        for input_field in self.inputs:
            input_field.delete(0, ctk.END)
        for label in self.result_labels:
            label.configure(text="")

# Execução do aplicativo
if __name__ == "__main__":
    app = SorteioApp()
    app.mainloop()
