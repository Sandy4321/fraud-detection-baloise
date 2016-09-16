from string import split

class DamageCase():

    data = None

    def generateFromFormData(self, form_data):
        self.data = {}
        form_data_split = split(form_data, "&")
        for attribute in form_data_split:
            attribute_split = split(attribute, "=")
            self.data[attribute_split[0]] = attribute_split[1]

class Person():

    #Implement person data as dictionaries i.e. get them from data_access.person
    #first the data_access.person class needs to be initialized with profie

    data = None