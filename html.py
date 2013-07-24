import HTML
import db_connector

table_data = [
        [db_connector.row[0]]
    ]

htmlcode = HTML.table(table_data)

def print_html(self):
    return htmlcode
