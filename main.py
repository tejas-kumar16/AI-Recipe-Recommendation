import openai
import streamlit as st
from ultralytics import YOLO
from PIL import Image

# Set up OpenAI API key
openai.api_key = "API_KEY"

# Function to interact with ChatGPT
def chat_with_gpt(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message['content']
    except Exception as e:
        st.error("Error connecting to OpenAI API.")
        return None

# Function to recommend recipes
def recommend_recipes(vegetables):
    prompt = f"Recommend me three different Indian recipes with these vegetables: {', '.join(vegetables)}. Give a brief description for each."
    messages = [{"role": "user", "content": prompt}]
    response = chat_with_gpt(messages)
    recipes = response.split("\n\n")  # Adjust based on response formatting
    return recipes[:3]  # Return first three recipes

# Function to provide ingredients and instructions based on user preferences
def provide_recipe_instructions(recipe_choice, portion_size, spice_level):
    prompt = (f"Give me the ingredients and cooking instructions for '{recipe_choice}'. "
              f"It should be for {portion_size} people and the spice level should be {spice_level}.")
    messages = [{"role": "user", "content": prompt}]
    return chat_with_gpt(messages)

# Model Prediction Function
def model_prediction(image):
    try:
        model = YOLO('trained_yolov8x_model (1).pt')
        results = model(image)
        predicted_classes = [model.names[int(box.cls)] for box in results[0].boxes]
        return predicted_classes
    except Exception as e:
        st.error("Error loading the model or processing the image.")
        return []


# List of predefined recipes without images
predefined_recipes = [
    {
        "name": "Traditional Chicken Curry",
        "description": "A delicious Indian dish with rich spices and flavors.",
        "image_url": "C:/Users/ASUS/Desktop/AIOT PROJECT/basic/chicken.jpg"
    },
    {
        "name": "Shahi Paneer",
        "description": "A savory, traditional Indian recipe enjoyed by many.",
        "image_url": "C:/Users/ASUS/Desktop/AIOT PROJECT/basic/shahi.jpg"
    },
    {
        "name": "Dum Aloo",
        "description": "A spicy, mouthwatering treat to satisfy your cravings.",
        "image_url": "C:/Users/ASUS/Desktop/AIOT PROJECT/basic/dum.jpg"
    },
    {
        "name": "Aloo ke Parathe",
        "description": "A light and flavorful dish, perfect for a quick meal.",
        "image_url": "C:/Users/ASUS/Desktop/AIOT PROJECT/basic/aloo_parathe.jpg"
    },
    {
        "name": "Okra curry",
        "description": "A hearty, comforting Indian classic.",
        "image_url": "C:/Users/ASUS/Desktop/AIOT PROJECT/basic/okra.jpg"
    },
    {
        "name": "Egg Curry",
        "description": "An aromatic dish with a delightful mix of spices.",
        "image_url": "C:/Users/ASUS/Desktop/AIOT PROJECT/basic/egg_curry.jpg"
    },
    {
        "name": "Chicken Biryani",
        "description": "A fusion of spices and flavors in every bite.",
        "image_url": "C:/Users/ASUS/Desktop/AIOT PROJECT/basic/chicken_biryani.jpg"
    },
    {
        "name": "Veg Pulao",
        "description": "A vibrant and fresh dish to uplift your mood.",
        "image_url": "C:/Users/ASUS/Desktop/AIOT PROJECT/basic/veg_pulao.jpg"
    }
]

# Streamlit UI
def main():
    # Set page title and layout
    st.set_page_config(page_title="Indian Recipe AI Assistant", layout="centered", initial_sidebar_state="expanded")


    st.markdown("""
        <style>
        
        /* Sidebar title */
        .sidebar-title {
            font-size: 22px;
            font-weight: bold;
            color: #FFA500;
            margin-bottom: 15px;
            text-align: center;
            position: relative; /* Position relative to be on top of overlay */
            z-index: 1;
        }
        /* Navigation options styling */
        .stRadio > label {
            font-size: 18px;
            font-weight: 500;
            color: #FFFFFF;  /* White color for better readability */
            padding: 5px;
            border-radius: 4px;
            position: relative;
            z-index: 1; /* Ensures text is above overlay */
        }
        .stRadio > label:hover {
            color: #FFA500;
        }
        </style>
        """, unsafe_allow_html=True)
    st.sidebar.markdown("<div class='sidebar-title'>🍲 How can we help you today? </div>", unsafe_allow_html=True)
    page = st.sidebar.radio(" ", ["AI Recipe Recommendation", "Predefined Recipe Selection","Get Instructions for a Dish"])
    # Page Title
    if page == "AI Recipe Recommendation":
        st.markdown("<h1 style='text-align: center; color: #FFA500;'>🍲 Recipe AI Assistant 🍲</h1>", unsafe_allow_html=True)
        st.subheader("Upload an Image of Vegetables")

        # Step 1: Image upload and vegetable detection
        uploaded_file = st.file_uploader("Upload an image of vegetables", type=["png", "jpg", "jpeg"])
        
        if uploaded_file:
            image = Image.open(uploaded_file)
            # Run vegetable detection (placeholder list)
            vegetable_list = model_prediction(image)

            # Recipe recommendation
            if "recipe_options" not in st.session_state:
                st.session_state.recipe_options = recommend_recipes(vegetable_list)

            recipe_options = st.session_state.recipe_options
            st.markdown("<h3>Choose a Recipe:</h3>", unsafe_allow_html=True)
            selected_recipe = st.radio("Select one recipe:", options=recipe_options)

            # Customization options
            with st.form("preferences_form"):
                portion_size = st.number_input("How many people?", min_value=1, step=1)
                spice_level = st.selectbox("Spice level", ["mild", "medium", "hot"])
                submit_button = st.form_submit_button(label="Get Ingredients and Instructions")

            if submit_button:
                recipe_instructions = provide_recipe_instructions(selected_recipe, portion_size, spice_level)
                if recipe_instructions:
                    st.markdown("<h3>Ingredients and Instructions:</h3>", unsafe_allow_html=True)
                    st.write(recipe_instructions)

    # Page 2: Predefined Recipe Selection
    elif page == "Predefined Recipe Selection":
        # CSS for consistent image size and padding between items
        st.markdown("""
            <style>
            .recipe-container {
                padding: 15px;                /* Padding around each recipe box */
                background-color: #f9f9f9;    /* Light background color */
                border-radius: 8px;           /* Rounded corners */
                text-align: center;           /* Center-align text */
                margin: 10px;                 /* Space between each recipe container */
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Add shadow for depth */
            }
            .recipe-container img {
                width: 100%;                  /* Full width within container */
                height: 150px;                /* Fixed height */
                object-fit: cover;            /* Crop and fit image */
                border-radius: 8px;           /* Rounded corners for images */
            }
            </style>
            """, unsafe_allow_html=True)
        
        # Display recipes in a 4x2 grid with padding
        st.markdown("<h1 style='text-align: center; color: #FFA500;'>🍲 Browse Our Recipes 🍲</h1>", unsafe_allow_html=True)
        st.markdown("### Click on any recipe to get the full instructions!")
        
        # Arrange recipes in a grid with padding
        for i in range(0, len(predefined_recipes), 4):
            cols = st.columns(4)  # Create four columns in each row
            for j, col in enumerate(cols):
                if i + j < len(predefined_recipes):
                    recipe = predefined_recipes[i + j]
                    with col:
                        # Apply CSS class for container
                        st.markdown("<div class='recipe-container'>", unsafe_allow_html=True)
                        st.image(recipe["image_url"], use_column_width=True)  # Use CSS-controlled dimensions
                        st.markdown(f"**{recipe['name']}** - {recipe['description']}")
                        if st.button(f"Get Recipe for {recipe['name']}", key=f"{recipe['name']}_button"):
                            st.session_state.selected_recipe = recipe["name"]
                        st.markdown("</div>", unsafe_allow_html=True)  # Close container
        
        # Show selected recipe instructions
        if "selected_recipe" in st.session_state:
            selected_recipe = st.session_state.selected_recipe
            st.markdown(f"<h3>{selected_recipe} Recipe Details</h3>", unsafe_allow_html=True)
        
            with st.form("portion_spice_form"):
                portion_size = st.number_input("Serving Size:", min_value=1, value=2)
                spice_level = st.selectbox("Preferred Spice Level:", ["mild", "medium", "hot"])
                get_instructions = st.form_submit_button("Get Instructions")
        
            if get_instructions:
                recipe_instructions = provide_recipe_instructions(selected_recipe, portion_size, spice_level)
                st.write(recipe_instructions)

    elif page == "Get Instructions for a Dish":
        st.markdown("<h1 style='text-align: center; color: #FFA500;'>🍲 Get Instructions for a Dish 🍲</h1>", unsafe_allow_html=True)
        st.subheader("Enter the dish name and your preferences")

        # Form for user to input dish name, portion size, and spice level
        with st.form("dish_instructions_form"):
            dish_name = st.text_input("Dish Name", placeholder="Enter the name of the dish you want to cook")
            portion_size = st.number_input("Serving Size:", min_value=1, value=2)
            spice_level = st.selectbox("Preferred Spice Level:", ["mild", "medium", "hot"])
            get_instructions_button = st.form_submit_button("Get Ingredients and Instructions")

        # If the form is submitted, fetch and display instructions
        if get_instructions_button and dish_name:
            # Get recipe instructions
            recipe_instructions = provide_recipe_instructions(dish_name, portion_size, spice_level)
            if recipe_instructions:
                st.markdown(f"<h3>{dish_name} Recipe Details</h3>", unsafe_allow_html=True)
                st.write(recipe_instructions)
            else:
                st.error("Sorry, we couldn't fetch the instructions. Please try again.")

        
# Run the main function
if __name__ == "__main__":
    main()
