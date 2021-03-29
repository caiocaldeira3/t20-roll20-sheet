attack_template_default = (
    "&{template:t20-attack}{{character=@{character_name}}}{{attackname="
    "@{nomeataque}}}{{attackroll=[[1d20cs>@{margemcriticoataque}+"
    "[[@{ataquepericia}]]+@{bonusataque}]]}} {{damageroll=[[@{danoataque}+"
    "@{modatributodano}+@{danoextraataque}]]}} {{criticaldamageroll="
    "[[@{danoataque}*@{multiplicadorcriticoataque}"  # DAMAGE MULTIPLIER CRITICAL
    "+@{modatributodano}+@{danoextraataque}]]}}"
    "{{typeofdamage=@{ataquetipodedano}}}{{description=@{ataquedescricao}}}"
)

attack_template_orcandroll = (
    "&{template:t20-attack}{{character=@{character_name}}}{{attackname="
    "@{nomeataque}}}{{attackroll=[[1d20cs>@{margemcriticoataque}+"
    "[[@{ataquepericia}]]+@{bonusataque}]]}} {{damageroll=[[@{danoataque}+"
    "@{modatributodano}+@{danoextraataque}]]}} {{criticaldamageroll="
    "[[@{danocriticoataque}"  # ORC AND ROLL CRITICAL
    "+@{modatributodano}+@{danoextraataque}]]}}"
    "{{typeofdamage=@{ataquetipodedano}}}{{description=@{ataquedescricao}}}"
)

ability_template = (
    "&{template:t20-info}{{infoname=@{nameability}}}{{description="
    "@{abilitydescription}}}"
)

power_template = (
    "&{template:t20-info}{{infoname=@{namepower}}}"
    "{{description=@{powerdescription}}}"
)

spell_template = (
    "&{template:spell}{{character=@{character_name}}}{{spellname="
    "@{namespell}}}{{type=@{spelltipo}}}{{execution=@{spellexecucao}}}{{duration="
    "@{spellduracao}}}{{range=@{spellalcance}}}{{targetarea=@{spellalvoarea}}}"
    "{{resistance=@{spellresistencia}}}{{description=@{spelldescription}}}{{cd="
    "@{spellcd}}}"
)
