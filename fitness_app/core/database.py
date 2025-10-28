# fitness_app/core/database.py

from tinydb import TinyDB, Query
from datetime import datetime
import os
from .abc import RepositorioBase

# Garante que o diretório de dados exista
os.makedirs('fitness_app/data', exist_ok=True)

# 1. Criamos a instância global do banco de dados UMA VEZ e partilhamo-la.
db = TinyDB('fitness_app/data/fitness.json')

class RepositorioTinyDB(RepositorioBase):
    # 2. Removemos o 'db_path' - já não é necessário
    def __init__(self, tabela): 
        super().__init__(tabela)
        
        # 3. ESTA É A CORREÇÃO CRÍTICA:
        # Em vez de criar um novo TinyDB(), usamos a instância 'db' global.
        self._db = db 
        # -------------------------
        
        self._table = self._db.table(tabela) 

    def inserir(self, obj):
        data = obj.to_dict() if hasattr(obj, 'to_dict') else obj
        if 'criado_em' not in data or data['criado_em'] is None:
             data['criado_em'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        return self._table.insert(data)

    def listar(self, query=None, model_cls=None):
        regs = self._table.search(query) if query else self._table.all()
        if model_cls and hasattr(model_cls, 'from_dict'):
            return [model_cls.from_dict(r) for r in regs]
        return regs

    def obter(self, id, model_cls=None):
        rec = self._table.get(Query().id == id)
        if rec and model_cls:
            return model_cls.from_dict(rec)
        return rec

    def obter_por_usuario(self, id, usuario_email, model_cls=None):
        Q = Query()
        rec = self._table.get((Q.id == id) & (Q.usuario_email == usuario_email))
        if rec and model_cls:
            return model_cls.from_dict(rec)
        return rec
        
    def atualizar(self, id, data, usuario_email=None):
        Q = Query()
        query = (Q.id == id)
        if usuario_email:
            # Garante que só atualize se o email do usuário também bater
            query &= (Q.usuario_email == usuario_email)
        
        return self._table.update(data, query) > 0

    def deletar(self, id, usuario_email=None):
        Q = Query()
        query = (Q.id == id)
        if usuario_email:
            # Garante que só delete se o email do usuário também bater
            query &= (Q.usuario_email == usuario_email)

        return self._table.remove(query) > 0

    def truncate(self):
        self._table.truncate()

    def usuario_existe(self, field, value):
        return self._table.contains(Query()[field] == value)

# Encapsulamento para controle de acesso do módulo
__all__ = [
    "db", "RepositorioTinyDB"
]