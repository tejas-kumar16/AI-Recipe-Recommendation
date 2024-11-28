# AI-Recipe-Recommendation

This is an AIOT project, using computer vision.
You get recipe recommendations by simply uplaoding images of vegetables available in your fridge. 
You choose teh portion and spice levels and you get your recipe with instructions.

## How it works?

Step 1: We trained a YOLO model to detect vegetables in an image.
Step 2: We save the detected vegetables in a list.
step 3: Using ChatGPT API Key, we send the available vegetables.
Step 4: The recommended recipes and shown.
