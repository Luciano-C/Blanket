
def clean_message(message):
    message = message.clean_content
    message = message.casefold()

    symbols = [",", ".", "\"", "#", "$", "%", "&", "/", "(", ")", "?", "¿", "´", "!", "¡", "+", "-", "~", "*", "{", "}", "[", "]", ":", ";"]

    for symbol in symbols:
        message = message.replace(symbol, " ")


    message = message.strip()
    cleaned_message = " " + message + " "

    return cleaned_message

