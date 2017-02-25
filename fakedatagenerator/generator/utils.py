from csv import writer
from json import dump
from random import random, choice

def generate(n_predictors, n_data_points, file_name, task="regression", file_format="txt"):
        """
        Creates a fake dataset with the given specs
        n_predictors: number of predictors - int
        n_data_points: number of observations - int
        file_name: name of output file - string
        task: regression or classification - string - default: regression
        file_format: txt or csv - string - default: txt
        return value: txt file, csv file or json file
        """
        row_header = ["y"]
        row_header.extend(["x"+str(i+1) for i in range(n_predictors)])
        length_of_header = len(row_header)
        if file_format == "txt":
            file = open(file_name+".txt", "w+")
            
            file.write(" ".join(row_header) + "\n")
            
            if task == "regression":
                for i in range(n_data_points):
                    values = [round(random(),2) for i in range(length_of_header)]
                    file.write(" ".join(map(str, values)) + "\n")
            
            elif task == "classification":
                for i in range(n_data_points):
                    values = [choice([0,1])]
                    values.extend([round(random(),2) for i in range(length_of_header-1)])
                    file.write(" ".join(map(str, values)) + "\n")
        elif file_format == "csv":
            file = open(file_name+".csv", "w+")
            datawriter = writer(file, lineterminator="\n")
            datawriter.writerow(row_header)
            if task == "regression":
                for i in range(n_data_points):
                    values = [round(random(),2) for i in range(length_of_header)]
                    datawriter.writerow(values)
            elif task == "classification":
                for i in range(n_data_points):
                    values = [choice([0,1])]
                    values.extend([round(random(),2) for i in range(length_of_header-1)])
                    datawriter.writerow(values)
                    
        elif file_format == "json":
            file = open(file_name+".json", "w+")
            json_data = {}
            for i in range(n_data_points):
                if task == "regression":
                    json_data[i+1] = {"y": round(random(),2)}
                elif task == "classification":
                    json_data[i+1] = {"y": choice([0,1])}
                for j in range(n_predictors):
                    var_name = "x"+str(j)
                    json_data[i+1][var_name] = round(random(),2)
                    
            dump(json_data, file)    
        file.close()    
        return file
    