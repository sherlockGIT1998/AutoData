import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config    

class AutoCarPrice():
    def __init__(self,normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,width,num_of_cylinders,engine_size,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,fuel_system):

        self.normalized_losses = normalized_losses 
        self.fuel_type = fuel_type 
        self.aspiration = aspiration
        self.num_of_doors = num_of_doors 
        self.drive_wheels = drive_wheels
        self.engine_location = engine_location  
        self.width = width
        self.num_of_cylinders = num_of_cylinders
        self.engine_size = engine_size
        self.stroke = stroke
        self.compression_ratio = compression_ratio
        self.horsepower= horsepower
        self.peak_rpm =peak_rpm
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg

        self.make_col = 'make_' + make
        self.body_style_col = "body-style_" + body_style 
        self.engine_type_col = 'engine-type_' + engine_type 
        self.fuel_system_col = "fuel-system_" + fuel_system 

    def load_models(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.data_save = json.load(f)

            self.column_names = np.array(self.data_save["column_names"])  # use this in finding the index of coulumn     
     

    def get_predicted_price(self):
        
        self.load_models()

        make_col_index = np.where(self.column_names == self.make_col)[0][0]
        body_style_col_index = np.where(self.column_names == self.body_style_col)[0][0]
        engine_type_col_index = np.where(self.column_names == self.engine_type_col)[0][0]
        fuel_system_col_index = np.where(self.column_names == self.fuel_system_col)[0][0]

        array = np.zeros(len(self.data_save['column_names']))
        
        array[0] = self.normalized_losses
        array[1] = self.data_save["fuel_type_select"][self.fuel_type]
        array[2] = self.data_save["aspiration_select"][self.aspiration]
        array[3] = self.data_save['num_of_doors_select'][self.num_of_doors]
        array[4] = self.data_save['drive_wheels_select'][self.drive_wheels]
        array[5] = self.data_save['engine_location_select'][self.engine_location]
        array[6] = self.width
        array[7] = self.data_save['num_of_cylinders_select'][self.num_of_cylinders]
        array[8] = self.engine_size
        array[9] = self.stroke
        array[10] = self.compression_ratio
        array[11] = self.horsepower
        array[12] = self.peak_rpm
        array[13] = self.city_mpg
        array[14] = self.highway_mpg

        array[make_col_index] = 1
        array[body_style_col_index] = 1
        array[engine_type_col_index] = 1
        array[fuel_system_col_index] = 1

        print("TEST Array -->\n", array)

        price = round(self.model.predict([array])[0],2)

        return price

if __name__ == "__main__":

    normalized_losses = 115.00
    fuel_type = 'gas'
    aspiration = 'turbo'
    num_of_doors = 'four'
    drive_wheels = 'fwd'
    engine_location = 'front'
    width = 64.10
    num_of_cylinders = 'four'
    engine_size = 130.00
    stroke = 2.68
    compression_ratio = 9.00
    horsepower = 111.00
    peak_rpm = 5000.00
    city_mpg = 21.00
    highway_mpg = 27.00

    make = 'mercedes-benz'
    body_style = 'sedan'
    engine_type = 'rotor'
    fuel_system = 'mpfi'

    car_price = AutoCarPrice(normalized_losses,fuel_type,aspiration,num_of_doors,drive_wheels,engine_location,width,num_of_cylinders,engine_size,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,make,body_style,engine_type,fuel_system)

    price = car_price.get_predicted_price()
    print("PRICE of Your Dream CAR would be: $", round(price , 2))
        


