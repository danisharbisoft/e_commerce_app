# e_commerce_app

## Idea:
The idea behind this app is to create a small interface where sellers can post their products, buyers can view various products and order them.

## Functions:
- You can register and use the e_commerce_app as a buyer and seller.
- The functions of the e_commerce_app are divided into three categories:
  - User Authentication:
    - The app allows you to create and log into accounts.
    - You can log out of accounts without losing your data.
    - Each user has their cart and their products which they may have published as a seller.
  - Seller Interface:
    - As a seller, you can add new products, review your older ones, make changes to them, and delete them if you would like to.
  - Buyer Interface:
    - As a buyer, you can view all products posted by different sellers, including yourself.
    - You can click on any item to view its details.
    - You can add it to your cart and continue shopping, checkout, or even log out. The app will remember your cart items.
    - The moment you provide details and confirm your order, the app will clear your cart and send you a confirmation e-mail.
    (In order to access the email properties of the app, you will have to give your email ID and password in the settings of the app as the host e-mail)

## Technical Details:
The e_commerce_app repository consists of the following 4 directories:
- E_commerce_site: This is the main project directory which has the settings and the apps registered.
- user_authentication: This app handles user creation, authentication, logout, etc.
- seller: This app handles the seller interface.
- Buyer: This app handles the buyer interface.

Directory structures of each of the 4 directories:
### E_commerce_site:
- settings.py: Has the necessary settings for the project.
- urls.py: Has the URLs for the different apps.
- templates: Has a few templates which are the basis for other templates in different apps. This is done to avoid code repetition following the DRY principle.
  - layout.html
  - generic_delete_page.html
  - base_details_for_product_view_html

### user_authentication:
- admin.py: Registers models to the admin interface.
- apps.py
- forms.py: Contains necessary forms for the application.
- models.py: Contains necessary models.
- urls.py: Contains URLs for the different views.
- views.py: Contains all the views for the user_authentication app.

### seller:
- admin.py: Registers models to the admin interface.
- apps.py
- forms.py: Contains necessary forms for the application.
- models.py: Contains necessary models.
- urls.py: Contains URLs for the different views.
- views.py: Contains all the views for the seller app.

### buyer:
- admin.py: Registers models to the admin interface.
- apps.py
- forms.py: Contains necessary forms for the application.
- models.py: Contains necessary models.
- urls.py: Contains URLs for the different views.
- views.py: Contains all the views for the buyer app.

## SETUP INSTRUCTIONS:
- Create a virtual environment and download Django within it.
- Clone the repository onto your system.
- Create a Media File to store the images which will be uploaded.
- Enter your email information in the settings file.
- Run the server.
- Test the application by performing different tasks.
