## Welcome
Hi Amelia, Jasper, and Dad!
This project aims to teach you how to code some basic Python.
In this project, we will be building a football data API. I am sure some of you 
have alot of questions about why I chose this project to be your first and 
questions about what even is an API. Don't worry I will answer all of them!

## WTF is an API
Firstly, what the hell is an API, and why do I even care? API stands for Application
Programming Interface, which in simple terms is first making an application (or an App), then
making it have an interface that you can interact with programmatically. Almost all web applications
and mobile apps rely on APIs, and being able to build APIs helps you better think about data
and programming, and how they interact. This project will not be super intense, but I hope 
it can give you a solid base to think about what else you can build.

## The project
The scope of this project is to build an API for NFL football data, such that we can eventually set 
up a server that Dad can use to get the data he needs for his football simulation. Currently, Dad uses
web scraping techniques, and these sites are constantly changing their website design, making it hard to scrape
and get the data he wants. I hope that we can build something useful for him and teach you guys some basic skills.

## Setup
In a terminal type: (ignore $ it's just convention)
```
$ git clone https://github.com/William-Metz/footballapi.git
$ cd footballapi
$ make setup
$ make run
```

## Example
In you web browser enter

```
http://127.0.0.1:5000/
```
It should say "Hello, guest!"
```
http://127.0.0.1:5000/?name=will
```
It should say "Hello, will!"

You can also open another terminal and enter: 
```
 curl -X POST http://127.0.0.1:5000/ \
     -H "Content-Type: application/json" \
     -d '{"name": "Will"}'
```


## Homework 1
I have already created a welcome endpoint that says hi to the user
or guest (if name is not specified)
You can see this in `example.py` ,please add your new endpoint in that file too
You're task for this week is to create an endpoint ``` http://127.0.0.1:5000/family/ ```
that will take a name and return whether they are part of the family and a fun fact
``` http://127.0.0.1:5000/family/?name=sam ```
It should say something like: "Sam is a member of the family and is our favorite dog."
But something like
`http://127.0.0.1:5000/family/?name=aaron `
Should say, "There is no Aaron in the Metz family."
Please also handle if there is no name given

This is quite open-ended, so if you have any other ideas, feel free to share them as well.
This should work easily on Jasper's, Amelia's, and Dad's computers. We may do a Zoom call. 
Good luck, and please don't hesitate to send any questions you may have. Try to finish this by Friday (it shouldn't take more than an hour, if it does, please ask for help)!

