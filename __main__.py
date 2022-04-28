import json


def main() -> None:
    with open("./extensions.json") as file:
        extension_dict = json.load(file)

    extensions = [row["identifier"]["id"] for row in extension_dict]

    with open("./result.json", mode="w") as file:
        json.dump(extensions, file)


if __name__ == "__main__":
    main()
