# LinguaAI 🌐

Plataforma gratuita de ensino de idiomas com **Inteligência Artificial como professor personalizado**.

O aluno escolhe o idioma que quer aprender e a IA assume o papel de professor — com plano de estudos adaptativo, aulas reais, exercícios, recursos de áudio, biblioteca de conteúdo e uma conversa que parece humana, não um robô.

Tudo gratuito. Tudo automático. Tudo ajustado ao ritmo de quem aprende.

---

## ✨ Funcionalidades

- **Professor IA personalizado** — conversa fluida e natural, sem parecer chatbot
- **Suporte a qualquer idioma** — o aluno escolhe o idioma no início da sessão
- **Plano de estudos automático** — gerado e ajustado conforme o desempenho real do aluno
- **Cronograma adaptativo** — muda de acordo com a evolução, sem ritmo fixo
- **Aulas estruturadas** — conteúdo real de gramática, vocabulário e conversação
- **Exercícios para casa** — gerados automaticamente ao fim de cada aula
- **Recursos de áudio via IA** — pronúncia e escuta integradas
- **Biblioteca de recursos** — livros, vídeos e materiais indicados por idioma e nível
- **Avaliação contínua de desempenho** — o sistema sabe o que o aluno já domina e o que precisa reforçar

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3 |
| Interface | Streamlit |
| IA / LLM | API de IA (OpenAI / Gemini) |
| Áudio | Text-to-Speech via API |
| Estado da sessão | Streamlit Session State |

---

## 📐 Estrutura do Projeto

```
lingua-ai/
├── app.py                  # Ponto de entrada da aplicação Streamlit
├── professor.py            # Lógica do professor IA — prompts e contexto
├── plano_estudos.py        # Geração e atualização do plano adaptativo
├── avaliacao.py            # Avaliação de desempenho e progresso do aluno
├── exercicios.py           # Geração automática de exercícios
├── biblioteca.py           # Curadoria de recursos por idioma e nível
├── audio.py                # Integração com Text-to-Speech
├── utils.py                # Funções auxiliares
└── requirements.txt        # Dependências do projeto
```

---

## ⚙️ Como Executar Localmente

### Pré-requisitos
- Python 3.10+
- Chave de API (OpenAI ou Google Gemini)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/manoelalmorais/lingua-ai.git
cd lingua-ai
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure sua chave de API no arquivo `.env`:
```env
OPENAI_API_KEY=sua_chave_aqui
# ou
GOOGLE_API_KEY=sua_chave_aqui
```

4. Execute:
```bash
streamlit run app.py
```

Acesse em `http://localhost:8501`

---

## 🎯 Como Funciona

```
Aluno escolhe o idioma
        ↓
IA avalia o nível inicial (diagnóstico rápido)
        ↓
Plano de estudos gerado automaticamente
        ↓
Aulas, exercícios e recursos adaptados ao nível
        ↓
Desempenho avaliado continuamente
        ↓
Cronograma ajustado conforme a evolução
```

---

## 🔭 Próximos Passos

- [ ] Backend dedicado (Java Spring Boot) para persistência entre sessões
- [ ] Autenticação de usuários — salvar progresso entre acessos
- [ ] Dashboard de progresso com histórico de desempenho
- [ ] App mobile (PWA)

---

## 💡 Motivação

Este projeto nasceu de uma pergunta simples: *por que aprender um idioma ainda custa caro, quando a IA já consegue ensinar melhor do que muitos cursos pagos?*

O objetivo é democratizar o acesso ao ensino de idiomas — com qualidade, personalização e custo zero para o aluno.

---

## 👨‍💻 Desenvolvedor

**Manoel Almeida de Morais**
Desenvolvedor Backend Java | Power Platform | Python | Aracaju/SE

- 📧 manoelalmorais@gmail.com
- 💼 [LinkedIn](https://linkedin.com/in/manoelalmorais)
- 🐙 [GitHub](https://github.com/manoelalmorais)


# LinguaAI 🌐

A free language learning platform powered by **Artificial Intelligence as your personal teacher**.

The student picks any language they want to learn and the AI takes on the role of teacher — with an adaptive study plan, real lessons, exercises, audio resources, a content library, and a conversation that feels human, not robotic.

All free. All automatic. All adjusted to the learner's own pace.

---

## ✨ Features

- **Personalized AI teacher** — natural, fluid conversation that doesn't feel like a chatbot
- **Any language supported** — the student chooses their target language at the start
- **Automatic study plan** — generated and updated based on the student's real performance
- **Adaptive schedule** — adjusts to progress, no fixed rigid pace
- **Structured lessons** — real grammar, vocabulary and conversation content
- **Homework exercises** — automatically generated at the end of each lesson
- **AI audio resources** — pronunciation and listening practice built in
- **Resource library** — books, videos and materials curated by language and level
- **Continuous performance assessment** — the system knows what the student has mastered and what needs reinforcement

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Interface | Streamlit |
| AI / LLM | AI API (OpenAI / Gemini) |
| Audio | Text-to-Speech via API |
| Session state | Streamlit Session State |

---

## 📐 Project Structure

```
lingua-ai/
├── app.py                  # Streamlit app entry point
├── professor.py            # AI teacher logic — prompts and context
├── plano_estudos.py        # Adaptive study plan generation and updates
├── avaliacao.py            # Performance evaluation and progress tracking
├── exercicios.py           # Automatic exercise generation
├── biblioteca.py           # Resource curation by language and level
├── audio.py                # Text-to-Speech integration
├── utils.py                # Helper functions
└── requirements.txt        # Project dependencies
```

---

## ⚙️ Running Locally

### Prerequisites
- Python 3.10+
- API key (OpenAI or Google Gemini)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/manoelalmorais/lingua-ai.git
cd lingua-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your API key in a `.env` file:
```env
OPENAI_API_KEY=your_key_here
# or
GOOGLE_API_KEY=your_key_here
```

4. Run the app:
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🎯 How It Works

```
Student picks a language
        ↓
AI runs a quick initial level assessment
        ↓
Personalized study plan generated automatically
        ↓
Lessons, exercises and resources adapted to the level
        ↓
Performance evaluated continuously
        ↓
Schedule adjusted as the student progresses
```

---

## 🔭 Roadmap

- [ ] Dedicated backend (Java Spring Boot) for persistent data between sessions
- [ ] User authentication — save progress across logins
- [ ] Progress dashboard with performance history
- [ ] Mobile app (PWA)

---

## 💡 Motivation

This project started from a simple question: *why does learning a language still cost money, when AI can already teach better than many paid courses?*

The goal is to democratize language learning — with quality, personalization and zero cost to the student.

---

## 👨‍💻 Developer

**Manoel Almeida de Morais**
Backend Java Developer | Power Platform | Python | Aracaju, Brazil

- 📧 manoelalmorais@gmail.com
- 💼 [LinkedIn](https://linkedin.com/in/manoelalmorais)
- 🐙 [GitHub](https://github.com/manoelalmorais)
