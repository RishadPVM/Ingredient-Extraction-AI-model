import random
import json

ingredients = [
    "turmeric","red chili powder","cumin","coriander powder","garam masala","kashmiri chili",
"black pepper","white pepper","fennel seeds","mustard seeds","nigella seeds",
"fenugreek seeds","carom seeds","bay leaf","cloves","cardamom","black cardamom",
"cinnamon","star anise","mace","nutmeg","asafoetida","dry mango powder","chaat masala",
"sambar powder","rasam powder","tandoori masala","chicken masala","fish masala",
"pav bhaji masala","biryani masala","peri peri","paprika","smoked paprika",
"cayenne pepper","oregano","basil","thyme","rosemary","tarragon","parsley",
"mint","dried mint","dill","sage","chili flakes","onion powder","garlic powder",
"ginger powder","curry powder","kitchen king masala","schezwan pepper","five spice powder",
"herbes de provence","za'atar","sumac","harissa spice","berbere spice","allspice",
"mustard powder","cajun seasoning","italian seasoning","lemon pepper","celery salt",
"kosher salt","sea salt","pink salt","smoked salt","cocoa powder","cinnamon sugar",
"vanilla powder","brown mustard seeds","yellow mustard seeds","turmeric leaves",
"green cardamom","black sesame seeds","white sesame seeds","poppy seeds",
"turmeric paste","ginger paste","garlic paste","coriander seeds","fennel powder",
"fenugreek powder","nutritional yeast","jalapeño powder","chipotle powder",
"peri peri seasoning","taco seasoning","ranch seasoning","wasabi powder",
"ginger garlic paste","himalayan pink salt"


"onion","tomato","potato","green chili","carrot","beans","capsicum","cauliflower",
"broccoli","spinach","cabbage","peas","sweet corn","beetroot","raddish","okra",
"eggplant","bitter gourd","bottle gourd","ridge gourd","snake gourd","drumstick",
"pumpkin","zucchini","lettuce","spring onion","leeks","artichoke","celery",
"mushroom","garlic","ginger","shallots","yam","taro root","sweet potato","cucumber",
"raw banana","raw mango","avocado","jalapeno","red bell pepper","yellow bell pepper",
"green bell pepper","asparagus","kale","mint leaves","coriander leaves","parsley",
"methi leaves","curry leaves","coconut","green peas","snow peas","baby corn",
"turnip","lotus stem","spinach puree","tomato puree","ginger slices",
"garlic cloves","ginger julienne"


"chicken","chicken breast","chicken thighs","mutton","beef","pork","lamb",
"turkey","duck","fish","salmon","tuna","prawns","shrimp","crab","squid",
"octopus","anchovies","sardines","egg","egg white","egg yolk","quail eggs",
"fish fillet","fish curry cut","king fish","pomfret","seer fish","tilapia",
"catfish","beef mince","chicken mince","liver","kidney","mutton curry cut",
"bone broth","chicken stock"


"milk","curd","yogurt","buttermilk","paneer","cheese","cheddar cheese",
"mozzarella","parmesan","butter","ghee","cream","fresh cream","malai",
"milk powder","condensed milk","evaporated milk","sour cream","whipping cream",
"cream cheese","khoa","ricotta","yogurt whey","butter milk","chocolate milk",
"milkmaid","ice cream","unsalted butter","salted butter","skimmed milk",
"full fat milk","buffalo milk"


"rice","basmati rice","brown rice","idli rice","parboiled rice","wheat flour",
"maida","corn flour","rice flour","rava","semolina","oats","quinoa","barley",
"millet","foxtail millet","finger millet","sago","poha","vermicelli","noodles",
"pasta","macaroni","spaghetti","lentils","moong dal","toor dal","urad dal",
"masoor dal","chana dal","black chana","white chana","rajma","kidney beans",
"black beans","soybeans","millet flour","gram flour","besan","cornmeal",
"couscous","wheat berries","idiyappam flour"


"olive oil","vegetable oil","sunflower oil","mustard oil","sesame oil","coconut oil",
"ghee","butter","soy sauce","vinegar","apple cider vinegar","white vinegar",
"balsamic vinegar","chili sauce","tomato ketchup","mustard sauce","barbecue sauce",
"oyster sauce","fish sauce","peri peri sauce","hot sauce","chili garlic sauce",
"schezwan sauce","mayonnaise","ranch","tahini","honey","maple syrup","molasses",
"peanut butter","jam","pesto","harissa paste","green chutney","mint chutney",
"tamarind paste","soy paste","ginger garlic paste","sesame paste"


"bread","bun","tortilla","naan","chapati","idli","dosa batter","pizza dough",
"burger bun","cake flour","baking soda","baking powder","yeast","cocoa powder",
"chocolate chips","brown sugar","white sugar","castor sugar","icing sugar",
"corn syrup","gluten","vanilla essence","almond essence","food color"


"almonds","cashews","raisins","walnuts","pistachios","hazelnuts","dates",
"prunes","apricots","pine nuts","chia seeds","pumpkin seeds","hemp seeds",
"sunflower seeds","flax seeds","sesame seeds","melon seeds","nut mix","peanut",
"roasted peanuts","roasted chana dal","dry coconut","figs"


"gelatin","agar agar","cornstarch","tapioca starch","rice vinegar","mirin",
"jaggery","brown sugar","rock salt","tamarind","coconut cream",
"lemongrass","galangal","tofu","tempeh","miso","nori sheets","kimchi",
"pickles","caper","olives","jalapenos","mustard greens","beef broth",
"chicken broth","vegetable broth","wine vinegar","white wine","red wine",
"rose water","kewra water","saffron","edible silver leaf","edible gold leaf"

]

templates = [
    "Add {i1}, {i2}, and {i3} to the bowl.",
    "Mix {i1}, {i2}, {i3}, and {i4}.",
    "Use {i1} with {i2} and {i3}.",
    "Combine {i1}, {i2}, {i3}, {i4}, and {i5}.",
]

# def generate_sentence():
#     template = random.choice(templates)
#     picks = random.sample(ingredients, template.count("{"))
#     text = template.format(**{f"i{k+1}":v for k,v in enumerate(picks)})

#     entities=[]
#     for ing in picks:
#         start = text.lower().find(ing.lower())
#         end = start + len(ing)
#         entities.append((start,end,"INGREDIENT"))

#     return (text, {"entities": entities})

# dataset = [generate_sentence() for _ in range(2000)]

# print(dataset)



def generate_dataset(count=1000):
    dataset = {"annotations": []}

    for _ in range(count):
        i1, i2, i3 = random.sample(ingredients, 3)
        template = random.choice(templates)

        sentence = template.format(i1=i1, i2=i2, i3=i3)

        # Find entity positions
        entities = []
        for ing in [i1, i2, i3]:
            start = sentence.lower().index(ing)
            end = start + len(ing)
            entities.append([start, end, "INGREDIENT"])

        dataset["annotations"].append({
            "text": sentence,
            "entities": entities
        })

    return dataset

data = generate_dataset(2000)

with open("ingredients_dataset.json", "w") as f:
    json.dump(data, f, indent=4)

print("Dataset created successfully!")
