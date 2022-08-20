from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)


@app.route('/person_update/<id_person>', methods=['GET'])
def person_update(id_person):
    return render_template('person_update.html', value=id_person)


@app.route('/person_update_detail', methods=['POST'])
def person_update_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    status = request.form['status']
    """
    update_data = {
                        "id_person": id_person,
                        "category": {
                            "id_person": 0,
                            "first_name": "string",
                            "last_name": "string"
                        },
                        "first_name": first_name,
                        "last_name": last_name,
                        "photoUrls": [
                            "string"
                        ],
                        "tags": [
                            {
                                "id_person": 0,
                                "first_name": "string",
                                "last_name": "string"
                            }
                        ],
                        "status": status
                    }
    """

    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=(id_person, first_name, last_name, status))


@app.route('/person_delete/<id_person>', methods=['GET'])
def person_delete(id_person):
    for i in model:
        if i.id_person == id_person:
            temp = i
            model.remove(i)
    return render_template('delete_user.html', value="Delete successfully")

if __name__ == '__main__':
    app.run()
