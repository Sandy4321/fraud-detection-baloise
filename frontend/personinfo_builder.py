from data.data_access import LocalData as Data

class PersonInfoBuilder():

    person_table_headers =  "<tr>" \
                            "<th>Name</th>" \
                            "<th>Birthday</th>" \
                            "<th>Police</th>" \
                            "<th>Address</th>" \
                            "</tr>"

    person_table_rows = "<tr>" \
                        "<th>{name}</th>" \
                        "<th>{birthday}</th>" \
                        "<th>{police}</th>" \
                        "<th>{address}</th>" \
                        "</tr>"

    damage_table_headers = "<tr>" \
                           "<th>Damage Number</th>" \
                           "<th>Damage Group</th>" \
                           "<th>Damage Type</th>" \
                           "<th>Damage Date</th>" \
                           "<th>Damage Kind</th>" \
                           "<th>Damage Reason</th>" \
                           "<th>Feedback Rules</th>" \
                           "<th>Feedback Learning</th>" \
                           "</tr>"

    damage_table_rows = "<tr>" \
                        "<th>{name}</th>" \
                        "<th>{birthday}</th>" \
                        "<th>{police}</th>" \
                        "<th>{address}</th>" \
                        "</tr>"

    html_header = "" \
                  "<!DOCTYPE html>"  \
                  "<html lang=\"en\">" \
                    "<head>"  \
                    "<meta charset=\"UTF-8\">"  \
                    "<title>New damage case</title>"  \
                    "<link rel=\"stylesheet\" href=\"bootstrap.css\">"  \
                    "</head>"  \
                    "<body>"  \
                    "<table>"

    html_footer = ""

    def buildPersonInfo(self, police):
        self.person_table_rows = self.person_table_rows.format(Data.customers[police])
        damages = Data.customers[police]["damage_cases"]
        for damage in damages:
            #TODO: Add row for each damage_case
            pass
        return NotImplemented

    def toString(self):
        return self.html_header + \
               self.person_table_headers + \
               self.person_table_rows + \
               self.damage_table_headers + \
               self.damage_table_rows + \
               self.html_footer
