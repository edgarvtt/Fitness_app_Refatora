# 🏋 Fitness_app_Refatoração 

Código Original: https://github.com/jfdt10/Projeto_Software_OO_Fitness_App 

Sistema completo de gerenciamento fitness desenvolvido com foco em Programação Orientada a Objetos, demonstrando os Cinco pilares fundamentais: Herança, Polimorfismo, Encapsulamento, Abstração e Composição.

## Status Atual 

V.1.0 Refatoração - Analisando os requesitos 

## Funcionalidades

todas as funcionalidades foram aplicadas corretamentes após testes, são elas:

✅ Cadastro e autenticação de usuários com validação <br/>
✅ Criação de planos de treino personalizados e pré-prontos <br/>
✅ Registro de atividades físicas com múltiplos tipos <br/>
✅ Análise nutricional com base de alimentos pré-cadastrada <br/>
✅ Sistema de metas com acompanhamento de progresso <br/>
✅ Integração com wearables através de simulação e CSV <br/>
✅ Recursos sociais incluindo desafios entre usuários <br/>
✅ Fórum da comunidade com posts e comentários <br/>
✅ Sistema de feedback e avaliações <br/>
✅ Conteúdo educativo com integração de vídeos <br/>
✅ Recomendações personalizadas baseadas no perfil <br/>

## Estrutura do Projeto 

"referência do código original"

` fitness_app/
├── main.py                     # Ponto de entrada CLI
├── requirements.txt            # Dependências do projeto
│
├── core/                       # Núcleo do sistema
│   ├── models.py              # Todos os modelos com OOP
│   ├── database.py            # Repository Pattern + TinyDB
│   ├── auth.py                # Sistema de autenticação
│   ├── abc.py                 # Classes abstratas
│   └── utils.py               # Utilitários
│
├── services/                   # Camada de negócios
│   ├── workout.py             # Serviço de treinos
│   ├── activity.py            # Serviço de atividades
│   ├── nutrition.py           # Serviço nutricional
│   ├── goal.py                # Serviço de metas
│   ├── wearable.py            # Serviço wearable
│   ├── social.py              # Serviço social
│   ├── video.py               # Serviço de vídeos
│   ├── recommendation.py      # Serviço de recomendações
│   ├── feedback.py            # Serviço de feedback
│   └── forum.py               # Serviço de fórum
│
├── terminal/                   # Interface de usuário
│   ├── interface.py           # Menus e navegação
│   └── menus.py               # Lógica dos menus
│
├── data/                       # Dados e banco
│   ├── fitness.json           # Banco principal TinyDB
│   ├── workouts.json          # Treinos pré-cadastrados
│   ├── food_database.json     # Base de alimentos
│   └── wearable_data.csv      # Dados simulados
│
└── scripts/                    # Scripts auxiliares
    ├── gerar_dados.py         # Gerador de dados simulados
    └── seed_database.py       # Populador do banco`
 
