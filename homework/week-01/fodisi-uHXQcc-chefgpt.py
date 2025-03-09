from openai import OpenAI

client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are an experienced 3-michelin-star japanese chef that helps people by suggesting detailed recipes for dishes they want to cook, sourcing the best recipes based on ingredients provided or even offer constructive feedback. However, you randomly add tweaks from different nationalities to your food suggestions. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. Your answers use a language style based on fictional Japanese chef from a Manga based in 1500 having the japanese culture as background for your growth",
    }
]
messages.append(
    {
        "role": "system",
        "content": "Your client is going to provide you one of these three specific types of user inputs: a) Ingredient-based dish suggestions, where you're expected to return a list of dish names without recipes; b) a dish name where the expected return is a detailed recipe for the given dish name; c) a food recipe where the expected return are critiques and improvement suggestions. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish, the ingredients listed or the recipe. If you know the dish, ingredients or recipe you must answer directly with the expected return for each type of input. If you don't know the dish, ingredients or recipe you should answer that you don't know and end the conversation.",
    }
)

while True:
    print("Welcome to your chef concierge. Choose an option:")
    print("Choose an option:")
    print("a. Ingredient-based dish suggestions")
    print("b. Recipe requests for specific dishes")
    print("c. Recipe critiques and improvement suggestions")
    option = input("Type the desired option (a, b, or c):\n").strip().lower()

    if option in ['a', 'b', 'c']:
        break
    else:
        print("Invalid option. Please choose a valid option (a, b, or c).")

user_input = ""

if option == 'a':
    user_input = input("Type the ingredients that you want to use in the recipe. We will provide you a list of dish names without full recipes\n")
    messages.append(
        {
            "role": "user",
            "content": f"Suggest me a list of dishes (dish names only) that can be prepared using these ingredients: {user_input}",
        }
    )
elif option == 'b':
    user_input = input("Type the name of the dish you want a recipe for:\n")
    messages.append(
        {
            "role": "user",
            "content": f"Suggest me a detailed recipe and the preparation steps for making: {user_input}",
        }
    )
elif option == 'c':
    user_input = input("Type the recipe that you want to critique or improve:\n")
    messages.append(
        {
            "role": "user",
            "content": f"Suggest me a critique or improvements for this recipe: {user_input}",
        }
    )


model = "gpt-4o-mini"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append({"role": "system", "content": "".join(collected_messages)})

while True:
    print("\n")
    user_input = input()
    messages.append({"role": "user", "content": user_input})
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append({"role": "system", "content": "".join(collected_messages)})