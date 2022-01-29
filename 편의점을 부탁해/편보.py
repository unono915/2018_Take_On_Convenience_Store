#편의점을 보탁해

def price(food):
    sum=0
    for x in recipe[food]:
        sum+=ingredient_price[x]
    return sum

def set_menu(menu,inHome):
    if inHome=="응":
        for inHave in have:
            for key in recipe:
                if(inHave in recipe[key] and key not in menu and money>=price(key)):
                    menu.append(key)
    elif inHome=="아니":
        for key in recipe:
            if(key not in menu and money>=price(key)):
                menu.append(key)
                
def print_need(food):
    print("필요한 재료: ",end='')
    for i in recipe[food]:
        if i not in have:
            print(i,"",end='')
    print()

def print_less_money(food_price):
    for x in have:
        if x in recipe[food]:
            food_price-=ingredient_price[x]
    print("필요한 금액:",food_price)
    
def print_recipe(food):
    print()
    filename=food+".txt"
    with open(filename) as data:
        contents=data.read()
        print(contents)

ingredient=['','자이언트떡볶이','스파게티컵라면', '치즈','\n','불닭볶음면', '참치', '스팸', '햇반', '너구리','\n', '사리곰탕', '오감자', '김치찌개라면', '3분카레','\n','소시지', '냉동만두', '삼각김밥', '비빔반숙란','\n', '편의점햄버거', '돈가스도시락', '튀김우동']
ingredient_price={'자이언트떡볶이':2000,'스파게티컵라면':1000,'치즈':1000,'소시지':2000,'불닭볶음면':1500,'삼각김밥':1000,'튀김우동':1000,'햇반':1000,'참치':2000,'사리곰탕':1000,'냉동만두':2000,'김치찌개라면':1500,'스팸':2000,'오감자':1500,'편의점햄버거':1500,'돈가스도시락':3500,'비빔반숙란':1000,'너구리':1000,'3분카레':2000}
recipe={'마크정식':['자이언트떡볶이','스파게티컵라면','치즈','소시지'],
'불닭치즈볶음밥' : ['불닭볶음면', '삼각김밥', '치즈'],
'컵밥튀김우동' : ['튀김우동', '햇반', '참치'],
'사리곰탕만둣국' : ['사리곰탕', '냉동만두'],
'김치부대찌개라면' : ['김치찌개라면', '햇반', '참치', '소시지', '스팸'],
'삼각김밥전' : ['치즈', '삼각김밥'],
'오지치즈후라이' : ['오감자', '치즈'],
'불닭버거' : ['불닭볶음면', '편의점햄버거'],
'돈가스돈부리' : ['돈가스도시락', '비빔반숙란'],
'카구리' : ['너구리', '3분카레']}



print("<<<편의점을 보탁해>>>")
money=int(input("가지고있는 돈의 액수를 입력하세요:"))
inHome=input("집에 재료가 있다고 생각합니까?(응/아니):")
print()
menu=[]
have=[]

if(inHome=="응"):
    print("  =================재료=================")
    for x in ingredient:
        print(x," ",end='')
    print("\n  =======================================\n")
    print("주어진 재료 중 가지고있는 재료를 하나씩 입력하세요.\n다 입력하셨으면 0을 입력하세요.")
    
    while(True):
        print("담겨진 재료:",have)
        a=input("재료 입력: ")
        if a=="0":
            break
        elif a in ingredient and a not in have:
            have.append(a)
        else:
            print("잘못 입력하셨습니다.")

    
    set_menu(menu,inHome)
    print(menu)
    food=input("마음에 드는 요리를 선택하세요: ")
    food_price=price(food)
    
    print_less_money(food_price)
    print_need(food)

    print_recipe(food)
    
    
elif(inHome=="아니"):
    set_menu(menu,inHome)
    print(menu)
    food=input("마음에 드는 요리를 선택하세요: ")
    food_price=price(food)
    
    print_less_money(food_price)
    print_need(food)
    
    print_recipe(food)
    
else:
    print("wrong input")
