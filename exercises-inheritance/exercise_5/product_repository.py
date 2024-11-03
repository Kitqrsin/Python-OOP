from product import Product


class ProductRepository:
    products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for curr_product in self.products:
            if curr_product.name == product_name:
                return curr_product

    def remove(self, product_name: str):
        for curr_product in self.products:
            if curr_product.name == product_name:
                self.products.remove(curr_product)

    def __repr__(self):

        list_result = '\n'.join([f"{el.name}: {el.quantity}" for el in self.products])
        return list_result
