This repository contains code for an RAG application with access to information from FrameNet version 1.7. ChatGPT-3.5-turbo is used as an LLM, and AstraDB is used as a vector store. Information for each frame is stored as an individual embedding and includes the definition, core FEs and their definitions, lexical units, and frame relations.
Steps for implentation and use are as follows:
1. Download the two files in the FrameNetRAG folder
2. Install Langflow (preferably in a virtual environment) using the command: python -m pip install langflow --pre --force-reinstall
3. In the FrameNetChatFinal JSON document, input an OpenAI secret key where the file indicates with keyword "KEYHERE". The key will need to be entered in three places, which can be located easily using find and replace with the keyword.
4. Run the FrameNetChat Python file.
5. When prompted by the program, input your question into the terminal.
