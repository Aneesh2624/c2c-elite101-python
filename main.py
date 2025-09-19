def get_user_name():
    return input("Please enter your name: ")

def get_user_age():
    return input("Please enter your age: ")

def greet_user(name, age):
    print(f"Hello, {name}. You are {age} years old.")

def show_menu():
    print("\nHow can I help you?")
    print("1. Learn about this program")
    print("2. Get a study tip")
    print("3. Just chat")
    print("4. Exit")

def main():
    print("Welcome to Elite 101. This is your starter chatbot project.")

    name = get_user_name()
    age = get_user_age()
    greet_user(name, age)

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("This program helps you practice coding and learn tools for internships.")
        elif choice == "2":
            print("Study tip: Practice a little bit every day, not all at once.")
        elif choice == "3":
            print("I'm glad we are talking. Keep learning.")
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
