import json, sys, os
from datetime import datetime

#LOGFILE_PATH = ""

class test:
    class_var = "lol"
    alass_var2 = "lool"
    var_class3 = "loool"

    def __init__(self):
        self.string= "oaaaa"
        self.int = 2
        self.float= 33.021213123
        # TODO: fix callable() in the Log file, to accept multiple func states and make it return that it is a method and if it returns something or not @F
        self.fanccall = self.tt
        self.fanccall2 = self.tt1()
        self.fanccall3 = self.ar3()
    
    def tt(self):
        a = []
        return a
    def tt1(self):
        return
    def ar3(self):
        return


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
        self.object = self.object_extraction(obj)
        self.class_attributes = []
        #print(f"super().__init__(): {super().__init__()}")
        #for self_arg, value in super().__init__():
        #    attribute = setattr(self_arg, value)
        #    self.class_attributes.append(str(attribute))
        print(f"self.object.__name__: {self.object}")


        self.default_logfile_path = "_logs"
        
        self.json_file()
        self.logfile_data = self.load_json()
        self.check_oject_in_logfile = self.check_object(obj)

    # TODO: Check for cls. ?
    # TODO: Other specific checks ?
    def object_extraction(self, object):
        

        #print(object.__dir__())
        print(f"\n\nattribute & funcs:")
        ll = []
        for word in object.__dir__():
            if not "__" in word:
                ll.append(word)
        print(f"{ll}\n")
        #print(f"\natribute list:\n{list(object.)}")
        #print(f"\natribute list:\n{list(object.__static_attributes__)}")
        


        print(f"\natribute list:")
        longest_attribute_length = 0
        longest_value_length = 0
        longest_float_concantenation_length = 1
        for attribute in list(object.__static_attributes__):
            
            
            if not callable(getattr(object, attribute)):
                #longest attribute_length setter
                accountingfor_selfandpoint_in_attribute_variable = 5
                new_attribute_length = (len(attribute) + accountingfor_selfandpoint_in_attribute_variable)
                if new_attribute_length > longest_attribute_length:
                    longest_attribute_length = new_attribute_length
                

                #longest value_length setter
                new_value_length = len(str(getattr(object, attribute)))
                if new_value_length > longest_value_length:
                    longest_value_length = new_value_length


                #longest float_concatenation_length setter
                floaat = ""
                for key, value in enumerate(str(getattr(object, attribute))):
                    floaat += value
                # Check if the string can be converted to a number
                try: # float or int @F
                    new_float_concantenation_length = len(str(int(float(floaat))))
                    if new_float_concantenation_length > longest_float_concantenation_length:
                        longest_float_concantenation_length = new_float_concantenation_length
                except ValueError: # strings
                    # Skip conversion for non-numeric strings
                    pass
                #if new_float_concantenation_length > longest_float_concantenation_length:
                #    longest_float_concantenation_length = new_float_concantenation_length


            else:
                # attribute is a func
                pass


        # Acheiving synamic formating spaces & printing back in terimal !
        for attribute in list(object.__static_attributes__): 
            
            
            accountingfor_decimalpoint = 1
            accountingfor_floatdecimalplaces = 0
            accountingfor_selfandpoint_in_attribute_variable = 5


            attribute_length = (len(attribute) + accountingfor_selfandpoint_in_attribute_variable)
            value_length = len(str(getattr(object, attribute)))
            
            
            # TODO: wtf is this, try to calculate better -.-
            if type(getattr(object, attribute)) == float:
                accountingfor_floatdecimalplaces = (len(str(getattr(object, attribute))) - longest_float_concantenation_length - accountingfor_decimalpoint)
                formatting_spacing = (longest_attribute_length + value_length - accountingfor_floatdecimalplaces) - value_length + (longest_value_length - value_length) + (longest_attribute_length - attribute_length) + accountingfor_floatdecimalplaces
            
            
            # TODO: wtf is this, try to calculate better -.-
            elif type(getattr(object, attribute)) == int:
                formatting_spacing_old = (longest_attribute_length - value_length)
                formatting_spacing = ((longest_attribute_length - value_length) + (longest_attribute_length - formatting_spacing_old)) + (longest_value_length - value_length) + (longest_attribute_length - attribute_length)

            
            # TODO: wtf is this, try to calculate better -.-
            else:
                formatting_spacing_old = (longest_attribute_length - value_length) + accountingfor_decimalpoint
                formatting_spacing_new = (longest_attribute_length - value_length) + (longest_attribute_length - formatting_spacing_old)
                formatting_spacing = (formatting_spacing_new + (accountingfor_floatdecimalplaces + accountingfor_decimalpoint + value_length)) - (longest_attribute_length - formatting_spacing_new) - value_length + (longest_value_length - value_length) + (longest_attribute_length - attribute_length) + accountingfor_decimalpoint
            

            #print(f"longest_float_number_concantenation_length: {longest_float_concantenation_length}")
            #print(f"formatting_spacing: {formatting_spacing}")
            #print(f"longest_attribute_length: {longest_attribute_length}")
            #print(f"longest_value_length: {longest_value_length}")
            #print(f"value_length: {value_length}")


            # TODO: Try to add dynamic formatting spaces :') @F
            if callable(getattr(object, attribute)):
                #print("callable")
                #print(getattr(object, attribute))
                #print(f"self.{attribute} = {str(getattr(object, attribute)): >{length}}{f' -> Type {str(type(getattr(object, attribute))): >5}'}")
                object_as_str = str(type(object)).replace("<class '__main__.", "").replace("'>", "")
                func_as_str = ""
                func_lenth = 0


                remove_beginning = str(getattr(object, attribute)).replace("<bound method ", "")
                replace_name_of_object = remove_beginning.replace(object_as_str, "")
                #replace_object_with_self = remove_beginning.replace(object_as_str, "self")
                #print(remove_beginning)
                #print(replace_name_of_object)
                

                for key, value in enumerate(replace_name_of_object):
                    if value != " ":
                        func_as_str += value
                        func_lenth += 1
                    else:
                        break


                #print(f"func_as_str: {func_as_str}")
                #print(f"func_lenth+6: {func_lenth+6}")
                print(f"self.{attribute} = {"self"+func_as_str+"()": >{func_lenth+6}}{f'-> Type {str(type(getattr(object, attribute))): >{15}}'}")
                #print()
                continue

            else:
                #print(f"self.{attribute} = {str(getattr(object, attribute)): >{length}}{f'  -> Type {str(type(getattr(object, attribute))): >{15}}'}")
                print(f"self.{attribute} = {"": <{formatting_spacing}}{str(getattr(object, attribute))}{f'-> Type {str(type(getattr(object, attribute))): >{15}}'}")
            




        print(f"\n\nfuncs:")
        funcs = []
        cl = list(object.__static_attributes__)
        for func in ll:
            if func not in cl:
                funcs.append(func)
        print(f"{funcs}\n\n")


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
log1 = Log(t)
#log1.object = t
#log1.log_object()

#print(t.one)
#print(t.two0)
#print(t.three)

#print(log1.object.__dir__())
#ll = []
#for word in log1.object.__dir__():
#    if not "__" in word:
#        ll.append(word)
#print(f"\nattribute & funcs:\n{ll}")
#
#print(f"\natribute list:\n{list(log1.object.__static_attributes__)}")
#
#funcs = []
#cl = list(log1.object.__static_attributes__)
#for func in ll:
#    if func not in cl:
#        funcs.append(func)
#print(f"\nfuncs:\n{funcs}")

# TODO: extract attributes, funcs & class variables from the sorted log1.object.__dir__() list!

##print(log1.object.t.class_var)
        
#print(log1.object.)
    