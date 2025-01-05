def main():
    with open("books/frankenstein.txt") as f:
        mySet = {chr(x): 0 for x in range(97, 123)}
        file_contents = f.read()
        sum = 0
        extracted = "".join(filter(str.isalpha, file_contents.lower()))
        for _ in file_contents.split():
            sum += 1

        for ch in list(extracted):
            mySet[ch] += 1

        sortedAlphas = sorted(mySet.items(), key=lambda item: item[1], reverse=True)
        print("--- Begin report of books/frankenstein.txt ---")
        for key in sortedAlphas:
            print(f"The '{key[0]}' character was found {key[1]} times")


main()
