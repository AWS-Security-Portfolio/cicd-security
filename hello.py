# hello.py

def greet(name):
    # Intentionally insecure: using input directly in f-string (for CodeGuru demo)
    print(f"Hello, {name}!")

def main():
    user = input("Enter your name: ")
    greet(user)

if __name__ == "__main__":
    main()
