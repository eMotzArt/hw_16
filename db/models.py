from db.db_init import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    age = db.Column(db.SmallInteger)
    email = db.Column(db.String(255))
    role = db.Column(db.String(255))
    phone = db.Column(db.String(255))

    #связи, при удалении юзера -> каскадное удаление связанных офферов и ордеров, в которых юзер указан как fk
    as_executor_in_offers = db.relationship('Offer', back_populates="executor", cascade='all, delete', foreign_keys="Offer.executor_id")
    as_customer_in_orders = db.relationship("Order", back_populates="customer", cascade='all, delete', foreign_keys="Order.customer_id")
    as_executor_in_orders = db.relationship("Order", back_populates="executor", cascade='all, delete', foreign_keys="Order.executor_id")

    @staticmethod
    def attrs():
        return ['id', 'first_name', 'last_name', 'age', 'email', 'role', 'phone']

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }

class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.String)
    price = db.Column(db.Integer, db.CheckConstraint('price > 0'))

    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    customer: User = db.relationship('User', back_populates="as_customer_in_orders", foreign_keys=[customer_id])
    executor: User = db.relationship('User', back_populates="as_executor_in_orders", foreign_keys=[executor_id])

    #связи, при удалении ордера -> каскадное удаление связанных офферов, в которых ордер указан как fk
    as_order_in_offers = db.relationship('Offer', back_populates="order", cascade='all, delete')

    @staticmethod
    def attrs():
        return ['id', 'name', 'description', 'start_date', 'end_date', 'address', 'price', 'customer_id', 'executor_id']

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "customer_name": self.customer.to_dict()['first_name'],
            "executor_id": self.executor_id,
            "executor_name": self.executor.to_dict()['first_name'],
        }

class Offer(db.Model):
    __tablename__ = 'offer'

    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    order: Order = db.relationship('Order', back_populates="as_order_in_offers", foreign_keys=[order_id])
    executor: User = db.relationship('User', back_populates="as_executor_in_offers", foreign_keys=[executor_id])

    @staticmethod
    def attrs():
        return ['id', 'order_id', 'executor_id']

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "order_info": self.order.to_dict(),
            "executor_id": self.executor_id,
            "executor_info": self.executor.to_dict()
        }