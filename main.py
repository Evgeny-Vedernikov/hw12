from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route("/")
def page_index():
    return render_template('index.html', **settings)

@app.route('/candidate/<id>')
def page_profile(id):
    for candidate in candidates:
        if candidate['id'] == int(id):
            return render_template('candidate.html', **candidate)
    return "<b>Not found!</b>"

@app.route('/list/')
def page_cand_list():
    return render_template('cand_list.html', cands = candidates)

@app.route('/search/')
def page_search():
    name = request.args.get("name")
    found_list = []
    if name:
        if settings["case_sensitive"] == False:
            name = name.lower()
        for cand in candidates:
            cand_name = cand["name"]
            if settings["case_sensitive"] == False:
                cand_name = cand_name.lower()
            if name in cand_name:
                found_list.append(cand)

    return render_template('found_list.html', found_list = found_list, )




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
    global candidates, settings
    candidates, settings = read_jsons()
    app.run()

if __name__ == "__main__":
   main()
