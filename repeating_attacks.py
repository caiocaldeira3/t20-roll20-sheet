import pyperclip as pyclip

from base import repeat, describe

print("Cole aqui o ID do ataque que você quer repetir:")
print("(Caso CTRL-V não cole o ID do poder recomendo testar CTRL+SHIFT+V)")

attack_id = input()

attack_name = repeat("repeating_attacks", attack_id, "nomeataque")
attack_description = repeat("repeating_attacks", attack_id, "ataquedescricao")

recommended = describe(attack_name, attack_description)

print(f"Macro para o nome do ataque: {attack_name}")
print(f"Macro para o nome do ataque: {attack_description}")

print(f"Macro recomendada: {recommended}")

print("Caso todos os pacotes recomendados tenham sido baixados a macro recomendada já deve ter sido automáticamente copiada para o seu clipboard.")
print("Para salvar a macro basta apertar CTRL+V no espaço de macro desejado.")
pyclip.copy(recommended)
