import regex as re

def repeat(rpt_type: str, rpt_id: str, rpt_attr: str) -> str:
	return f"@{{{rpt_type}_{rpt_id}_{rpt_attr}}}"

def describe(rpt_name: str, rpt_desc: str) -> str:
	return f"**{rpt_name}**: {rpt_desc}"

