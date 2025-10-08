# fitness_app/services/workout.py

from fitness_app.core.models import PlanoTreino, Video
from fitness_app.core.abc import ServicoBase
from fitness_app.core.database import RepositorioTinyDB


class ServicoTreino(ServicoBase):
    def __init__(self, repo=None, repo_planos=None):
        super().__init__(repo or RepositorioTinyDB('treinos_prontos'))
        self.repo_planos = repo_planos or RepositorioTinyDB('planos_treino')
        self.plano_treino_base = PlanoTreino(
            usuario_email="",
            nome="",
            exercicios=[],
            objetivo="",
            nivel=""
        )

    def recomendar_treinos(self, usuario):
        treinos = self.repo.listar(model_cls=type(self.plano_treino_base))
        nivel_usuario = getattr(usuario, 'nivel_experiencia', None) or getattr(usuario, 'nivel_atividade', None)
        objetivo_usuario = getattr(usuario, 'objetivo', None)
        
        if nivel_usuario is None and objetivo_usuario is None:
            return treinos

        def valor_treino(t, campo):
            return getattr(t, campo, None)

        recomendados = [
            t for t in treinos
            if (nivel_usuario is None or valor_treino(t, 'nivel') == nivel_usuario) and
               (objetivo_usuario is None or valor_treino(t, 'objetivo') == objetivo_usuario)
        ]
        return recomendados

    def criar(self, usuario_email, nome, exercicios, objetivo, nivel):
        plano = type(self.plano_treino_base)(
            usuario_email=usuario_email,
            nome=nome,
            exercicios=exercicios,
            objetivo=objetivo,
            nivel=nivel
        )
        self.repo_planos.inserir(plano)
        return plano

    def listar(self, usuario_email=None):
        planos = self.repo_planos.listar(model_cls=type(self.plano_treino_base))
        if usuario_email:
            return [p for p in planos if getattr(p, 'usuario_email', None) == usuario_email]
        return planos

    def atualizar(self, id, dados: dict, usuario_email: str):
        return self.repo_planos.atualizar(id, dados, usuario_email=usuario_email)

    def deletar(self, id, usuario_email: str):
        return self.repo_planos.deletar(id, usuario_email=usuario_email)

    def add_exercicio(self, plano_id, usuario_email, exercicio):
        plano = self.repo_planos.obter_por_usuario(plano_id, usuario_email, model_cls=type(self.plano_treino_base))
        if plano:
            plano.add_exercicio(exercicio)
            return self.repo_planos.atualizar(plano_id, {'exercicios': plano.exercicios}, usuario_email)
        return False

    def remove_exercicio(self, plano_id, usuario_email, nome_exercicio):
        plano = self.repo_planos.obter_por_usuario(plano_id, usuario_email, model_cls=type(self.plano_treino_base))
        if plano:
            exercicio_para_remover = next((ex for ex in plano.exercicios if ex.get('nome') == nome_exercicio), None)
            if exercicio_para_remover:
                plano.remove_exercicio(exercicio_para_remover)
                return self.repo_planos.atualizar(plano_id, {'exercicios': plano.exercicios}, usuario_email)
        return False

    def associar_video(self, plano_id: str, usuario_email: str, video: Video):
        video_info = {
            "id": video.id,
            "titulo": video.titulo,
            "url": video.url
        }
        return self.repo_planos.atualizar(plano_id, {"video_favorito": video_info}, usuario_email)