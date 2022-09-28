def intro():
    slash()
    print('''
 #  #  ####  #      ##    ##   #  #  #### 
 #  #  #     #     #  #  #  #  ####  #    
 #  #  #     #     #     #  #  ####  #    
 #  #  ###   #     #     #  #  #  #  ###  
 ####  #     #     #     #  #  #  #  #    
 ####  #     #     #  #  #  #  #  #  #    
 #  #  ####  ####   ##    ##   #  #  #### 
 ''')
    print('''
 #  #  ###    ##    ##   #  # 
 #  #   #    #  #  #  #  #  # 
 # #    #    #  #  #     # #  
 ##     #    #  #   ##   ##   
 # #    #    #  #     #  # #  
 #  #   #    #  #  #  #  #  # 
 #  #  ###    ##    ##   #  #
 ''')
    slash()
    print()

def vending():
    slash()
    print("@@@상품 4종이 준비되어 있습니다. 번호를 골라 선택하세요.@@@\n")
    print("[ : : :]-----------------------]   [1] 오~로나민A --- 500원")
    print("|    | ┌------------------┒|") 
    print("|    |  | [ ! ]    [ / ]   [ * ] | |    [2] 비타 콜 -------- 600원")
    print("|    |  | __________________ | |")
    print("|    |  | [ + ]  [  ]   [  ]    | |    [3] 쏘~이다 -------  800원")
    print("|    |  | __________________ | |")
    print("|    | ┌------------------┒|    [4] 막심커피 ------- 700원")
    print("|    |  |                       | |")
    print("\n")

def change(count):
    if count == 0:
        return
    print("딸그락~\n")
    count -= 1
    change(count)
    
def DotLine():
    print("---------------------------------------------")
def slash():
    print("//////////////////////////////////////////////////////////////////////")

def goodbye():
    print("찾아주셔서 감사합니다 안녕히 가세요.")

def buy(num):
    print("고객님이 투입한 금액은 %d 원이고 "%money + menu[num] + " 상품을 선택하셨습니다.")
    if money < price[num]:
        print("투입한 금액이 부족합니다. 다시 시작하십시오.")
        goodbye()
    else:
        cha = money - price[num]
        coin = cha / 100
        change(coin)
        print("선택한 상품 " + menu[num] + ", 거스름돈 %d 원을 확인하십시오."%cha)
        DotLine()
        goodbye()
        return cha

        

 
if __name__ == '__main__':

    menu = ("[1] 오~로나민A", "[2] 비타 콜", "[3] 쏘~이다", "[4] 막심커피")
    price = (500, 600, 800, 700)
    money = 0

    intro()
    vending()
 
    while (1):
        product = int(input("▶▷ 상품 번호를 입력하세요 => "))
        if product > 0 and product < 5:
           money = int( input("▶▷ 투입할 금액을 입력하세요 => \\ ") )
           if money % 100 != 0:
               print("100원단위로 넣어주세요.")
           else:
               DotLine()
               money = buy(product-1)
               break


