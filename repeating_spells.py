import pyperclip as pyclip

from base import repeat, describe

print("Cole aqui o ID da magia que você quer repetir:")
print("(Caso CTRL-V não cole o ID da magia recomendo testar CTRL+SHIFT+V)")

spell_id = input()

print("Explicite o círculo da magia (default=1): ", end="")
spell_circle = input()
spell_circle = "1" if spell_circle == "" else spell_circle

spell_name = repeat(f"repeating_spells{spell_circle}", spell_id, "namespell")
spell_description = repeat(f"repeating_spells{spell_circle}", spell_id, "spelldescription")

recommended = describe(spell_name, spell_description)

print(f"Macro para o nome da magia: {spell_name}")
print(f"Macro para o nome da magia: {spell_description}")

print(f"Macro recomendada: {recommended}")

print("Caso todos os pacotes recomendados tenham sido baixados a macro recomendada já deve ter sido automáticamente copiada para o seu clipboard.")
print("Para salvar a macro basta apertar CTRL+V no espaço de macro desejado.")
pyclip.copy(recommended)
