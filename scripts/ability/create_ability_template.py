import sys
import pyperclip as pyclip

from pathlib import Path

base_path = Path(__file__).resolve().parent
sys.path.append(str(base_path.parent.parent))

import base
print("Cole aqui o ID da habilidade que irá criar o template:")
print("(Caso CTRL-V não cole o ID da habilidade recomendo testar CTRL+SHIFT+V)")

ability_id = input()

recommended = base.create_ability_template(ability_id)

print(f"Macro recomendada: {recommended}")

print(
    "Caso todos os pacotes recomendados tenham sido baixados a macro recomendada",
    "já deve ter sido automáticamente copiada para o seu clipboard."
)
print("Para salvar a macro basta apertar CTRL+V no espaço de macro desejado.")
pyclip.copy(recommended)
