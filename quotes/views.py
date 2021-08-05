from quotes.models import Stock
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StockForm
# Create your views here.
###################<HOME PAGE>####################
# home page of your website its a function
def home(request):
	# install the requests
	import requests
	import json
	if request.method == 'POST':
		ticker = request.POST['ticker']
		#pk_25ce1537b9004f15ad4b5422fad0f552 api request using the token from the url
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_25ce1537b9004f15ad4b5422fad0f552")
	#to get the API and load its contents
		try:
			api = json.loads(api_request.content)
	# if any exceptions print error - python handles errors
		except Exception as e:
			api = "Error"
		return render(request, 'home.html', {'api': api})
	else:
		return render(request, 'home.html', {'ticker': "Enter a valid ticker symbol above"})
###################<HOME PAGE>####################

###################<TEST PAGE>####################
# Test page of your website its a function
def test(request):
	# install the requests
	return render(request, 'test.html',{})
###################<TEST PAGE>####################

###################<ABOUT ME PAGE>################
# This is a function defined for about page
def about(request):
	return render(request, 'about.html',{})
###################<ABOUT ME PAGE>################

###################<ADD STOCK PAGE>###############
# This is a function for Add_stock page
def add_stock(request):
	import requests
	import json
# this ifcondition is to create a entry in database
	if request.method == 'POST':
		form = StockForm(request.POST or None)
# to see if the entered value is valid and added to database
		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added"))
			return redirect('add_stock')
	else:
		ticker = Stock.objects.all()
# create an empty list and save to data to the list
		output = []
# this for loop is to look for the ticker and add to the table on the webpage 		
		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_25ce1537b9004f15ad4b5422fad0f552")
			try:
				api = json.loads(api_request.content)
# below output.append will pass the api request data to the empty list			
				output.append(api)
# if any exceptions print error - python handles errors
			except Exception as e:
				api = "Error"		
		return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})
###################<ADD STOCK PAGE>####################

####################<DELETE STOCK PAGE>################
def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock has been deleted"))
	return redirect(delete_stock)
#####################<DELETE STOCK PAGE>###############

###################<DELETE STOCK PAGE>#################
# This is a function for Add_stock page
def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html',{'ticker': ticker})
###################<DELETE STOCK PAGE>#################