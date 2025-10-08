# 🏋 Fitness_app_Refatoração 

Código Original: https://github.com/jfdt10/Projeto_Software_OO_Fitness_App , será refatorado com padrões de projeto

**Observação caro leitor(a) 🙂:** Emoticons foram usados de forma intencional para tornar a leitura mais leve e dinâmica, principalmente para destacar algumas parte do texto. Eles fazem parte de uma proposta de leitura simplificada e não são resultado de um simples ctrl+c/ctrl+v de uma LLM (que costuma usar a mesma prática). Todo o conteúdo foi escrito manualmente pelo autor deste repositório, e considero importante destacar isso para evitar qualquer ambiguidade, obrigado.

<img width="1002" height="552" alt="image" src="https://github.com/user-attachments/assets/11ccd226-5d4f-42ed-97e3-22e996c0088b" />


## Versão Atual 

V.1.3 Aplicando Padrões de Projetos - Comportamentais

[versões anteriores](https://github.com/edgarvtt/Fitness_app_Refatora?tab=readme-ov-file#vers%C3%B5es-anteriores)

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

# Padrões de Projeto

Abaixo estão os Padrões de Projetos Criacionais adotados para a refatoração do Projeto

## 🏭 Abstract Factory {Padrão Criacional}

foi implementado o padrão 'Abstract Factory' para centralizar e desagrupar a criação dos "Serviços" (como ServicoTreino, ServicoAtividade, etc...) da lógica principal do app.<br/>

**😨Problema:** Antes, o arquivo main.py criava cada serviço diretamente o que o deixava ele dependente da nossa implementação específica de banco de dados, o TinyDB.<br/><br/>
**💡Solução:** Construi uma "Factory" (TinyDBServiceFactory) que é a única responsável por saber como construir todos os serviços. O main.py agora apenas instancia essa fábrica uma vez e a distribui para onde for necessário.<br/><br/>
**✅Benefício:** Se no futuro quiser trocar o TinyDB por outro banco de dados, só precisaremos criar uma nova fábrica. O resto do código não precisa de nenhuma alteração, tornando o sistema muito mais flexível e fácil de manter.<br/><br/>

## ⌘ Command {Padrão Comportamental}

Foi implementado o padrão 'Command' para transformar cada ação do menu em um objeto independente, desacoplando a interface do usuário da lógica que executa a ação, resumindo o padrão Command encapsula um pedido como um objeto, permitindo separar quem solicita a ação de quem efetivamente a executa.<br/><br/>

**😨Problema:** Antes, a função que gerenciava o menu de treinos (gerenciar_treinos) continha uma longa estrutura if/elif/else, com isso deixava o código do menu fortemente acoplado, pois ele precisava saber exatamente qual método de qual serviço chamar para cada opção.<br/><br/>
**💡Solução:** Agora, cada ação do menu (como "Criar Plano" ou "Adicionar Exercício") foi colocada para sua própria classe dentro do novo arquivo commands.py. a função gerenciar_treinos foi simplificada para apenas mapear a opção do usuário a um desses objetos de comando e executar, sem precisar saber os detalhes da operação.<br/><br/>
**✅Benefício:** O código do menu ficou muito mais limpo e organizado. Adicionar novas opções se tornou mais fácil (basta criar uma nova classe de comando) e a lógica principal ficou completamente independente das ações que ela dispara, aumentando a flexibilidade e facilitando a manutenção.<br/><br/>

## Estrutura do Projeto 

"referência do código original"

```text
fitness_app/
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
    └── seed_database.py       # Populador do banco
```
## Instalação e Configuração

"referência do código original"

### |_ Requisitos
Python 3.8 ou superior<br/>
Dependências listadas em requirements.txt

### |_ Passos de instalação

####  ★ Clone o repositório:

```
git clone https://github.com/jfdt10/Projeto_Software_OO_Fitness_App.git

cd Projeto_Software_OO_Fitness_App
```
####  ★ Crie um ambiente virtual:

```
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

####  ★ Instale as dependências:
```
pip install -r requirements.txt
```

####  ★ Configure o banco de dados:

```
# Popular com dados iniciais
python -m fitness_app.scripts.seed_database

# Gerar dados simulados (opcional)
python -m fitness_app.scripts.gerar_dados

```
#### Interface de Terminal
```
python -m fitness_app.main
```

## Versões Anteriores
V.1.0 Refatoração - Analisando os requesitos funcionais
V.1.1 Aplicando Padrões de Projetos Criacionais
V.1.2 Aplicando Padrões de Projetos Comportamentais
