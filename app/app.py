def add(a, b):
    return a + b


def get_app_version():
    return "1.0.0"


if __name__ == "__main__":
    print("Enterprise CI/CD Application")
    print(f"Version: {get_app_version()}")
    print(f"2 + 3 = {add(2, 3)}")
