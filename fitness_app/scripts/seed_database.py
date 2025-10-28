# fitness_app/scripts/seed_database.py

from fitness_app.core.database import RepositorioTinyDB, db  # Importe a instância 'db'
from fitness_app.core.models import Usuario, PlanoTreino
import json
import os

def popular_usuarios():
    print("Limpando e populando a tabela de usuários...")
    
    # Use a instância 'db' importada para aceder à tabela
    tabela_usuarios = db.table('usuarios')
    tabela_usuarios.truncate()
    
    # O repositório agora usará a mesma instância 'db'
    repo = RepositorioTinyDB('usuarios')
    
    usuarios = [
        ("Admin", "admin@email.com", "123456"),
        ("Edgar", "edgar@email.com", "123456"),
        ("Vini", "vini@email.com", "123456")
    ]
    
    for nome, email, senha in usuarios:
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)
            repo.inserir(usuario)
        except ValueError as e:
            print(f"Erro ao criar usuário {nome}: {e}")
    
    print(f"{len(usuarios)} usuários inseridos.")

def popular_treinos_prontos():
    print("Limpando e populando a tabela de treinos prontos...")
    
    # Use a instância 'db' importada
    tabela_treinos = db.table('treinos_prontos')
    tabela_treinos.truncate()
    
    repo = RepositorioTinyDB('treinos_prontos')

    try:
        base_path = os.path.dirname(__file__)
        json_path = os.path.join(base_path, '..', 'data', 'workouts.json')
        
        with open(json_path, 'r', encoding='utf-8') as f:
            treinos = json.load(f)
            
            for treino_data in treinos:
                plano = PlanoTreino(
                    usuario_email=None,  # É um plano global
                    nome=treino_data['nome'],
                    exercicios=treino_data['exercicios'],
                    objetivo=treino_data['objetivo'],
                    nivel=treino_data['nivel']
                )
                repo.inserir(plano)
            
            print(f"{len(treinos)} treinos prontos inseridos.")
            
    except FileNotFoundError:
        print("Erro: 'fitness_app/data/workouts.json' não encontrado.")
    except Exception as e:
        print(f"Erro ao popular treinos: {e}")

if __name__ == "__main__":
    popular_usuarios()
    popular_treinos_prontos()
    print("Base de dados populada com sucesso!")
    
    db.close()
