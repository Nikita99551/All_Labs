class Restaurant:
    def init(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print('Название ресторана: ',self.restaurant_name ,"\nКухня ресторана: ",self.cuisine_type)
    def open_restaurant(self):
        print('Ресторан открыт к посещению !')
newRestaurant = Restaurant('Кавказкая','Индийская')
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

class Restaurant:
    def init(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print('Название ресторана: ',self.restaurant_name ,"\nКухня ресторана: ",self.cuisine_type)
    def open_restaurant(self):
        print('Ресторан открыт к посещению !')
newRestaurant = Restaurant('Кавказкая','Индийская')
secondRestaurant=Restaurant('Сон',"Японская")
thirdRestaurant=Restaurant('Friends','Грузинская')
newRestaurant.describe_restaurant()
secondRestaurant.describe_restaurant()
thirdRestaurant.describe_restaurant()

class Restaurant:
    rating=4
    def init(self,restaurant_name,cuisine_type,rating):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.rating=rating
    def describe_restaurant(self):
        print('Название ресторана: ',self.restaurant_name ,"\nКухня ресторана: ",self.cuisine_type,"\nРейтинг" ,self.rating)
    def open_restaurant(self):
        print('Ресторан открыт к посещению !')
    def changerating(self,newrating):
        self.rating=newrating

newRestaurant = Restaurant('Кавказкая','Индийская',4)
newRestaurant.describe_restaurant()
newRestaurant.changerating(3)
newRestaurant.describe_restaurant()