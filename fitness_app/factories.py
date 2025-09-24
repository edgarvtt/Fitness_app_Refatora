
from abc import ABC, abstractmethod
from fitness_app.core.database import RepositorioTinyDB
from fitness_app.services.activity import ServicoAtividade
from fitness_app.services.goal import ServicoMeta
from fitness_app.services.nutrition import ServicoNutricional
from fitness_app.services.social import ServicoSocial
from fitness_app.services.workout import ServicoTreino
from fitness_app.services.feedback import ServicoFeedback
from fitness_app.services.forum import ServicoForum
from fitness_app.services.video import ServicoVideo
from fitness_app.services.wearable import ServicoWearable
from fitness_app.services.recommendation import ServicoRecomendacao

class ServiceFactory(ABC):

    @abstractmethod
    def create_workout_service(self) -> ServicoTreino:
        pass

    @abstractmethod
    def create_activity_service(self) -> ServicoAtividade:
        pass

    @abstractmethod
    def create_nutrition_service(self) -> ServicoNutricional:
        pass

    @abstractmethod
    def create_goal_service(self) -> ServicoMeta:
        pass

    @abstractmethod
    def create_social_service(self) -> ServicoSocial:
        pass
    
    @abstractmethod
    def create_feedback_service(self) -> ServicoFeedback:
        pass

    @abstractmethod
    def create_forum_service(self) -> ServicoForum:
        pass

    @abstractmethod
    def create_video_service(self) -> ServicoVideo:
        pass

    @abstractmethod
    def create_wearable_service(self) -> ServicoWearable:
        pass

    @abstractmethod
    def create_recommendation_service(self) -> ServicoRecomendacao:
        pass


class TinyDBServiceFactory(ServiceFactory): #caso vá usar banco de dados futuramente

    def create_workout_service(self) -> ServicoTreino:
        return ServicoTreino(repo_planos=RepositorioTinyDB('planos_treino'))

    def create_activity_service(self) -> ServicoAtividade:
        return ServicoAtividade(repo=RepositorioTinyDB('atividades'))

    def create_nutrition_service(self) -> ServicoNutricional:
        return ServicoNutricional(repo=RepositorioTinyDB('nutricao'))

    def create_goal_service(self) -> ServicoMeta:
        return ServicoMeta(repo=RepositorioTinyDB('metas'))

    def create_social_service(self) -> ServicoSocial:
        return ServicoSocial(repo=RepositorioTinyDB('desafios'))

    def create_feedback_service(self) -> ServicoFeedback:
        return ServicoFeedback(repo=RepositorioTinyDB('feedbacks'))

    def create_forum_service(self) -> ServicoForum:
        return ServicoForum()

    def create_video_service(self) -> ServicoVideo:
        return ServicoVideo(repo=RepositorioTinyDB('videos_favoritos'))
    
    def create_wearable_service(self) -> ServicoWearable:
        return ServicoWearable(repo=RepositorioTinyDB('dados_wearable'))

    def create_recommendation_service(self) -> ServicoRecomendacao:
        return ServicoRecomendacao(repo=RepositorioTinyDB('recomendacoes'))