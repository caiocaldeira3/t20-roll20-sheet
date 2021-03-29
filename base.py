import regex as re

from enum import Enum
from typing import Sequence, Union
from templates.templates import (
    attack_template_default, attack_template_orcandroll,
    ability_template, power_template, spell_template
)

class CriticalTypes(Enum):
    DAMAGE = 0
    DICE = 1

def repeat(rpt_type: str, rpt_id: str, rpt_attr: str) -> str:
    return f"@{{{rpt_type}_{rpt_id}_{rpt_attr}}}"

def describe(rpt_name: str, rpt_desc: str) -> str:
    return f"**{rpt_name}**: {rpt_desc}"

substitute_regex = r"@{(?!character_name)(.*?)}"
def sub_template(action_template: str, action_id: str) -> str:
    return re.sub(substitute_regex, action_template, "@{_{action_id}_)")

def padronize(
    rpt_type: str, rpt_id: str, rpt_attrs: Union[Sequence[str], str]
) -> list[str]:
    if not isinstance(rpt_attrs, Sequence):
        rpt_attrs = [rpt_attrs]
    elif isinstance(rpt_attrs, str):
        rpt_attrs = [rpt_attrs]

    results = [
        repeat(rpt_type, rpt_id, rpt_attr) for rpt_attr in rpt_attrs
    ]
    return results

def rpt_ability(ability_id: str, rpt_attrs: Union[Sequence[str], str]) -> list[str]:
    if not isinstance(rpt_attrs, Sequence):
        rpt_attrs = [rpt_attrs]
    elif isinstance(rpt_attrs, str):
        rpt_attrs = [rpt_attrs]

    ability_attrs = padronize(
        "repeating_abilities", ability_id, rpt_attrs
    )
    return ability_attrs

def rpt_power(power_id: str, rpt_attrs: Union[Sequence[str], str]) -> list[str]:
    if not isinstance(rpt_attrs, Sequence):
        rpt_attrs = [rpt_attrs]
    elif isinstance(rpt_attrs, str):
        rpt_attrs = [rpt_attrs]

    power_attrs = padronize(
        "repeating_powers", power_id, rpt_attrs
    )
    return power_attrs

def rpt_attack(attack_id: str, rpt_attrs: Union[Sequence[str], str]) -> list[str]:
    if not isinstance(rpt_attrs, Sequence):
        rpt_attrs = [rpt_attrs]
    elif isinstance(rpt_attrs, str):
        rpt_attrs = [rpt_attrs]

    attack_attrs = padronize(
        "repeating_attacks", attack_id, rpt_attrs
    )
    return attack_attrs

def rpt_spell(
    spell_id: str, spell_circle: str, rpt_attrs: Union[Sequence[str], str]
) -> list[str]:
    if not isinstance(rpt_attrs, Sequence):
        rpt_attrs = [rpt_attrs]
    elif isinstance(rpt_attrs, str):
        rpt_attrs = [rpt_attrs]

    spell_attrs = padronize(
        f"repeating_spells{spell_circle}", spell_id, rpt_attrs
    )
    return spell_attrs

def create_attack_template(
    attack_id: str, critical: CriticalTypes = CriticalTypes.DAMAGE
) -> str:
    return re.sub(
        r"@{(?!character_name)(.*?)}",
        lambda x: rpt_attack(attack_id, x.group(1))[0],
        attack_template_default
        if critical == CriticalTypes.DAMAGE
        else attack_template_orcandroll
    )

def create_ability_template(ability_id: str) -> str:
    return re.sub(
        r"@{(?!character_name)(.*?)}",
        lambda x: rpt_ability(ability_id, x.group(1))[0], ability_template
    )

def create_power_template(power_id: str) -> str:
    return re.sub(
        r"@{(?!character_name)(.*?)}",
        lambda x: rpt_power(power_id, x.group(1))[0], power_template
    )


def create_spell_template(spell_id: str, spell_circle: str) -> str:
    return re.sub(
        r"@{(?!character_name)(.*?)}",
        lambda x: rpt_spell(spell_id, spell_circle, x.group(1))[0], spell_template
    )
