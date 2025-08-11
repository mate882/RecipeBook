from django.core.management.base import BaseCommand
from django.utils.text import slugify
from recipes.models import Category, Recipe

class Command(BaseCommand):
    help = 'Populate the database with sample recipes'

    def handle(self, *args, **options):
        # Clear existing data
        Recipe.objects.all().delete()
        Category.objects.all().delete()
        
        # Create categories
        categories_data = [
            'Italian',
            'Asian',
            'Mexican',
            'Mediterranean',
            'American',
            'French',
            'Indian',
            'Thai',
            'Japanese',
            'Desserts'
        ]
        
        categories = {}
        for cat_name in categories_data:
            category = Category.objects.create(
                name=cat_name,
                slug=slugify(cat_name)
            )
            categories[cat_name] = category
            self.stdout.write(f"Created category: {cat_name}")
        
        # Sample recipes data
        recipes_data = [
            {
                'title': 'Classic Spaghetti Carbonara',
                'category': 'Italian',
                'description': 'A traditional Roman pasta dish with eggs, cheese, and pancetta.',
                'ingredients': '''400g spaghetti
200g pancetta or guanciale, diced
4 large eggs
100g Pecorino Romano cheese, grated
2 cloves garlic, minced
Black pepper to taste
Salt for pasta water''',
                'instructions': '''Cook spaghetti in salted boiling water until al dente.
Meanwhile, cook pancetta in a large pan until crispy.
Whisk eggs with grated cheese and black pepper in a bowl.
Drain pasta, reserving 1 cup pasta water.
Add hot pasta to the pan with pancetta.
Remove from heat and quickly stir in egg mixture.
Add pasta water gradually until creamy.
Serve immediately with extra cheese and pepper.''',
                'prep_time': 15,
                'cook_time': 20,
                'servings': 4,
                'difficulty': 'medium'
            },
            {
                'title': 'Chicken Tikka Masala',
                'category': 'Indian',
                'description': 'Tender chicken in a rich, creamy tomato-based curry sauce.',
                'ingredients': '''1kg chicken breast, cubed
200ml plain yogurt
2 tbsp garam masala
1 tbsp ground cumin
1 tbsp ground coriander
2 tsp paprika
1 large onion, diced
4 cloves garlic, minced
2 tbsp fresh ginger, grated
400ml canned tomatoes
200ml heavy cream
Fresh cilantro for garnish''',
                'instructions': '''Marinate chicken in yogurt and half the spices for 2 hours.
Cook marinated chicken in a hot pan until done. Set aside.
Sauté onion until soft, add garlic and ginger.
Add remaining spices, cook for 1 minute.
Add tomatoes, simmer for 15 minutes.
Stir in cream and cooked chicken.
Simmer for 10 minutes until sauce thickens.
Garnish with cilantro and serve with rice.''',
                'prep_time': 30,
                'cook_time': 45,
                'servings': 6,
                'difficulty': 'medium'
            },
            {
                'title': 'Classic Caesar Salad',
                'category': 'American',
                'description': 'Crisp romaine lettuce with homemade Caesar dressing and croutons.',
                'ingredients': '''2 large romaine lettuce heads
1/2 cup grated Parmesan cheese
2 cloves garlic, minced
2 anchovy fillets
1 egg yolk
2 tbsp lemon juice
1/2 cup olive oil
1 tsp Dijon mustard
2 cups bread cubes for croutons
Salt and pepper to taste''',
                'instructions': '''Make croutons by toasting bread cubes with olive oil.
Wash and chop romaine lettuce.
Make dressing by whisking egg yolk, lemon juice, and mustard.
Add minced garlic and anchovies.
Slowly drizzle in olive oil while whisking.
Season with salt and pepper.
Toss lettuce with dressing.
Top with Parmesan cheese and croutons.''',
                'prep_time': 20,
                'cook_time': 10,
                'servings': 4,
                'difficulty': 'easy'
            },
            {
                'title': 'Beef Tacos with Salsa Verde',
                'category': 'Mexican',
                'description': 'Seasoned ground beef tacos with fresh salsa verde and toppings.',
                'ingredients': '''500g ground beef
1 packet taco seasoning
8 taco shells
1 cup shredded lettuce
1 cup diced tomatoes
1 cup shredded cheese
1/2 cup sour cream
1/4 cup diced red onion
For salsa verde:
6 tomatillos, husked
2 jalapeños
1/4 cup cilantro
2 cloves garlic
1 lime, juiced''',
                'instructions': '''Brown ground beef in a large skillet.
Add taco seasoning and water, simmer until thickened.
For salsa verde: roast tomatillos and jalapeños until charred.
Blend roasted vegetables with cilantro, garlic, and lime juice.
Warm taco shells according to package directions.
Fill shells with seasoned beef.
Top with lettuce, tomatoes, cheese, and sour cream.
Serve with salsa verde on the side.''',
                'prep_time': 25,
                'cook_time': 20,
                'servings': 4,
                'difficulty': 'easy'
            },
            {
                'title': 'Thai Green Curry',
                'category': 'Thai',
                'description': 'Aromatic green curry with vegetables and your choice of protein.',
                'ingredients': '''2 tbsp green curry paste
400ml coconut milk
300g chicken or tofu, cubed
1 Thai eggplant, sliced
1 bell pepper, sliced
100g green beans, trimmed
2 tbsp fish sauce
1 tbsp brown sugar
Thai basil leaves
2 kaffir lime leaves
1 red chili, sliced
Jasmine rice for serving''',
                'instructions': '''Heat 2 tbsp of thick coconut milk in a wok.
Add curry paste and fry until fragrant.
Add remaining coconut milk gradually.
Add protein and cook until nearly done.
Add vegetables, starting with harder ones.
Season with fish sauce and brown sugar.
Add lime leaves and Thai basil.
Simmer until vegetables are tender.
Serve over jasmine rice with fresh chili.''',
                'prep_time': 20,
                'cook_time': 25,
                'servings': 4,
                'difficulty': 'medium'
            },
            {
                'title': 'Greek Moussaka',
                'category': 'Mediterranean',
                'description': 'Layered casserole with eggplant, meat sauce, and béchamel.',
                'ingredients': '''2 large eggplants, sliced
500g ground lamb or beef
1 large onion, diced
3 cloves garlic, minced
400g canned tomatoes
2 tbsp tomato paste
1 tsp dried oregano
1/2 cup red wine
For béchamel:
50g butter
50g flour
500ml milk
100g grated cheese
2 egg yolks
Nutmeg to taste''',
                'instructions': '''Slice and salt eggplant, let drain for 30 minutes.
Pat dry and brush with oil, then grill or bake until golden.
Make meat sauce: sauté onion and garlic, add meat.
Add tomatoes, paste, oregano, and wine. Simmer 30 minutes.
Make béchamel: melt butter, add flour, cook 2 minutes.
Gradually add milk, whisk until thick.
Add cheese, egg yolks, and nutmeg.
Layer eggplant, meat sauce, repeat.
Top with béchamel and bake at 180°C for 45 minutes.''',
                'prep_time': 45,
                'cook_time': 90,
                'servings': 8,
                'difficulty': 'hard'
            },
            {
                'title': 'Classic French Onion Soup',
                'category': 'French',
                'description': 'Rich beef broth with caramelized onions and melted Gruyère cheese.',
                'ingredients': '''6 large yellow onions, thinly sliced
4 tbsp butter
2 tbsp olive oil
1 tsp sugar
1 tsp salt
1/2 cup dry white wine
1.5L beef stock
2 bay leaves
4 fresh thyme sprigs
6 baguette slices
200g Gruyère cheese, grated
Black pepper to taste''',
                'instructions': '''Heat butter and oil in a large pot.
Add onions, sugar, and salt. Cook slowly for 45 minutes until caramelized.
Add wine and scrape up any browned bits.
Add stock, bay leaves, and thyme. Simmer 30 minutes.
Toast baguette slices until golden.
Ladle soup into oven-safe bowls.
Top with toasted bread and cheese.
Broil until cheese is bubbly and golden.
Serve immediately while hot.''',
                'prep_time': 20,
                'cook_time': 90,
                'servings': 6,
                'difficulty': 'medium'
            },
            {
                'title': 'California Sushi Rolls',
                'category': 'Japanese',
                'description': 'Inside-out sushi rolls with crab, avocado, and cucumber.',
                'ingredients': '''2 cups sushi rice
3 tbsp rice vinegar
1 tbsp sugar
1 tsp salt
4 nori sheets
200g imitation crab meat
1 avocado, sliced
1 cucumber, julienned
Sesame seeds
Soy sauce for serving
Wasabi and pickled ginger''',
                'instructions': '''Cook sushi rice and season with vinegar mixture.
Let rice cool to room temperature.
Place nori on bamboo mat, shiny side down.
Spread rice evenly, leaving 1cm border.
Flip so nori is on top.
Add crab, avocado, and cucumber in a line.
Roll tightly using the mat.
Sprinkle with sesame seeds.
Slice with a sharp, wet knife.
Serve with soy sauce, wasabi, and ginger.''',
                'prep_time': 45,
                'cook_time': 20,
                'servings': 4,
                'difficulty': 'hard'
            },
            {
                'title': 'Chocolate Chip Cookies',
                'category': 'Desserts',
                'description': 'Classic chewy chocolate chip cookies that are perfect every time.',
                'ingredients': '''225g butter, softened
200g brown sugar
100g white sugar
2 large eggs
2 tsp vanilla extract
350g plain flour
1 tsp baking soda
1 tsp salt
300g chocolate chips''',
                'instructions': '''Preheat oven to 190°C.
Cream butter and both sugars until light and fluffy.
Beat in eggs one at a time, then vanilla.
In separate bowl, whisk flour, baking soda, and salt.
Gradually mix dry ingredients into wet ingredients.
Stir in chocolate chips.
Drop rounded tablespoons onto ungreased baking sheets.
Bake 9-11 minutes until golden brown.
Cool on baking sheet for 5 minutes before transferring.''',
                'prep_time': 15,
                'cook_time': 11,
                'servings': 36,
                'difficulty': 'easy'
            },
            {
                'title': 'Pad Thai',
                'category': 'Thai',
                'description': 'Thailand\'s most famous noodle dish with a perfect balance of sweet, sour, and salty.',
                'ingredients': '''200g rice noodles
200g prawns or chicken, sliced
2 eggs
3 tbsp vegetable oil
3 cloves garlic, minced
2 tbsp tamarind paste
3 tbsp fish sauce
2 tbsp palm sugar
1 tbsp chili flakes
100g bean sprouts
3 spring onions, chopped
2 tbsp crushed peanuts
Lime wedges for serving''',
                'instructions': '''Soak rice noodles in warm water until soft.
Heat oil in wok over high heat.
Add garlic and protein, stir-fry until cooked.
Push to one side, scramble eggs on other side.
Add drained noodles and sauce ingredients.
Toss everything together for 2-3 minutes.
Add bean sprouts and spring onions.
Stir-fry for another minute.
Serve with peanuts and lime wedges.''',
                'prep_time': 20,
                'cook_time': 15,
                'servings': 4,
                'difficulty': 'medium'
            },
            {
                'title': 'Ratatouille',
                'category': 'French',
                'description': 'Traditional French vegetable stew from Provence.',
                'ingredients': '''1 large eggplant, cubed
2 zucchini, sliced
2 bell peppers, chunked
4 tomatoes, chopped
1 large onion, sliced
4 cloves garlic, minced
1/4 cup olive oil
2 tsp herbs de Provence
1 tsp salt
1/2 tsp black pepper
Fresh basil for garnish''',
                'instructions': '''Heat olive oil in large pot over medium heat.
Sauté onion until translucent, about 5 minutes.
Add garlic and cook 1 more minute.
Add eggplant, cook for 10 minutes stirring occasionally.
Add peppers and zucchini, cook 10 minutes more.
Add tomatoes and seasonings.
Simmer covered for 20-30 minutes until vegetables are tender.
Stir occasionally and add water if needed.
Garnish with fresh basil before serving.''',
                'prep_time': 25,
                'cook_time': 50,
                'servings': 6,
                'difficulty': 'easy'
            },
            {
                'title': 'New York Cheesecake',
                'category': 'Desserts',
                'description': 'Rich and creamy classic New York-style cheesecake.',
                'ingredients': '''For crust:
200g graham crackers, crushed
85g butter, melted
2 tbsp sugar
For filling:
900g cream cheese, softened
200g sugar
3 large eggs
1 tsp vanilla extract
240ml sour cream
2 tbsp flour''',
                'instructions': '''Preheat oven to 160°C.
Mix crust ingredients and press into springform pan.
Beat cream cheese until smooth and fluffy.
Gradually add sugar, beating until combined.
Beat in eggs one at a time, then vanilla.
Mix in sour cream and flour until just combined.
Pour over crust and smooth top.
Bake 55-60 minutes until center is almost set.
Cool completely, then refrigerate overnight.
Run knife around edge before removing from pan.''',
                'prep_time': 30,
                'cook_time': 60,
                'servings': 12,
                'difficulty': 'medium'
            }
        ]
        
        # Create recipes
        for recipe_data in recipes_data:
            category = categories[recipe_data['category']]
            
            recipe = Recipe.objects.create(
                title=recipe_data['title'],
                slug=slugify(recipe_data['title']),
                category=category,
                description=recipe_data['description'],
                ingredients=recipe_data['ingredients'],
                instructions=recipe_data['instructions'],
                prep_time=recipe_data['prep_time'],
                cook_time=recipe_data['cook_time'],
                servings=recipe_data['servings'],
                difficulty=recipe_data['difficulty']
            )
            
            self.stdout.write(f"Created recipe: {recipe.title}")
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {len(categories_data)} categories and {len(recipes_data)} recipes'
            )
        )