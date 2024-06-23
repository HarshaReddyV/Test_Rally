#Final Project submission for CS50W Programming with python and Javascript

###Distinctiveness and Complexity:

    As a part of final project for cs50w I chose to build a forum for share market investors based on Indian Capital market. In this project all the stocks traded on two major stock exchanges in India namely NSE and BSE are listed on the home page with a search functionality at the top. User can sign in/up through the navigation menu before accessing the webapp. I have made changes to the authentication backends to use user's mail addresses for authenication instead of the default username. This particular project was chosen as it is quite frustrating to not find anything similar in the Indian market and also inspired from other forum *hotcopper.com.au* which I have addictively used while in Australia. I chose to address the issue by building something i can probably want for myself and hopefully share it with other users like me in the future. It is distinct from other projects in the course as I have populated with market data and integrated rich text editors in the comments and used user email as a authentication backend I have also used webscraping tool yfinance to get the prices for the share market in near real time as alternative to paid api's.  

    User can acces stocks either through search or scrolling on homepage. Navigate to the stock of their choice and add topics for discussion such as the recent financial results and change of management. User can add the stock to their watchlist to access it in the future which is updated using Javascript Api call to the backend without reloading the page. 

    In this project two apps were registered namely, *home* to deal with the navigation on the front end, user authenication and *forum* to deal with the posts comments and watchlist items. For Models, in *home* we have User,WatchList,Tickers and in *forum* we have Topic and Comments. 

    I am looking forward to improve the front end using react and tailwindcss and integrate oAuth for sign in/up for the users. 
    I have hosted the website in azure appservice using github deployement at [http://rallyproduction.azurewebsites.net/]http://rallyproduction.azurewebsites.net/

    Thank you for the course and oppurtunity. 
