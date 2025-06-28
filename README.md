## Welcome
Hi Amelia, Jasper, and Dad!
This project will hopefully teach your guys how to code some basic python.
In this project we will be building a football data API. I am sure some of you 
have alot of questions about why I chose this project to be your first and 
questions about what even is an API. Don't worry I will answer all of them!

## WTF is an API
Firstly, what the hell is an API and why do I even care? API stands for Application
programming Interface which in simple terms is first making an application (or an App) then
making that it has an interface that you can interact with programatically. Almost all web applications,
and mobile app rely on APIs, and being able to build APIs helps you better think about data
and programming, and how they interact. This project will not be super intense but I hope 
it can give you solid base to think about what else you can build.

## The project
The scope of this project is building API for NFL football data such that we can eventually set 
up a server that dad can use to get the data he needs for his football simulation. Currently dad uses
web scraping techinques and these sites are constantly changing their website design making it hard to scrape
and get the data he wants. My hope is we can build something useful for him and teach you guys some basic skills

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

You can also open another terminal and enter 
```
 curl -X POST http://127.0.0.1:5000/ \
     -H "Content-Type: application/json" \
     -d '{"name": "Will"}'
```


## Homework 1
I have already created a welcome end point that says hi to the user
or guest (if name is not specified)
You can see this in `example.py` please add your new end point in that file too
You're task for this week is to create and endpoint ``` http://127.0.0.1:5000/family/ ```
that will take name and return whether they are part of the family and a fun fact
``` http://127.0.0.1:5000/family/?name=sam ```
It should say something like: "Sam is member of the family and is our favorite dog"
But something like
`http://127.0.0.1:5000/family/?name=aaron `
Should say, "Their is no aaron in the metz family"
Please also handle if there is no name given

This is pretty open ended so if you have any other ideas feel free to do that too.
This should work pretty easy on Jasper computer, amelia and dad we may to do a zoom call. 
Good luck and send questions if you them. Try to finish this by friday!

