spells = {"Alohomora": "Unlocks doors", "Expecto Patronum": "Repels Dementors", "Leviosa": "Makes objects float"}
spell = "Expecto Patronum"
print(f'The spell "{spell}" is used for: {spells.get(spell, "Spell not found!")}')