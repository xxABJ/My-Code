import json, sys, os
from datetime import datetime

#LOGFILE_PATH = ""

class test:
    class_var = "lol"
    alass_var2 = "lool"
    var_class3 = "loool"

    def __init__(self):
        self.one = "one"
        self.two = 2
        self.three = 3.098
    
    def tt(self):
        pass
    def tt1():
        pass
    def ar3(self):
        pass


class test2:
    def __init__(self):
        pass

# TODO: Find a way to make the class be able to log other objects without executing/calling extra commands
class Log:
    LOGFILE_PATH = ""
    LOGFILE_NAME = "Logs.json"
    TEMPLATE = {
        f"_logs.json (Created at {datetime.now()})":{
            "object":{
            }
        }
    }


    def __init__(self, obj= None):
        self.object = obj
        self.class_attributes = []
        #print(f"super().__init__(): {super().__init__()}")
        #for self_arg, value in super().__init__():
        #    attribute = setattr(self_arg, value)
        #    self.class_attributes.append(str(attribute))
        print(self.object)


        self.default_logfile_path = "_logs"
        
        self.json_file()
        self.logfile_data = self.load_json()
        self.check_oject_in_logfile = self.check_object(obj)


    def json_file(self):
        print(f"\n\n {" Accessing Log file:"::>22}\n {f" {Log.LOGFILE_PATH}/{Log.LOGFILE_NAME}"::>14}")

        try:
            load_test = self.load_json()
            print(f" {" Successful.":=>16}\n\n")
            

        except:
            print(f" {" Failure.":x>13}\n\n {" Creating a new logfile:"::>26}\n {f" /{self.default_logfile_path}/{Log.LOGFILE_NAME}"::>20}")

            if Log.LOGFILE_PATH != "":
                # Create directory if it doesn't exist
                os.makedirs(Log.LOGFILE_PATH, exist_ok=True)
                with open(f"{Log.LOGFILE_PATH}/{Log.LOGFILE_NAME}", "x") as new_logfile:
                    json.dump(Log.TEMPLATE, new_logfile)
                print(f" {" Successful.":=>16}\n\n")


            else:
                os.makedirs(self.default_logfile_path, exist_ok=True)
                with open(f"{self.default_logfile_path}/{Log.LOGFILE_NAME}", "x") as new_logfile:
                    json.dump(Log.TEMPLATE, new_logfile)
                    print(f" {" Successful.":=>16}\n\n")


    def load_json(self) -> dict:
        if Log.LOGFILE_PATH != "":
            with open(f"{Log.LOGFILE_PATH}/{Log.LOGFILE_NAME}", "r") as logfile:
                return json.load(logfile)
            

        else:
            with open(f"{self.default_logfile_path}/{Log.LOGFILE_NAME}", "r") as logfile:
                return json.load(logfile)
        
        #print("load json")


    # TODO: Fix if needed
    def check_object(self, obj) -> bool:
        json_logfile = Log.TEMPLATE
        for key, value in json_logfile.items():
            for k, v in value.items():
                for object_name, list in v.items():
                    if object_name == object:
                        return True
        return False


    def log_object(self, obj) -> None:

        def update_jsonfile(logfile_data, logfile_object):
            object_as_str = str(type(logfile_object)).replace("<class '__main__.", "").replace("'>", "")

            if object_as_str in logfile_data[str(list(logfile_data.keys())[0])]["object"].keys():
                pass


            else:
                logfile_data[str(list(logfile_data.keys())[0])]["object"][str(type(logfile_object)).replace("<class '__main__.", "").replace("'>", "")] = []


            if Log.LOGFILE_PATH != "":    
                with open(f"{Log.LOGFILE_PATH}/{Log.LOGFILE_NAME}", "w") as logfile:    
                    json.dump(logfile_data, logfile)
                    print(f"logfile:\n{logfile_data}")


            else:    
                with open(f"{self.default_logfile_path}/{Log.LOGFILE_NAME}", "w") as logfile:
                    json.dump(logfile_data, logfile)
                    print(f"logfile:\n{logfile_data}")
        

        if Log.LOGFILE_PATH != "":
            print(f"\n\n {" Updating Log file:":>>21}\n {f" /{Log.LOGFILE_PATH}/{Log.LOGFILE_NAME}":>>15}\n\n")


        else:
            print(f"\n\n {" Updating Log file:":>>21}\n {f" /{self.default_logfile_path}/{Log.LOGFILE_NAME}":>>20}\n\n")


        logfile_data = self.load_json()
        update_jsonfile(logfile_data= logfile_data, logfile_object= obj)
        self.check_oject_in_logfile = self.check_object(obj)
        self.logfile_data = self.load_json()
        #print(f"new: {self.logfile_data}")


    #l1 = Log()
#print(l1.check_oject_in_logfile)
#print(l1.logfile_data)

    #testobject1 = test()
#l1 = Log(testobject1)
#print(l1.check_oject_in_logfile)
#print(l1.logfile_data)

    #testobject2 = test2()
#l1 = Log(testobject2)
#print(l1.check_oject_in_logfile)
#print(l1.logfile_data)

#print(testobject1.__name__)

    #l1.log_object(testobject1)
#print(l1.check_oject_in_logfile)
#print(l1.logfile_data)

    #l1.log_object(testobject2)
#print(l1.check_oject_in_logfile)
#print(l1.logfile_data)

#testobject1 = test()
#l.object = testobject1

#t = test()
#print(help(dir(test)))

t = test()
log1 = Log()
log1.object = t
#log1.log_object()


print(log1.object.__dir__())
ll = []
for word in log1.object.__dir__():
    if not "__" in word:
        ll.append(word)
print(f"\nattribute & funcs:\n{ll}")

print(f"\natribute list:\n{list(log1.object.__static_attributes__)}")

funcs = []
cl = list(log1.object.__static_attributes__)
for func in ll:
    if func not in cl:
        funcs.append(func)
print(f"\nfuncs:\n{funcs}")

# TODO: extract attributes, funcs & class variables from the sorted log1.object.__dir__() list!

##print(log1.object.t.class_var)
        
#print(log1.object.)
    