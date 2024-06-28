from myproject.news.models import Order, Product, Client


def create_client(name, email, phone_number, address):
    """Создает нового клиента."""
    client = Client.objects.create(
        name=name, email=email, phone_number=phone_number, address=address
    )
    return client

def get_client_by_id(client_id):
    """Возвращает клиента по его ID."""
    try:
        client = Client.objects.get(pk=client_id)
        return client
    except Client.DoesNotExist:
        return None

def update_client(client_id, name=None, email=None, phone_number=None, address=None):
    """Обновляет данные клиента."""
    client = get_client_by_id(client_id)
    if client:
        if name:
            client.name = name
        if email:
            client.email = email
        if phone_number:
            client.phone_number = phone_number
        if address:
            client.address = address
        client.save()
        return client
    return None

def delete_client(client_id):
    """Удаляет клиента по его ID."""
    client = get_client_by_id(client_id)
    if client:
        client.delete()
        return True
    return False

def create_product(name, description, price, quantity):
    """Создает новый товар."""
    product = Product.objects.create(
        name=name, description=description, price=price, quantity=quantity
    )
    return product

def get_product_by_id(product_id):
    """Возвращает товар по его ID."""
    try:
        product = Product.objects.get(pk=product_id)
        return product
    except Product.DoesNotExist:
        return None

def update_product(product_id, name=None, description=None, price=None, quantity=None):
    """Обновляет данные товара."""
    product = get_product_by_id(product_id)
    if product:
        if name:
            product.name = name
        if description:
            product.description = description
        if price:
            product.price = price
        if quantity:
            product.quantity = quantity
        product.save()
        return product
    return None

def delete_product(product_id):
    """Удаляет товар по его ID."""
    product = get_product_by_id(product_id)
    if product:
        product.delete()
        return True
    return False

def create_order(client_id, products, total_amount):
    """Создает новый заказ."""
    client = get_client_by_id(client_id)
    if client:
        order = Order.objects.create(client=client, total_amount=total_amount)
        for product_id, quantity in products.items():
            product = get_product_by_id(product_id)
            if product:
                order.products.add(product, through_defaults={'quantity': quantity})
        return order
    return None

def get_order_by_id(order_id):
    """Возвращает заказ по его ID."""
    try:
        order = Order.objects.get(pk=order_id)
        return order
    except Order.DoesNotExist:
        return None

def update_order(order_id, client_id=None, products=None, total_amount=None):
    """Обновляет данные заказа."""
    order = get_order_by_id(order_id)
    if order:
        if client_id:
            client = get_client_by_id(client_id)
            if client:
                order.client = client
        if products:
            order.products.clear()
            for product_id, quantity in products.items():
                product = get_product_by_id(product_id)
                if product:
                    order.products.add(product, through_defaults={'quantity': quantity})
        if total_amount:
            order.total_amount = total_amount
        order.save()
        return order
    return None

def delete_order(order_id):
    """Удаляет заказ по его ID."""
    order = get_order_by_id(order_id)
    if order:
        order.delete()
        return True
    return False