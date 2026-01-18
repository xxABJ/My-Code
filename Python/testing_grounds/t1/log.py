import json, sys
from datetime import datetime

#LOGFILE_PATH = ""

class test:
    def __init__(self):
        pass

class Log:
    LOGFILE_PATH = "testing_grounds/t1"
    LOGFILE_NAME = "Logs.json"
    TEMPLATE = {
        f"logs (Created at {datetime.now()})":{
            "object":{
                "":[]
            }
        }
    }

    def __init__(self, object= None):
        self.json_file()
        self.logfile_data = self.load_json()
        self.check_oject_in_logfile = self.check_object(object)
        self.object = object

    def json_file(self):
        print(f"\nAccessing Log file:\n {Log.LOGFILE_PATH}/{Log.LOGFILE_NAME}")

        try:
            #if Log.LOGFILE_PATH != "":
            with open(f"{Log.LOGFILE_NAME}", "r") as logfile:
                print("  Successful.\n")

        except:
            print(f"  Failure.\n\nCreating a new logfile:\n {Log.LOGFILE_PATH}/{Log.LOGFILE_NAME}")
            with open(f"{Log.LOGFILE_NAME}", "x") as new_logfile:
                json.dump(Log.TEMPLATE, new_logfile)
                print("  Successful.\n")

    def load_json(self) -> dict:
        print("load json")
        with open(f"{Log.LOGFILE_NAME}", "r") as logfile:
            return json.load(logfile)


    def check_object(self, object) -> bool:
        json_logfile = Log.TEMPLATE
        for key, value in json_logfile.items():
            for k, v in value.items():
                for object_name, list in v.items():
                    if object_name == object:
                        return True
        return False
    
    def log_object(self, object) -> None:
        
        
        def update_jsonfile(logfile_data, logfile_object):
            object_as_str = str(type(logfile_object)).replace("<class '__main__.", "").replace("'>", "")


            if object_as_str in logfile_data[str(list(logfile_data.keys())[0])]["object"].keys():
                #print(object_as_str)
                #print(logfile_data[str(list(logfile_data.keys())[0])]["object"].keys())
                pass
            else:
                logfile_data[str(list(logfile_data.keys())[0])]["object"] = {str(type(logfile_object)).replace("<class '__main__.", "").replace("'>", ""): []}

            
            with open(f"{Log.LOGFILE_NAME}", "w") as logfile:
                json.dump(logfile_data, logfile)
                print()
                print(f"logfile:\n{logfile_data}")
                print("  Successful.\n")
        

        print(f"\nUpdating Log file:\n {Log.LOGFILE_PATH}/{Log.LOGFILE_NAME}")
        with open(f"{Log.LOGFILE_NAME}", "r") as logfile:
            logfile_data = json.load(logfile)


        update_jsonfile(logfile_data= logfile_data, logfile_object= object)
        self.__init__()
        self.check_oject_in_logfile = self.check_object(object)
        self.logfile_data = self.load_json()
        #self.logfile_data = self.newlogfile_data
        print(f"new: {self.logfile_data}")
        #return self


l1 = Log()
print(l1.check_oject_in_logfile)
print(l1.logfile_data)

testobject1 = test()
l1 = Log(testobject1)
print(l1.check_oject_in_logfile)
print(l1.logfile_data)

#print(testobject1.__name__)

l1.log_object(testobject1)
print(l1.check_oject_in_logfile)
print(l1.logfile_data)

#testobject1 = test()
#l.object = testobject1
    