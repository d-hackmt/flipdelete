from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# # ————————————————————————————
# # Context rewrite prompt
# # ————————————————————————————
# CONTEXT_REWRITE_PROMPT = ChatPromptTemplate.from_messages(
#     [
#         ("system", """Given the chat history and user question, 
#                     rewrite it as a standalone question."""),
#         MessagesPlaceholder(variable_name="chat_history"),
#         ("human", "{input}"),
#     ]
# )

# ————————————————————————————
# QA prompt
# ————————————————————————————
QA_PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", """You're an e-commerce bot answering product-related queries 
                    based on reviews and titles.
                    
                    And To find the answers 
                    Use the provided context —

                    CONTEXT:
                    {context}

                    QUESTION: {input}
                    
                    if you do not know an 
                    answer politely say that 
                    i dont know the answer please 
                    contact our customer care +97 98652365.
                    
                    """),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)
