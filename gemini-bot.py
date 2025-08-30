import google.generativeai as genai
API_KEY = "AIzaSyCWWXnP7by6B03Z3iSbJo7jtkqz5Yts07w"
genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat()

print("Welcome to the Gemini Chatbot! Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("Gemini: " + response.txt)



