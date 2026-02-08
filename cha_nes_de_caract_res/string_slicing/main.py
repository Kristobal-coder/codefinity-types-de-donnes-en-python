full_name = "  Ada Lovelace  "
sentence = "The (quick) brown-fox jumps over 13 lazy dogs!"
email = "  Support@Example.COM \n"
SEP = " | "

# 1) supprimer les espaces superflus de `full_name`.
name_clean = full_name.strip()

# 2) vérifier si `"quick"` apparaît dans `sentence` (insensible à la casse).
has_quick = "quick" in sentence.lower()

# 3) extraire le texte entre parenthèses `(` et `)`.
start = sentence.find("(")
end = sentence.find(")")
inside_parens = sentence[start+1:end]

# 4) compter le nombre de lettres `'o'` dans `sentence` (insensible à la casse).
o_count = sentence.lower().count("o")

# 5) à partir de `email`, prendre tout ce qui suit `@` (après avoir supprimé les espaces et mis en minuscules).
email_clean = email.strip().lower()
at_pos = email_clean.find("@")
domain = email_clean[at_pos+1:]

# 6) construire `"Name | Domain | Count"` en utilisant un f-string et `SEP`.
report = f"{name_clean}{SEP}{domain}{SEP}{o_count}"

print(name_clean, has_quick, inside_parens, o_count, domain)
print(report)