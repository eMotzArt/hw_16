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

    as_executor_in_offers = db.relationship('Offer', cascade='all, delete')
    as_customer_in_orders = db.relationship("Order", cascade='all, delete', foreign_keys="Order.customer_id")
    as_executor_in_orders = db.relationship("Order", cascade='all, delete', foreign_keys="Order.executor_id")

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

    customer: User = db.relationship('User', foreign_keys=[customer_id])
    executor: User = db.relationship('User', foreign_keys=[executor_id])

    as_order_in_offers = db.relationship('Offer', cascade='all, delete')


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
            "customer_info": self.customer.to_dict(),
            "executor_id": self.executor_id,
            "executor_info": self.executor.to_dict(),
        }

class Offer(db.Model):
    __tablename__ = 'offer'

    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    order: Order = db.relationship('Order', foreign_keys=[order_id])
    executor: User = db.relationship('User', foreign_keys=[executor_id])


    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "order_info": self.order.to_dict(),
            "executor_id": self.executor_id,
            "executor_info": self.executor.to_dict()
        }