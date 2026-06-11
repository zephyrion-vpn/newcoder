def main() -> None:
    number = 8
    if number > 0:
        if number % 2 == 0:
            print("положительное четное")
        else:
            print("положительное нечетное")
    else:
        print("не положительное")


if __name__ == "__main__":
    main()
