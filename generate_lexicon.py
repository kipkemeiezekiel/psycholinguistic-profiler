import pandas as pd

# Define the comprehensive master database schema matching your custom lexicon requirements
master_lexicon_data = {
    "Trait": [
        "Ego & Hubris", 
        "Docility & Passivity", 
        "Existential Detachment", 
        "Interpersonal Guardedness",
        "Gluttony & Excess",
        "Cognitive Deficit",
        "Malicious Hostility"
    ],
    "Keywords": [
        "i, me, my, myself, always, never, obviously, clearly, superior, boastful, proud",
        "whatever, sorry, apologize, agree, depend, submissive, yield, docile, simp",
        "nothing, perish, grave, void, meaningless, empty, futile, escapism, sloth",
        "toxic, suffer, betray, distance, laughed, enemies, shield, protect, jealous, gossip",
        "gluttony, excess, consumed, promiscuous, slut, hunger, addictive, indulgence",
        "imbecile, stupid, foolish, slow, ignorance, blind, confused, dense",
        "rude, thief, steal, malice, hateful, insult, attack, strike, spiteful"
    ],
    # Mapped mathematical Big Five weights (OCEAN Vectors)
    "O": [0.10, -0.20, 0.50, 0.00, -0.10, -0.40, -0.20],
    "C": [0.00, 0.10, -0.30, 0.20, -0.50, -0.30, -0.40],
    "E": [0.40, -0.40, -0.60, -0.50, 0.30, -0.20, 0.10],
    "A": [-0.60, 0.70, 0.00, -0.50, -0.20, -0.10, -0.70],
    "N": [-0.30, 0.40, 0.50, 0.60, 0.40, 0.30, 0.50]
}

# Compile data matrix directly using pandas dataframes
df = pd.DataFrame(master_lexicon_data)
output_path = "Universal_Human_Lexicon_Mega_Edition_v3.xlsx"

# Write file to local disk architecture
df.to_excel(output_path, index=False)
print(f"✅ Success! Master spreadsheet file generated locally at: {output_path}")
