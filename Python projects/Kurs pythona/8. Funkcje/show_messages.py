def show_messages(messages):
    for message in messages:
        print(message)

def show_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ['zamknij system', 'zresetuj system', 'uruchom system']
sent_messages = []
show_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)