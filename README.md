# Smart_Traffic_Appserver

This is the server part of the Smart traffic light project, which takes on the managing and the updating of the database.
The client disturb first client there are two types of the service client the first client is an mobile app which interacts using AWS amplify and the API gateway after logging in the application will keep sending the GPS location to the server and the server will automatically calculate each users location and

The other client is there traffic light smart traffic light part which in this project is the raspberry pi module that has a camera and a LiDAR sensor and when the raspberry pi attacks and object using the camera well identify the object and locate its exact distance from the traffic light using the LiDAR sensor the processing of the object will be assisted with using the Google coral computing stick board after identifying and calculating the distance of an object it will upload do you information to the third verse database ideally the smart self driving car will access to the traffic lights database and it will try to make a more accurate image of an environment around the traffic light the cloud server and the app server is consistent with it's based on a three tier architecture first the client access the server with the API gateway which is managed by the AWS Cognito authorizer only the user who is authorized will be able to use the API and then the second tier is the lamb dissection which is the server less computing section only if an API is used  it will try to access DRDSNDS3 service 

After searching or updating the data it will return the results to the client 

We are currently planning to make a GPS calculating server by using EC to virtual machine services which could be able to access the RDS server it will constantly searching for the user who is near the traffic light and if 

And it will constantly calculates the optimal green light time signal and will send the time results to the raspberry pie client IIs t

<img width="1277" alt="Screen Shot 2021-09-08 at 1 40 09 AM" src="https://user-images.githubusercontent.com/30145956/132381052-d04f3514-d4e7-4b4b-ae9e-4c11f54bb2f9.png">

