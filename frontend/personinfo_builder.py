from data.data_access import LocalData as Data

class PersonInfoBuilder():

    person_table_headers =  "<tr>" \
                            "<th>Name</th>" \
                            "<th>Birthday</th>" \
                            "<th>Police</th>" \
                            "<th>Address</th>" \
                            "</tr>"

    person_table_rows = "<tr>" \
                        "<td>{name}</td>" \
                        "<td>{birthday}</td>" \
                        "<td>{police}</td>" \
                        "<td>{address}</td>" \
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

    damage_table_rows_format = "<tr>" \
                               "<td>{damage_no}</td>" \
                               "<td>{damage_group}</td>" \
                               "<td>{damage_type}</td>" \
                               "<td>{damage_date}</td>" \
                               "<td>{damage_kind}</td>" \
                               "<td>{damage_reason}</td>" \
                               "<td bgcolor = \"{rule_color}\">{rule_reason}</td>" \
                               "<td bgcolor = \"{ml_color}\">{ml_prob}</td>" \
                               "</tr>"

    damage_table_rows = ""

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
            damage_case = Data.damage_cases[damage]
            if damage_case["ml_fraud"]:
                damage_case["ml_color"] = "#FF0000"
            else:
                damage_case["ml_color"] = "#00FF00"

            if damage_case["rule_fraud"]:
                damage_case["rule_color"] = "#FF0000"
            else:
                damage_case["rule_color"] = "#00FF00"

            self.damage_table_rows += self.damage_table_rows_format.format(damage_case)

    def toString(self):
        return self.html_header + \
               self.person_table_headers + \
               self.person_table_rows + \
               self.damage_table_headers + \
               self.damage_table_rows + \
               self.html_footer
