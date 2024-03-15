import streamlit as st
import pandas as pd
import numpy as np
st.title('3d Modeling Idea Generator')
st.write("Want to 3d model something but need some inspiration? You've come to the right place! Click the button below, and get a randomly generated idea! If you don't like your first one, just try again!")

import random
import string
adjectives = ['poopy', 'stinky', 'big', 'red', 'orange', 'yellow', 'green',
              'blue', 'purple', 'pink', 'black', 'white', 'gray', 'brown',
              'colorful', 'rainbow', 'woven', 'wooden', 'musical', 'old',
              'snowy', 'soft', 'hard', 'monochromatic', 'fast', 'slow',
              'shiny', 'dull', 'neon', 'reflective', 'supersonic',
              'hypersonic', 'explosive', 'flaming', 'big', 'small',
              'tiny', 'microscopic', 'huge', 'leather', 'felt', 'silky',
              'pixelated', 'rough', 'leathery', 'metallic', 'futuristic', 'steampunk',
              'high-tech', 'reinforced', 'low poly']

nouns = ['computer', 'mouse', 'mug', 'placemat', 'coaster', 'glass', 'spork',
         'bottle', 'faucet', 'book', 'box', 'oven', 'spoon' , 'violin', 'piano',
         'stand mixer', 'measuring cup', 'measuring spoon', 'rock', 'axe', 'pan',
         'kettle', 'plate', 'chair', 'table', 'pillow', 'handle', 'container',
         'pot', 'vase', 'shoe', 'banana', 'speaker', 'keycap', 'shelf', 'bowl',
         'knob', 'hook', 'bus', 'car', 'truck', 'mailbox', 'flag', 'house', 'sign', 'jeep',
         'tank(container or war machine)', 'bush', 'tree', 'plant', 'lightbulb', 'birdfeeder',
         'wheel', 'pillow', 'couch', 'donut', 'burrito', 'taco', 'chair', 'lamppost', 'backpack',
         'purse', 'trash can', 'heater', 'pool', 'neon sign', 'viola', 'cello', 'bass', 'speaker',
         'acoustic guitar', 'electric guitar', 'drum' ,'drum set', 'bulldozer', 'tractor', 'wheel',
         'tire', 'dumpster', 'generator', 'ladder', 'van', 'dog', 'cat', 'phone', 'watch', 'bird']

space = ' '

response = st.button('Generate')
if response == True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    idea = adjective + space + noun
    st.write('Your 3d modeling idea is: %s' %idea)
