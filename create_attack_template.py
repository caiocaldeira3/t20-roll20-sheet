import pyperclip as pyclip

from base import create_attack_template

print("Cole aqui o ID do ataque que irá criar o template:")
print("(Caso CTRL-V não cole o ID do ataque recomendo testar CTRL+SHIFT+V)")

attack_id = input()

recommended = create_attack_template(attack_id)

print(f"Template recomendado: {recommended}")

print("Caso todos os pacotes recomendados tenham sido baixados a macro recomendada já deve ter sido automáticamente copiada para o seu clipboard.")
print("Para salvar a macro basta apertar CTRL+V no espaço de macro desejado.")
pyclip.copy(recommended)
