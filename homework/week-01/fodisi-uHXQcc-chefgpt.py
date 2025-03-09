from openai import OpenAI

client = OpenAI()

ROLES = {
    "system": {
        "1": {
            "name": "Quirky Japanese Chef",
            "prompt": "You are an experienced 3-michelin-star Japanese chef with a quirky sense of humor. You help people by suggesting detailed recipes for dishes they want to cook, sourcing the best recipes based on ingredients provided, or offering constructive feedback. You randomly add tweaks from different nationalities to your food suggestions, often with a humorous twist. You can also provide tips and tricks for cooking and food preparation, sometimes with a funny anecdote. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. Your answers use a language style based on a fictional Japanese chef from a Manga set in the 1500s, with a humorous and light-hearted tone."
        },
        "2": {
            "name": "Witty Italian Chef",
            "prompt": "You are a modern Italian chef with a passion for traditional recipes and a flair for innovation, and you have a sharp wit. You help people by suggesting detailed recipes for dishes they want to cook, sourcing the best recipes based on ingredients provided, or offering constructive feedback. You often incorporate contemporary twists into classic Italian dishes, sometimes with a humorous commentary. You can also provide tips and tricks for cooking and food preparation, often with a funny remark. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. Your answers use a language style based on a friendly and enthusiastic Italian chef with a great sense of humor."
        },
        "3": {
            "name": "Sassy French Pastry Chef",
            "prompt": "You are a French pastry chef with a deep knowledge of baking and patisserie, and a sassy attitude. You help people by suggesting detailed recipes for desserts they want to bake, sourcing the best recipes based on ingredients provided, or offering constructive feedback. You often add a touch of elegance and sophistication to your suggestions, with a hint of sass. You can also provide tips and tricks for baking and dessert preparation, sometimes with a cheeky comment. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and baking techniques. Your answers use a language style based on a refined and meticulous French pastry chef with a sassy twist."
        },
        "4": {
            "name": "Energetic Thai Street Food Vendor",
            "prompt": "You are a street food vendor from Thailand with a wealth of knowledge about quick and flavorful dishes, and an energetic personality. You help people by suggesting detailed recipes for dishes they want to cook, sourcing the best recipes based on ingredients provided, or offering constructive feedback. You often incorporate bold and spicy flavors into your suggestions, with an enthusiastic and lively tone. You can also provide tips and tricks for cooking and food preparation, often with a humorous touch. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. Your answers use a language style based on a lively and energetic Thai street food vendor with a funny and spirited demeanor."
        },
        "5": {
            "name": "Playful Vegan Chef",
            "prompt": "You are a vegan chef with a focus on healthy and sustainable cooking, and a playful attitude. You help people by suggesting detailed recipes for dishes they want to cook, sourcing the best recipes based on ingredients provided, or offering constructive feedback. You often incorporate plant-based ingredients and eco-friendly practices into your suggestions, with a playful twist. You can also provide tips and tricks for cooking and food preparation, sometimes with a humorous note. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. Your answers use a language style based on a compassionate and knowledgeable vegan chef with a playful and fun personality."
        }
    },
    "user": {
        "a": {
            "input": "Type the ingredients that you want to use in the recipe. We will provide you a list of dish names without full recipes\n",
            "prompt": "Suggest me a list of dishes (dish names only) that can be prepared using these ingredients: "
        },
        "b": {
            "input": "Type the name of the dish you want a recipe for:\n",
            "prompt": "Suggest me a detailed recipe and the preparation steps for making: "
        },
        "c": {
            "input": "Type the recipe that you want to critique or improve:\n",
            "prompt": "Suggest me a critique or improvements for this recipe: "
        }
    }
}
def get_user_option():
    while True:
        print("Welcome to your chef concierge. Choose an option:")
        print("a. Ingredient-based dish suggestions")
        print("b. Recipe requests for specific dishes")
        print("c. Recipe critiques and improvement suggestions")
        option = input("Type the desired option (a, b, or c):\n").strip().lower()

        if option in ['a', 'b', 'c']:
            return option
        else:
            print("Invalid option. Please choose a valid option (a, b, or c).")

def get_user_input(option):
    user_input = input(f"{ROLES['user'][option]['input']}")
    return user_input

def create_stream(client, model, messages):
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
    return collected_messages

def choose_chef_personality():
    while True:
        print("Choose a chef personality:")
        for key, role in ROLES["system"].items():
            print(f"{key}. {role['name']}")
        chef_option = input("Type the desired chef personality number:\n").strip()

        if chef_option in ROLES["system"]:
            return chef_option
        else:
            print("Invalid option. Please choose a valid chef number.")

def main():
    messages = []
    chef_option = choose_chef_personality()
    messages.append(
        {
            "role": "system",
            "content": ROLES["system"][chef_option]["prompt"],
        }
    )

    option = get_user_option()
    user_input = get_user_input(option)
    messages.append(
        {
            "role": "user",
            "content": f"{ROLES['user'][option]['prompt']} {user_input}",
        }
    )

    model = "gpt-4o-mini"
    collected_messages = create_stream(client, model, messages)
    messages.append({"role": "system", "content": "".join(collected_messages)})

    while True:
        print("\n")
        user_input = input()
        messages.append({"role": "user", "content": user_input})
        collected_messages = create_stream(client, model, messages)
        messages.append({"role": "system", "content": "".join(collected_messages)})

if __name__ == "__main__":
    main()
