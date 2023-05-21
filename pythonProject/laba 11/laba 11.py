def zadacha1():
    def z1():
        class Restaurant: #Используется для создания объектов, описывающих рестораны
            def __init__(self,restaurant_name,cuisine_type):#определяет метод-конструктор класса "Restaurant", который будет вызываться при создании новых объектов.
                self.restaurant_name=restaurant_name
                self.cuisine_type=cuisine_type
            def describe_restaurant(self):
                print('\nНазвание ресторана: ',self.restaurant_name ,"\n Кухня ресторана: ",self.cuisine_type)
            def open_restaurant(self):
                print('  Ресторан открыт к посещению !')
        newRestaurant = Restaurant(input("Введите название ресторана: "),input("Введите кухню для ресторана: "))
        newRestaurant.describe_restaurant()
        newRestaurant.open_restaurant()
    z1()
    def z2():
        class Restaurant:
            def __init__(self,restaurant_name,cuisine_type):
                self.restaurant_name=restaurant_name
                self.cuisine_type=cuisine_type
            def describe_restaurant(self):
                print('\nНазвание ресторана: ',self.restaurant_name ,"\n Кухня ресторана: ",self.cuisine_type)
            def open_restaurant(self):
                print('\nРесторан открыт к посещению !')
        newRestaurant = Restaurant('Морген','Китайская')
        secondRestaurant=Restaurant('Сияние',"Французская")
        thirdRestaurant=Restaurant('Шашлыкофф','Узбекская')
        newRestaurant.describe_restaurant()
        secondRestaurant.describe_restaurant()
        thirdRestaurant.describe_restaurant()
    z2()
    def z3():
        class Restaurant:
            rating=4
            def __init__(self,restaurant_name,cuisine_type,rating):
                self.restaurant_name=restaurant_name
                self.cuisine_type=cuisine_type
                self.rating=rating
            def describe_restaurant(self):
                print('\nНазвание ресторана: ',self.restaurant_name ,"\n Кухня ресторана: ",self.cuisine_type,"\nРейтинг" ,self.rating)
            def open_restaurant(self):
                print('Ресторан открыт к посещению !')
            def changerating(self,newrating):
                self.rating=newrating

        newRestaurant = Restaurant('Морген','Китайская',rating=4)
        newRestaurant.describe_restaurant()
        newRestaurant.changerating(int(input("\n Какую оценку Вы поставите этому ресторану? ")))
        newRestaurant.describe_restaurant()
    z3()
zadacha1()