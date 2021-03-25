import pyperclip as pyclip

from base import repeat, describe

print("Cole aqui o ID do poder que você quer repetir:")
print("(Caso CTRL-V não cole o ID do poder recomendo testar CTRL+SHIFT+V)")

power_id = input()

power_name = repeat("repeating_powers", power_id, "namepower")
power_description = repeat("repeating_powers", power_id, "powerdescription")

recommended = describe(power_name, power_description)

print(f"Macro para o nome da poder: {power_name}")
print(f"Macro para o nome da poder: {power_description}")

print(f"Macro recomendada: {recommended}")

print("Caso todos os pacotes recomendados tenham sido baixados a macro recomendada já deve ter sido automáticamente copiada para o seu clipboard.")
print("Para salvar a macro basta apertar CTRL+V no espaço de macro desejado.")
pyclip.copy(recommended)
