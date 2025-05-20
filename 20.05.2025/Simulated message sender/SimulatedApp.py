def is_valid_email(email):
    if "@" not in email:
        return False

    username, separator, domain = email.partition("@")

    if not username or not domain:
        return False
    if "." not in domain:
        return False

    return True

def send_message(email, message):
    if not is_valid_email(email):
        return "Невалиден адрес."

    print(f"Изпращане до: {email}")
    print(f"Съобщение: {message}")

    return "Съобщението беше успешно изпратено."

email = "zdravkoanev@abv.bg"
message = "Готово"
print(send_message(email, message))
