import sys
import pyperclip as pyclip

from pathlib import Path

base_path = Path(__file__).resolve().parent
sys.path.append(str(base_path.parent.parent))

import base

print("Cole aqui o ID da magia que irá criar o template:")
print("(Caso CTRL-V não cole o ID da magia recomendo testar CTRL+SHIFT+V)")

spell_id = input()

print("Explicite o círculo da magia (default=1): ", end="")
spell_circle = input()
spell_circle = "1" if spell_circle == "" else spell_circle

recommended = base.create_spell_template(spell_id, spell_circle)

print(f"Macro recomendada: {recommended}")

print(
    "Caso todos os pacotes recomendados tenham sido baixados a macro recomendada",
    "já deve ter sido automáticamente copiada para o seu clipboard."
)
print("Para salvar a macro basta apertar CTRL+V no espaço de macro desejado.")
pyclip.copy(recommended)
