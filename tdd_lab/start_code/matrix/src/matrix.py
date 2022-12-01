class Matrix:
    def __init__(self, input_matrix_string):
        self.matrix_string = input_matrix_string

    # Methods:
    def return_matrix_by_row(self):
        print(self.matrix_string.splitlines())
        return self.matrix_string.splitlines()

    def return_matrix_by_column(self):
        return_list = []
        rows = self.return_matrix_by_row() #returns list - ["1 2 3", "4 5 6", "7 8 9"]
        editing_column = 0 #used to splice the string 'rows'
        column_string = "" #
        while editing_column < len(rows[0]): #We don't know how long the matrix will be so need a while...
            for row in rows: # row = ["1 2 3"]
                column_string += row[editing_column] # = "1"
                column_string += " "
            #format and add to return list
            formatted_column_string = column_string.strip()
            return_list.append(formatted_column_string) #add "1 "
            #reset and go to next column
            column_string = ""
            editing_column += 2
        return return_list

    def row(self, index):
        pass

    def column(self, index):
        pass
