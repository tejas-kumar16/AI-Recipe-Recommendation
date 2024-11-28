AI-Recipe-Recommendation 🍽️
AI-Recipe-Recommendation is an AIoT (Artificial Intelligence of Things) project that leverages computer vision to recommend recipes based on the vegetables available in your fridge. Simply upload an image of the vegetables, select portion size and spice levels, and receive personalized recipes with step-by-step instructions.

🔧 How It Works
1. Vegetable Detection 🥦🍅
We trained a custom YOLO (You Only Look Once) model to detect and identify various vegetables from an uploaded image.

2. Data Processing 📋
The detected vegetables are saved in a list, representing the ingredients available.

3. AI-Powered Recipe Recommendation 🤖
The list of detected vegetables is sent to the ChatGPT API, which generates recipe recommendations based on the available ingredients.

4. Personalized Recipe Output 🍴
The user selects the desired portion size and spice level, and the system provides a tailored recipe with easy-to-follow cooking instructions.

🚀 Features
Real-time Vegetable Detection: Upload images directly from your fridge.
Personalized Recipes: Customize portion size and spice preferences.
Seamless Integration: Combines YOLO for object detection with the power of AI-driven recipe generation.

📦 Technologies Used
YOLOv5: For object detection and vegetable recognition.
ChatGPT API: For dynamic recipe generation based on detected ingredients.

💡 How to Use
Upload an Image: Take a photo of the vegetables in your fridge and upload it.
Customize: Select your desired portion size and spice level.
Receive Recipes: Get a personalized recipe with detailed cooking instructions.
