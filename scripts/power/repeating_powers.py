import sys
import pyperclip as pyclip

from pathlib import Path

base_path = Path(__file__).resolve().parent
sys.path.append(str(base_path.parent.parent))

import base

print("Cole aqui o ID do poder que você quer repetir:")
print("(Caso CTRL-V não cole o ID do poder recomendo testar CTRL+SHIFT+V)")

power_id = input()

power_name, power_description = base.rpt_power(
    power_id, ["namepower", "powerdescription"]
)
recommended = base.describe(power_name, power_description)

print(f"Macro para o nome da poder: {power_name}")
print(f"Macro para o nome da poder: {power_description}")

print(f"Macro recomendada: {recommended}")

print(
    "Caso todos os pacotes recomendados tenham sido baixados a macro recomendada",
    "já deve ter sido automáticamente copiada para o seu clipboard."
)
print("Para salvar a macro basta apertar CTRL+V no espaço de macro desejado.")
pyclip.copy(recommended)
