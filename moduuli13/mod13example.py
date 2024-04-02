# Mod 13 - Python-palvelinesimerkki Flaskilla
import json

from flask import Flask, request, Response

app = Flask(__name__)

def calc_sum(a, b):
    return a + b

def multiply(a, b):
    return a * b

@app.route('/calc/<type>')
def calculate(type):
    # print(request.args)
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        if type == "sum":
            result = calc_sum(num1, num2)
        elif type == "multiply":
            result = multiply(num1, num2)
        else:
            response_body = json.dumps(
                {"error": "unknown calculation type", "status": 400}
            )
            return Response(response=response_body, status=400, mimetype="application/json")
        # oletuksena dictionary muutetaan http-vastaukseen automaattisesti jsoniksi
        # statuksella 200 (OK)
        return {"result": result, "numbers": [num1, num2]}
    except:
        # TODO: muuta virhekoodi myös http-vastauksen otsikkotiedoissa
        return {"error": "invalid parameters", "status": 400}

@app.errorhandler(404)
def page_not_found(error):
    response_body = json.dumps(
        {"error": error.name, "description": error.description, "status": error.code}
    )
    return Response(
        response=response_body,
        status=error.code,
        mimetype="application/json")


if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
