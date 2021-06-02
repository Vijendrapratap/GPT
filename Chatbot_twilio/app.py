from chatbot import ask, append_interaction_to_chat_log
chat_log = None

while 1: 
	question = input("ASk Question to GPT3: ")
	answer = ask(question, chat_log) 
	chat_log = append_interaction_to_chat_log(question, answer, chat_log)
	print(answer)
	if question == "exit" or question == "stop":
		break

