import sys
import pyperclip as pyclip

from pathlib import Path

base_path = Path(__file__).resolve().parent
sys.path.append(str(base_path.parent.parent))

import base

print("Cole aqui o ID da magia que você quer repetir:")
print("(Caso CTRL-V não cole o ID da magia recomendo testar CTRL+SHIFT+V)")

spell_id = input()

print("Explicite o círculo da magia (default=1): ", end="")
spell_circle = input()
spell_circle = "1" if spell_circle == "" else spell_circle

spell_name, spell_description = base.rpt_spell(
    spell_id, spell_circle, ["namespell", "spelldescription"]
)
recommended = base.describe(spell_name, spell_description)

print(f"Macro para o nome da magia: {spell_name}")
print(f"Macro para o nome da magia: {spell_description}")

print(f"Macro recomendada: {recommended}")

print(
    "Caso todos os pacotes recomendados tenham sido baixados a macro recomendada",
    "já deve ter sido automáticamente copiada para o seu clipboard."
)
print("Para salvar a macro basta apertar CTRL+V no espaço de macro desejado.")
pyclip.copy(recommended)
