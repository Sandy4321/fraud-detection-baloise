from string import split

class DamageCase():

    data = None

    def generateFromFormData(self, form_data):
        self.data = {}
        form_data_split = split(form_data, "&")
        for attribute in form_data_split:
            attribute_split = split(attribute, "=")
            self.data[attribute_split[0]] = attribute_split[1]
