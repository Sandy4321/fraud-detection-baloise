from data.data_access import LocalData as Data

class PersonInfoBuilder():

    person_table_headers =  "<tr>" \
                            "<th>Name</th>" \
                            "<th>Geburtstag</th>" \
                            "<th>Policenummer</th>" \
                            "<th>Adresse</th>" \
                            "</tr>"

    person_table_rows = "<tr>" \
                        "<td>{{name}}</td>" \
                        "<td>{{birthday}}</td>" \
                        "<td>{{police}}</td>" \
                        "<td>{{address}}</td>" \
                        "</tr>"

    damage_table_headers = "<tr>" \
                           "<th>Schadennumnmber</th>" \
                           "<th>Versicherungsartengruppe</th>" \
                           "<th>Versicherungsart</th>" \
                           "<th>Schadendatum</th>" \
                           "<th>Schadenart</th>" \
                           "<th>Schadenursache</th>" \
                           "<th>Feedback Vorlagekriterien</th>" \
                           "<th>Feedback Machine Learning</th>" \
                           "</tr>"

    damage_table_rows_format = "<tr>" \
                               "<td>{{damage_no}}</td>" \
                               "<td>{{damage_group}}</td>" \
                               "<td>{{damage_type}}</td>" \
                               "<td>{{damage_date}}</td>" \
                               "<td>{{damage_kind}}</td>" \
                               "<td>{{damage_reason}}</td>" \
                               "<td bgcolor = \"{{rule_color}}\">{{rule_reason}}</td>" \
                               "<td bgcolor = \"{{ml_color}}\">{{ml_prob}}</td>" \
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
        data = Data()
        person_data = data.customers[int(police)]
        print (person_data["name"])
        self.person_table_rows = self.person_table_rows.format(person_data)
        damages = data.customers[int(police)]["damage_cases"]
        for damage in damages:
            damage_case = data.damage_cases[damage]
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
