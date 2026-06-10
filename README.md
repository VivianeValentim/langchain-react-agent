# langchain-react-agent
Agente inteligente construído com o paradigma ReAct e Langchain, capaz de raciocinar e executar ações de forma autônoma. Este projeto implementa um **Assistente de Inteligência Artificial baseado em Agentes**, capaz de rotear dinamicamente o fluxo de resposta com base na intenção do usuário. Ele decide de forma autônoma entre utilizar seu conhecimento interno para perguntas gerais ou acionar ferramentas externas (Tool Calling) para resolver problemas exatos.

## Objetivo e Comportamento

O sistema resolve um problema clássico de Modelos de Linguagem (LLMs): a imprecisão em cálculos matemáticos (alucinação). O agente foi instruído através de *Prompt Engineering* a seguir um fluxo rigoroso:

1. **Conhecimento Geral:** Se o usuário perguntar *"Quem foi Albert Einstein?"*, o modelo responde naturalmente com base em seu treinamento.
2. **Cálculos Matemáticos:** Se o usuário perguntar *"Quanto é 128 vezes 46?"*, o modelo **pausa a geração de texto**, invoca uma função Python isolada (`calculadora`) para obter o resultado exato (5888) e, só então, formula a resposta final.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.12.10
* **Framework IA:** LangChain
* **Modelo de Linguagem:** OpenAI API
* **Gerenciamento de Ambiente:** `python-dotenv`

## Estrutura do Projeto

A arquitetura foi desenhada separando responsabilidades para facilitar a manutenção e escalabilidade do agente:

```text
agentic_query_router/
│
├── src/
│   ├── __init__.py      # Define o diretório como um módulo Python
│   ├── tools.py         # Lógica isolada da ferramenta (Calculadora com segurança)
│   └── agent.py         # Orquestração do LLM, System Prompt e Tool Calling
│
├── main.py              # Ponto de entrada (Interface interativa de terminal - CLI)
├── requirements.txt     # Lista de dependências do projeto
├── .env.example         # Exemplo de configuração de variáveis de ambiente
└── .gitignore           # Omissão de arquivos sensíveis e temporários

# Como Configurar e Executar

1. Pré-requisitos
Certifique-se de ter o Python instalado e uma chave de API válida da OpenAI.

2. Clonando e preparando o ambiente

## Crie um ambiente virtual
python -m venv venv

## Ative o ambiente (Windows)
venv\Scripts\activate
## Ative o ambiente (Mac/Linux)
source venv/bin/activate

3. Instalação das Dependências
pip install -r requirements.txt

4. Configuração das Variáveis de Ambiente
Crie um arquivo chamado .env na raiz do projeto e insira a sua chave de API.

5. Executando a Aplicação
python main.py
