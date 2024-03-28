def main():
    cse_expr = input()
    cse_components = cse_expr.split(" ")
    if len(cse_components) != 5:
        return
    print(cse_components)

if __name__ == "__main__":
    main()
