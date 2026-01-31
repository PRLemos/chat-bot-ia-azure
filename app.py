import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import AzureOpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import RetrievalQA

# ======================
# CONFIGURAÇÕES AZURE
# ======================
os.environ["AZURE_OPENAI_ENDPOINT"] = "SEU_ENDPOINT"
os.environ["AZURE_OPENAI_API_KEY"] = "SUA_API_KEY"
os.environ["AZURE_OPENAI_API_VERSION"] = "2024-02-01"

# ======================
# CARREGAR PDFs
# ======================
docs = []
pdf_folder = "pdfs"

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(pdf_folder, file))
        docs.extend(loader.load())

# ======================
# QUEBRAR TEXTO
# ======================
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

documents = text_splitter.split_documents(docs)

# ======================
# EMBEDDINGS + BASE VETORIAL
# ======================
embeddings = AzureOpenAIEmbeddings(
    deployment="text-embedding-3-large"
)

vectorstore = FAISS.from_documents(documents, embeddings)

# ======================
# MODELO DE CHAT
# ======================
llm = AzureChatOpenAI(
    deployment_name="gpt-4o-mini",
    temperature=0
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True
)

# ======================
# CHAT INTERATIVO
# ======================
print("🤖 Chatbot acadêmico iniciado! Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        break

    resposta = qa(pergunta)
    print("\n🤖 Resposta:")
    print(resposta["result"])
    print("-" * 50)

