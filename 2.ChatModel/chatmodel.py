from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash', credentials_path="path/to/your/credentials.json")

prompt=input("Ask Your Question:")

result=llm.invoke(prompt)

print(result.content)

