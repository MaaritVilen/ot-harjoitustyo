"""The module defines basic game setup elements"""

class GaimSettings():
    """Defines some basic game setup elements"""
    def __init__(self):
        self.speed=30

    def speed_of_the_shape(self, scores):
        """Controls the speed of the game"""
        if scores<30:
            self.speed=30
        elif scores>=30<60:
            self.speed=45
        else:
            self.speed=60
        return self.speed

    def save_result(self, name, result):
        """Saves the result of the game"""
        new_name="yes"
        new_result="no"
        with open("results.csv") as results:
            new_list=[]
            for line in results:
                sub_list=[]
                line=line.replace("\n","")
                parts=line.split(";")
                for part in parts:
                    sub_list.append(part)
                if sub_list[0]==name:
                    new_name="no"
                    if int(sub_list[1])<result:
                        new_result="yes"
                        sub_list[1]=result
                new_list.append(sub_list)

        if new_name=="yes":
            with open("results.csv","a") as updated_results:
                updated_results.write(f"{name};{result}\n")
        elif new_result=="yes":
            with open("results.csv", "w") as updated_results:
                for line in new_list:
                    updated_results.write(f"{line[0]};{line[1]}\n")

    def previous_results(self,name):
        """Gets previous result of the game from file"""
        result=0
        with open("results.csv") as results:
            for line in results:
                line=line.replace("\n","")
                parts=line.split(";")
                if parts[0]==name:
                    result=parts[1]
        return result
    