#gaim settings like speed of the game are defined here
class GaimSettings():
    def __init__(self):
        pass

    def create_game():
        pass

    def ask_name():
        pass

    def drop_speed_of_the_shape():
        pass

    # When shape stops the function checks whether the row should be deleted.
    def check_row():
        pass

    def save_result(self, name, result):
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
        result=0
        with open("results.csv") as results:
            for line in results:
                line=line.replace("\n","")
                parts=line.split(";")
                if parts[0]==name:
                    result=parts[1]
        return result


