import pyperclip as pyclip

from base import describe, rpt_ability

print("Cole aqui o ID da habilidade que você quer repetir:")
print("(Caso CTRL-V não cole o ID da habilidade recomendo testar CTRL+SHIFT+V)")

ability_id = input()

ability_name, ability_description = rpt_ability(ability_id, ["nameability", "abilitydescription"])

recommended = describe(ability_name, ability_description)

print(f"Macro para o nome da habilidade: {ability_name}")
print(f"Macro para o nome da habilidade: {ability_description}")

print(f"Macro recomendada: {recommended}")

print("Caso todos os pacotes recomendados tenham sido baixados a macro recomendada já deve ter sido automáticamente copiada para o seu clipboard.")
print("Para salvar a macro basta apertar CTRL+V no espaço de macro desejado.")
pyclip.copy(recommended)
