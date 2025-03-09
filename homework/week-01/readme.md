# Weekend Project - Week 1

## Project Description
Full reference: [Encode Club Decentralized AI Bootcamp Weekend 1 Project](https://github.com/Encode-Club-AI-Bootcamp/DeAI/tree/main/Lesson-04#weekend-project)

**Quick reference:**
To consolidate the knowledge acquired this week, students should complete the following project:

1. Create a new GitHub repository for your project.
2. Invite all members of your group to collaborate on the repository.
3. Write a simple README.md file explaining your project
4. Modify and expand the `Chef GPT script` by incorporating a unique personality for your AI chef
   - Tweak the system prompt to include a unique personality for your AI chef
   - Example personalities:
     - A young, enthusiastic Indian chef specializing in Biryani
     - A seasoned Italian chef with a passion for pasta-making
     - An old Brazilian grandma who loves to cook classic dishes
5. Develop individual scripts for each group member, each featuring a distinct AI chef personality
6. Program the AI to respond to three specific types of user inputs:
   a. Ingredient-based dish suggestions
   b. Recipe requests for specific dishes
   c. Recipe critiques and improvement suggestions
7. Give enough instructions in the system prompt to make the AI conform to give the responses according to the scenarios above
   - Implement the following logic:
   - If the user's initial input doesn't match these scenarios, politely decline and prompt for a valid request.
     - For ingredient inputs: Suggest only dish names without full recipes.
     - For dish name inputs: Provide a detailed recipe.
     - For recipe inputs: Offer a constructive critique with suggested improvements.
   - Ideally, the same AI would be able to handle the three scenarios above
     - But if you can't get the same AI to do that, you can make three different scripts for each personality to proceed with your project
8. Conduct a comprehensive experiment:
   - The first person should use one script with one personality to suggest a dish based on given ingredients
     - After running the script, send the response for one of your group members (via Discord or any other means)
   - The second person should request a recipe for that dish using a second script with a different personality
     - After running the script, send the response for another of your group members
   - The third person should critique the provided recipe using a third script with a different personality
9. Compile a simple report documenting:
   - The experiment process
   - The system prompts used in each script
   - Comparative analysis of the different user prompts and their responses
10. Submit your completed project through the designated submission form.




## Implementation Test Results
`$python3 homework/week-01/fodisi-uHXQcc-chefgpt.py`


### Test 1
#### Inputs:
```shell
# chef personality: 4
# input option: 3
# ingredients: onion carrot mango papaya fish lemon
```

#### Output:
```
Choose a chef personality:
1. Quirky Japanese Chef
2. Witty Italian Chef
3. Sassy French Pastry Chef
4. Energetic Thai Street Food Vendor
5. Playful Vegan Chef
Type the desired chef personality number:
4
Welcome to your chef concierge. Choose an option:
a. Ingredient-based dish suggestions
b. Recipe requests for specific dishes
c. Recipe critiques and improvement suggestions
Type the desired option (a, b, or c):
a
Type the ingredients that you want to use in the recipe. We will provide you a list of dish names without full recipes
onion carrot mango papaya fish lemon
Oh, ho! You’ve got a fantastic mix of ingredients there! Let’s spice things up, shall we? Here’s a sizzling list of mouthwatering dishes you can whip up with those goodies:

1. **Mango Papaya Salad (Som Tum)** – A refreshing twist that’ll dance on your taste buds!
2. **Fish with Lemon Sauce** – A zesty delight that’s super quick and full of flavor!
3. **Carrot and Onion Stir-Fried Fish** – A colorful and tasty plate that’ll make you smile!
4. **Mango Fish Tacos** – Let’s take a trip with flavors and wrap it all up!
5. **Papaya Fish Curry** – Creamy, spicy, and oh-so-delicious!
6. **Onion and Carrot Mango Salsa** – A vibrant topping for grilled dishes, yum!
7. **Papaya and Carrot Slaw** – Crunchy and zesty, it’s the perfect side!

Get your cooking shoes on because it’s about to get flavorful in the kitchen! Let me know if you want recipes for any of these dishes!
```


### Test 2
#### Inputs:
```shell
# chef personality: 5
# input option: 2
# dish name: rice lentils and beans sautee
```

#### Output:
```
Oh, you’re in for a delicious, protein-packed adventure with this rice, lentils, and beans sauté! Grab your apron and let’s get cooking, my friend!

### Rice, Lentils, and Beans Sauté

#### Ingredients:
- **1 cup brown rice (or any rice of your choice)**
- **1 cup green or brown lentils**
- **1 can (15 oz) black beans (or your favorite beans) – drained and rinsed**
- **1 medium onion, diced**
- **3 cloves garlic, minced**
- **1 bell pepper (any color), diced**
- **1 medium zucchini, diced**
- **1 tsp cumin powder**
- **1 tsp smoked paprika (for that smokey deliciousness!)**
- **Salt and pepper to taste**
- **2 tbsp olive oil (or coconut oil for a tropical twist)**
- **Fresh cilantro or parsley, chopped (for garnish)**
- **Juice of 1 lime (to brighten everything up!)**

#### Instructions:

1. **Cook the Rice and Lentils:**
   - Start by rinsing your brown rice and lentils under cold water. This helps wash away any pesky dirt and debris!
   - In two separate pots, cook the rice and lentils according to their package instructions. Usually, you’d boil the rice in about 2 cups of water (or broth for extra flavor) and the lentils in about 3 cups of water. Simmer until both are tender (about 30-40 mins for rice, 20-30 mins for lentils). **Tip:** You can combine them in one pot for the last 10-15 minutes if you want to save time!

2. **Sauté the Veggies:**
   - While the rice and lentils are having their spa day, grab a large skillet and heat the olive oil over medium heat. *Let those aromas beckon your neighbors!*
   - Add the diced onion and bell pepper. Sauté for about 5-7 minutes until they become soft and a bit translucent.
   - Toss in the minced garlic and zucchini, continuing to sauté for another 3-4 minutes. Stir occasionally and don’t let that garlic burn, or your kitchen might smell like a vampire convention!

3. **Combine Everything:**
   - Once your rice and lentils are cooked, drain them (if there’s any extra water). Add them to the skillet along with the drained black beans.
   - Sprinkle in the cumin, smoked paprika, salt, and pepper. **Give it a good stirring dance** so all the ingredients mesh together like the best of friends at a potluck.

4. **Heat It Up:**
   - Let everything cook together for about 5 more minutes, stirring occasionally until heated through. You can even add a splash of water or vegetable broth if it feels a bit dry or stubborn.

5. **Finish It Off:**
   - Just before serving, squeeze the lime juice over the sauté and mix it in. This zingy twist will elevate your dish like a confetti explosion at a party!

6. **Garnish and Serve:**
   - Spoon your glorious sauté into bowls and sprinkle with freshly chopped cilantro or parsley. **Boom! Your healthy, vibrant dish is ready to shine!**

### Enjoy Your Creation!
This dish is not only nutritious but also super versatile. Feel free to swap in any veggies you have hanging around, and don’t forget to dance while you cook. Cooking is always better with a little shimmy!

--- 

And voilà! You’ve got yourself a delightful sauté that’s bound to impress all who dare to taste it. Enjoy every bite, and may your kitchen be filled with giggles and delicious aromas! 🌱🍚🌶️💚
```


### Test 3
#### Inputs:
```shell
# chef personality: 2
# input option: c
# recipe: 2 eggs, pinch of salt, 1tbs oil heat the oil in a fry-pan over high heat. add egss and salt. scramb with anything you can find like a spoon or fork until fully cooked
```

#### Output:
```
Ah, bellissimo! I see you’re trying to whip up a delightful plate of scrambled eggs, but it looks like we need to give that recipe a little Italian love, shall we? Here’s my cheeky critique and some improvements to elevate your scrambled eggs from "eh" to "mamma mia!"

### Ingredients

- 2 eggs
- Pinch of salt
- 1 tbsp olive oil (because every dish deserves a little Italian touch!)
- Optional: a splash of milk or cream (for creaminess)
- Optional: fresh herbs (like parsley or basil) or grated cheese (like Parmigiano Reggiano—because why not?)

### Instructions

1. **Prepare Your Ingredients:**
   - Crack those eggs into a bowl, add a pinch of salt, and if you’re feeling fancy, a splash of milk or cream. Whisk them together until they’re all frothy and in a harmonious relationship! Go wild like you’re dancing at a lively Italian festival!

2. **Heat the Oil:**
   - In a non-stick pan, heat your olive oil over medium heat—not high heat, or you'll end up with scrambled eggs that feel like they just ran a marathon! We want them soft and fluffy, like a cloud over the Amalfi Coast. 

3. **Cook the Eggs:**
   - Once the oil is shimmering (but not smoking like it just got its heart broken), pour in your egg mixture. Now, here’s the key: use a spatula, not just any old spoon or fork. A spatula is your best friend here—think of it as your sous-chef! 

4. **Scramble with Care:**
   - Gently push the eggs around the pan, letting the uncooked mixture flow to the bottom. We're looking for a creamy consistency, not scrambled eggs that resemble rubber! The whole process should take about 3-5 minutes. 

5. **Final Touch:**
   - When they’re almost cooked through but still a touch runny (they’ll keep cooking after you take them off the heat), sprinkle them with fresh herbs or grated cheese. You need that bit of flair because let’s face it – it’s not just what you eat, but how it looks, too! 

6. **Serve and Enjoy:**
   - Plate them up (preferably on a colorful plate—like throwing a party for your taste buds!), and enjoy your fabulous creation! Maybe a side of toast or fresh tomatoes? Just remember, less time worrying and more time savoring!

### Tips and Tricks

- ***Don’t Rush It:*** Remember, good things take time (like a perfect espresso)! 
- ***Experiment:*** Always feel free to toss in whatever herbs, spices, or even leftover veggies you have going on in the fridge. Just don’t go full Mad Scientist on it—keep it tasteful!
- ***Cleaning Up:*** If you manage to get egg everywhere—yes, there’s a secret egg splatter technique that no one told you about—don’t worry, my friend, it happens to the best of us! Just laugh and get the sponge ready.

So, there you have it, a simple scramble turned into a feast fit for an Italian family! Buon appetito! 🍳🇮🇹
```