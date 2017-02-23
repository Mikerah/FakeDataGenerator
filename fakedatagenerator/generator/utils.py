from csv import writer
import random

def generate(n_predictors, n_data_points, file_name, task="regression", file_format="txt"):
        """
        Creates a fake dataset with the given specs
        n_predictors: number of predictors - int
        n_data_points: number of observations - int
        file_name: name of output file - string
        task: regression or classification - string - default: regression
        file_format: txt or csv - string - default: txt
        return value: txt file or csv file
        """
        row_header = ["y"]
        row_header.extend(["x"+str(i+1) for i in range(n_predictors)])
        length_of_header = len(row_header)
        if file_format == "txt":
            file = open(file_name+".txt", "w+")
            
            file.write(" ".join(row_header) + "\n")
            
            if task == "regression":
                for i in range(n_data_points):
                    values = [round(random.random(),2) for i in range(length_of_header)]
                    file.write(" ".join(map(str, values)) + "\n")
            
            elif task == "classification":
                for i in range(n_data_points):
                    values = [random.choice([0,1])]
                    values.extend([round(random.random(),2) for i in range(length_of_header-1)])
                    file.write(" ".join(map(str, values)) + "\n")
        elif file_format == "csv":
            file = open(file_name+".csv", "w+")
            datawriter = writer(file, lineterminator="\n")
            datawriter.writerow(row_header)
            if task == "regression":
                for i in range(n_data_points):
                    values = [round(random.random(),2) for i in range(length_of_header)]
                    datawriter.writerow(values)
            elif task == "classification":
                for i in range(n_data_point):
                    values = [random.choice([0,1])]
                    values.extend([round(random.random(),2) for i in range(length_of_header-1)])
                    datawriter.writerow(values)
                    
        file.close()    
        return file
    