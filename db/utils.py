import json
from db.db_init import db

def fill_db(data_file: str, table_name: db.Model):
    with open(data_file) as file:
        data = json.load(file)

    list_to_append = [table_name(**kwarg) for kwarg in data]
    for item in list_to_append:
        db.session.add(item)
        db.session.commit()
    # db.session.add_all(list_to_append)
    # db.session.commit()
    print(db.session.query(table_name).all())
    db.session.close()