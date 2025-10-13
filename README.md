<div align="center">

# 🧙‍♀️ Ranking de Bruxas e Magos  

### *Códigos, Magia e Mistérios Digitais*

<img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange" alt="Status">
<img src="https://img.shields.io/badge/Linguagem-Python%203.13.0-blue" alt="Linguagem">
<img src="https://img.shields.io/badge/Banco-MongoDB%20Atlas-green" alt="Banco">
<img src="https://img.shields.io/badge/Interface-CustomTKinter-purple" alt="Interface">
<img src="https://img.shields.io/badge/Segurança-Argon2-red" alt="Segurança">

---

*Um sistema místico que conecta magos e bruxas a uma interface digital, registrando pontos, protegendo segredos com criptografia segura e classificando os mais poderosos em um ranking encantado.*

[🪄 **Visão Geral**](#-sobre-o-projeto) • [⚙️ **Tecnologias**](#-tecnologias-utilizadas) • [🏗️ **Arquitetura**](#-arquitetura-do-sistema) • [🚀 **Execução**](#-instalação) • [📚 **Funcionalidades**](#-principais-funcionalidades) • [🧛 **Autores**](#-equipe)

</div>

---

## 🎯 **Sobre o Projeto**

O **Ranking de Bruxas e Magos** é um sistema de cadastro desenvolvido em **Python**, projetado para armazenar e gerenciar informações de usuários mágicos — bruxas e magos — com total segurança e praticidade.

Os dados são protegidos com **criptografia Argon2** e armazenados no **MongoDB Atlas**, um banco de dados em nuvem robusto e confiável.  
A interface é construída com **CustomTkinter**, oferecendo uma experiência visual moderna e intuitiva que permite:

- Cadastrar novos magos e bruxas 🧙‍♀️  
- Alterar informações existentes 🪶  
- Excluir registros obsoletos 💀  
- Exibir um **ranking mágico**, listando todos os cadastrados em **ordem crescente de pontos**, revelando os mais poderosos do clã.  

O projeto encontra-se **em fase final de desenvolvimento**, faltando apenas ajustes visuais e refinamentos na interface.

---

## ⚙️ **Tecnologias Utilizadas**

```
🐍 Python 3.13.0
💾 MongoDB Atlas
🪟 CustomTkinter + Tkinter
🔐 Pymongo
🧠 Argon2 (Criptografia)
```

---

## 🏗️ **Arquitetura do Sistema**

```mermaid
graph TD
    A[Interface CustomTkinter] --> B[Camada de Controle Python]
    B --> C[Pymongo]
    C --> D[MongoDB Atlas]
    A --> E[Telas de Cadastro e Ranking]
    B --> F[Validação Argon2]
    D --> G[Armazenamento Seguro de Dados]
```

### **Estrutura de Pastas**
```
projetoBD4bim/
├── 📁 interface/               # Interface gráfica com CustomTkinter
│   ├── main.py                 # Arquivo principal da aplicação
│   └── assets/                 # Imagens e ícones da interface
├── 📁 database/                # Conexão e operações com o MongoDB
│   └── db_manager.py
├── 📁 models/                  # Estrutura de dados e classes
│   └── usuario.py
├── 📁 controllers/             # Lógica de CRUD e ranking
│   └── user_controller.py
└── 📄 README.md
```

---

## 🚀 **Instalação**

### **Pré-requisitos**
- Python **3.13.0** instalado  
- Conta e cluster configurados no **MongoDB Atlas**  

### **1. Clone o repositório**
```bash
git clone https://github.com/jeanmbr/projetoBD4bim.git
cd projetoBD4bim
```

### **2. Instale as dependências**
```bash
pip install pymongo customtkinter argon2-cffi
```

### **3. Configure o Banco de Dados**
Crie um arquivo `.env` na raiz do projeto com sua **string de conexão MongoDB Atlas**:
```
MONGO_URI="sua_string_de_conexao"
```

### **4. Execute a aplicação**
```bash
python main.py
```

---

## 📚 **Principais Funcionalidades**

| Feitiço | Descrição |
|---------|------------|
| 🔮 **Cadastro de Bruxas e Magos** | Registra novos usuários mágicos com segurança Argon2 |
| ✏️ **Edição de Registros** | Permite modificar dados armazenados no banco |
| 💀 **Remoção de Usuários** | Exclui magos e bruxas do sistema |
| 🧙‍♂️ **Ranking Mágico** | Ordena todos os usuários de acordo com sua pontuação |
| 🔐 **Criptografia Avançada** | Protege senhas com Argon2, garantindo máxima segurança |

---

## 👥 **Equipe**

<div align="center">

**Desenvolvido com 🖤 paixão sombria por:**

- 🧙‍♂️ [@jeanmbr](https://github.com/jeanmbr)  
- 🧛 [@Doringgg](https://github.com/Doringgg)  
- 🧝 [@Caua-Macedo](https://github.com/Caua-Macedo)

---

*"Nem todo feitiço é magia... alguns são apenas boas linhas de código."* 💻✨  

</div>
