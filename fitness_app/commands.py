# fitness_app/commands.py

from abc import ABC, abstractmethod
from fitness_app.core.models import PlanoTreino, Usuario
from fitness_app.services.workout import ServicoTreino
from fitness_app.services.video import ServicoVideo

# --- Interface do Comando ---
class Command(ABC):
    """
    A interface Command declara um método para executar uma operação.
    """
    @abstractmethod
    def execute(self):
        pass

# --- Comandos Concretos para Planos de Treino ---

class ListarPlanosTreinoCommand(Command):
    def __init__(self, servico_treino: ServicoTreino, usuario: Usuario):
        self.servico_treino = servico_treino
        self.usuario = usuario

    def execute(self):
        print("\n--- Meus Planos de Treino ---")
        planos = self.servico_treino.listar(self.usuario.email)
        if not planos:
            print("Nenhum plano de treino encontrado.")
            return
        for plano in planos:
            exercicios_str = ", ".join([ex.get('nome', 'N/A') for ex in plano.exercicios])
            print(f"ID: {plano.id} | Nome: {plano.nome} | Objetivo: {plano.objetivo} | Nível: {plano.nivel}")
            print(f"  Exercícios: {exercicios_str if exercicios_str else 'Nenhum'}")
            if hasattr(plano, 'video_favorito') and getattr(plano, 'video_favorito', None):
                 print(f"  -> Vídeo Associado: {plano.video_favorito.get('titulo', 'N/A')}")
            print("-" * 20)

class CriarPlanoTreinoCommand(Command):
    def __init__(self, servico_treino: ServicoTreino, usuario: Usuario):
        self.servico_treino = servico_treino
        self.usuario = usuario

    def execute(self):
        print("\n--- Criar Novo Plano de Treino ---")
        nome = input("Nome do plano: ")
        objetivo = input("Objetivo (ex: 'emagrecimento', 'hipertrofia'): ")
        nivel = input("Nível (ex: 'iniciante', 'intermediario', 'avancado'): ")
        
        self.servico_treino.criar(
            usuario_email=self.usuario.email,
            nome=nome,
            exercicios=[],
            objetivo=objetivo,
            nivel=nivel
        )
        print("Plano de treino criado com sucesso!")

class DeletarPlanoTreinoCommand(Command):
    def __init__(self, servico_treino: ServicoTreino, usuario: Usuario):
        self.servico_treino = servico_treino
        self.usuario = usuario
    
    def execute(self):
        print("\n--- Deletar Plano de Treino ---")
        plano_id = input("Digite o ID do plano a ser deletado: ")
        if self.servico_treino.deletar(plano_id, self.usuario.email):
            print("Plano deletado com sucesso!")
        else:
            print("Erro: Plano não encontrado ou não pertence a você.")

class AssociarVideoCommand(Command):
    def __init__(self, servico_treino: ServicoTreino, servico_video: ServicoVideo, usuario: Usuario):
        self.servico_treino = servico_treino
        self.servico_video = servico_video
        self.usuario = usuario

    def execute(self):
        print("\n--- Associar Vídeo Favorito a um Plano ---")
        plano_id = input("ID do Plano de Treino: ")
        
        videos_favoritos = self.servico_video.listar(self.usuario.email)
        if not videos_favoritos:
            print("Você não tem vídeos favoritos para associar.")
            return

        print("Seus Vídeos Favoritos:")
        for i, video in enumerate(videos_favoritos):
            print(f"{i + 1}. {video.titulo}")

        try:
            video_idx = int(input("Escolha o número do vídeo: ")) - 1
            if 0 <= video_idx < len(videos_favoritos):
                video_selecionado = videos_favoritos[video_idx]
                if self.servico_treino.associar_video(plano_id, self.usuario.email, video_selecionado):
                    print("Vídeo associado com sucesso!")
                else:
                    print("Erro: Plano não encontrado ou não pertence a você.")
            else:
                print("Seleção de vídeo inválida.")
        except ValueError:
            print("Entrada inválida.")

class AdicionarExercicioCommand(Command):
    def __init__(self, servico_treino: ServicoTreino, usuario: Usuario):
        self.servico_treino = servico_treino
        self.usuario = usuario

    def execute(self):
        print("\n--- Adicionar Exercício a um Plano ---")
        plano_id = input("ID do Plano de Treino: ")
        nome_exercicio = input("Nome do Exercício: ")
        series = input("Séries: ")
        repeticoes = input("Repetições: ")
        exercicio = {"nome": nome_exercicio, "series": series, "repeticoes": repeticoes}
        
        if self.servico_treino.add_exercicio(plano_id, self.usuario.email, exercicio):
            print("Exercício adicionado com sucesso.")
        else:
            print("Erro: Plano não encontrado ou não pertence a você.")

class RemoverExercicioCommand(Command):
    def __init__(self, servico_treino: ServicoTreino, usuario: Usuario):
        self.servico_treino = servico_treino
        self.usuario = usuario

    def execute(self):
        print("\n--- Remover Exercício de um Plano ---")
        plano_id = input("ID do Plano de Treino: ")
        nome_exercicio = input("Nome do Exercício a ser removido: ")
        
        if self.servico_treino.remove_exercicio(plano_id, self.usuario.email, nome_exercicio):
            print("Exercício removido com sucesso.")
        else:
            print("Erro: Plano ou exercício não encontrado.")

class AtualizarPlanoCommand(Command):
    def __init__(self, servico_treino: ServicoTreino, usuario: Usuario):
        self.servico_treino = servico_treino
        self.usuario = usuario

    def execute(self):
        print("\n--- Atualizar Plano de Treino ---")
        plano_id = input("ID do plano a ser atualizado: ")
        novo_nome = input("Novo nome do plano (deixe em branco para não alterar): ")
        novo_objetivo = input("Novo objetivo (deixe em branco para não alterar): ")
        novo_nivel = input("Novo nível (deixe em branco para não alterar): ")

        dados_atualizados = {}
        if novo_nome:
            dados_atualizados['nome'] = novo_nome
        if novo_objetivo:
            dados_atualizados['objetivo'] = novo_objetivo
        if novo_nivel:
            dados_atualizados['nivel'] = novo_nivel
        
        if not dados_atualizados:
            print("Nenhum dado para atualizar.")
            return

        if self.servico_treino.atualizar(plano_id, dados_atualizados, self.usuario.email):
            print("Plano atualizado com sucesso!")
        else:
            print("Erro: Plano não encontrado ou não pertence a você.")