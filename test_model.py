import spacy

nlp = spacy.load("ingredient_model")

text = "Marinate chicken with garlic powder, salt, pepper and lemon juice."

doc = nlp(text)

print([ent.text for ent in doc.ents if ent.label_ == "INGREDIENT"])
