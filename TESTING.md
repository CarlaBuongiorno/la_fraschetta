# **Testing And Project Barrier Solutions**

[Return to README.md](https://github.com/CarlaBuongiorno/The-Collector/blob/master/README.md)

[View the live site here](https://the-collector-project.herokuapp.com/)

![Final project image home page](docs/screenshots/amiresponsive.png)

## **Contents**

[Testing User Stories](#testing-user-stories)

[Automated Testing](#automated-testing)

[Code Validation](#code-validation)

[Responsiveness And Compatibility](#responsiveness-and-compatibility)

[Testing Performance](#testing-performance)
* [Lighthouse](#lighthouse)

[Project Barriers and Solutions](#project-barriers-and-solutions)
* [Solved Bugs](#solved-bugs)
* [Known Bugs](#known-bugs)

---

## **Testing User Stories**

### Viewing and Navigation
* #### As a Shopper:
    * I wish to easily navigate the site so that I can have a good user experience.
    * I wish to get visual feedback so that I see when an action has been completed.
    * I wish to view all the products so that I can choose some to buy.
    * I wish to search for a specific product or category so that I may find the item that I want.
    * I wish to view full product information so that I can see the details of a specific product including the price, description, product rating and product image.
    * I wish to easily see my bag total so that I can stick to my budget.

---

### Registration and User Accounts
* #### As a Site User:
    * I wish to create an account for future purchases so that I can view my order history and confirmations, and save my payment information.
    * I wish to easily login or logout so that I can access my profile and manage my personal details.
    * I wish to be able to request a password reset so that I can receive an email to reset my password incase I forget it.
    * I wish to get an email confirmation after registering so that I can verify my registration was successful.

---

### Reviews and Wishlist
* #### As a Registered User:
    * I wish to be able to add my own reviews to products so that I may share my experience.
    * I wish to be able to edit/delete my reviews so that I can amend any errors or, in case I change my opinion.
    * I wish to be able to add products to my wishlist so that I can view those products later.
    * I wish to be able to remove products from my wishlist so that my wishlist only consists of products I want to have saved.

---

### Sorting and Searching
* #### As a Shopper:
    * I wish to be able to sort the list of available products so that I can sort relevant products alphabetically, by name or by price.
    * I wish to be able to sort a category of products so that I can sort relevant products alphabetically, by name or by price.
    * I wish to be able to sort multiple categories simultaneously so that I can find the best rated or priced products across broad categories.
    * I wish to be able to search for a specific product by name or description so that I can quickly find items I'm interested in. 
    * I wish to be able to view a list of search results so that I can see if the product I want is available to purchase.
    * I wish to be able to easily see what I've searched for and the number of results so that I can quickly decide whether the product I'm looking for is available.

---

### Purchasing and Checkout
* #### As a Shopper:
    * I wish to buy products online as a guest so that I can checkout without having to create an account.
    * I wish to easily add, update the quantity, or delete products in my bag so that I can adjust my purchase to fit my preferences before checkout.
    Easily enter my payment information	Have a smooth checkout experience
    * I wish to be able to easily enter my payment information so that I can have a smooth checkout experience.
    * I wish to experience that my payment and personal information are secure so that I can be confident enough to provide the neccessary information to purchase products securely.
    * I wish to view a summary of my order before completing my purchase so that I can check that I havn't made any mistakes.
    * I wish to receive a confirmation email of my purchase so that I can be confident that the purchase has been made successfully and view my order details.

---

### Admin and Store Management
* #### As a Store Owner:
    * I wish to be able to add a new product so that I can add new products to my store.
    * I wish to be able to edit any product so that I can update the details of products.
    * I wish to be able to delete any product so that I can remove old items from my store.

[Back to Top](#testing-and-project-barrier-solutions)

---

## **Automated Testing**


[Back to Top](#testing-and-project-barrier-solutions)

---

## **Code Validation**

### W3C Markup Validation Service:


---

### W3C CSS Validation Service:


---

### JSHint:


---

### Python 8:


[Back to Top](#testing-and-project-barrier-solutions)

---

## **Responsiveness And Compatibility**

The website was tested through the following browsers:

### Google Chrome

* 
    * ![]()

### Microsoft Edge

* 
    * 

### Mozilla Firefox

* 

### Safari

* 

---

DevTools were used to test the site across a range of widths:

### Mobiles: 

* iphone5(320px)
    * 
        * ![]()
    
* Moto G4 (340px)
    * 

* iPhone 6/7/8 (375px)
    * 

* iPhone 6/7/8 Plus (414px)
    * 

---

### Tablets:

* iPad (768px)
    * 

* iPad Pro (1024px)
    * 

---

### Desktops:

* Laptop (1200px)
    * 

* Desktop screen (1400px)
    * 


---

The site was tested on the following physical devices:

### Mobiles: 

* Huawei P30
    * 

* Sony Xperia 1 II
    * 

* iPhone X
    * 

---

### Laptops:

* MacBook Pro 13inch
    * 
        * ![]()

[Back to Top](#testing-and-project-barrier-solutions)

---

## **Testing Performance**

### Lighthouse


[Back to Top](#testing-and-project-barrier-solutions)

---

## **Project Barriers and Solutions**

### Solved Bugs

1. The 'My Account' dropdown menu was not working. To fix this I Changed the Bootstrap version to Bootstrap4 instead of Bootstrap5 and added jquery to the head in base.html.
![Categories Dropdown Menu](documentation/screenshots/search_categories.png)

2. When trying to render the products in the products.html template, they would not render. Instead I would get a 404 Page Not Found error.
![Products 404](documentation/screenshots/render_products.png)
The issue was that the `products/` path for the products app was inside the products app urls instead of the project level urls.

3. Search and filter categories would only work for a single word category eg: 'dolci', but not for 2 word category eg: `pasta_risotto`. It appeared correctly in the url `pasta,risotto`, but returned no products.
![Toasts](documentation/screenshots/search_categories.png)
To fix this, I added a comma in the html to separate the words instead of the actual backend name => `pasta,risotto` instead of `pasta_risotto`.

4. The 'Categories' list disappeared from main nav dropdown menu while on home page. It seemed I couldn't access the product views from the project level template html file.
The solution was a Context Processor. I had to separate the categories list from the products view and put it into a _contexts.py_ file to make it available site wide in order for the dropdown categories in the main menu to access the category list.

5. The logo would disappear while on the Products page. The problem was that `<src>` was missing a '/' --> `src="media/logo.png"` instead of `src="/media/logo.png"`.
![Logo Disappeared](documentation/screenshots/search_categories.png)

6. When making a payment at checkout, an error would occur on the card field "Received unknown parameter: payment_method_data[shipping]"
![Stripe Card Element Error](documentation/screenshots/unknown_parameter.png)
A closer look at the `payment_method` object in the 'stripe_elements.js' file showed that there was a closing bracket missing on the `billing_method` and the `shipping_method` was over-indented. Fixing these to things resolved the issue.
![Billing and Shipping Method](documentation/screenshots/billing_shipping_method.png)

7. The Stripe Card Element was disappeared on the Checkout form. The issue was again in the 'stripe_elements.js' file. There was a comma missing from the `payment_method` object.
![Stripe Card Element](documentation/screenshots/stripe_card_element.png)

8. Some of the toast messages were falling off the page.
![Toasts](documentation/screenshots/toasts_positioning.png)
To fix this I had to set a `min-width` css property to the `.message-container` class in order to force its position. 

9. Stripe 'payment_intent.success' was failing with a server 500 error.
![payment_intent.success](documentation/screenshots/stripe.png)
The problem was in the 'webhook_handler.py' file. In the `handle_payment_intent_succeeded` function, while attempting to get the order objects, I had `grand_total__iexact=grand_total,`.
![iexact](documentation/screenshots/iexact.png)
Using `__iexact` on an integer means you're calling upper() on a float, which will result in an error.
Changing this to just `grand_total=grand_total`, the error went away and payments were successful.

### Known Bugs

* 

[Back to Top](#testing-and-project-barrier-solutions)