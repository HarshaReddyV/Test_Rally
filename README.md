# Final Project submission for CS50W Programming with python and Javascript

#### As a part of final project for cs50w I chose to build a forum for share market investors participating in Indian share market trade based on Indian Capital market. In this project all the stocks traded on two major stock exchanges in India namely NSE (National Stock Exchange) and BSE(Bombay Stock Exchange) are listed on the home page with a search functionality at the top. In order to see the posts inside the each stocks users needs to either signin/up through the redirected url to the respective pages.Alternatively Users can sign in/up through the navigation menu before accessing the webapp. I have made changes to the authentication backends to use user's mail addresses for authenication instead of the default username. This particular project was chosen as it is quite frustrating to not find anything similar in the Indian market and also inspired from other forum *hotcopper.com.au* which I have addictively used while in Australia. I chose to address the issue by building something i can probably want for myself and hopefully share it with other users like me in the future. It is distinct from other projects in the course as I have populated with market data and integrated rich text editors in the comments and used user email as a authentication backend I have also used webscraping tool yfinance to get the prices for the share market in near real time as alternative to paid api's. The webapp is developed with mobile first approach and in a responsive manner using bootstrap and custom css. Javascript was utilised to make api calls to update the watchlist.   

#### Distinctiveness and Complexity:
- The project is distinctive from the course material in the sense that it uses a different authentication methods using email instead of username which is the default of django project
- Integrates live stock market data using api calls to yfinance (webscraping tool) to retrieve data such as price,volume and market capital
- Data entry from reading csv files to inject data manually as it requires processing to filter out the inactive stocks from different markets 
- Integration of rich text editor on the front end.CkEditor is provided for editing comments under posts in each stock/ticker
- Storing of RichText in db
- Hosted on Azure AppServices using ci/cd through github
- Configured security settings to be able to host on Azure AppServices

#### User can acces stocks either through search or scrolling on homepage. Navigate to the stock of their choice and add topics for discussion such as the recent financial results and change of management. User can add the stock to their watchlist to access it in the future which is updated using Javascript Api call to the backend without reloading the page. 

#### In this project two apps were registered namely,
- *home* to deal with the navigation on the front end, user authenication 
    - models.py consists of models for Tickers, Users and Watchlist
    - nse.csv to inject data to the tickers using an url /data
    - views.py to deal with the home page functionality of adding, removing to watchlists and search and signin/up functionality 
    - backends.py to authenticate users by verifying password

    - templates folder to host all front end html pages
    - static folder to store logs and favicons on homepage

- *forum* to deal with the posts comments and watchlist items
    - models.py consists of models to store topics and comments that users make in the posts in each stock
    - views.py deals with adding of topics and comments and setting replies to comments

- *Settings.py*
    - Customised to use email authentication instead of  username
    - Added whitenoise middleware to server static files
    - Customised CKEditor elements 
    - Customised Security config for Azure hosting

#### How to Run the application
- You can see the webiste at [http://rallyproduction.azurewebsites.net/](http://rallyproduction.azurewebsites.net/)
- Install Pip
- Install Packages in requirements.txt or manually install
   - Django>=4.2.5
   - whitenoise>=6.5.0
   - django-ckeditor
   - yfinance
- Run Python manage.py runserver in the Directory

#### I am looking forward to improve the front end using react and tailwindcss and integrate oAuth for sign in/up for the users. 
#### I have hosted the website in azure appservice using github deployement at [http://rallyproduction.azurewebsites.net/](http://rallyproduction.azurewebsites.net/)

##### Thank you for the course and oppurtunity to learn CS50W Programming with Python and Javascript. 
