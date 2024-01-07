"""
마트 계산 시스템

마트 계산 프로세스
- 고객이 상품을 카트에 담는다.
- 마트오너는 계산하기 전 지불 정보를 만든다.
- 고객은 지불 정보를 바탕으로 결제한다.(결제 수단은 오직 카드뿐이다.)

가이드
1. 마트 계산 시스템을 구성하는 메세지는 무엇일까?
2. 마트 계산 시스템에는 어떤 객체가 필요하고, 각 객체는 어떤 책임을 가져야할까?(Hint. 고객, 상품, 카트, 마트오너 + etc)
3. 어떻게 협력해야할까?
"""
class Product:
    """
    ### 상품
    - name
    - price
    """
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

class Cart:
    """
    ### 쇼핑 카트
    - add_item : 제품과 협력한다.
    - cal_total : 제품의 총 가격을 계산한다.
    """
    def __init__(self):
        self.items = []

    def add_item(self, product: Product, quantity: int = 1):
        self.items.append({"product": product, "quantity": quantity})

    def cal_total(self):
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        return total

class PaymentInfo:
    """
    ### 지불정보
    - total_Amount
    - card_number
    """
    def __init__(self, total_amount: int, card_number: str):
        self.total_amount = total_amount
        self.card_number = card_number

class Owner:
    """
    ### 마트 오너
    - create_payment_info : 카트의 지불정보를 생성한다.
    """
    def create_payment_info(self, cart: Cart):
        total_amount = cart.cal_total()
        return PaymentInfo(total_amount, "1234-5678-9012-3456")

class Customer:
    """
    손님
    - add_to_cart : 카트에 물건을 담는다.
    - checkout : 오너가 생성한 지불정보로 결제 함수를 실행한다.
    - pay : 지불정보로 결제한다.
    """
    def __init__(self):
        self.cart = Cart()

    def add_to_cart(self, product: Product, quantity: int = 1):
        self.cart.add_item(product, quantity)

    def checkout(self, mart_owner: Owner):
        payment_info = mart_owner.create_payment_info(self.cart)
        self.pay(payment_info)

    def pay(self, payment_info: PaymentInfo):
        print(f"결제 완료! 총 금액: {payment_info.total_amount}, 카드번호: {payment_info.card_number}")

# 예시 사용
if __name__ == "__main__":
    # 마트 오너 생성
    mart_owner = Owner()

    # 상품 생성
    apple = Product("사과", 1000)
    banana = Product("바나나", 1500)

    # 고객 생성
    customer = Customer()

    # 고객이 상품을 카트에 담음
    customer.add_to_cart(apple, 2)
    customer.add_to_cart(banana, 3)

    # 마트 오너가 결제 정보를 생성하고, 고객이 결제
    customer.checkout(mart_owner)
