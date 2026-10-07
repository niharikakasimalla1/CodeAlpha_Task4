# CodeAlpha Python Programming Internship
# Task 4 - Basic Chatbot

# Chatbot start message
print("================================")
print("       BASIC CHATBOT")
print("================================")

print("Hello! I am a simple chatbot.")
print("You can say: hello, how are you, or bye.")


# Function for chatbot responses
def chatbot_response(user_message):

    # Check if the user says hello
    if user_message == "hello":
        return "Hi! Nice to meet you."

    # Check if the user asks how are you
    elif user_message == "how are you":
        return "I'm fine, thanks!"

    # Check if the user says bye
    elif user_message == "bye":
        return "Goodbye!"

    # If the chatbot does not understand
    else:
        return "Sorry, I don't understand that."


# Keep the conversation running
while True:

    # Ask the user for a message
    user_message = input("\nYou: ")

    # Convert the message to lowercase
    user_message = user_message.lower()

    # Get the chatbot's response
    response = chatbot_response(user_message)

    # Display the chatbot's response
    print("Bot:", response)

    # Stop the chatbot when the user says bye
    if user_message == "bye":
        break


# Final message
print("Chatbot session ended.")