import json

def read_jsons():
    try:
        with open('json/candidates.json', 'r', encoding='utf-8') as f:
            candidates = json.load(f)
    except IOError:
        print("Нет файла json/candidates.json !")
        exit()
    except Exception:
        print("Ошибка файле json/candidates.json !")
        exit()

    try:
        with open('json/settings.json', 'r', encoding='utf-8') as f:
            settings = json.load(f)
    except IOError:
        print("Нет файла json/settings.json !")
        exit()
    except json.decoder.JSONDecodeError:
        print("Ошибка файле json/settings.json !")
        exit()
    return candidates, settings



def main():
    candidates, settings = read_jsons()
    print(candidates, "\n", settings)

if __name__ == "__main__":
   main()