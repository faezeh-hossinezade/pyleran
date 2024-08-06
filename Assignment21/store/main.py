import sqlite3
DATABASE_FILE_PRODUCT = "store.db"
###
conproduct=sqlite3.connect(DATABASE_FILE_PRODUCT)
dbprodct=conproduct.cursor()
###
def create_database_product():
  """ Creates a new database and table if they don't exist. """
  TABLE_NAME = "products"
  conproduct = sqlite3.connect(DATABASE_FILE_PRODUCT)
  dbprodct = conproduct.cursor()
  dbprodct.execute(f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                  id INTEGER NOT NULL,
                  name TEXT NOT NULL,
                  price INTEGER NOT NULL,
                  count INTEGER NOT NULL
              )""")
  conproduct.commit()
  conproduct.close()

  
  
def add_product():
    id=int(input("Please enter a id for your new product : "))
    name=input("Please enter a name for your new product : ")
    count=int(input("How many of this product do you have ? "))
    price=float(input("How much is this ? "))
    dbprodct.execute(f"INSERT INTO products(id,name,count,price) VALUES({id},'{name}',{count},{price});")
    conproduct.commit()
    print(" ✅ ")
    
    
####

def edit_product():
    id=int(input("What is product's id ? "))
    new_name=input("Please enter a new name for your new product : ")
    new_count=int(input("Enter new count :"))
    new_price=float(input("Enter new price: "))
    dbprodct.execute(f"UPDATE products SET name='{new_name}',count={new_count},price={new_price} WHERE id={id} ;")
    conproduct.commit()
    print("✅")


def delete_product():
    id=int(input("What is product's id ? "))
    Condition = input("Do you sure of delete this product? (yes/no):")
    if Condition == "yes":
        dbprodct.execute(f"DELETE FROM products WHERE id={id}")
        conproduct.commit()
        print("✅")
        
def buy_product():
    id=int(input("What is product's id ? "))
    cnt=int(input("How many products do you want to buy? please select less than toatal products! "))
    dbprodct.execute(f"UPDATE products SET count = count - {cnt}  WHERE id={id}")
    conproduct.commit()
    search_product()
    print("✅")
    
def search_product():
    id=int(input("What is product's id ? "))
    dbprodct.execute(f"SELECT* FROM products WHERE id={id}")
    myresult = dbprodct.fetchall()
    for x in myresult:
        print(x)
     
     
def show_product():
    myresult = dbprodct.execute(f"SELECT* FROM products").fetchall()
    print("All products are:")
    for p in myresult:
        print(p)
        print("\n")
    
def exit_shop():
    exit(0)

def show_menu():
    print("1- Add Product")
    print("2- Edit Product")
    print("3- Remove Product")
    print("4- Purchase Product")
    print("5- Search Product")
    print("6- Show Products")
    print("7- Exit")
    
##main
print("Welcome to Faeze store")
while True:
    show_menu()
    your_choice=int(input("Choose a number of Menu: "))
    create_database_product()
    if your_choice==1:
        add_product()
    elif your_choice==2:
        edit_product()
    elif your_choice==3:
        delete_product()
    elif your_choice==4:
        buy_product()
    elif your_choice==5:
        search_product()  
    elif your_choice==6:
        show_product() 
    elif your_choice==7:
        exit_shop()