### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount in ingredients.items():
            if self.machine_resources[ingredient] < amount:
                print("Sorry! there is not enough " + ingredient)
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins")
        largeDollars = int(input("How many dollars? ")) * 1.00
        halfDollars = int(input("How many half-dollars? ")) * .50
        quarters = int(input("How many quarters? ")) * 0.25
        nickles = int(input("How many nickles? ")) * 0.05
        total = largeDollars + halfDollars + quarters + nickles
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print ("sorry, thats not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount
        print (f" {sandwich_size} sandich is ready. Bon appetit!")

    def report(self):##report to list all available ingredients
        for resource, amount in self.machine_resources.items():
            if resource in ["bread", "ham",]:
                unit = "slice(s)"##if resource is bread or ham, list it in slices
            else:
                unit = "pounds"##if resource is cheese, list in pounds
            print(f" {resource.capitalize()}: {amount} {unit}")

### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)

while True:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
    if choice == "off":
        break

    elif choice == "report":
        machine.report()

    elif choice in ["small", "medium", "large"]:##if choice is a size
        sandwhich = recipes[choice]##creating sandwich variable for size

        if machine.check_resources(sandwhich["ingredients"]):##if there are sufficient ingredients
            transaction = machine.process_coins()##variable to complete transaction

            if machine.transaction_result(transaction, sandwhich["cost"]):##calling transaction function
                machine.make_sandwich(choice, sandwhich["ingredients"])##making sandwich with size and type
    else:
        print("Invalid choice. Please choose again")


