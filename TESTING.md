# **Testing And Project Barrier Solutions**

[Return to README.md](https://github.com/CarlaBuongiorno/la_fraschetta/blob/master/README.md)

[View the live site here](https://la-fraschetta.herokuapp.com/)

![Final project image home page](documentation/screenshots/amiresponsive/amiresponsive.png)

## **Contents**

[Testing User Stories](#testing-user-stories)

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
        * The main navigation bar is easy to understand and is visible on every page of the site.
        * Clicking on a menu item in the navigation bar displays the relevant page without errors.
        * The __Account__ menu item is a dropdown that displays differently depending on what access the user has.
        * The logo at the top left of the page, takes the user back to the home page at any given point.
        * The __Delicatessen__ menu item is a dropdown displaying a list of all the categories a user can navigate to in order to find the relevant products in that category.
            * ![Main Menu Large Screen](documentation/screenshots/main-nav-lg.png)
            * ![Main Menu Small Screen](documentation/screenshots/main-nav-sm.png)
        * Scrolling down the _Home_ page, the list of categories are displayed and clicking into any of them will take the user to the _Products_ page displaying the relevant products in that category.
            * ![Home Categories Large and Small Screen](documentation/screenshots/home-categories.png)
        * On the _Products_ page of a large screen, there is a side navigation menu displaying the list of categories where a user can navigate/filter through the products by means of their category groups. On a small screen this is displayed by means of a select-box.
            * ![Product Page Categories Menu](documentation/screenshots/categories-menu.png)
        * On each page a user navigates to, there are buttons giving the user the option to navigate elsewhere, eg. back to the _Delcatessen_ (the _Products_ page), their _Profile_ page, the _Checkout_ page, etc.
            * ![Navigation Buttons](documentation/screenshots/nav-btns.png)

    * I wish to get visual feedback so that I see when an action has been completed.
        * There are validation messages for all the forms if a user doesn't enter the correct format of information.
        * Toast messages are presented to the user in the form of:
            * Success messages
            * Error messages
            * Info messages (containing information for the user)
            * Warning messages

    * I wish to view all the products so that I can choose some to buy.
        * On the _Products_ page, all the products are displayed with one underneath the other on small screens, two in a row on md screens and four in a row on large screens.
            * ![Products Page](documentation/screenshots/products.png)
        
    * I wish to search for a specific product or category so that I may find the item that I want.
        * There is a _search bar_ in the main navigation menu where a user can search for products or categories.
            * ![Search Site](documentation/screenshots/search-site.png)
            * ![Search for Spaghetti](documentation/screenshots/search-spaghetti.png)
            (Two products are found for search term 'spaghetti'. The second product (Pecorino) contains the word 'spaghetti' in its description.)
    
    * I wish to view full product information so that I can see the details of a specific product including the price, description, product rating and product image.
        * Clicking on a product brings the user to the _Product Details_ page. Here it is clear what the product is by its image, it's name, the price, the category it belongs to, and the average ratings it has.
            * ![Product Details](documentation/screenshots/product-detail.png)

    * I wish to easily see my bag total so that I can stick to my budget.
        * Each time a product gets added to the cart, the total gets updated under the basket icon in the main navigation bar.
        * A success message also appears with a preview of the cart details.
            * ![Bag Total and Preview](documentation/screenshots/bag-total.png)

---

### Registration and User Accounts
* #### As a Site User:
    * I wish to create an account for future purchases so that I can view my order history and confirmations, and save my payment information.
        * A user is able to register for an acount by clicking the 'Register' link in the _My Account_ dropdown in the main navigation menu.
            * ![Register Link](documentation/screenshots/login-register.png)
        * A __Sign Up__ form is presented to the user to complete, and a message is displayed to inform the user they will receive an email and should click on the link from the email and then on the 'Confirm' email button to complete the verification process.
            * ![Register Form](documentation/screenshots/register-verify.png)
        * A user can then click on 'My Profile' under the 'My Account' menu dropdown and will be taken to their __Profile__ page. Here they have the ability to update their information as well as view their order history
            * ![Profile](documentation/screenshots/profile.png)


    * I wish to easily login or logout so that I can access my profile and manage my personal details.
        * A user is able to login to their acount by clicking the 'Login' link in the _My Account_ dropdown in the main navigation menu.
            * ![Login Link](documentation/screenshots/login-register.png)
        * A __Sign In__ form is be presented to the user to complete, and a success toast message will display once logged in.
            * ![Login Form](documentation/screenshots/sign-in.png)
        * A user is able to logout of their acount by clicking the 'Logout' link in the _My Account_ dropdown in the main navigation menu.
            * ![Logout](documentation/screenshots/logout-profile.png)
        * A __Sign Out__ confirmation button is be presented to the user, and a success toast message will display once signed out.
            * ![Sign Out Form](documentation/screenshots/signout-confirmation.png)

    * I wish to be able to request a password reset so that I can receive an email to reset my password incase I forget it.
        * On the __Sign In__ page, a user can click the 'Forgot Password?' link. This will take the user to a page where they have to enter their email. Upon receipt of an email, the user can follow the emailed link back to a page where they can enter a new password. They will then receive a message that the password change was successful.
            * ![Password Reset](documentation/screenshots/password-reset.png)

---

### Reviews and Wishlist
* #### As a Registered User:
    * I wish to be able to add my own reviews to products so that I may share my experience.
        * If a user is registered and logged in, they will have acces to a _Review_ form on the _Product Detail_ page in order to add their own review to a product.
        * The newly added review will then be displayed on the _Product Detail_ page also with the date in which it was created.
            * ![Reviews](documentation/screenshots/reviews.png)
            
    * I wish to be able to add products to my wishlist so that I can view those products later.
        * If a user is registered and logged in, they will have the ability to click on the wishlist heart displayed on the __Product Detail__ page.
        * The heart will turn red and immediately get added to the user's wislist.
        * The user's 'wished-for' items are displayed with image, description, and price on the __Wishlist__ page.
        * All the user's 'wished-for' items also get a little red heart on them on the __All Products__ page. 
            * ![Add To Wishlist](documentation/screenshots/add-to-wishlist.png)

    * I wish to be able to remove products from my wishlist so that my wishlist only consists of products I want to have saved.
        * To remove the product from the _Wishlist_ a user can either click on the red heart, which will make it turn back to green, or navigate to the __Wishlist__ page and remove by clicking on the trash can for that product.
            * ![Remove From Wishlist](documentation/screenshots/remove-from-wishlist.png)

---

### Sorting and Searching
* #### As a Shopper:
    * I wish to be able to sort the list of available products so that I can sort relevant products alphabetically, by name or by price.
        * A user has the ability to sort the products by _Price_, _Name_, _Category_, and _Ratings_.
            * ![Sort By](documentation/screenshots/sort-by.png)

    * I wish to be able to sort a category of products so that I can sort relevant products alphabetically, by name or by price.
        * A user has the ability to sort the products by _Price_, _Name_, and _Ratings_ within the sorted categories.
            * ![Categories](documentation/screenshots/categories-menu.png)

    * I wish to be able to search for a specific product by name or description so that I can quickly find items I'm interested in. 
        * There is a _search bar_ in the main navigation menu where a user can search for products or categories.
            * ![Search Site](documentation/screenshots/search-site.png)
            
    * I wish to be able to view a list of search results so that I can see if the product I want is available to purchase.
        * After entering a search term, the user is presented with a list of relevant products.
            * ![Search for Spaghetti](documentation/screenshots/search-spaghetti.png)
            (Two products are found for search term 'spaghetti'. The second product (Pecorino) contains the word 'spaghetti' in its description.)

    * I wish to be able to easily see what I've searched for and the number of results so that I can quickly decide whether the product I'm looking for is available.
        * A user can easily see what they have searched for and how many products match the search term at top left side of the screen (under the page title) on large screens, and just under the page title on small screens.
            * ![Products Found](documentation/screenshots/products-found.png)

---

### Purchasing and Checkout
* #### As a Shopper:
    * I wish to buy products online as a guest so that I can checkout without having to create an account.
        * A guest user has the ability to make purchases without having to sign up for an account.
            * ![Guest Purchase](documentation/screenshots/guest-purchase.png)

    * I wish to easily add, update the quantity, or delete products in my bag so that I can adjust my purchase to fit my preferences before checkout.
        * On the __Product Detail__ page the user has the ability to add more than one of the same item to their bag.
        * Upon navigating to the __Shopping Cart__ page, a user has the ability to increase or decrease the quantity of a given item, as well as remove it entirely from the cart by means of the 'trash can' icon.
        * Any adjustments are followed my toast messages as visual feedback for the user and the cart's total is adjusted accordingly.
            * ![Quantity](documentation/screenshots/quantity.png)


    * I wish to be able to easily enter my payment information so that I can have a smooth checkout experience.
        * Clicking the 'Secure Checkout' button takes the user to the __Checkout__ page where the user can fill out a form consisting of their delivery and payment details. All fields are labelled clearly for the user.
            * ![Checkout Form](documentation/screenshots/checkout-form.png)

    * I wish to experience that my payment and personal information are secure so that I can be confident enough to provide the neccessary information to purchase products securely.
        * Stripe is used to handle all card payments on this site. Stripe is certified to PCI Service Provider Level 1, which is the most stringent level of certification available in the payments industry. All card numbers are encrypted with AES-256 (Advanced Encryption Standard - 256 bits), and decryption keys are stored on separate machines.

    * I wish to view a summary of my order before completing my purchase so that I can check that I havn't made any mistakes.
        * A summary of the user's order is displayed on the __Checkout__ page onder above the form on small screens and on the right side of the form on large screens.
            * ![Checkout Summary](documentation/screenshots/checkout-summary.png)

    * I wish to receive a confirmation email of my purchase so that I can be confident that the purchase has been made successfully and view my order details.
        * After clicking the 'Complete Order' button, an email is sent to the user confirming their order and order number.
        * A message is displayed informing the user an email has been sent and a summary of the order is displayed on this page.
            * ![Confirmation Email Purchase](documentation/screenshots/confirmation-email-purchase.png)

---

### Admin and Store Management
* #### As a Store Owner:
    * I wish to be able to add a new product so that I can add new products to my store.
        * A store owner has the additional ability to add products and categories to the site. 
        * The __Add Product__ and __Add Category__ forms can ba found by clicking the 'My Account' menu item in the navigation menu.
        * The forms are easy to understand and fill out and the added products and categories get stored in the database.
            * ![Add Category and Add Product](documentation/screenshots/add-product.png)

    * I wish to be able to edit any product so that I can update the details of products.
        * A store owner can edit any product by clicking on the 'Edit' link either on a product on the __All Products__ page, or on the __Product Detail__ page.
        * The user will be taken to the same form as the __Add Product__ form but will now have the existing product details filled in and can then update any detail.
            * ![Edit a Product](documentation/screenshots/edit-delete-product.png)

    * I wish to be able to delete any product so that I can remove old items from my store.
        * A store owner can delete any product by clicking on the 'Delete' link either on a product on the __All Products__ page, or on the __Product Detail__ page.
        * ![Delete a Product](documentation/screenshots/delete-product.png)

[Back to Top](#testing-and-project-barrier-solutions)

---

## **Code Validation**

### W3C Markup Validation Service:
* The HTML for this site was validated by running each page through the [W3C HTML Markup Validator](https://validator.w3.org/) and returned no errors.
    * Home
        * ![Home](documentation/screenshots/w3c-html/home.png)
    * Our Story
        * ![Our Story](documentation/screenshots/w3c-html/our-story.png)
    * Products
        * ![Products](documentation/screenshots/w3c-html/products.png)
    * Product Details
        * ![Product Details](documentation/screenshots/w3c-html/product-details.png)
    * Profile
        * ![Profile](documentation/screenshots/w3c-html/profile.png)
    * Wishlist
        * ![Wishlist](documentation/screenshots/w3c-html/wishlist.png)
    * Shopping Cart
        * ![Shopping Cart](documentation/screenshots/w3c-html/shopping-cart.png)
    * Checkout
        * ![Checkout](documentation/screenshots/w3c-html/checkout.png)
    * Checkout Success
        * ![Checkout Success](documentation/screenshots/w3c-html/checkout-success.png)


---

### W3C CSS Validation Service:
* The CSS for this site was validated by running each page through the [W3C CSS Validator]() via direct input and returned no errors.
    * Home
        * ![Home](documentation/screenshots/w3c-css/home.png)
    * Our Story
        * ![Our Story](documentation/screenshots/w3c-css/our-story.png)
    * Products
        * ![Products](documentation/screenshots/w3c-css/products.png)
    * Product Details
        * ![Product Details](documentation/screenshots/w3c-css/product-details.png)
    * Profile
        * ![Profile](documentation/screenshots/w3c-css/profile.png)
    * Wishlist
        * ![Wishlist](documentation/screenshots/w3c-css/wishlist.png)
    * Shopping Cart
        * ![Shopping Cart](documentation/screenshots/w3c-css/shopping-cart.png)
    * Checkout
        * ![Checkout](documentation/screenshots/w3c-css/checkout.png)
    * Checkout Success
        * ![Checkout Success](documentation/screenshots/w3c-css/checkout-success.png)
    * Add Category
        * ![Add Category](documentation/screenshots/w3c-css/add-category.png)
    * Add Product
        * ![Add Product](documentation/screenshots/w3c-css/add-product.png)
    * Edit Product
        * ![Edit Product](documentation/screenshots/w3c-css/edit-product.png)

---

### JSHint:
* All javascript files were tested with [JSHint](https://jshint.com/) and returned no errors.
    * Product and Category Image
        * ![Product and Category Image](documentation/screenshots/js-hint/image.png)
    * Bag
        * ![Bag](documentation/screenshots/js-hint/bag.png)
    * Country Fields Functionality
        * ![Country Fields Functionality](documentation/screenshots/js-hint/countryfield.png)
    * Quantity Input Field
        * ![Quantity Input Field](documentation/screenshots/js-hint/product-qty.png)
    * Sort
        * ![Sort](documentation/screenshots/js-hint/sort.png)
    * Stripe Payments
        * ![Stripe Payments](documentation/screenshots/js-hint/stripe-payments.png)
            * Errors highlighted in 'stripe_elements.js' pertain to Stripe import.

---

### PEP8:
* All python files were tested with [PEP8 online](http://pep8online.com/) and returned no errors.
    * Some lines are too long and cannot be broken up, therefore `# noqa:` is used in order for Flake8 to ignore them.
        * ![Products views.py PEP8 Check](documentation/screenshots/pep8/pep8.png)

* The python extention was also used to test Python for PEP8 compliance with it's built in linting.
    * Errors that related to files that were auto generated by Django were left untouched.
    * ./checkout/app.py - 'checkout.signals' imported but unused
        * The import is used to let Django know there is a signals module, listening for changes to automatically update the totals.
            * ![Flake8](documentation/screenshots/pep8/flake8.png)

[Back to Top](#testing-and-project-barrier-solutions)

---

## **Responsiveness And Compatibility**

The website was tested through the following browsers:

### Google Chrome

* Home
    * ![Home](documentation/screenshots/google-chrome/home.png)
* Products
    * ![Products](documentation/screenshots/google-chrome/products.png)
* Product Details
    * ![Product Details](documentation/screenshots/google-chrome/product.png)
* Added a Review
    * ![Added a Review](documentation/screenshots/google-chrome/added-review.png)
* Remove From Wishlist
    * ![Remove From Wishlist](documentation/screenshots/google-chrome/remove-from-wishlist.png)
* Add to Bag
    * ![Add to Bag](documentation/screenshots/google-chrome/add-to-bag.png)
* Checkout Success
    * ![Checkout Success](documentation/screenshots/google-chrome/checkout-success.png)

### Mozilla Firefox

* Sign Up
    * ![Register](documentation/screenshots/modzilla-firefox/register.png)
* Verify Email
    * ![Verify Email](documentation/screenshots/modzilla-firefox/verify-email.png)
* Profile
    * ![Profile](documentation/screenshots/modzilla-firefox/profile.png)
* Products
    * ![Products](documentation/screenshots/modzilla-firefox/products.png)
* Shopping Cart
    * ![Bag](documentation/screenshots/modzilla-firefox/bag.png)
* Checkout Success
    * ![Checkout Success](documentation/screenshots/modzilla-firefox/checkout-success.png) 

---

DevTools were used to test the site across a range of widths:

### Mobiles: 

* iPhone SE (375px)
    * Menu
        * ![Menu](documentation/screenshots/iphone375/menu.png)
    * Added to Wishlist
        * ![Added to Wishlist](documentation/screenshots/iphone375/added-to-wishlist.png)
    * Wishlist
        * ![Wishlist](documentation/screenshots/iphone375/wishlist2.png)
    * Profile
        * ![Profile](documentation/screenshots/iphone375/profile.png)
    * Profile Updated
        * ![Profile Updated](documentation/screenshots/iphone375/profile-updated.png)
    * Sort By Ratings Descending
        * ![Sort By Ratings Descending](documentation/screenshots/iphone375/sortby-ratings-desc.png)
    * Error 404
        * ![Error 404](documentation/screenshots/iphone375/error404.png) 
    
* Samsung Galaxy S20 Ultra (412px)
    * Signed Out
        * ![Signed Out](documentation/screenshots/samsung412/signed-out.png)
    * Add to Bag
        * ![Add to Bag](documentation/screenshots/samsung412/add-to-bag.png)
    * Shopping Cart
        * ![Shopping Cart](documentation/screenshots/samsung412/bag.png)
    * Updated Quantity
        * ![Updated Quantity](documentation/screenshots/samsung412/updated-qty.png)
    * Checkout
        * ![Checkout](documentation/screenshots/samsung412/checkout.png)

---

### Tablets:

* iPad Air (820px)
    * Sign Out
        * ![Sign Out](documentation/screenshots/ipad820/signout.png)
    * Our Story
        * ![Our Story](documentation/screenshots/ipad820/our-story.png)
    * Product Details
        * ![Product Details](documentation/screenshots/ipad820/product-details.png)
    * Wishlist
        * ![Wishlist](documentation/screenshots/ipad820/wishlist.png)
    * Checkout
        * ![Checkout](documentation/screenshots/ipad820/checkout.png)

---

### Large Screen Devices:

* Nest Hub (1024px)
    * Home Categories Signed In
        * ![Home Categories Signed In](documentation/screenshots/nest-hub/home.png)
    * Error 404
        * ![Error 404](documentation/screenshots/nest-hub/error404.png)
    * Search -> No Results
        * ![Search -> No Results](documentation/screenshots/nest-hub/search-no-results.png)
    * Search Tiramisu
        * ![Search Tiramisu](documentation/screenshots/nest-hub/search-tiramisu.png)
    * Sort Condiments By Price Ascending
        * ![Sort Condiments By Price Ascending](documentation/screenshots/nest-hub/sort-condiments-price-asc.png)

* Desktop screen (1400px)
    * Empty Shopping Cart
        * ![Empty Shopping Cart](documentation/screenshots/lg-screen/empty-bag.png)
    * Edit Product
        * ![Edit Product](documentation/screenshots/lg-screen/edit-product.png)
    * Updated Product
        * ![Updated Product](documentation/screenshots/lg-screen/updated-product.png)
    * Profile
        * ![Profile](documentation/screenshots/lg-screen/profile.png)
    * Past Confirmation Order
        * ![Past Confirmation Order](documentation/screenshots/lg-screen/past-confirmation-order.png)

---

The site was tested on the following physical devices:

### Mobiles: 

* Huawei P30
    * Sign In
        * ![Sign In](documentation/screenshots/huawei/sign-in.jpg)
    * Our Story
        * ![Our Story](documentation/screenshots/huawei/our-story.jpg)
    * Profile
        * ![Profile](documentation/screenshots/huawei/profile.jpg)
    * Profile Updated
        * ![Profile Updated](documentation/screenshots/huawei/profile-updated.jpg)
    * Wishlist
        * ![Wishlist](documentation/screenshots/huawei/wishlist.jpg)
    * Removed From Wishlist
        * ![Removed From Wishlist](documentation/screenshots/huawei/removed-from-wishlist.jpg)
    * Shopping Cart
        * ![Shopping Cart](documentation/screenshots/huawei/bag.jpg) 
    * Update Product Quantity
        * ![Update Product Quantity](documentation/screenshots/huawei/update-qty.jpg) 
    * Loading
        * ![Loading](documentation/screenshots/huawei/loading.jpg) 
    * Checkout Success
        * ![Checkout Success](documentation/screenshots/huawei/checkout-success.jpg) 

---

### Laptops:

* MacBook Pro 13inch
    * Home
        * ![Home](documentation/screenshots/google-chrome/home.png)
    * Products
        * ![Products](documentation/screenshots/google-chrome/products.png)
    * Product Details
        * ![Product Details](documentation/screenshots/google-chrome/product.png)
    * Added a Review
        * ![Added a Review](documentation/screenshots/google-chrome/added-review.png)
    * Remove From Wishlist
        * ![Remove From Wishlist](documentation/screenshots/google-chrome/remove-from-wishlist.png)
    * Add to Bag
        * ![Add to Bag](documentation/screenshots/google-chrome/add-to-bag.png)
    * Checkout Success
        * ![Checkout Success](documentation/screenshots/google-chrome/checkout-success.png)

* Dell Windows X11 (Ubuntu 20.04.3 LTS)
    * Sign Up
        * ![Register](documentation/screenshots/modzilla-firefox/register.png)
    * Verify Email
        * ![Verify Email](documentation/screenshots/modzilla-firefox/verify-email.png)
    * Profile
        * ![Profile](documentation/screenshots/modzilla-firefox/profile.png)
    * Products
        * ![Products](documentation/screenshots/modzilla-firefox/products.png)
    * Shopping Cart
        * ![Bag](documentation/screenshots/modzilla-firefox/bag.png)
    * Checkout Success
        * ![Checkout Success](documentation/screenshots/modzilla-firefox/checkout-success.png)

[Back to Top](#testing-and-project-barrier-solutions)

---

## **Testing Performance**

### Lighthouse

* Google Lighthouse was run on different pages returning different results. Below is an extract of the reports for the 'Home' page, 'Product Details' page and 'Shopping Cart' page:
    * Home
        * ![Home](documentation/screenshots/lighthouse/home.png)
    * Product Details
        * ![Product Details](documentation/screenshots/lighthouse/product-details.png)
    * Shopping Cart
        * ![Bag](documentation/screenshots/lighthouse/bag.png)


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

* There are no known bugs that I am aware of.

[Back to Top](#testing-and-project-barrier-solutions)