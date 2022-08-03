from db.db_init import db
from db.models import User, Offer, Order

class User_db_worker:
    def __init__(self):
        self.target = User

    def get_all(self):
        """Возвращает список со словарями-данными всех сущностей класса <self.target>"""
        all = db.session.query(self.target).all()
        return [item.to_dict() for item in all]

    def get_by_id(self, id):
        """Возвращает словарь c сущностью класса <self.target> с указанным id"""
        item_by_id = db.session.query(self.target).get(id)
        return item_by_id.to_dict() if item_by_id else None

    def add(self, data):
        """Добавляет новую сущность к <self.target>"""
        for attr in data.keys():
            if not (attr in self.target.attrs()):
                raise AttributeError(f'В таблице отсутствует поле {attr}, либо отсутствует доступ к полю')

        new_item = [self.target(**data)][0]
        db.session.add(new_item)
        db.session.commit()
        return {"status": "Item added successfully", "new_item": new_item.to_dict()}

    def update(self, id, data):
        """Обновляет данные сущности класса <self.target>"""
        item = db.session.query(self.target).get(id)
        if not item:
            raise IndexError(f"Элемент с id {id} в базе не найден")

        for attribute, new_value in data.items():
            if attribute not in self.target.attrs():
                raise AttributeError(f'У таблицы отсутствует поле {attribute}')
            setattr(item, attribute, new_value)

        db.session.commit()
        return {"status": "Info changed successfully", "changed_item": item.to_dict()}

    def delete(self, id):
        """Удаляет сущность класса <self.target> с указанным id"""
        item = db.session.query(self.target).get(id)

        if not item:
            raise IndexError(f"Элемент с id {id} в базе не найден")

        db.session.delete(item)
        db.session.commit()
        return {"status": "Item deleted successfully"}

class Order_db_worker(User_db_worker):
    def __init__(self):
        self.target = Order

class Offer_db_worker (User_db_worker):
    def __init__(self):
        self.target = Offer
