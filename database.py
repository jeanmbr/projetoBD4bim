from pymongo import MongoClient
from argon2 import PasswordHasher

try:
    client = MongoClient("mongodb+srv://root:12345@univap.gox6oor.mongodb.net/?retryWrites=true&w=majority&appName=Univap")
    db = client["projetoBD4bim"]
    collection = db["users"]
    ph = PasswordHasher()
    print('=-'*43)
    print("Conexão com o MongoDB estabelecida com sucesso!")
    print('=-'*43)
except Exception as erro:
    print(f"Erro na conexão com o MongoDB: {erro}")

def insert_user(username, password, points):
    try:
        if collection.find_one({"username": username}):
            return False, "Usuário já existe!"
        
        password_hash = ph.hash(password)
        usuario = {
            "username": username,
            "password_hash": password_hash,
            "points": points
        }
        collection.insert_one(usuario)
        return True, "Usuário registrado com sucesso!"
    except Exception as e:
        return False, f"Erro ao registrar usuário: {e}"

def verify_password(username, password):
    try:
        usuario = collection.find_one({"username": username})
        if usuario:
            ph.verify(usuario["password_hash"], password)
            return True
        return False
    except Exception:
        return False

def update_user(old_username, new_username, password):
    try:
        if not verify_password(old_username, password):
            return False, "Senha incorreta!"
        
        if new_username != old_username and collection.find_one({"username": new_username}):
            return False, "Novo nome de usuário já existe!"
        
        collection.update_one(
            {"username": old_username},
            {"$set": {"username": new_username}}
        )
        return True, "Nome de usuário atualizado com sucesso!"
    except Exception as e:
        return False, f"Erro ao atualizar usuário: {e}"

def update_password(username, old_password, new_password):
    try:
        if not verify_password(username, old_password):
            return False, "Senha antiga incorreta!"
        
        new_hash_password = ph.hash(new_password)
        collection.update_one(
            {"username": username},
            {"$set": {"password_hash": new_hash_password}}
        )
        return True, "Senha atualizada com sucesso!"
    except Exception as e:
        return False, f"Erro ao atualizar senha: {e}"

def update_points(username, password, new_points):
    try:
        if not verify_password(username, password):
            return False, "Senha incorreta!"
        
        collection.update_one(
            {"username": username},
            {"$set": {"points": int(new_points)}}
        )
        return True, "Pontos atualizados com sucesso!"
    except Exception as e:
        return False, f"Erro ao atualizar pontos: {e}"

def delete_user(username, password):
    try:
        if not verify_password(username, password):
            return False, "Senha incorreta!"
        
        result = collection.delete_one({"username": username})
        if result.deleted_count > 0:
            return True, "Usuário excluído com sucesso!"
        else:
            return False, "Usuário não encontrado!"
    except Exception as e:
        return False, f"Erro ao excluir usuário: {e}"

def get_ranking():
    try:
        users = list(collection.find({}, {"username": 1, "points": 1, "_id": 0}).sort("points", -1))
        return True, users
    except Exception as e:
        return False, f"Erro ao obter ranking: {e}"

def exist_user(username):
    try:
        return collection.find_one({"username": username}) is not None
    except Exception:
        return False