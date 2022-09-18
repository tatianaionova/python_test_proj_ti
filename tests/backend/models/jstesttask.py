class JsTestTask():
    def __init__(product, name, image, price):
        product.name = name
        product.image = image
        product.price = price

    def __getitem__(self, key):
        return getattr(self, key)