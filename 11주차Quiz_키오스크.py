class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price

# 음료 객체 생성
coffee = Beverage("커피", 3000)
green_tea = Beverage("녹차", 2500)
ice_tea = Beverage("아이스티", 3000)

# 사용자 입력 받기
order_name = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티):")

# 선택한 음료에 따라 객체 선택 및 계산
if order_name == "커피":
    selected_beverage = coffee
elif order_name == "녹차":
    selected_beverage = green_tea
elif order_name == "아이스티":
    selected_beverage = ice_tea
else:
    print("잘못된 음료를 선택하셨습니다.")
    selected_beverage = None

if selected_beverage:
    try:
        quantity = int(input("수량을 입력하세요:"))
        total_price = selected_beverage.calculate(quantity)
        print(f"{order_name} {quantity}잔의 가격은 {total_price}원입니다.")
    except ValueError:
        print("유효한 수량을 입력하세요.")
