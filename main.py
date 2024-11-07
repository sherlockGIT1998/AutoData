from flask import Flask, jsonify, render_template, request

from project_app.utils import AutoCarPrice

app = Flask(__name__) 

@app.route("/")    # home Api
def hello_flask():
    print("Welcome to Car Price Prediction Model")
    return render_template("auto.html")   

@app.route("/predict_prices",methods = ["POST", "GET"])
def get_car_prices():
    if request.method == "GET":
        print("We are in a GET Method")

        normalized_losses = eval(request.args.get("normalized_losses"))
        fuel_type  = request.args.get("fuel_type")
        aspiration =  request.args.get("aspiration")
        num_of_doors = request.args.get("num_of_doors")
        drive_wheels  = request.args.get("drive_wheels")
        engine_location = request.args.get("engine_location") 
        width = eval(request.args.get("width"))
        num_of_cylinders = request.args.get("num_of_cylinders")
        engine_size = eval(request.args.get("engine_size"))
        stroke = eval(request.args.get("stroke"))
        compression_ratio = eval(request.args.get("compression_ratio"))
        horsepower = eval(request.args.get("horsepower"))
        peak_rpm =  eval(request.args.get("peak_rpm"))
        city_mpg  = eval(request.args.get("city_mpg"))
        highway_mpg  = eval(request.args.get("highway_mpg"))
    
        make = request.args.get("make")
        body_style = request.args.get("body_style")
        engine_type =  request.args.get("engine_type")
        fuel_system = request.args.get("fuel_system")

        print("normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,width,num_of_cylinders,engine_size,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,fuel_system",normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,width,num_of_cylinders,engine_size,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,fuel_system)

        
        car_price = AutoCarPrice(normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,width,num_of_cylinders,engine_size,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,fuel_system)

        price = car_price.get_predicted_price()

        return render_template("auto.html", prediction = price )
    
    else:
        print("We are in a POST Method")

        
        normalized_losses = eval(request.args.get("normalized_losses"))
        fuel_type  = request.args.get("fuel_type")
        aspiration =  request.args.get("aspiration")
        num_of_doors = request.args.get("num_of_doors")
        drive_wheels  = request.args.get("drive_wheels")
        engine_location = request.args.get("engine_location") 
        width = eval(request.args.get("width"))
        num_of_cylinders = request.args.get("num_of_cylinders")
        engine_size = eval(request.args.get("engine_size"))
        stroke = eval(request.args.get("stroke"))
        compression_ratio = eval(request.args.get("compression_ratio"))
        horsepower = eval(request.args.get("horsepower"))
        peak_rpm =  eval(request.args.get("peak_rpm"))
        city_mpg  = eval(request.args.get("city_mpg"))
        highway_mpg  = eval(request.args.get("highway_mpg"))
    
        make = request.args.get("make")
        body_style = request.args.get("body_style")
        engine_type =  request.args.get("engine_type")
        fuel_system = request.args.get("fuel_system")

        print("normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,width,num_of_cylinders,engine_size,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,fuel_system",normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,width,num_of_cylinders,engine_size,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,fuel_system)

        
        car_price = AutoCarPrice(normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,width,num_of_cylinders,engine_size,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,fuel_system)

        price = car_price.get_predicted_price()

        return render_template("auto.html", prediction= price)
    
    


print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run()


     