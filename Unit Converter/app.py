from flask import Flask, render_template, request


app = Flask(__name__)

def convert_length(value,from_unit,to_unit):
    length_units = {
        "millimeter": 0.001,
        "meter" : 1,
        "kilometer" : 1000,
        "inch" : 0.0393700787,
        "foot" : 0.3048,
        "mile" : 1609.34
    }
    meters = float(length_units[from_unit] * value)
    result = meters / length_units[to_unit]
    result = int(result) if result == int(result) else result
    return result


def convert_weight(value,from_unit,to_unit):
    weight_units = {
        "killogram": 1,
        "gram" : 0.001,
        "milligram" : 0.000001,
        "ton" : 1000,
        "pound" : 0.453592,
        "ounce" : 0.0283495,
    }
    value = float(value)
    kilograms = float(weight_units[from_unit] * value)

    result = kilograms / weight_units[to_unit]
    result = int(result) if result == int(result) else result

    return result


def convert_temperature(value,from_unit,to_unit):
    value = float(value)
    result = None
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:
        raise ValueError("Invalid from_unit")

    if to_unit == "celsius":
        result = celsius
    elif to_unit == "fahrenheit":
        result = ((celsius * 9 / 5) + 32)
    elif to_unit == "kelvin":
        result = (celsius + 273.15)
    else:
        raise ValueError("Invalid to_unit")
    
    result = int(result) if result == int(result) else result
    return result



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/length",methods = ['GET','POST']) 
def length():
    result = None
    value = 0
    from_unit = ""
    to_unit = ""
    if request.method == 'POST':
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        result = convert_length(value,from_unit,to_unit)



    return render_template(
        "length.html",
        result = result,
        value= int(value) if int(value) == value else value,
        from_unit=from_unit,
        to_unit=to_unit
    )



@app.route("/weight",methods = ['GET','POST'])
def weight():
    result = None
    value = 0
    from_unit = ""
    to_unit = ""
    if request.method == 'POST':
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        result = convert_weight(value,from_unit,to_unit)  
    return render_template(
        "weight.html",
        result=result,
        value=int(value) if int(value) == value else value,
        from_unit=from_unit,
        to_unit=to_unit
    )




@app.route("/temperature",methods = ['GET','POST'])
def tempreture():
    result = None
    value = 0
    from_unit = ""
    to_unit = ""
    if request.method == 'POST':
        value = float(request.form["value"])
        from_unit = request.form["from_unit"]
        to_unit = request.form["to_unit"]
        result =  convert_temperature(value,from_unit,to_unit)  
    return render_template(
        "temperature.html",
        result=result,
        value = int(value) if int(value) == value else value,
        from_unit=from_unit,
        to_unit=to_unit
    )

if __name__ == "__main__":
    app.run(debug=True)