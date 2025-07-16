# Vulnérabilité d'injection SQL
user_input = input('Nom: ')
query = f"SELECT * FROM users WHERE name = '{user_input}'"
# FIXME: pas d'échappement, vulnérable à l'injection 