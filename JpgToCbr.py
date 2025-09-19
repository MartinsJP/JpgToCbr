import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import shutil
from pathlib import Path

class MangaCBRConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Conversor de Mangá para CBR")
        self.root.geometry("600x500")
        
        self.main_folder = None
        self.selected_volumes = []
        self.selected_chapters = []
        
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Seleção da pasta principal
        ttk.Label(main_frame, text="1. Selecione a pasta principal do mangá:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        folder_frame = ttk.Frame(main_frame)
        folder_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        
        self.folder_label = ttk.Label(folder_frame, text="Nenhuma pasta selecionada", relief="sunken", width=50)
        self.folder_label.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        
        ttk.Button(folder_frame, text="Procurar", command=self.select_main_folder).grid(row=0, column=1)
        
        # Seleção dos volumes
        ttk.Label(main_frame, text="2. Selecione os volumes:").grid(row=2, column=0, sticky=tk.W, pady=(20, 5))
        
        volumes_frame = ttk.Frame(main_frame)
        volumes_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=5)
        
        self.volumes_listbox = tk.Listbox(volumes_frame, selectmode=tk.MULTIPLE, height=6)
        volumes_scrollbar = ttk.Scrollbar(volumes_frame, orient="vertical", command=self.volumes_listbox.yview)
        self.volumes_listbox.configure(yscrollcommand=volumes_scrollbar.set)
        
        self.volumes_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        volumes_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        ttk.Button(volumes_frame, text="Atualizar Volumes", command=self.update_volumes).grid(row=1, column=0, pady=5)
        
        # Seleção dos capítulos
        ttk.Label(main_frame, text="3. Selecione os capítulos:").grid(row=4, column=0, sticky=tk.W, pady=(20, 5))
        
        chapters_frame = ttk.Frame(main_frame)
        chapters_frame.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=5)
        
        self.chapters_listbox = tk.Listbox(chapters_frame, selectmode=tk.MULTIPLE, height=6)
        chapters_scrollbar = ttk.Scrollbar(chapters_frame, orient="vertical", command=self.chapters_listbox.yview)
        self.chapters_listbox.configure(yscrollcommand=chapters_scrollbar.set)
        
        self.chapters_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        chapters_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        ttk.Button(chapters_frame, text="Atualizar Capítulos", command=self.update_chapters).grid(row=1, column=0, pady=5)
        
        # Botão de conversão
        ttk.Button(main_frame, text="Converter para CBR", command=self.convert_to_cbr, style="Accent.TButton").grid(row=6, column=0, pady=20)
        
        # Barra de progresso
        self.progress = ttk.Progressbar(main_frame, length=400, mode='determinate')
        self.progress.grid(row=7, column=0, sticky=(tk.W, tk.E), pady=5)
        
        # Status
        self.status_label = ttk.Label(main_frame, text="Aguardando seleção da pasta...")
        self.status_label.grid(row=8, column=0, pady=5)
        
        # Configurar redimensionamento
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        volumes_frame.columnconfigure(0, weight=1)
        chapters_frame.columnconfigure(0, weight=1)
        folder_frame.columnconfigure(0, weight=1)
    
    def select_main_folder(self):
        folder = filedialog.askdirectory(title="Selecione a pasta principal do mangá")
        if folder:
            self.main_folder = folder
            self.folder_label.config(text=os.path.basename(folder))
            self.status_label.config(text="Pasta selecionada. Clique em 'Atualizar Volumes'")
            self.volumes_listbox.delete(0, tk.END)
            self.chapters_listbox.delete(0, tk.END)
    
    def update_volumes(self):
        if not self.main_folder:
            messagebox.showwarning("Aviso", "Selecione primeiro a pasta principal!")
            return
        
        self.volumes_listbox.delete(0, tk.END)
        
        try:
            volumes = []
            for item in os.listdir(self.main_folder):
                item_path = os.path.join(self.main_folder, item)
                if os.path.isdir(item_path):
                    volumes.append(item)
            
            volumes.sort()
            for volume in volumes:
                self.volumes_listbox.insert(tk.END, volume)
            
            self.status_label.config(text=f"Encontrados {len(volumes)} volumes. Selecione os desejados.")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler volumes: {str(e)}")
    
    def update_chapters(self):
        if not self.main_folder:
            messagebox.showwarning("Aviso", "Selecione primeiro a pasta principal!")
            return
        
        selected_indices = self.volumes_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Aviso", "Selecione pelo menos um volume!")
            return
        
        self.chapters_listbox.delete(0, tk.END)
        
        try:
            all_chapters = []
            for index in selected_indices:
                volume_name = self.volumes_listbox.get(index)
                volume_path = os.path.join(self.main_folder, volume_name)
                
                for item in os.listdir(volume_path):
                    item_path = os.path.join(volume_path, item)
                    if os.path.isdir(item_path):
                        # Verifica se tem arquivos JPG na pasta
                        jpg_files = [f for f in os.listdir(item_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                        if jpg_files:
                            chapter_info = f"{volume_name}/{item}"
                            all_chapters.append(chapter_info)
            
            all_chapters.sort()
            for chapter in all_chapters:
                self.chapters_listbox.insert(tk.END, chapter)
            
            self.status_label.config(text=f"Encontrados {len(all_chapters)} capítulos com imagens. Selecione os desejados.")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler capítulos: {str(e)}")
    
    def check_rar_installation(self):
        """Verifica se o WinRAR está instalado"""
        possible_paths = [
            r"C:\Program Files\WinRAR\rar.exe",
            r"C:\Program Files (x86)\WinRAR\rar.exe",
            "rar"  # Se estiver no PATH
        ]
        
        for path in possible_paths:
            try:
                result = subprocess.run([path], capture_output=True, text=True, timeout=5)
                return path
            except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
                continue
        
        return None
    
    def create_cbr_from_folder(self, folder_path, output_path, rar_path):
        """Cria um arquivo CBR a partir de uma pasta com imagens"""
        try:
            # Lista todos os arquivos de imagem na pasta
            image_files = []
            for file in os.listdir(folder_path):
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')):
                    image_files.append(os.path.join(folder_path, file))
            
            if not image_files:
                return False, "Nenhuma imagem encontrada na pasta"
            
            # Ordena os arquivos numericamente
            image_files.sort(key=lambda x: self.natural_sort_key(os.path.basename(x)))
            
            # Cria o arquivo RAR temporário
            temp_rar = output_path.replace('.cbr', '.rar')
            
            # Comando para criar o RAR
            cmd = [rar_path, 'a', '-ep1', temp_rar] + image_files
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                # Renomeia para .cbr
                if os.path.exists(temp_rar):
                    shutil.move(temp_rar, output_path)
                    return True, "Sucesso"
                else:
                    return False, "Arquivo RAR não foi criado"
            else:
                return False, f"Erro no RAR: {result.stderr}"
                
        except Exception as e:
            return False, f"Erro: {str(e)}"
    
    def natural_sort_key(self, text):
        """Função para ordenação natural (1, 2, 10 ao invés de 1, 10, 2)"""
        import re
        return [int(s) if s.isdigit() else s.lower() for s in re.split(r'(\d+)', text)]
    
    def convert_to_cbr(self):
        if not self.main_folder:
            messagebox.showwarning("Aviso", "Selecione primeiro a pasta principal!")
            return
        
        selected_indices = self.chapters_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Aviso", "Selecione pelo menos um capítulo!")
            return
        
        # Verifica se o RAR está disponível
        rar_path = self.check_rar_installation()
        if not rar_path:
            messagebox.showerror("Erro", 
                "WinRAR não encontrado!\n\n"
                "Por favor, instale o WinRAR ou certifique-se de que o comando 'rar' "
                "esteja disponível no PATH do sistema.\n\n"
                "Você pode baixar o WinRAR em: https://www.win-rar.com/")
            return
        
        # Solicita pasta de destino
        output_folder = filedialog.askdirectory(title="Selecione a pasta onde salvar os arquivos CBR")
        if not output_folder:
            return
        
        # Configurar barra de progresso
        total_chapters = len(selected_indices)
        self.progress['maximum'] = total_chapters
        self.progress['value'] = 0
        
        success_count = 0
        error_list = []
        
        try:
            for i, index in enumerate(selected_indices):
                chapter_info = self.chapters_listbox.get(index)
                volume_name, chapter_name = chapter_info.split('/', 1)
                
                # Caminho da pasta do capítulo
                chapter_path = os.path.join(self.main_folder, volume_name, chapter_name)
                
                # Nome do arquivo CBR
                safe_filename = f"{volume_name}_{chapter_name}".replace('/', '_').replace('\\', '_')
                cbr_filename = f"{safe_filename}.cbr"
                cbr_path = os.path.join(output_folder, cbr_filename)
                
                # Atualizar status
                self.status_label.config(text=f"Convertendo: {chapter_info}")
                self.root.update()
                
                # Criar CBR
                success, message = self.create_cbr_from_folder(chapter_path, cbr_path, rar_path)
                
                if success:
                    success_count += 1
                else:
                    error_list.append(f"{chapter_info}: {message}")
                
                # Atualizar barra de progresso
                self.progress['value'] = i + 1
                self.root.update()
        
        except Exception as e:
            messagebox.showerror("Erro", f"Erro durante a conversão: {str(e)}")
            return
        
        # Mostrar resultados
        if error_list:
            error_msg = f"Conversão concluída!\n\nSucesso: {success_count}/{total_chapters}\n\nErros:\n" + "\n".join(error_list[:5])
            if len(error_list) > 5:
                error_msg += f"\n... e mais {len(error_list) - 5} erros."
            messagebox.showwarning("Conversão Concluída com Erros", error_msg)
        else:
            messagebox.showinfo("Sucesso", f"Todos os {success_count} capítulos foram convertidos com sucesso!")
        
        self.status_label.config(text="Conversão concluída!")
        self.progress['value'] = 0

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MangaCBRConverter()
    app.run()