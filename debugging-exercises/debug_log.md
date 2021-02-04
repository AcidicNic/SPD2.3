# Debug Log

**Explain how you used the the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

## Exercise 1

I tried ordering a pizza with all the toppings:
 - expected: pizza order form submits without errors
 - actual: TypeError: 'topping' is an invalid keyword argument for PizzaTopping
 - break point: line 79 in app.py
 - It looks like "topping" should've been "topping_type", when creating a new PizzaTopping object on line 79.

I'm now getting a new error when trying to order a pizza:
 - expected: pizza order form submits without errors.
 - actual: BuildError: Could not build url for endpoint '/'
 - break point: line 84
 - The string inside of url_for(), should be the name of a function for a route, not the route itself. I changed '/' to 'home' to fix this.

After ordering a pizza, I'm successfully redirected to the home page, and I can see the "Your order has been submitted!" flash coming through, but no pizza orders are listed on the home page.
 - I discovered 2 things causing this problem:
    1. After adding to the db on line 81, I added "db.session.commit()" to actually push the new pizza to the DB.
    2. Lines 67 and 68 are grabbing values from the form elements "name" and "size". But in templates/order.html, those form elements don't exist. They're called "order_name" and "pizza_size".
 - After making those 2 changes, pizzas are displaying properly on the home page.

Edge case: If the order form is submitted with no values, it throws an error while committing to the DB:
 - To fix this, I changed the html to make size, name, and crust type required fields.

I noticed that the toppings were all being added to the pizza, regardless of which toppings I selected.
 - I changed "request.form.get" on line 70, to "request.form.getlist", to get a list of all the input values with the name "toppings".
 - Then I changed the for loop on line 78, to iterate through "toppings_list", rather than "ToppingType".


## Exercise 2

I tried submitting the form on '/'
 - error: KeyError: 'name'
 - line 52 of app.py. looks like result_json doesn't have a 'name' key.
 - I tried printing result_json and discovered that the api isn't returning properly.
 - After looking at the API docs, I found that it's expecting the city name in the param 'q'. So on line 45 I changed "place" to "q"

The API is returning status code 400
 - I tried printing the result.url, before using .json(), and found that there is no q param in the URL.
 - On line 40, "city = request.args.get('users_city')"
 - but there is no users_city, so when we send the API req, the q param is empty.

The api is returning what we want, trying to access but result_json['main']['temperature'] throws an error!
 - KeyError: 'temperature'
 - After looking at results_json which I still have printed in the console, I found that it should be result_json['main']['temp']

Other Stuff:
 - home.html has an opening h2 tag with a closing h1 tag
 - To avoid unhandled errors being displayed to the user, I added an edge case. if result_json['cod'] is equal to 400, the user will be redirected to the home page and a small error message will be displayed at the top of the page.


## Exercise 3

Line 37 in utils.py throws an error -- IndexError: list index out of range
 - I tried printing i, k, len(arr), and len(right_side) inside the while loop.
 - This confirmed that right_side[i] is what's causing the error.
 - I noticed that the while loop condition on line 36 should be preventing this. ("while j < len(right_side):")
 - But the variable being used on line 37 is i, not j.
 - I changed "right_side[i]" to "right_side[j]", to resolve the bug.

merge_sort() is working now, but binary_search() is throwing an error on line 51 in utils.py! -- TypeError: list indices must be integers or slices, not float
 - `if arr[mid] < elem:`
 - This must mean mid is a float. So I went back to line 48, where mid is defined.
 - `mid = (high + low) / 2`
 - the `/` should be `//`! One slash will divide and return a float, two will return an integer without the remainder, which is what we want.
