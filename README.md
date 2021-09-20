# TASK C - REST API with authentication and authorization

## Set-up instructions:
1. `git clone` this repository
2. Open a terminal window to the local cloned folder and set up a python virtual environment using - `virtualenv bin`
3. Activate the python environment - `source env/bin/activate`
4. Run `pip install -r requirements.txt` 
5. Activate the flask app by running `FLASK_APP=auth`
6. To set up the sqllite database for testing - Open the interactive python interpreter using the command `python` and run commands `from auth import db, create_app` and `db.create_all(app=create_app())`
7. Now we can run the flask app by simply running - `flask run`

## Testing signup and login
1. Open postman and in the form-data body add three fields. {Key:username, Value: `string`}, {Key: password, Value: `string`}, {Key: isAdmin, Value: 1 }) and send a post request to `http://localhost:5000/signup`

2. Upon sending this you will recieve a status on whether the user already exists or was newly created

   ![image-20210920113133599](C:\Users\banik\AppData\Roaming\Typora\typora-user-images\image-20210920113133599.png)

3. In the Authorization tab of postman add the username and password and send a post request to `http://localhost:5000/login`

4. You will receive a `Token` from the API after sending this request

   ![image-20210920113228896](C:\Users\banik\AppData\Roaming\Typora\typora-user-images\image-20210920113228896.png)

5. In the params tab of postman add a field of {"x-access-tokens": `Token`} and in the body tab add a field of {"description": `string`}

   ![image-20210920113408049](C:\Users\banik\AppData\Roaming\Typora\typora-user-images\image-20210920113408049.png)

6. Send a post request to `http://localhost:5000/todo` and recieve a response of `Todo Added` 

   ![image-20210920113455254](C:\Users\banik\AppData\Roaming\Typora\typora-user-images\image-20210920113455254.png)

7. In the params tab of postman add a field of {"x-access-tokens": `Token`} - place an invalid token in this case, and in the body tab add a field of {"description": `string`}.

8. Send this post request to `http://localhost:5000/todo` and recieve a 401 response of `Token is invalid`.

   ![image-20210920120005281](C:\Users\banik\AppData\Roaming\Typora\typora-user-images\image-20210920120005281.png)

9. In the params tab of postman keep the field of {"x-access-tokens": `Token`} and send a get request to `http://localhost:5000/todos`

10. Recieve a list of todos linked to your username

    ![image-20210920120837724](C:\Users\banik\AppData\Roaming\Typora\typora-user-images\image-20210920120837724.png)

11. To test authorization create a new user using step 1 with the isAdmin field = 0. Repeat steps 3, 5, 6 and 9. You will recieve a 403 error of "Not authorized".

    ![image-20210920121057420](C:\Users\banik\AppData\Roaming\Typora\typora-user-images\image-20210920121057420.png)
