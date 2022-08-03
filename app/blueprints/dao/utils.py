from db.db_init import db
from db.models import User, Offer, Order

def get_all_users_list():
    """Возвращает список со словарями-данными всех юзеров"""
    all_users = db.session.query(User).all()
    to_return = [user.to_dict() for user in all_users]
    return to_return

def get_user_by_id(id):
    """Возвращает словарь-юзера с указанным id"""
    user = db.session.query(User).get(id)
    # если юзер найден
    if user:
        return user.to_dict()
    return None

def get_all_orders_list():
    """Возвращает список со словарями-данными всех заказов"""
    all_orders = db.session.query(Order).all()
    to_return = [order.to_dict() for order in all_orders]
    return to_return

def get_order_by_id(id):
    """Возвращает словарь-заказ с указанным id"""
    order = db.session.query(Order).get(id)
    if order:
        return order.to_dict()
    return None

def get_all_offers_list():
    """Возвращает список со словарями-данными всех предложений"""
    all_offers = db.session.query(Offer).all()
    to_return = [offer.to_dict() for offer in all_offers]
    return to_return

def get_offer_by_id(id):
    """Возвращает словарь-предложение с указанным id"""
    offer = db.session.query(Offer).get(id)
    if offer:
        return offer.to_dict()
    return None


def add_new_user_to_db(user_data: dict):
    """Добавляет нового пользователя с данными из user_data"""
    # Валидация на наличие аттрибутов (колонок) в таблице
    for key in user_data.keys():
        try:
            getattr(User, key)
        except AttributeError:
            raise AttributeError(f'В таблице User отсутствует поле {key}')

    new_user = [User(**user_data)][0]
    db.session.add(new_user)
    db.session.commit()
    return {"status": "User added successfully", "User": new_user.to_dict()}

def update_user_info(user_id, data):
    """Обновляет данные пользователя на новые"""
    user = db.session.query(User).get(user_id)
    if not user:
        raise IndexError(f"Пользователь с id {user_id} в базе не найден")

    for k, v in data.items():
        try:
            getattr(user, k)
        except AttributeError:
            raise AttributeError(f'У пользователя отсутствует поле {k}')
        setattr(user, k, v)

    db.session.commit()
    return {"status": "User info changed successfully", "User": user.to_dict()}

def delete_user_from_db(user_id):
    """Удаляет пользователя с указанным id"""
    user = db.session.query(User).get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {"status": "User deleted successfully"}
    raise IndexError(f"Пользователь с id {user_id} в базе не найден")



#orders
def add_new_order_to_db(order_data: dict):
    """Добавляет новый заказ с данными из user_data"""
    # Валидация на наличие аттрибутов (колонок) в таблице
    for key in order_data.keys():
        try:
            getattr(Order, key)
        except AttributeError:
            raise AttributeError(f'В таблице Order отсутствует поле {key}')

    # ПРОВЕРКИ на наличие пользователей
    if not User.query.get(order_data['customer_id']):
        raise IndexError(f"Заказчик с id {order_data['customer_id']} в базе не найден")

    if not User.query.get(order_data['executor_id']):
        raise IndexError(f"Исполнитель с id {order_data['executor_id']} в базе не найден")


    new_order = [Order(**order_data)][0]
    db.session.add(new_order)
    db.session.commit()
    return {"status": "Order added successfully", "Order": new_order.to_dict()}

def update_order_info(order_id, data):
    """Обновляет данные заказа на новые"""
    order = db.session.query(Order).get(order_id)
    if not order:
        raise IndexError(f"Заказ с id {order_id} в базе не найден")

    for k, v in data.items():
        try:
            getattr(order, k)
        except AttributeError:
            raise AttributeError(f'У заказа отсутствует поле {k}')

        if not User.query.get(data['customer_id']):
            raise IndexError(f"Заказчик с id {data['customer_id']} в базе не найден")

        if not User.query.get(data['executor_id']):
            raise IndexError(f"Исполнитель с id {data['executor_id']} в базе не найден")
        setattr(order, k, v)

    db.session.commit()
    return {"status": "Order info changed successfully", "Order": order.to_dict()}

def delete_order_from_db(order_id):
    """Удаляет заказ с указанным id"""
    order = db.session.query(Order).get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return {"status": "Order deleted successfully"}
    raise IndexError(f"Пользователь с id {order_id} в базе не найден")

#offers
def add_new_offer_to_db(offer_data: dict):
    """Добавляет новое предложение с данными из offer_data"""
    # Валидация на наличие аттрибутов (колонок) в таблице
    for key in offer_data.keys():
        try:
            getattr(Offer, key)
        except AttributeError:
            raise AttributeError(f'В таблице Offer отсутствует поле {key}')

    # ПРОВЕРКИ на наличие пользователя и заказа
    if not User.query.get(offer_data['executor_id']):
        raise IndexError(f"Исполнитель с id {offer_data['executor_id']} в базе не найден")

    if not Order.query.get(offer_data['order_id']):
        raise IndexError(f"Заказ с id {offer_data['order_id']} в базе не найден")


    new_offer = [Offer(**offer_data)][0]
    db.session.add(new_offer)
    db.session.commit()
    return {"status": "Offer added successfully", "Offer": new_offer.to_dict()}

def update_offer_info(offer_id, data):
    """Обновляет данные предложения на новые"""
    offer = db.session.query(Offer).get(offer_id)
    if not offer:
        raise IndexError(f"Предложение с id {offer_id} в базе не найден")

    for k, v in data.items():
        try:
            getattr(offer, k)
        except AttributeError:
            raise AttributeError(f'У предложения отсутствует поле {k}')
        if not User.query.get(data['executor_id']):
            raise IndexError(f"Исполнитель с id {data['executor_id']} в базе не найден")
        if not Order.query.get(data['order_id']):
            raise IndexError(f"Заказ с id {data['order_id']} в базе не найден")
        setattr(offer, k, v)
    db.session.commit()
    return {"status": "Offer info changed successfully", "Offer": offer.to_dict()}

def delete_offer_from_db(offer_id):
    """Удаляет предложение с указанным id"""
    offer = db.session.query(Offer).get(offer_id)
    if offer:
        db.session.delete(offer)
        db.session.commit()
        return {"status": "Offer deleted successfully"}
    raise IndexError(f"Предложение с id {offer_id} в базе не найден")