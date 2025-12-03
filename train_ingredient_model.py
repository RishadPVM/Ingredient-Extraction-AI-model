import spacy
from spacy.training.example import Example
from ingredient_training_data import TRAINING_DATA

# Load English base model
nlp = spacy.load("en_core_web_sm")

# Add new NER label
ner = nlp.get_pipe("ner")
ner.add_label("INGREDIENT")

# Disable other pipes during training
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.initialize()
    for epoch in range(30):        # Train for 30 iterations
        losses = {}
        for text, annotations in TRAINING_DATA:
            example = Example.from_dict(nlp.make_doc(text), annotations)
            nlp.update([example], sgd=optimizer, losses=losses)
        print(f"Epoch {epoch+1} Losses: {losses}")

# Save the trained model
nlp.to_disk("ingredient_model")
print("Model training complete! Saved to ingredient_model/")
