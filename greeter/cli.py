import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: say-hello <name>")
        sys.exit(1)

    name = sys.argv[1]
    print(f"Helloooooooooo, {name}!")

if __name__ == '__main__':
    main()
