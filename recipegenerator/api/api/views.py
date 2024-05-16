from rest_framework.response import Response

from rest_framework.decorators import api_view
from base.models import Item
from .serializer import ItemSerializer
import random
food_dictionary = {
    1: "Pizza",
    2: "Burger",
    3: "Pasta",
    4: "Sushi",
    5: "Tacos",
    6: "Salad",
    7: "Steak",
    8: "Fried Chicken",
    9: "Sandwich",
    10: "Soup",
    11: "Rice Bowl",
    12: "Grilled Cheese",
    13: "Lasagna",
    14: "Sushi Rolls",
    15: "Burrito",
    16: "Roast Beef",
    17: "Tofu Stir-Fry",
    18: "Fried Rice",
    19: "Mashed Potatoes",
    20: "Fish and Chips",
    21: "Pancakes",
    22: "Waffles",
    23: "Omelette",
    24: "Pulled Pork Sandwich",
    25: "Caesar Salad",
    26: "Fajitas",
    27: "Stuffed Peppers",
    28: "Chili",
    29: "Shrimp Scampi",
    30: "Chicken Alfredo",
    31: "Meatloaf",
    32: "Beef Stew",
    33: "Chicken Curry",
    34: "Hamburger Steak",
    35: "Fish Tacos",
    36: "Chicken Salad",
    37: "Pork Chops",
    38: "Eggplant Parmesan",
    39: "Potato Salad",
    40: "Ramen",
    41: "Pho",
    42: "Enchiladas",
    43: "Baked Ziti",
    44: "Pad Thai",
    45: "Garlic Bread",
    46: "Cobb Salad",
    47: "Tomato Soup",
    48: "Buffalo Wings",
    49: "Beef Tacos",
    50: "BBQ Ribs",
    # Add more foods as needed
}

# You can access the food items using their corresponding numbers like food_dictionary[1] for "Pizza"
@api_view(['GET'])
def getData(request):
    return Response(food_dictionary[random.randint(1,50)])
@api_view(['POST'])
def postData(request):
    serializer=ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
