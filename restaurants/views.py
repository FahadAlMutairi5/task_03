from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {

    		"my_list" : [

    					{
    						"restaurant_name" : "Hr",
    						"food_type" : "Ch",
    					},

    					{
    						"restaurant_name" : "kn",
    						"food_type" : "Me",
    					},

    					{
    						"restaurant_name" : "Sd",
    						"food_type" : "Re",
    					},

    					{
    						"restaurant_name" : "We",
    						"food_type" : "Qe",
    					},
    		]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    		"my_object" : {

    					"restaurant_name" : "Favorite Re",
    					"food_type" : "Check",
    		}
    }
    return render(request, 'detail.html', context)
