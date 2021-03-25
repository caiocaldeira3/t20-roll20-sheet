import pyperclip as pyclip

from base import repeat, describe

print("Cole aqui o ID da abilidade que você quer repetir:")
print("(Caso CTRL-V não cole o ID da abilidade recomendo testar CTRL+SHIFT+V)")

ability_id = input()

ability_name = repeat("repeating_abilities", ability_id, "nameability")
ability_description = repeat("repeating_abilities", ability_id, "abilitydescription")

recommended = describe(ability_name, ability_description)

print(f"Macro para o nome da abilidade: {ability_name}")
print(f"Macro para o nome da abilidade: {ability_description}")

print(f"Macro recomendada: {recommended}")

print("Caso todos os pacotes recomendados tenham sido baixados a macro recomendada já deve ter sido automáticamente copiada para o seu clipboard.")
print("Para salvar a macro basta apertar CTRL+V no espaço de macro desejado.")
pyclip.copy(recommended)
