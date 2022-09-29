## Create a VPC
-A vpc is a virtual private cloud. It is a private cloud that you can use to create your own data centers and create things like subnets.
![Screenshot (117)](https://user-images.githubusercontent.com/97908618/192110253-514d3340-a0db-4c35-a8a2-ab2d9fc843f2.png)

## Create a subnet
-A subnet is a range of ip adresses that are in your VPC. Each subnet has its own Availability zone.
![Screenshot (118)](https://user-images.githubusercontent.com/97908618/192110257-2926e8bf-bbbc-4f5f-9642-5f4a3d084526.png)

## Create an internet gateway
-A internet gateway is basically when a network sends data it stops at the gateway so that we can send and recive data.
![Screenshot (116)](https://user-images.githubusercontent.com/97908618/192109952-5104692a-85ac-42db-a296-2e6731ab792a.png)

## Create a route table
-A route table tells us where network traffic is going or where the gateway is sending and receiving data. This can happen with or without the subnet.
![Screenshot (115)](https://user-images.githubusercontent.com/97908618/192110049-9d222cb8-28e8-49b7-b634-b1c2dba5080a.png)
![Screenshot (119)](https://user-images.githubusercontent.com/97908618/192287038-59b22393-b1c9-435e-90ea-65fff720d9ff.png)

## Create a security group
- A security group id basically wear you can a control inbound and outbound traffic for you instance.
![Screenshot (128)](https://user-images.githubusercontent.com/97908618/192925278-e5744021-bb75-4b14-94b1-dad7c2e2c1fb.png)

## New instance
-The AMI that i selcted was the ubuntu AMI. I used the Ubuntu AMI because i am using the Ubuntu defult user for my system.
-When the machine got created it chose for itself a private Ip adress. WHat we have to do is take out elastic ip and associate it with our instance. It will the auto selct a private ip adress.

-How i connected my VPC to my instace is when i created my instace i had edited the network settings and changed the VPC to my Cheema-vpc

-How i created my instance was i went onto the new instances tab clicked on launch instances. Then i taged it with my last name naming it Cheema-instance.
-To get my Elastic ip adress i went under the network tab and clicked on elastic ip and then clicked on allocate elastic ip. And then also taged it with my last name.
-

![Screenshot (126)](https://user-images.githubusercontent.com/97908618/192825615-ccac8dc4-53f2-48a0-a269-180cc627aac7.png)
![Screenshot (130)](https://user-images.githubusercontent.com/97908618/192926138-a114529e-a608-4e58-9c38-403af14c06d2.png)


