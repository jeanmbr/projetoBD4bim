import customtkinter as ctk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

import database as db

def upload_image(file_name, size=(300, 400)):
    try:
        dir_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(dir_base, "assets", "images", file_name)
        
        if not os.path.exists(image_path):
            print(f"❌ Arquivo não encontrado: {image_path}")
            return None
            
        image = Image.open(image_path)
        
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        
        data = image.getdata()
        new_data = []
        
        for item in data:
            if item[0] > 200 and item[1] > 200 and item[2] > 200: 
                new_data.append((255, 255, 255, 0)) 
            else:
                new_data.append(item)
        
        image.putdata(new_data)
        image = image.resize(size, Image.Resampling.LANCZOS)
        
        return ctk.CTkImage(light_image=image, dark_image=image, size=size)
        
    except Exception as e:
        print(f"❌ Erro ao carregar imagem {file_name}: {e}")
        return None

def main_window():
    window = ctk.CTk()
    window.title("Ranking de Bruxas e Magos")
    
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        icon_path = os.path.join(project_root, "assets", "images", "patolino.ico")
        
        print(f"Tentando carregar: {icon_path}")
        print(f"Arquivo existe: {os.path.exists(icon_path)}")
        
        if os.path.exists(icon_path):
            window.iconbitmap(icon_path)
            print("Ícone patolino.ico carregado com sucesso!")
        else:
            print("Arquivo não encontrado!")       
    except Exception as e:
        print(f"Erro ao carregar ícone: {e}")
    
    window.state('zoomed')
    
    main_frame = ctk.CTkFrame(window, fg_color="#2b2b2b")
    main_frame.pack(fill="both", expand=True, padx=40, pady=40)
    
    central_container = ctk.CTkFrame(main_frame, fg_color="transparent")
    central_container.pack(expand=True, fill="both")
    
    central_container.grid_columnconfigure(0, weight=1)  
    central_container.grid_columnconfigure(1, weight=2)  
    central_container.grid_columnconfigure(2, weight=1)  
    central_container.grid_rowconfigure(0, weight=1)
    central_container.grid_rowconfigure(1, weight=1)
    central_container.grid_rowconfigure(2, weight=3)
    
    title = ctk.CTkLabel(
        central_container, 
        text="✨ RANKING DE BRUXAS E MAGOS ✨", 
        font=("Arial", 32, "bold"),
        text_color="#f0f0f0"
    )
    title.grid(row=1, column=0, columnspan=3, pady=40)
    
    left_frame = ctk.CTkFrame(central_container, fg_color="transparent")
    left_frame.grid(row=2, column=0, sticky="nsew", padx=0, pady=10)
    
    mage_picture = upload_image("witch.png")
    if mage_picture:
        mage_label = ctk.CTkLabel(left_frame, image=mage_picture, text="")
        mage_label.pack(expand=True)
    else:
        mage_placeholder = ctk.CTkLabel(
            left_frame, 
            text="🧙‍♂️\nMAGO", 
            font=("Arial", 24, "bold"), 
            text_color="#4CAF50"
        )
        mage_placeholder.pack(expand=True)
    
    buttons_frame = ctk.CTkFrame(central_container, fg_color="#3b3b3b")
    buttons_frame.grid(row=2, column=1, sticky="nsew", padx=100, pady=50)
    
    button_config = {
        "height": 60,
        "font": ("Arial", 18, "bold"),
        "corner_radius": 15
    }
    
    btn_ranking = ctk.CTkButton(
        buttons_frame,
        text="📊 VER RANKING COMPLETO",
        fg_color="#4CAF50",
        hover_color="#45a049",
        command=open_ranking,
        **button_config
    )
    btn_ranking.pack(pady=20, fill="x", padx=100)
    
    btn_insert = ctk.CTkButton(
        buttons_frame,
        text="➕ INSERIR NOVO USUÁRIO",
        fg_color="#2196F3",
        hover_color="#1976D2",
        command=open_insert_window,
        **button_config
    )
    btn_insert.pack(pady=20, fill="x", padx=100)
    
    btn_update = ctk.CTkButton(
        buttons_frame,
        text="✏️ ALTERAR DADOS DO USUÁRIO",
        fg_color="#FF9800",
        hover_color="#F57C00",
        command=open_update_window,
        **button_config
    )
    btn_update.pack(pady=20, fill="x", padx=100)
    
    btn_delete = ctk.CTkButton(
        buttons_frame,
        text="🗑️ EXCLUIR USUÁRIO",
        fg_color="#F44336",
        hover_color="#D32F2F",
        command=open_delete_window,
        **button_config
    )
    btn_delete.pack(pady=20, fill="x", padx=100)
    
    btn_exit = ctk.CTkButton(
        buttons_frame,
        text="🚪 SAIR",
        fg_color="#757575",
        hover_color="#616161",
        command=window.quit,
        **button_config
    )
    btn_exit.pack(pady=20, fill="x", padx=100)
    
    right_frame = ctk.CTkFrame(central_container, fg_color="transparent")
    right_frame.grid(row=2, column=2, sticky="nsew", padx=0)
    
    witch_picture = upload_image("mage.png")
    if witch_picture:
        witch_label = ctk.CTkLabel(right_frame, image=witch_picture, text="")
        witch_label.pack(expand=True)
    else:
        witch_placeholder = ctk.CTkLabel(
            right_frame, 
            text="🧙‍♀️\nBRUXA", 
            font=("Arial", 24, "bold"), 
            text_color="#E91E63"
        )
        witch_placeholder.pack(expand=True)
    
    return window

def validate_fields(*fields):
    for field in fields:
        if not field.get().strip():
            return False
    return True

def validate_user(username):
    return len(username.strip()) >= 3

def open_ranking():
    ranking_window = ctk.CTkToplevel()
    ranking_window.title("Ranking Completo")
    ranking_window.geometry("600x400")
    ranking_window.grab_set()
    
    frame = ctk.CTkFrame(ranking_window)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    title = ctk.CTkLabel(frame, text="RANKING DE BRUXAS E MAGOS", font=("Arial", 18, "bold"))
    title.pack(pady=10)
    
    tree = ttk.Treeview(frame, columns=("Posição", "Usuário", "Pontos"), show="headings", height=15)
    tree.heading("Posição", text="Posição")
    tree.heading("Usuário", text="Usuário")
    tree.heading("Pontos", text="Pontos")
    tree.column("Posição", width=80)
    tree.column("Usuário", width=200)
    tree.column("Pontos", width=100)
    
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    success, data = db.get_ranking()
    if success:
        for i, user in enumerate(data, 1):
            if isinstance(user, dict):
                username = user.get("username", "N/A")
                points = user.get("points", 0)
                tree.insert("", "end", values=(i, username, points))
    else:
        error_message = str(data)
        messagebox.showerror("Erro", error_message)

def open_insert_window():
    window = ctk.CTkToplevel()
    window.title("Inserir Novo Usuário")
    window.geometry("400x350")
    window.grab_set()
    
    frame = ctk.CTkFrame(window)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    title = ctk.CTkLabel(frame, text="CADASTRAR NOVO USUÁRIO", font=("Arial", 16, "bold"))
    title.pack(pady=15)
    
    ctk.CTkLabel(frame, text="Nome de usuário:").pack(pady=8)
    entry_user = ctk.CTkEntry(frame, width=250)
    entry_user.pack(pady=8)
    
    ctk.CTkLabel(frame, text="Senha:").pack(pady=8)
    entry_password = ctk.CTkEntry(frame, width=250, show="*")
    entry_password.pack(pady=8)
    
    ctk.CTkLabel(frame, text="Pontos:").pack(pady=8)
    entry_points = ctk.CTkEntry(frame, width=250)
    entry_points.pack(pady=8)
    
    def register():
        username = entry_user.get()
        password = entry_password.get()
        points = entry_points.get()
        
        if not validate_fields(entry_user, entry_password, entry_points):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return
        
        if not validate_user(username):
            messagebox.showerror("Erro", "Nome de usuário deve ter pelo menos 3 caracteres!")
            return
        
        try:
            points_int = int(points)
        except ValueError:
            messagebox.showerror("Erro", "Pontos devem ser um número inteiro!")
            return
        
        success, message = db.insert_user(username, password, points_int)
        if success:
            messagebox.showinfo("Sucesso", message)
            window.destroy()
        else:
            messagebox.showerror("Erro", message)
    
    btns_frame = ctk.CTkFrame(frame, fg_color="transparent")
    btns_frame.pack(pady=20)
    
    btn_register = ctk.CTkButton(
        btns_frame,
        text="✅ CADASTRAR",
        font=("Arial", 14, "bold"),
        fg_color="#4CAF50",
        hover_color="#45a049",
        width=150,
        height=40,
        command=register
    )
    btn_register.pack(side="left", padx=10)
    
    btn_cancel = ctk.CTkButton(
        btns_frame,
        text="❌ CANCELAR",
        font=("Arial", 14, "bold"),
        fg_color="#757575",
        hover_color="#616161",
        width=150,
        height=40,
        command=window.destroy
    )
    btn_cancel.pack(side="left", padx=10)

def open_update_window():
    window = ctk.CTkToplevel()
    window.title("Alterar Dados do Usuário")
    window.geometry("400x250")
    window.grab_set()
    
    frame = ctk.CTkFrame(window)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    title = ctk.CTkLabel(frame, text="O QUE DESEJA ALTERAR?", font=("Arial", 16, "bold"))
    title.pack(pady=15)
    
    def open_update_user():
        update_user_window = ctk.CTkToplevel()
        update_user_window.title("Alterar Nome de Usuário")
        update_user_window.geometry("400x350")
        update_user_window.grab_set()
        
        frame_alt = ctk.CTkFrame(update_user_window)
        frame_alt.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(frame_alt, text="Usuário atual:").pack(pady=8)
        entry_old_user = ctk.CTkEntry(frame_alt, width=250)
        entry_old_user.pack(pady=8)
        
        ctk.CTkLabel(frame_alt, text="Novo nome de usuário:").pack(pady=8)
        entry_new_user = ctk.CTkEntry(frame_alt, width=250)
        entry_new_user.pack(pady=8)
        
        ctk.CTkLabel(frame_alt, text="Senha:").pack(pady=8)
        entry_password = ctk.CTkEntry(frame_alt, width=250, show="*")
        entry_password.pack(pady=8)
        
        def confirm_update():
            old_username = entry_old_user.get()
            new_username = entry_new_user.get()
            password = entry_password.get()
            
            if not validate_fields(entry_old_user, entry_new_user, entry_password):
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
                return
            
            if not validate_user(new_username):
                messagebox.showerror("Erro", "Novo nome de usuário deve ter pelo menos 3 caracteres!")
                return
            
            if not db.exist_user(old_username):
                messagebox.showerror("Erro", "Usuário não encontrado!")
                return
            
            success, message = db.update_user(old_username, new_username, password)
            if success:
                messagebox.showinfo("Sucesso", message)
                update_user_window.destroy()
                window.destroy()
            else:
                messagebox.showerror("Erro", message)
        
        btns_frame = ctk.CTkFrame(frame_alt, fg_color="transparent")
        btns_frame.pack(pady=20)
        
        btn_confirm = ctk.CTkButton(
            btns_frame,
            text="✅ CONFIRMAR",
            fg_color="#4CAF50",
            hover_color="#45a049",
            width=120,
            command=confirm_update
        )
        btn_confirm.pack(side="left", padx=10)
        
        btn_cancel = ctk.CTkButton(
            btns_frame,
            text="❌ CANCELAR",
            fg_color="#757575",
            hover_color="#616161",
            width=120,
            command=update_user_window.destroy
        )
        btn_cancel.pack(side="left", padx=10)
    
    def open_update_password():
        update_password_window = ctk.CTkToplevel()
        update_password_window.title("Alterar Senha")
        update_password_window.geometry("400x300")
        update_password_window.grab_set()
        
        frame_alt = ctk.CTkFrame(update_password_window)
        frame_alt.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(frame_alt, text="Nome de usuário:").pack(pady=8)
        entry_user = ctk.CTkEntry(frame_alt, width=250)
        entry_user.pack(pady=8)
        
        ctk.CTkLabel(frame_alt, text="Senha antiga:").pack(pady=8)
        entry_old_password = ctk.CTkEntry(frame_alt, width=250, show="*")
        entry_old_password.pack(pady=8)
        
        ctk.CTkLabel(frame_alt, text="Nova senha:").pack(pady=8)
        entry_new_password = ctk.CTkEntry(frame_alt, width=250, show="*")
        entry_new_password.pack(pady=8)
        
        def confirm_update():
            username = entry_user.get()
            old_password = entry_old_password.get()
            new_password = entry_new_password.get()
            
            if not validate_fields(entry_user, entry_old_password, entry_new_password):
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
                return
            
            if not db.exist_user(username):
                messagebox.showerror("Erro", "Usuário não encontrado!")
                return
            
            success, message = db.update_password(username, old_password, new_password)
            if success:
                messagebox.showinfo("Sucesso", message)
                update_password_window.destroy()
                window.destroy()
            else:
                messagebox.showerror("Erro", message)
        
        btns_frame = ctk.CTkFrame(frame_alt, fg_color="transparent")
        btns_frame.pack(pady=20)
        
        btn_confirm = ctk.CTkButton(
            btns_frame,
            text="✅ CONFIRMAR",
            fg_color="#4CAF50",
            hover_color="#45a049",
            width=120,
            command=confirm_update
        )
        btn_confirm.pack(side="left", padx=10)
        
        btn_cancel = ctk.CTkButton(
            btns_frame,
            text="❌ CANCELAR",
            fg_color="#757575",
            hover_color="#616161",
            width=120,
            command=update_password_window.destroy
        )
        btn_cancel.pack(side="left", padx=10)
    
    def open_update_points():
        update_points_window = ctk.CTkToplevel()
        update_points_window.title("Alterar Pontos")
        update_points_window.geometry("400x300")
        update_points_window.grab_set()
        
        frame_alt = ctk.CTkFrame(update_points_window)
        frame_alt.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(frame_alt, text="Nome de usuário:").pack(pady=8)
        entry_user = ctk.CTkEntry(frame_alt, width=250)
        entry_user.pack(pady=8)
        
        ctk.CTkLabel(frame_alt, text="Senha:").pack(pady=8)
        entry_password = ctk.CTkEntry(frame_alt, width=250, show="*")
        entry_password.pack(pady=8)
        
        ctk.CTkLabel(frame_alt, text="Novos pontos:").pack(pady=8)
        entry_points = ctk.CTkEntry(frame_alt, width=250)
        entry_points.pack(pady=8)
        
        def confirm_update():
            username = entry_user.get()
            password = entry_password.get()
            points = entry_points.get()
            
            if not validate_fields(entry_user, entry_password, entry_points):
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
                return
            
            if not db.exist_user(username):
                messagebox.showerror("Erro", "Usuário não encontrado!")
                return
            
            try:
                points_int = int(points)
            except ValueError:
                messagebox.showerror("Erro", "Pontos devem ser um número inteiro!")
                return
            
            success, message = db.update_points(username, password, points_int)
            if success:
                messagebox.showinfo("Sucesso", message)
                update_points_window.destroy()
                window.destroy()
            else:
                messagebox.showerror("Erro", message)
        
        btns_frame = ctk.CTkFrame(frame_alt, fg_color="transparent")
        btns_frame.pack(pady=20)
        
        btn_confirm = ctk.CTkButton(
            btns_frame,
            text="✅ CONFIRMAR",
            fg_color="#4CAF50",
            hover_color="#45a049",
            width=120,
            command=confirm_update
        )
        btn_confirm.pack(side="left", padx=10)
        
        btn_cancel = ctk.CTkButton(
            btns_frame,
            text="❌ CANCELAR",
            fg_color="#757575",
            hover_color="#616161",
            width=120,
            command=update_points_window.destroy
        )
        btn_cancel.pack(side="left", padx=10)
    
    btn_update_user = ctk.CTkButton(frame, text="ALTERAR NOME DE USUÁRIO", command=open_update_user)
    btn_update_user.pack(pady=10, fill="x")
    
    btn_update_password = ctk.CTkButton(frame, text="ALTERAR SENHA", command=open_update_password)
    btn_update_password.pack(pady=10, fill="x")
    
    btn_update_points = ctk.CTkButton(frame, text="ALTERAR PONTOS", command=open_update_points)
    btn_update_points.pack(pady=10, fill="x")

def open_delete_window():
    window = ctk.CTkToplevel()
    window.title("Excluir Usuário")
    window.geometry("400x250")
    window.grab_set()
    
    frame = ctk.CTkFrame(window)
    frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    title = ctk.CTkLabel(frame, text="EXCLUIR USUÁRIO", font=("Arial", 16, "bold"))
    title.pack(pady=15)
    
    ctk.CTkLabel(frame, text="Nome de usuário:").pack(pady=8)
    entry_user = ctk.CTkEntry(frame, width=250)
    entry_user.pack(pady=8)
    
    ctk.CTkLabel(frame, text="Senha:").pack(pady=8)
    entry_password = ctk.CTkEntry(frame, width=250, show="*")
    entry_password.pack(pady=8)
    
    def confirm_delete():
        username = entry_user.get()
        password = entry_password.get()
        
        if not validate_fields(entry_user, entry_password):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return
        if not db.exist_user(username):
            messagebox.showerror("Erro", "Usuário não encontrado!")
            return
        
        response = messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o usuário {username}?")
        if response:
            success, message = db.delete_user(username, password)
            if success:
                messagebox.showinfo("Sucesso", message)
                window.destroy()
            else:
                messagebox.showerror("Erro", message)
    
    btns_frame = ctk.CTkFrame(frame, fg_color="transparent")
    btns_frame.pack(pady=20)
    
    btn_delete = ctk.CTkButton(
        btns_frame,
        text="✅ CONFIRMAR EXCLUSÃO",
        fg_color="#F44336",
        hover_color="#D32F2F",
        width=180,
        height=40,
        command=confirm_delete
    )
    btn_delete.pack(side="left", padx=10)
    
    btn_cancel = ctk.CTkButton(
        btns_frame,
        text="❌ CANCELAR",
        fg_color="#757575",
        hover_color="#616161",
        width=120,
        height=40,
        command=window.destroy
    )
    btn_cancel.pack(side="left", padx=10)

def main():
    window = main_window()
    window.mainloop()

if __name__ == "__main__":
    main() # 7 anos de azar pra quem colocar a 600° linha
