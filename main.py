from fastapi import FastAPI
from langchain_core.language_models.fake import FakeListLLM
from pydantic import BaseModel, ConfigDict, Field


app = FastAPI(title="Chatbot com Fake LLM")
REPLIES = {
    "olá": "Olá! Como posso ajudar?",
    "qual é o seu nome": "Sou um chatbot de demonstração.",
    "qual é a capital do brasil": "A capital do Brasil é Brasília.",
}
DEFAULT_REPLY = "Ainda não tenho uma resposta para essa pergunta."


class ChatInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    message: str = Field(min_length=1, max_length=1000)


class ChatOutput(BaseModel):
    reply: str


@app.post("/chat", response_model=ChatOutput)
def chat(body: ChatInput):
    question = " ".join(body.message.casefold().rstrip("?! .").split())
    reply = REPLIES.get(question, DEFAULT_REPLY)
    model = FakeListLLM(responses=[reply])
    return {"reply": model.invoke(body.message)}
