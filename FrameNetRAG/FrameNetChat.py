from langflow.load import run_flow_from_json

#allows for command line user input
question = input("Enter your question: ")

#generates a response using the Langflow model and the user input
result = run_flow_from_json(flow="FrameNetChatFinal.json",
                            input_value=question)

#outputs the response
print(result[0].outputs[0].results)
