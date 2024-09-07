def find_a(s):
    if "a" not in s.lower():
        return False
    else:
        s_list = list(s.lower())
        return s_list.count("a")

def main():
    s = input("String: ")
    if find_a(s):
        print(f"A letra 'a' aparece {find_a(s)} vezes.")
    else:
        print("A letra 'a' não aparece.")

if __name__ == "__main__":
    main()