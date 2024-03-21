import random
from colorama import init, Fore

init(autoreset=True)  # Initialize colorama

class Empire:
    def __init__(self, name):
        """Initialize the Empire object with initial resources and buildings."""
        self.name = name
        self.coin = 100
        self.men = 100
        self.stone_tablets = 100
        self.food = max(500, random.randint(500, 1000))  # Ensure at least 500 food
        self.masonrys = 0
        self.houses = 0
        self.marketplaces = 0
        self.foragers = 0
        self.expansions = 0
        self.seasons_passed = 0
        self.men_consumed = 0

    def fall(self):
        """Simulate the Fall season where resources decline."""
        coin_consumption = random.randint(10, 30)
        men_consumption = random.randint(10, 30)
        stone_tablets_consumption = random.randint(10, 30)
        food_consumption = random.randint(10, 30)

        print(f"Resources required: Coin: {coin_consumption}, Men: {men_consumption}, Stone Tablets: {stone_tablets_consumption}, Food: {food_consumption}")
        self.coin -= coin_consumption
        self.men -= men_consumption
        self.stone_tablets -= stone_tablets_consumption
        self.food -= food_consumption

    def spring(self):
        """Simulate the Spring season where resources increase and generate from buildings and foragers."""
        coin_generation = random.randint(20, 50)
        men_generation = random.randint(20, 50)
        stone_tablets_generation = random.randint(20, 50)
        food_generation = random.randint(20, 50)

        print(f"Resources generated: Coin: {coin_generation}, Men: {men_generation}, Stone Tablets: {stone_tablets_generation}, Food: {food_generation}")
        self.coin += coin_generation
        self.men += men_generation
        self.stone_tablets += stone_tablets_generation
        self.food += food_generation

        # Generating resources from buildings
        self.stone_tablets += self.masonrys * 10
        self.men += self.houses * 5
        self.coin += self.marketplaces * 30

        # Generating resources from foragers
        self.food += self.foragers * 15  # Generate additional food from foragers

        # Men consume food
        self.food -= self.men

        # Check if food is 0 or less for consecutive seasons
        if self.food <= 0:
            print(Fore.RED + "Game Over")
            print(f"Stats:")
            print(f"Expansions: {self.expansions}")
            print(f"Seasons passed: {self.seasons_passed}")
            print(f"Men consumed: {self.men_consumed}")
            return True
        return False

    def build_masonry(self):
        """Build a masonry if enough coins are available."""
        cost = 50
        if self.coin >= cost:
            self.masonrys += 1
            self.coin -= cost
            print("Masonry built!")
        else:
            print(f"Not enough coins to build Masonry. Current coins required: {cost}")

    def build_house(self):
        """Build a house if enough coins are available."""
        cost = 50
        if self.coin >= cost:
            self.houses += 1
            self.coin -= cost
            print("House built!")
        else:
            print(f"Not enough coins to build House. Current coins required: {cost}")

    def build_marketplace(self):
        """Build a marketplace if enough men are available."""
        men_cost = 50
        if self.men >= men_cost:
            self.marketplaces += 1
            self.men -= men_cost
            print("Marketplace built!")
        else:
            print(f"Not enough men to build Marketplace. Current men required: {men_cost}")

    def build_forager_hut(self):
        """Build a forager hut if enough men are available."""
        cost = 50
        if self.men >= cost:
            self.foragers += 1
            self.men -= cost
            print("Forager hut built!")
        else:
            print(f"Not enough men to build Forager hut. Current men required: {cost}")

    def expand_empire(self):
        """Expand the empire if enough men, coins, and food are available."""
        men_cost = random.randint(20, 50)
        coin_cost = random.randint(20, 50)
        food_cost = random.randint(20, 50)
        if self.men >= men_cost and self.coin >= coin_cost and self.food >= food_cost:
            self.men -= men_cost
            self.coin -= coin_cost
            self.food -= food_cost
            self.expansions += 1
            print("Empire expanded!")
        else:
            print(f"Not enough men, coins, or food to expand the empire. Current men required: {men_cost}, Current coins required: {coin_cost}, Current food required: {food_cost}")

    def display_status(self):
        """Display the current status of the empire."""
        print(f"Empire: {self.name}")
        print(f"Coin: {self.coin}")
        print(f"Men: {self.men}")
        print(f"Stone Tablets: {self.stone_tablets}")
        print(f"Food: {self.food}")
        print(f"Masonrys: {self.masonrys}")
        print(f"Houses: {self.houses}")
        print(f"Marketplaces: {self.marketplaces}")
        print(f"Foragers: {self.foragers}")

def main():
    empire_name = input("Enter the name of your empire: ")
    empire = Empire(empire_name)

    while True:
        # Determine season
        season = random.choice(["Fall", "Spring"])
        print(f"Season: {season}")
        print("=" * 30)

        if season == "Fall":
            empire.fall()
            empire.display_status()

            # User action
            user_action = input("Do you want to build? (yes/no): ").lower()
            if user_action == "yes":
                build_choice = input("What do you want to build? (Masonry/House/Marketplace/Forager Hut): ").lower()
                if build_choice == "masonry":
                    empire.build_masonry()
                elif build_choice == "house":
                    empire.build_house()
                elif build_choice == "marketplace":
                    empire.build_marketplace()
                elif build_choice == "forager hut":
                    empire.build_forager_hut()
                else:
                    print("Invalid choice.")
            elif user_action == "no":
                print("No buildings constructed.")

        elif season == "Spring":
            empire.spring()
            empire.seasons_passed += 1
            empire.display_status()

            # User action
            user_action = input("Do you want to expand your empire? (yes/no): ").lower()
            if user_action == "yes":
                empire.expand_empire()
            elif user_action == "no":
                print("Empire not expanded.")

        print("=" * 30)

        # Check for game over condition
        if empire.spring():
            break

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
