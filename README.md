<div style="color: white;">

# Southville Sporting Club | Full Stack Website

## Bristol Based Vintage Athletic Wear

This website has been created to sell UK created athletic wear, it is based on a small UK concept business. 

[![VisitWebsite][website-shield]][website-url]&nbsp;&nbsp;
[![Issues][issues-shield]][issues-url]&nbsp;&nbsp;
[![ClosedIssues][closed-shield]][closed-url]&nbsp;&nbsp;
[![LinkedIn][linkedin-shield]][linkedin-url]
<br/>

## **Table of Contents**

1. [User Experience](#user-experience)
2. [Design](#design)
3. [Features](#features)
4. [Testing](#testing)
5. [Accessibility](#accessibility)
6. [Technologies Used](#technologies-used)
7. [Deployment and Local Development](#deployment-and-local-development)
8. [Credits](#credits)
---
# User Experience

1. [Goals](#goals)
2. [Visual Design](#visual-design)

## Goals

1. [Business Goals](#business-goals)
2. [User Goals](#user-goals)
3. [Strategy](#strategy)

### Business Goals
------
This website performs a twofold mission, finely honed to achieve tangible results: firstly, by meticulously crafting an effortlessly navigable e-commerce platform that seamlessly converts visitors into loyal customers. The user-friendly online store is fortified with secure transactions and showcases the captivating 'Run with Nature' collection - a harmonious blend of vintage athletics and natural elements that guarantees an immersive and satisfying shopping experience, ultimately translating clicks into sales. Secondly, the ambition is to cement an unmistakable identity as the icon of vintage athletic wear intertwined with nature's allure, forging an enduring connection with Bristol's scenic landscapes. 
Mission Statement: "Southville Sporting Club's mission is to unite vintage athletics, nature's beauty, and seamless e-commerce, crafting an active, nostalgic, and environmentally attuned lifestyle."

### User Goals
------
Prospective users of this website seek a seamless and enjoyable online shopping experience where they can explore and purchase the captivating 'Run with Nature' collection. They aim to find high-quality vintage athletic wear that reflects their active lifestyle and appreciation for eco-friendly materials, all while connecting with the vibrant spirit of Bristol's scenic landscapes. Additionally, users intend to make secure and hassle-free transactions, converting their interest into a satisfying shopping journey.
### Strategy
------
The primary target audience for Southville Sporting Club is individuals aged 20-40 who seek stylish and sustainable unisex clothing that resonates with the spirit of vintage athletics and nature's beauty.

What the users would be looking for:
* Effortless Navigation: Users expect a user-friendly and intuitive interface that allows them to easily explore the website and find products.
* Account Creation: Users should be able to create a personal account for a customised shopping experience, including saving preferences and order history.
* Product Information: Comprehensive product descriptions, high-quality images, and sizing information to help users make informed choices.
* Security: Users want to feel confident that their personal and financial information is secure when making purchases.
* Sustainability Information: Details about the use of eco-friendly materials, reinforcing the brand's commitment to sustainability.
* Contact and Support: Access to customer support or contact information for inquiries and assistance.

[Back to top](#table-of-contents)

## Design

1. [Fonts](#fonts)
2. [Styling](#styling)
3. [Wireframes](#wireframes)
4. [Database Schema](#database-schema)
5. [Surface](#surface)
6. [Coolors](#coolors)

### Fonts 
------
I used Google fonts 'Helvetica' and 'Times New Roman'. I used the Times New Roman font to make the header text on the index page stand out from the regular font on the site. I then used 'Helvetica' as I thought it was very easy to read and looks professional.

### Styling 
------
* Materialize CSS files have been incorporated into the project to leverage its pre-defined class defaults and components.
* The class defaults of Materialize CSS have been overridden to align with the desired styling preferences.
* Customisation has been made easier by modifying the source files directly, allowing for a consistent and unified design.
* The website incorporates responsive web design, allowing the site to adjust dynamically based on the screen size.
* Links present on each page have been intelligently designed to redirect users to essential sections, such as the Client or the Register page, irrespective of their current location.

### Wireframes
------
<details>
<summary>Index</summary>

Desktop

![Desktop Index Wireframe](media/readme/wireframes/index-desktop.webp)
<!-- for when you're on AWS!! (static/images/readme/wireframes/index-desktop.webp) -->

Mobile

![Mobile Index Wireframe](media/readme/wireframes/index-mobile.webp)

</details>
<br>

<details>
<summary>Products</summary>

Desktop

![Desktop Products Wireframe](media/readme/wireframes/products-desktop.webp)
<!-- for when you're on AWS!! (static/images/readme/wireframes/index-desktop.webp) -->

Mobile

![Mobile Products Wireframe](media/readme/wireframes/products-mobile.webp)

</details>
<br>

<details>
<summary>Product Detail</summary>

Desktop

![Desktop Product Detail Wireframe](media/readme/wireframes/product-detail-desktop.webp)
<!-- for when you're on AWS!! (static/images/readme/wireframes/index-desktop.webp) -->

Mobile

![Mobile Product Detail Wireframe](media/readme/wireframes/product-detail-mobile.webp)

</details>
<br>

<details>
<summary>Bag</summary>

Desktop

![Desktop Bag Wireframe](media/readme/wireframes/bag-desktop.webp)
<!-- for when you're on AWS!! (static/images/readme/wireframes/index-desktop.webp) -->

Mobile

![Mobile Bag Wireframe](media/readme/wireframes/bag-mobile.webp)

</details>
<br>

<details>
<summary>Checkout</summary>

Desktop

![Desktop Checkout Wireframe](media/readme/wireframes/checkout-desktop.webp)
<!-- for when you're on AWS!! (static/images/readme/wireframes/index-desktop.webp) -->

Mobile

![Mobile Checkout Wireframe](media/readme/wireframes/checkout-mobile.webp)

</details>
<br>

<details>
<summary>Profile</summary>

Desktop

![Desktop Profile Wireframe](media/readme/wireframes/profile-desktop.webp)
<!-- for when you're on AWS!! (static/images/readme/wireframes/index-desktop.webp) -->

Mobile

![Mobile Profile Wireframe](media/readme/wireframes/profile-mobile.webp)

</details>
<br>

<details>
<summary>Contact</summary>

Desktop

![Desktop Contact Wireframe](media/readme/wireframes/contact-desktop.webp)
<!-- for when you're on AWS!! (static/images/readme/wireframes/index-desktop.webp) -->

Mobile

![Mobile Contact Wireframe](media/readme/wireframes/contact-mobile.webp)

</details>
<br>

<details>
<summary>Admin Dashboard</summary>

Desktop

![Desktop Admin Dashboard Wireframe](media/readme/wireframes/admin-dashboard-desktop.webp)
<!-- for when you're on AWS!! (static/images/readme/wireframes/index-desktop.webp) -->

Mobile

![Mobile Admin Dashboard Wireframe](media/readme/wireframes/admin-dashboard-mobile.webp)

</details>
<br>

<details>
<summary>Shipping & Terms</summary>

Desktop

![Desktop Shipping & Terms Wireframe](media/readme/wireframes/shipping-terms-desktop.webp)
<!-- for when you're on AWS!! (static/images/readme/wireframes/index-desktop.webp) -->

Mobile

![Mobile Shipping & Terms Wireframe](media/readme/wireframes/shipping-terms-mobile.webp)

</details>
<br>

### Database Schema
------
This map represents the current models in the relational database, a few of the database been modified or are completely new.

![Database Schema](media/readme/database-schema.webp)


### Surface
------

The color palette for the website is derived from the hero image. Using Photoshop, colors were extracted directly from the image, resulting in the shades noted below. 

These colors, including black and white for a clean, minimalistic appearance, were carefully selected to mirror the image's essence, offering a contemporary and visually striking aesthetic.

### Coolors
------
Using the coolors palette on the image I selected the colours from this along with a darker and lighter shade of contrasting colours to create a balanced palette. 

![Coolors](/media/readme/color-scheme.webp)

[Back to top](#table-of-contents)

# Features

This is a fully responsive website that was designed mobile-first as this is the most likely way it will be viewed; the website is divided into the 22 pages, along with a base template using allauth and toasts for extra functionality. The profile pages are not available until the user is logged into the website. There is also a 404 page for when someone ends up on an incorrect page.

- [Home](#home)
- [Navbar & Footer](#navbar-footer)
- [About Us](#about-us)
- [Contact Us](#contact-us)
- [Error](#error)
- [Shipping & Returns](#shipping-and-returns)
- [Sustainability](#sustainability)
- [Terms & Conditions](#terms-and-conditions)

- [Products](#products)
- [Product Detail](#product-detail)
- [Search & Nothing Found](#search-and-nothing-found)

- [Shopping Bag Overlay](#bag-overlay)
- [Checkout](#checkout)
- [Checkout Success](#checkout-success)

- [Admin Dashboard](#admin-dashboard)
- [Stock List](#stock-list)
- [Order List](#order-list)
- [Add Product](#add-product)
- [Edit Product](#edit-product)

- [Profile](#profile)
- [Register](#register)
- [Login](#login)

### Home

The index page has:

A "Shop Now" button, which takes the user to the "Latest Drop" page of the newest products. 

<details>
<summary>View Here</summary>

![Home](/media/readme/features/index.webp)

</details>
<br>
   

### Navbar Footer

The navbar has the following features:

A logo that when clicked takes the user back to the index page.

A search function

A drop-down menu for the user account. Which only shows 'log in' and 'register' if the user is not logged in, but shows 'Admin Dashboard', 'Profile' and 'logout'.

Drop down menus (on desktop) for the info and shopping buttons to see further information such as categories. 

A burger style navbar for mobile users with the same button functionality. 

The footer has the following features:

Buttons links to the Terms & Conditions, Shipping & Returns and Contact pages. 

Icons for payment types accepted and other standard company information. 

<details>
<summary>NavBar Desktop</summary>

![NavBar Desktop](/media/readme/features/navbar.webp)

</details>
<br>

<details>
<summary>NavBar Mobile</summary>

![NavBar Mobile](/media/readme/features/mobile-nav.webp)

</details>
<br>


<details>
<summary>Footer</summary>

![Footer](/media/readme/features/footer.webp)

</details>
<br>

### About Us

The about us page has the following features:

A hero image with a about us title and capturing caption to catch the users eye. 

Futher information about the brand and where the store is located. 

<details>
<summary>About Us Part 1</summary>

![About Us](/media/readme/features/about-us.webp)

</details>
<br>

<details>
<summary>About Us Part 2</summary>

![About Us Info](/media/readme/features/about-us-info.webp)

</details>
<br>

### Contact Us

The contact us page has the following features:

A form for the user to fill out to get in contact with the brand. 

Information about the location and opening times of the store. 

<details>
<summary>View Here</summary>

![Contact Us](/media/readme/features/contact.webp)

</details>
<br>

### Error

The error page has the following features:

A message notifying the user that they have found themselves on a page that doesn't exist. 

A button to return the user to the homepage. 

<details>
<summary>View Here</summary>

![Error](/media/readme/features/error.webp)

</details>
<br>

### Shipping & Returns

The shipping page has the following features:

A text based page to inform the user on the shipping and returns policy.  

<details>
<summary>View Here</summary>

![Shipping & Returns](/media/readme/features/shipping-returns.webp)

</details>
<br>

### Sustainability

The sustainability page has the following features:

A hero looping video with a title and capturing caption to catch the users eye. 

Futher information about the sustainability and mission of the brand.  

<details>
<summary>Sustainability Part 1</summary>

![Our Mission 1](/media/readme/features/our-mission.webp)

</details>
<br>

<details>
<summary>Sustainability Part 2</summary>

![Our Mission 2](/media/readme/features/our-mission-info.webp)

</details>
<br>

[Back to top](#table-of-contents)

### Terms & Conditions

The terms page has the following features:

A text based page to inform the user on the shipping and returns policy.

A button at the end of the text to send the user to the contact form if they have further questions. 

<details>
<summary>View Here</summary>

![Terms & Conditions](/media/readme/features/terms.webp)

</details>
<br>

### Products

The products page has the following features:

A list of products, which, when clicked, takes the user to the detail page of that specific product.

If the user is a superuser, at the bottom of each product are links to either edit or delete the product.

Text which lets the user know how many products there are in the category they are browsing. This also shows a link to "All Products".

A dropdown box with the ability to sort by price (low to high), price (high to low), name (a-z) and name (z-a). 

A scroll-up button on the bottom-right-hand-side of the page, which when clicked, will automatically scroll the page up to the top. This is available on all pages that are more than 100vh. 

<details>
<summary>View Here</summary>

![Products](/media/readme/features/products.webp)

</details>
<br>

<details>
<summary>Scroll Button</summary>

![Products](/media/readme/features/button.webp)

</details>
<br>

### Product Detail

The product details page has the following features:

If the user is a superuser, two links appear giving the user the ability to edit or delete the product.

The available sizes are button on the page for the user to choose form. If there is only one size then this is selected by default, and not changeable by the user. 

A button that will add the desired size of the product to the user’s checkout cart.

Three cards with a description, shipping returns and size guide for user to read if needed. The shipping section has a button to view the full shipping page. The description is opened on default. 

<details>
<summary>View Here</summary>

![Product Detail](/media/readme/features/product-detail.webp)

</details>
<br>

### Search & Nothing Found

The nothing found page has the following features:

Search for a product by name or description.

Easily see what I have searched for and the number of results.

A button that will add the desired size of the product to the user’s checkout cart.

If there are no results it routes to a nothing-found page that lets the user know there are 0 products for the search requested. 

<details>
<summary>Search Function</summary>

![Search Function](/media/readme/features/search-function.webp)

</details>
<br>

<details>
<summary>Nothing Found</summary>

![Nothing Found](/media/readme/features/nothing-found.webp)

</details>
<br>

### Bag Overlay

The bag overlay page has the following features:

The details of the products being bought, with an option to remove each product.

The details of the total and delivery price along with a button to continue to the checkout.

<details>
<summary>View Here</summary>

![Bag Overlay](/media/readme/features/bag-overlay.webp)

</details>
<br>

### Checkout

The checkout page has the following features:

A form that the user fills out to confirm their details for payment and shipping, if they already have an account this will be pre-populated with their information after first order is placed. 

An order summary for the user to see what they're about to purchase with a dynamic total that changes dependant on their shipping method chosen. 

A card payment function. 

A return to shopping button and a confirm checkout button labelled 'Pay Now'. 

<details>
<summary>Order History</summary>

![Order History](/media/readme/features/order-history.webp)

</details>
<br>

<details>
<summary>Checkout Form</summary>

![Checkout Form](/media/readme/features/checkout-form.webp)

</details>
<br>

### Checkout Success

The checkout page has the following features:

Information about the users order.

A toast popup confirming the order has been sent to the customers email address.

A button to continue shopping. 

<details>
<summary>Checkout Success</summary>

![Checkout Success](/media/readme/features/checkout-success.webp)

</details>
<br>

[Back to top](#table-of-contents)

### Admin Dashboard

The dashboard has the following features:

A card showing the site owners current monthly sales. 

4 cards with buttons attached linking to a stock list, order list, adding a new product and managing their own profiles. 

<details>
<summary>Admin Dashboard</summary>

![Admin Dashboard](/media/readme/features/admin-dashboard.webp)

</details>
<br>

### Stock List

The stock list page has the following features:

A table with all of the site owners current inventory. 

A return button that takes the site owner back to the admin dashboard.

<details>
<summary>Stock List</summary>

![Stock List](/media/readme/features/stock-list.webp)

</details>
<br>

### Order List

The order list page has the following features:

A table with all of the orders from the site. 

A checkbox so the site owner can track what orders they've processed. 

A return button that takes the site owner back to the admin dashboard.

<details>
<summary>Order List</summary>

![Order List](/media/readme/features/order-list.webp)

</details>
<br>

### Add Product

The page to add products has the following features:

A form for the site owner to complete and add items to the site. 

Several of the form inputs are mandatory to avoid errors. 

<details>
<summary>Add Product</summary>

![Add Product](/media/readme/features/add-product.webp)

</details>
<br>

### Edit Product

The page to edit products has the following features:

A form for the site owner to edit with pre-filled data on the item including the current quantity of each size in stock. 

<details>
<summary>Edit Product 1</summary>

![Edit Product 1](/media/readme/features/edit-product.webp)

</details>
<br>

<details>
<summary>Edit Product 2</summary>

![Edit Product 2](/media/readme/features/edit-product-btn.webp)

</details>
<br>

### Profile

The profile page has the following features:

A form where the user can update their personal information, which is then auto filled on the checkout form.

A section that shows the user their order history, the order number takes the user to the full information of their order. 

<details>
<summary>Profile</summary>

![Profile](/media/readme/features/profile.webp)

</details>
<br>

### Register

The register page has the following features:

A link to take the user to the sign-in page if they already have an account.

A form for the user to sign up if they do not already have an account.

This page is only seen if the user is not signed in.

<details>
<summary>Register</summary>

![Register](/media/readme/features/register.webp)

</details>
<br>

### Login

The login page has the following features:

A form for the user to input the necessary details to login to the site.

A login button that takes the user to the login page in case they already have an account.

A forgot password button for the user to reset their password via their email if they're having issues logging in. 

<details>
<summary>Login</summary>

![Login](/media/readme/features/login.webp)

</details>
<br>

[Back to top](#table-of-contents)

### Toasts & Messages

Many messages are included to alert the user that they have accomplished an action. 

## Testing

Testing was ongoing throughout the entire build. I utilised Chrome developer tools while building to pinpoint and troubleshoot any issues as I went along. Both manual testing and validation was employed.  

I tested the page and had 3 people also manually test it on their own devices. For validation, I used the W3C validator, CSS validator, Python Linter, JSHint validator, and Lighthouse. 

<br/>

### Validation

#### W3C Validator

The [W3C HTML Validator](https://validator.w3.org/) was used to validate the HTML on all pages of the website.

<details>
<summary>Home Page</summary>

![Home Page](/media/readme/validator/w3/index-w3.webp)

</details>
<br>

<details>
<summary>About Us</summary>

![About Us](/media/readme/validator/w3/about-us-w3.webp)

</details>
<br>

<details>
<summary>Contact</summary>

![Contact](/media/readme/validator/w3/contact-w3.webp)

</details>
<br>

<details>
<summary>Error</summary>

![Error](/media/readme/validator/w3/error-w3.webp)

</details>
<br>

<details>
<summary>Shipping & Returns</summary>

![Shipping & Returns](/media/readme/validator/w3/shipping-w3.webp)

</details>
<br>

<details>
<summary>Sustainability</summary>

![Sustainability](/media/readme/validator/w3/sustainability-w3.webp)

</details>
<br>

<details>
<summary>Terms & Conditions</summary>

![Terms & Conditions](/media/readme/validator/w3/terms-w3.webp)

</details>
<br>

<details>
<summary>Products</summary>

![Products](/media/readme/validator/w3/products-w3.webp)

</details>
<br>

<details>
<summary>Product Detail</summary>

![Product Detail](/media/readme/validator/w3/product-detail-w3.webp)

</details>
<br>

<details>
<summary>Nothing Found</summary>

![Nothing Found](/media/readme/validator/w3/nothing-found-w3.webp)

</details>
<br>

<details>
<summary>Search</summary>

![Search](/media/readme/validator/w3/search-w3.webp)

</details>
<br>

<details>
<summary>Shopping Bag Overlay</summary>

![Shopping Bag Overlay](/media/readme/validator/w3/bag-overlay-w3.webp)

</details>
<br>

<details>
<summary>Checkout</summary>

![Checkout](/media/readme/validator/w3/checkout-w3.webp)

</details>
<br>

<details>
<summary>Checkout Success</summary>

![Checkout Success](/media/readme/validator/w3/checkout-success-w3.webp)

</details>
<br>

<details>
<summary>Admin Dashboard</summary>

![Admin Dashboard](/media/readme/validator/w3/admin-dashboard-w3.webp)

</details>
<br>

<details>
<summary>Stock List</summary>

![Stock List](/media/readme/validator/w3/stock-list-w3.webp)

</details>
<br>

<details>
<summary>Order List</summary>

![Order List](/media/readme/validator/w3/order-list-w3.webp)

</details>
<br>


<details>
<summary>Add Product</summary>

![Add Product](/media/readme/validator/w3/add-product-w3.webp)

</details>
<br>

<details>
<summary>Edit Product</summary>

![Edit Product](/media/readme/validator/w3/edit-product-w3.webp)

</details>
<br>


- [Profile](#profile)


<details>
<summary>Register</summary>

![Register](/media/readme/validator/w3/register-w3.webp)

</details>
<br>

<details>
<summary>Login</summary>

![Login](/media/readme/validator/w3/login-w3.webp)

</details>
<br>

#### CSS Validation

The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS. There were no errors on the css. 

| Page | Test |
| ------------------------------ | --------------- |
| Home | ✓ |
| Bag | ✓ |
| Checkout | ✓ |
| Products | ✓ |
| Admin Dashboard | ✓ |
| Base Static | ✓ |

#### Javascript Testing

The [JSHint Validator](https://jshint.com/) was used to validate the JavaScript in the script.js file. I needed to use the following code at the top for the proper validation to be shown:   

`/*jshint esversion: 6 */`

I also needed to add the following code so that the use of jquery did not show $ as an undefined variable:

`/*globals $:false */`

| JS Page | Warning | Reasoning |
| --------------- | --------------- | --------------- |
| Admin Dashboard | 1 undefined variable ‘M’ | Relates to the Materialize framework I am using for this project |
| Bag | None | N/A |
| Checkout | None | N/A |
| Stripe | 1 undefined variable ‘Stripe’  | Relates to the payment system I am using for this project |
| Product Detail | 1 undefined variable ‘M’ | Relates to the Materialize framework I am using for this project |
| Product Detail | 1 unused variable ‘instances’ | Relates to the Materialize framework I am using for this project |
| Product Owner | None | N/A |
| Products | 2 undefined variables ‘M’ | Relates to the Materialize framework I am using for this project |
| Products | 2 used variables 'specificDropdownInstance', 'instances' | Relates to the Materialize framework I am using for this project |
| Profiles| None | N/A |

#### Pep8 Validator

The pep8 validator was installed onto gitpod to ensure correct styling throughtout creation. So the code should already be as it supposed to be. 

#### Lighthouse

The original results were improved by adding a meta tag with name and description to the base.html.

| Page | Viewing On | Performance | Accessibility | Best Practices | SEO |
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| Home | Desktop | 91 | 93 | 100 | 90 |
| Home | Mobile | 91 | 93 | 100 | 90 |
| About Us | Desktop | 92 | 90 | 100 | 90 |
| About Us | Mobile | XX | XX | XX | XX |
| Contact Us | Desktop | XX | XX | XX | XX |
| Contact Us | Mobile | XX | XX | XX | XX |
| Error | Desktop | XX | XX | XX | XX |
| Error | Mobile | XX | XX | XX | XX |
| Shipping & Returns | Desktop | XX | XX | XX | XX |
| Shipping & Returns | Mobile | XX | XX | XX | XX |
| Sustainability | Desktop | XX | XX | XX | XX |
| Sustainability | Mobile | XX | XX | XX | XX |
| Terms & Conditions | Desktop | XX | XX | XX | XX |
| Terms & Conditions | Mobile | XX | XX | XX | XX |
| Products | Desktop | XX | XX | XX | XX |
| Products | Mobile | XX | XX | XX | XX |
| Product Detail | Desktop | XX | XX | XX | XX |
| Product Detail | Mobile | XX | XX | XX | XX |
| Search & Nothing Found | Desktop | XX | XX | XX | XX |
| Search & Nothing Found | Mobile | XX | XX | XX | XX |
| Bag Overlay | Desktop | XX | XX | XX | XX |
| Bag Overlay | Mobile | XX | XX | XX | XX |
| Checkout | Desktop | XX | XX | XX | XX |
| Checkout | Mobile | XX | XX | XX | XX |
| Checkout Success | Desktop | XX | XX | XX | XX |
| Checkout Success | Mobile | XX | XX | XX | XX |
| Admin Dashboard | Desktop | XX | XX | XX | XX |
| Admin Dashboard | Mobile | XX | XX | XX | XX |
| Stock List | Desktop | XX | XX | XX | XX |
| Stock List | Mobile | XX | XX | XX | XX |
| Order List | Desktop | XX | XX | XX | XX |
| Order List | Mobile | XX | XX | XX | XX |
| Add Product | Desktop | XX | XX | XX | XX |
| Add Product | Mobile | XX | XX | XX | XX |
| Edit Product | Desktop | XX | XX | XX | XX |
| Edit Product | Mobile | XX | XX | XX | XX |
| Profile | Desktop | XX | XX | XX | XX |
| Profile | Mobile | XX | XX | XX | XX |
| Register | Desktop | XX | XX | XX | XX |
| Register | Mobile | XX | XX | XX | XX |
| Login | Desktop | XX | XX | XX | XX |
| Login | Mobile | XX | XX | XX | XX |



## Accessibility

I have been mindful during coding to ensure that the website is as accessible as possible. I have achieved this by:

* Using semantic HTML.
* Using descriptive alt attributes on images on the site.
* Supplying information for screen readers where there are icons used and no text, such as footer icons.
* Guaranteeing adequate colour contrast throughout the site.

## Technologies Used

<br/>

### Languages Used

HTML5, CSS3, Python, and JavaScript were used to create this website.

<br/>

### **Frameworks, Libraries & Programs Used**

* [Google Fonts](https://fonts.google.com/) was used to import Big Shoulders Text.
* [Git](https://git-scm.com/) was used for version control by using the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) was used to store the projects' code, and to handle version control.
* [Photoshop](https://www.adobe.com/uk/products/photoshop.html/) was used to edit and crop images.
* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) was used to troubleshoot and test features and solve issues with responsiveness and styling.
* [Am I Responsive?](https://ui.dev/amiresponsive) was used to show the website on a range of devices.
* [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) was used for debugging.
* [SQLAlchemy](https://www.sqlalchemy.org/) was used to connect Python code with the database.
* [Psycopg2](https://www.psycopg.org/docs/) was used to connect Python code with the database. 
* [Django](https://www.djangoproject.com/) is a high-level Python web framework.
* [Materialize](https://materializecss.com//) was used for responsive and pre-designed CSS.
* [PostgreSQL](https://www.postgresql.org/) was the object-relational database system used.
* [ElephantSQL](https://www.elephantsql.com/) was used to host the database.
* [Heroku](https://www.heroku.com/) was used to deploy the website.
* [Pexels](https://www.pexels.com/) was used for some royalty free images. 
* [Excel](https://www.microsoft.com/en-gb/microsoft-365/excel) was used to create CSV files.
* [Convert CSV](https://www.convertcsv.com/csv-to-json.htm) was used to convert CSV files to JSON files.
* [Font Awesome](https://fontawesome.com/) was used for the icons.
* [DBDiagram](https://dbdiagram.io/) was used to map the models.
* [Amazon Web Services](https://aws.amazon.com/) was used to host the images for the Heroku-hosted site.

### User Stories 

| AS A/AN | I WANT TO BE ABLE TO… | SO I CAN… |
| --------------- | --------------- | --------------- |
| Viewing and Navigation |
| Shopper | View a list of items | See if any interest me to purchase |
| Shopper  | View product details | View further information such as images, descriptions, prices, and availability.
| Shopper | View the homepage  | See featured products and promotions |
| Registration/Accounts |
| Shopper | Register for an account | Track my purchases |
| Site User | Log in to my account securely | Access my profile and saved information |
| Site User | Reset my password | Recover access to my account |
| Site User | Login through social media | Easily login and set up an account |
| Site User | Update profile information | Ensure items are received and payments are correct |
| Sorting and Searching |
| Shopper | Filter products | View products by various criteria such as popularity, price, and newest arrivals |
| Shopper | Refine my search | Find specific items based on color or size |
| Shopper | Search for specific products using keywords | Quickly find what I'm looking for |
| Purchase and Checkout |
| Shopper | Add items to my shopping cart | Keep for a later purchase |
| Shopper | View my cart | See a summary of selected items and their quantities |
| Shopper | Update quantities or remove items | Purchase the goods I want |
| Shopper | Apply coupon codes | Save money on my order |
| Shopper | Choose from different payment options | Easily pay for my order |
| Shopper | Review order summary | Ensure the order is correct |
| Shopper | Receive a confirmation email | Confirm order details are correct and ensure the order was processed |
| Shopper | Apply coupon codes | Save money on my order |
| Site Owner |
| Site Owner | Manage and process orders | Send items to customers |
| Site Owner | Add and remove items from the site |  Show customers items that are in stock |

### Wireframes

![Add Initial Mockup](media/readme/initial-mockup.webp)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- [issues-shield]:  -->
[issues-shield]: https://img.shields.io/badge/ISSUES-2%20OPEN-yellow?style=for-the-badge&logo=closed
<!--- [issues-url] -->
[issues-url]:https://github.com/nccadman19/southville-sporting-club/issues
<!-- [closed-shield]:  -->
[closed-shield]: https://img.shields.io/badge/CLOSED%20ISSUES-11%20CLOSED-blue?style=for-the-badge&logo=closed
<!-- [closed-url]:  -->
[closed-url]: https://github.com/nccadman19/southville-sporting-club/issues?q=is%3Aissue+is%3Aclosed
<!-- [linkedin-shield]:  -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
<!-- [linkedin-url]:  -->
[linkedin-url]: https://www.linkedin.com/in/nicoleccadman/
<!-- [website-shield]:  -->
[website-shield]: https://img.shields.io/badge/VISIT%20WEBSITE-HERE-green?style=for-the-badge&logo=closed
<!-- [website-url]:  -->
[website-url]: https://southville-sporting-club-ed7d11c9dd6e.herokuapp.com/


### Credit

Infinite Scrolling Banner
https://www.cssscript.com/responsive-text-scrolling-marquee/
Ordering footer col/row wise
https://codeburst.io/how-to-position-html-elements-side-by-side-with-css-e1fae72ddcc
Moving navbar dropdown items under the menu
https://stackoverflow.com/questions/51563809/materialize-css-navbar-menu-dropdown-wont-go-below-origin
Collapisble error on mobile 
https://stackoverflow.com/questions/53973266/materializecss-collapsibles-not-working-properly
Schema
https://dbdiagram.io/d
Products, Categories, Showing products on website
https://www.youtube.com/watch?v=obZMr9URmVI&list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng&index=2
Zoom on hover
https://www.w3schools.com/howto/howto_css_zoom_hover.asp
Collapsible product details page
https://materializecss.com/collapsible.html
center col in materialize 
https://stackoverflow.com/questions/38492194/centering-a-col-card-panel-in-materialize
cards on t&cs
https://stackoverflow.com/questions/41040506/materialize-scroll-tbody
adding multiple categories
https://www.sankalpjonna.com/learn-django/the-right-way-to-use-a-manytomanyfield-in-django
search function synonyms 
https://www.holisticseo.digital/python-seo/nltk/wordnet
button styling
https://stackoverflow.com/questions/59607164/adjust-width-of-multiple-buttons-to-follow-the-button-with-the-largest-wrap-cont
cart error help
https://stackoverflow.com/questions/63675859/attribute-error-int-object-has-no-attribute-get
remove button
https://stackoverflow.com/questions/72875203/remove-item-from-cart-and-manage-quantity-buttons-not-working-when-i-add-mor
address api
https://pypi.org/project/geopy/
dialogs
https://www.tutorialspoint.com/materialize/materialize_dialogs.html
country selector
https://stackoverflow.com/questions/2963930/django-country-drop-down-list
stripe
https://www.youtube.com/watch?v=722A27IoQnk&t=776s
stripe2
https://dev.to/documatic/integrate-stripe-payments-with-django-by-building-a-digital-products-selling-app-le5
stripe3
https://stripe.com/docs/checkout/quickstart
buttons
https://stackoverflow.com/questions/64232515/css-on-clickable-element-onclickhover
modal for delete buttons
https://materializecss.com/modals.html#!
detecting ctrl click
https://stackoverflow.com/questions/16190455/how-to-detect-controlclick-in-javascript-from-an-onclick-div-attribute
checkboxes
https://materializecss.com/checkboxes.html
fixing selected options
https://stackoverflow.com/questions/46415457/jquery-onclick-change-option-selected-attribute
slack thread 
- fixed the issue i was having with the webhook!!!!
getting quantity to show correctly 
https://www.quora.com/How-do-I-fix-AttributeError-int-object-has-no-attribute-get-in-Python
timezone help
https://stackoverflow.com/questions/18622007/runtimewarning-datetimefield-received-a-naive-datetime
favicon error
https://stackoverflow.com/questions/1321878/how-to-prevent-favicon-ico-requests



bugs
cannot get the cart popup to disappear when user clicks away from the display
xl being checked in edit product as its inside XXL 
