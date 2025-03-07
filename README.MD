# Recipe Catalog

This Recipe Catalog program allows you to manage your favorite recipes. You can add new recipes, search for recipes by title, and view detailed information about each recipe through a command-line interface.

## Features

- **Add a new recipe**: Add your favorite recipes to the catalog.
- **Search for a recipe by title**: Find recipes quickly by their title.
- **View recipe details**: Get detailed information about a specific recipe.
- **Browse all recipes**: List all recipes in the catalog.
- **Edit a recipe**: Edit an existing recipe. (Microservice A)
- **Delete a recipe**: Delete an existing recipe. (Microservice A)
- **Search recipes by ingredient**: Find recipes that use a specific ingredient. (Microservice B)
- **Submit a review**: Rate and review a recipe. (Microservice C)
- **View reviews**: View ratings and reviews for a recipe. (Microservice C)
- **Manage shopping list**: Add or remove ingredients from your shopping list. (Microservice D)
- **About/Help**: View information about the program and how to use it.
- **Exit**: Exit the application.

## Prerequisites

- Python 3.6 or higher

## Running the Program and Microservices

The main program and each of the four microservices run in different processes. This ensures that each component operates independently and can be scaled as needed.

To start the main program and microservices, you can use the following commands:

1. **Start Microservice A**:

   ```sh
   python microserviceA.py

   ```

2. **Start Microservice B**:

```sh
python microserviceB.py

```

3. **Start Microservice C**:

```sh
python microserviceC.py
```

4. **Start Microservice D**:

```sh
python microserviceD.py

```

3. **Run the Main Program**:

```sh
   python main.py
```
