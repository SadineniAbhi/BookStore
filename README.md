This is A Flask application 

HERE IS THE DOCKER IMAGE https://hub.docker.com/repository/docker/sadineniabhi/bookstore/general 

READ THE INSTALLATION.TXT CAREFULLY

#######################################################################################################################

TO ACCESS ADMIN PRIVILAGES

.username:- admin1234
.password:- admin1234

########################################################################################################################


@@@@@@@@@@@@@@@@@@@@@@@@@@@#####    API ROUTES       ########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

1. /api/books --- HANDLES GET POST PUT REQUEST TO MANAGE THE INVENTORY.
2. /api/orders --- HANDELS GET AND PUT REQUEST TO MANAGE ORDERS.

@ USE POSTMAN OR ANYOTHER REQUEST SENDER TO USE THE APIS

TAKE A LOOK AT THE CODE BEFORE MAKING ANY REQUESTS THE JSON OBJECT NEED TO CONFIGURED IN THE WAY THAT IT CAN BE HANDLED. 

@@@@@@@@@@@@@@@@@@@@@@

GOOGLE TOOL:-

#THE WEBSITE IS HOSTED AT https://quantum-star-403121.el.r.appspot.com/

  .The site is not handling post requests due to the using SQLite database checkout the link below for more details:-
  https://stackoverflow.com/questions/28184630/open-sqlite-database-on-google-app-engine#:~:text=You%20can%20use%20SQLITE%20on,%2C%20a%20writable%20%2Ftmp%20directory

  To fix the issue I should use GOOGLE-BIG-TABLE And it is more affordable compared to google sql instance.

  #Tried to host it on google compute instance but facing issues with the nginx.#


    
