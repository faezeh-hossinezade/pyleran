import qrcode
PRODUCTS=[]
def read_from_database():
    with open("database.txt", "r") as main_file:
        for line in main_file.readlines():
            result=line.split(',')
            product_dict={'code':result[0], 'name':result[1], 'price':result[2] , 'counters':result[3] }
            PRODUCTS.append(product_dict)
            print(product_dict)
            # print(line)


# for product in PRODUCTS:
#     print(product)
def add_product(code_product ):
    with open("database.txt", "r") as main_file:
        for line in main_file.readlines():
            result=line.split(',')
            product_dict={'code':result[0], 'name':result[1], 'price':result[2] , 'counters':result[3] }
            new_product=input("Please enter code, name, price and counters of new product: ")
            result_new=new_product.split(',')
            product_dict_new={'code':result_new[0], 'name':result_new[1], 'price':result_new[2] , 'counters':result[3]}
            PRODUCTS.append(product_dict_new)
            
            
def edit_product(code_product):
    datas = []
    with open('database.txt', 'r') as file:
        for line in file.readlines():
            datas.append(line)
    for data in datas:
        code, name, count, price = data.split(',')
        if code == code_product:
            while True:
                user_input = input('Edit Code or Name Or Count Or Price or All or Exit? ').strip()
                if user_input == 'Code':
                    code = input('Please Enter New Code: ').strip()
                    break
                elif user_input == 'Name':
                    name = input('Please Enter New Name: ').strip()
                    break
                elif user_input == 'Count':
                    count = input('Please Enter New Count: ').strip()
                    break
                elif user_input == 'Price':
                    price = input('Please Enter New Price: ').strip()
                    break
                elif user_input == 'Exit':
                    return
                elif user_input == 'All':
                    code = input('Please Enter New Code: ').strip()
                    name = input('Please Enter New Name: ').strip()
                    count = input('Please Enter New Count: ').strip()
                    price = input('Please Enter New Price: ').strip()
                    break
                else:
                    print('Mese adam vared kon :| ...')

            index = datas.index(data)
            datas[index] = f'{code},{name},{price},{count}\n'
            with open('database.txt', 'w') as file:
                for d in datas:
                    file.write(d)
            print('Data Has Been Updated')
            break

    else:
        print('Product Not Found')


def search_product(code_product):
   with open("database.txt", "r") as main_file:
        for line in main_file.readlines():
            result=line.split(',')
            product_dict={'code':result[0], 'name':result[1], 'price':result[2] , 'counters':result[3] }  
            if (code_product==product_dict['code']):
                print(product_dict['name'],product_dict['price'],product_dict['counters']) 
                img = qrcode.make(product_dict['code'],product_dict['name'],product_dict['price'],product_dict['counters'])
                type(img)  # qrcode.image.pil.PilImage
                img.save("qrcode.png")  
        

def delete_product(code_product):
    datas = []
    with open('database.txt', 'r') as file:
        for line in file.readlines():
            datas.append(line)
    for data in datas:
        code, name, price,count = data.split(',')
        if code == code_product:
            index = datas.index(data)
            datas[index] = ''
            with open('database.txt', 'w') as file:
                for d in datas:
                    file.write(d)
            print('The item has been removed')
            break

    else:
        print('Product Not Found')


def buy_product(code_product):
    datas = []
    with open('database.txt', 'r') as file:
        for line in file.readlines():
            datas.append(line)
    for data in datas:
        code, name, count, price = data.split(',')
        count = int(count)
        if code == code_product:
            user_input = int(input('Please Enter Count: '))
            if user_input > count:
                print('The Number Of goods Is Not Enough...')
                return
            else:
                count -= user_input
                if count == 0:
                    delete_product(code)
                else:
                    index = datas.index(data)
                    datas[index] = f'{code},{name},{count},{price}'
                    with open('database.txt', 'w') as file:
                        for d in datas:
                            file.write(d)
                    print('The Item Has Been Successfully Added To The Shopping Cart')
                    return {
                        'code_product': code,
                        'name_product': name,
                        'count_product': user_input,
                        'price_product': price
                    }


    else:
        print('Product Not Found')


def show_list():
    with open('database.txt', 'r') as file:
        for line in file.readlines():
            code, name, count, price = line.split(',')
            print(f'{code}\t {name}\t {price}\t {count}\t')
            
def exit_shop():
        exit()    
                                 
def show_menu():
    print("1- Add Product")
    print("2- Edit Product")
    print("3- Remove Product")
    print("4- Purchase Product")
    print("5- Search Product")
    print("6- Show Products")
    print("7- Exit")
    
##main
print("Welcome to Faeze store\nLoading...")
read_from_database()   
print("Data loaded successfully")
while True:
    show_menu()
    code_product=int(input("Please Enter Code of product: "))
    your_choice=int(input("Choose a number of Menu: "))
    if your_choice==1:
        add_product()
    elif your_choice==2:
        edit_product(code_product)
    elif your_choice==3:
        delete_product(code_product)
    elif your_choice==4:
        buy_product(code_product)
    elif your_choice==5:
        search_product(code_product)   
    elif your_choice==6:
        read_from_database()
    elif your_choice==7:
        exit_shop()