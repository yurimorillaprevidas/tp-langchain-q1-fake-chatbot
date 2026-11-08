# Parte 2 - Questão 1 - Chatbot com Fake LLM

Simula um chatbot com o `FakeListLLM` do LangChain.

## Como executar

Use Python 3.12. Se já descompactou o projeto, entre na pasta e pule a etapa de clonagem.

```bash
git clone https://github.com/yurimorillaprevidas/tp-langchain-q1-fake-chatbot.git
cd tp-langchain-q1-fake-chatbot
```

Crie e ative um ambiente virtual.

No Windows, use o PowerShell.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No macOS ou Linux, rode os comandos abaixo.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Instale as dependências.

```bash
python -m pip install -r requirements.txt
```

Inicie o servidor.

```bash
python -m uvicorn main:app
```

O servidor fica em `http://127.0.0.1:8000`.

## Como testar

Abra [a documentação interativa](http://127.0.0.1:8000/docs), selecione **POST /chat**, clique em **Try it out**, cole o JSON e clique em **Execute**.

```json
{
  "message": "Qual é a capital do Brasil?"
}
```

Exemplo de resposta HTTP 200.

```json
{
  "reply": "A capital do Brasil é Brasília."
}
```

As perguntas disponíveis são `Olá!`, `Qual é o seu nome?` e `Qual é a capital do Brasil?`. O bot ignora diferenças de maiúsculas e pontuação final. Para outra pergunta, responde `Ainda não tenho uma resposta para essa pergunta.`

O FastAPI retorna HTTP 422 se faltar o campo, se ele estiver vazio ou se exceder o limite.

[Documentação do modelo ou componente](<https://reference.langchain.com/python/langchain-core/language_models/fake/FakeListLLM>)
