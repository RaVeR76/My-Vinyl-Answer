# **My-Vinyl-Answer**
 
![My Vinyl Answer](https://github.com/RaVeR76/my-vinyl-answer/raw/master/wireframes/vinyl-showcase.png)
 

## **Project Goals**

I'm a DJ (mainly a Bedroom one though .... see my MS1 project ha ha) and have been DJing for 25 years. I do it because I love the music, I love the people and I love the feeling of making people smile through the freedom of my sets :)
I have hundreds of records, aka Vinyl, which I have been collecting from the mid 90s to now and I am still buying them .... it's like an addiction to be honest !
I've tried to attend V.A. classes *(Vinyls Anonymous)* but they will never change me so I may just try to keep track of what I am buying and why .....  
This is were my idea for a project comes from. I don't know how many vinyls I have, I don't know what genre they are when I look at them, obviously I know some like the classics, but the majority I need to play before I can ascertain what genre they are. The amount of times I have went through my whole vinyl selection to try and get some sort of order and organistaion is completely criminal and so time consuming it's unreal. 
Again, this is were my project comes in ! I want to have a once and for all list of my personal vinyl and as much information per vinyl as possible which I can search and hopefully help my keep track of .... I may even add a random function to help me select some cool SETS to play from the various genres I have :)


**Remember ..... Hug Harder, Laugh Louder, Smile Bigger & Love Longer !** 

--- 


## Contents
- [UX](#ux)
  * [User Goals](#user-goals)
  * [User Stories](#user-stories)
  * [Site Owner Goals](#site-owner-goals)
  * [User Requirements and Expectations](#user-requirements-and-expectations)
    + [Requirements](#requirements)
    + [Expectations](#expectations)
  * [Design Choices](#design-choices)
    + [Fonts](#fonts)
    + [Icons](#icons)
    + [Colours](#colours)
- [Wireframes](#wireframes)
- [Features](#features)
  * [Existing Features](#existing-features)
  * [Features to be implemented](#features-to-be-implemented)
- [Technologies Utilised](#technologies-utilised)
  * [Languages](#languages)
  * [Tools and Libraries](#tools-and-libraries)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Conclusion](#conclusion)
- [Credits](#credits)


## **UX**

### **User Goals**

* An easily accessible database for all my vinyl collection
* Be able to search my vinyl database for specific vinyl by their various attributes
* List my vinyl collect alphabetically when required
* The website will have to work well on all devices
* Navigate around the website with ease and pleasure
* An aesthetically pleasing and visually appealing website


### **User Stories**

* As a user, I want to be able to register for my own account
* As a user, I want to be able to login so I can have my own personal environment or enVINYLoment as I like to call it (sorry that was bad)
* As a user, I want to be able to know what vinyl I have collected over the years
* As a user, I want to list my vinyl collection by genre or year which are the most important aspects as a DJ .... (or by any attribute possibly)
* As a user, I want to be able to rate my vinyl as they are not all as good as the next one
* As a user, I want the website to be easy to use
* As a user, I want to possibly add some specific notes attached to each vinyl if required (a note like small scratch at start)
* As a user, I want to be able to add as many vinyls as I want
* As a user, I want to edit any vinyl info if I want
* As a user, I want to delete any vinyl I want (if I sell one personally or on another site)


### **Site Owner Goals**

* To have a great website that vinyl collectors can keep track of their personal vinyl collection
* To have an easily accessible website where the user can find specific vinyl by an easy search method
* Add login access for site user to perform CRUD (Create, Read, Update & Delete) within their personal vinyl collection / database
* Have a easily navigated and user friendly admin area for admin CRUD duties


[Back to Top](#contents)

### **User Requirements and Expectations**

#### Requirements 

* Multi page design
* Ease of navigation
* An aesthetically pleasing website
* Easy to perform CRUD operations on each vinyl stored in their database
* Contact form for contacting the developer with any bugs or future suggestions to make the site better
* A little uniqueness to hopefully stand out a little bit more


#### Expectations

* To enjoy the website layout and navigate freely with no issues
* Be able to search my vinyl collection by the various attributes 
* Contact options in case the user has found some bugs that need fixing
* For the user to be able to access their personal collection / database and make changes easily


### **Design Choices**

I am going to slip out of my comfort zone with this project and I'm going to use the framework Bulma, on the recommendation of my mentor.
He wants me to push myself and try new things so I'll give it a go for sure.
I just want it to be a simple and easy on the eye .... nothing too adventurous or loud !
It will be a multi page website so that the user can click between pages to utilise the full atonomy of my design :)
I will be using MongoDB as the database for my application as I found it fairly easy to use and have some knowledge of it now.


#### Fonts

For my fonts, I am going to use [Google Fonts](https://fonts.google.com/) as my source of inspiration :)
I have settled on the simplicity side of things & the more user friendly style of [Titillium Web](https://fonts.google.com/specimen/Titillium+Web)
for the main text and [Roboto](https://fonts.google.com/specimen/Roboto) for titles and section headings.

Below is an example of my fonts where the title is in ***Titillium*** and the text is in ***Roboto*** .....

![My-Vinyl-Answer Fonts](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/fonts-example.png)


#### Icons

[Font Awesome](https://fontawesome.com/) will be the main source for any icons that I require. 
I will deffo be using the various basic icons and some music icons on my website.
Other than them, we will just have to see what suits and fits the web page layout perfectly.


#### Colours

I love happy, bright, vibriant colours to be honest as I am an ex-raver and generally a chilled out happy go lucky person 
(I had to use the term *generally* because of JavaScript ha ha .... deffo lost a few hairs over that one).
Anyway, I don't want to make this website too loud and off putting but I want the colours to have like a chilled out vibriant feel, if you get what I mean.
Basically not too bright but not to dull either .... still confused, yeah me too ! I think AMBIENT is the keyword I'm looking for here :)  

So the colours I have mainly settled for are :

|Name                  |Hex Code   |Basic Description  |Usage                           |
|:--------------------:|:---------:|:-----------------:|:------------------------------:|
|***Cultured***        |#F5F5F5    |Off White          |Body background, text & titles  |
|***Blizzard Blue***   |#A1EAF7    |Light Sky Blue     |Body background                 |
|***Fuzzy Wuzzy***     |#E36464    |Bubblegum Pink     |Body background                 |
|***Smoky Black***     |#110303    |Off Black          |Body background, text & titles  |

Below is an image of the chosen colours .....

![My-Vinyl-Answer Colours](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/color-scheme.png)

Follow up on the colours used above.....
About half way in to this project whilst I love the colours above I just thought the overall website looked a bit boring and plain. So I jumped on the Google Image train to trans-central and searched for some free vinyl images I could use to revamp this project. I found a few and tried them but then I came across the reddish blueish vinyl on the deck one and I thought that's it there. I placed it as my body background and fell in love. The issue was my wee colours above were close but not close enough. I still use them for borders, buttons and my vinyl collasibles because they still fitted beautifully there but for the headers and titles then didn't. 
So I used an online site called [Image Color Picker](https://imagecolorpicker.com/en) to select some colours from my image .... the red and the blue to be precise and using them with the image as a backdrop works really well throughout website, in my opinion but who's to say I'm right ... eh ! I do and it looks cool as feck .... alright ha ha !
That's the story behind the colour changes but I had to, just to spice a little life into the visual aspect of the site.
P.S. I'm not sure if I am to change the original colours out or keep them up as these were my intial thoughts but the Smoky Black is the only O.G. left from the original line up.  

[Back to Top](#contents)

## **Wireframes**
---
The software that I used for my wireframes was Balsamiq. This was the third time I used this software & it was deffo a lot easier to understand what you need to do. The software allows you design the basic layout of your website on devices such as a desktop, tablet and mobile. They are just simple 2D sketches but I now understand how important these really are :) 
I think my wireframes look good & deffo give me a great starting point for the design process !

Anyway, you can have a wee look at my wireframes below:

#### Mobile Wireframes
- [Mobile Home Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/mobile-home.pdf)

- [Mobile About Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/mobile-about.pdf)

- [Mobile Login Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/mobile-login.pdf)

- [Mobile Register Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/mobile-register.pdf)

- [Mobile My Vinyl Collection Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/mobile-myvinylcollection.pdf)

#### Tablet Wireframes
- [Tablet Home Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/tablet-home.pdf)

- [Tablet About Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/tablet-about.pdf)

- [Tablet Login Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/tablet-login.pdf)

- [Tablet Register Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/tablet-register.pdf)

- [Tablet My Vinyl Collection Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/tablet-myvinylcollection.pdf)

#### Desktop Wireframes
- [Desktop Home Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/desktop-home.pdf)

- [Desktop About Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/desktop-about.pdf)

- [Desktop Login Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/desktop-login.pdf)

- [Desktop Register Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/desktop-register.pdf)

- [Desktop My Vinyl Collection Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/desktop-myvinylcollection.pdf)


[Back to Top](#contents)


## **Features**
---

### **Existing Features**

* The user will be able to register
* The user will therefore be able to login, in future (after intial registration of course)
* The user will be able to log out
* The user will be able to perform CRUD functions on their own vinyl collection
* Admin will have access for site maintenance
* Admin will be able to carry out CRUD functions on all database collections


### **Features To Be Implemented**

* Share vinyl list with other users for possible sales or swaps if duplicates
* Allow users to display their vinyl collection to other users but for view only
* 5 star ratings or something for users vinyl
* Add some pics of the vinyl for storage with the information in the database
* Have change and forgotten password options
* Add some visual graphics of the users collection per genre


[Back to Top](#contents)

## **Technologies Utilised**
---

### **Languages**

- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS) 
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) 
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) 

### **Tools and Libraries**

- [Git](https://en.wikipedia.org/wiki/Git) 
- [GitPod](https://www.gitpod.io/)
- [Heroku](https://id.heroku.com/login)
- [Bulma](https://bulma.io/)
- [jQuery](https://jquery.com/)
- [MongoDB Atlas](https://www.mongodb.com/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [PyMongo](https://pymongo.readthedocs.io/en/stable/tutorial.html)
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
- [Balsamiq](https://balsamiq.com/)
- [W3C HTML Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)

[Back to Top](#contents)

## **Testing**
---

### Do You Know Reggie Star?

#### User Story : I want to be able to register for my own account

* **Plan**  
I want the user to have the ability to register for **My Vinyl Answer** so they can log in anytime in the future with ease.
I will create a register form where they will have to input their full name, a username, an email address and a password. 
There will be a Sign Up button available which will POST the data to the database. 
I will add some defensive programming so that usernames will not be duplicated. I will check to see if the new username already exists in the database and if so flash up a an alert but if not then render their profile page. This will be populated with the information they just input and also a welcome message will appear ... obviously I will not be displaying their **password** within their profile or anywhere in fact ha ha !



* **Implementation**  
I created a simple *Sign up* page which has a simple form made from Bulma components. Once the new user fills these in and hits the button. My ```signup ()``` function
kicks into action and checks if the username exists, if it does then I let the user know by a wee flash message and return them to the signup page.
If the user doesn't exist then I take their filled in data and store it in a dictionary I called *signup* which I then *insert* into the Mongo Database. I also add the username to the session cookies for utilising whilst they are logged in. Let's not forget my wee flash message to welcome them to my website and  then send them to their profile page.
I added an input for the user to add a url of a pic they can use as a profile pic. It works most of the time if the truth be told but it's not perfect at present. Google images says to share the image and then copy the link this way but I find this doesn't work. If you find the image then right click and copy image address then this works for me. Anyways, I've added like a big smiley raver face as a default image so no one should be left with blank image or broken link.  
I added validation to all inputs and added some requirements like min lengths or @ for the email.
Password will be encripted by using hash method through the **werkzeug.security** utlity ..... generate_password_hash for generating and check_password_hash for, well you've guessed it ... checking ha ha ! So basically your wee password is taken and mashed, hashed, bashed up and stored in the database and when you login it becomes unbashed, unhashed and unmashed so that it can be compared with the login password at the login stage. 
That's the basic terms of it anyway .... all this hash talk is making me ***salivate*** to be honest, so let's move on quickly.  
I also added some Caps Lock code for super cool effect because if the truth be told, I sat for about an hour one evening trying to figure out why my login wasn't working and it was because I had Caps Lock on. You're thinking but should you not have noticed this at the username part ... well no is the answer because I was always clicking the selection from my input pop down history thingy so was never actually inputting my username. Anyway, that's the truth behind the reason why I have a Caps Lock check on the password entries.
Finally, I had to put the Javascript for Caps Lock function on each password page because when it was in my main js file, it conflicted with the users vinyl collapsible but this was a bug which I'll talk about in the bugs section.

* **Test**  
I have logged in with various fake users and my test users registered too. If a username already exists it tells them and if the user data doesn't match the specific criteria then it alerts them. If the user has Caps Lock On when inputting their password, it tells them. The user account is created when all the criteria is met and the user is redirected to their personal profile page. To be honest the Profile pic worked most of the time but sometimes it didn't but I know it's to do with the copy url link the user makes. The user gets a Big Happy Smiley Face anyways, so who's complaining .... gotta love a default image :)

* **Result**  
Sign up form works really well and as planned. The users personal information is stored safely in the MongoDB Users Collection and then retrieved for displaying on their profile page. Validation and minimum / maximum lengths keeps the data limited and everything in check. The form looks aesthetically pleasing and easily understandable. A flash message also appears to welcome the user after sign up.

* **Verdict** 
Let's face facts it's not gonna win **Best Form Design Of The Year** at the International Coding Awards but I am so happy with it. I love the vibrant blue which blends in with the blue from the background image (because I stole the blue from the image ha ha). It's easy to fill in and the users data gets stored correctly.



### EnVINYLoment Tut Tut

#### User Story : I want to be able to login so I can have my own personal environment or enVINYLoment as I like to call it (sorry that was bad)

* **Plan**  
I want to create a website that is unique to each person and allows them to feel welcome everytime they log on.
The user will first have to sign up with some basic details which will be added to the user database.
After this, each user will have a personal username which will be one of a kind, as I will add code to eliminate duplication.
They will have access to their own vinyl collection which they will have to build from scratch themselves obviously, unless I'm
some kinda vinyl stalker who knows what each user has in their record boxes or attics !
I may possibly add some sort of a simple profile pic code that the user can utilise to add a URL link for their profile pic (save db space plus keeps it simple)

In production, you could probably give the user the ability to delete their profile if they wanted to but I will add Admin Access to the website
for the ability to delete users.

* **Implementation**  
Ok so like I said above, the user signs up for the first time then they have access to their personal space moving forward. They can then use the simple login page for future logins. All they need here is their unique username and password. These two pieces of info are then passed to the ```login()``` function which basically checks the login combo against the database. If the user is unknown it will flash a generic error message and redirect to the login page again. If the user is known then it checks the users password using the hash method mentioned previously. If the password is incorrect it will flash the generic message and redirect the user to the login page yet again. 
Now after all them mind challenging tests that if the user gets their username right and the correct password is entered ... they will then be accepted into their own wee world of My Vinyl Answer :)  
Within the realms of My Vinyl Answer they will first see their profile page then they will have access to their personal vinyl collection ... obviously once they build it up over time. They will have access to the add vinyl form where they can start to build their collection. Finally a logout option. I know it's pretty basic for the user but it's got the potential to expand and be much better. Time constraints and lack of knowledge at this stage but as the project progresses, I think you'll see it gets better as I utilise Bulma a lot more in the Admin secton.

* **Test**  
So once the user signs up or logs in, they get redirected to their profile page form here they can navigate to their personal vinyl collection, they can add new vinyls or they can log out. All these links worked well with no issues. The add vinyl form was easy to use and worked well. The My Vinyl Collection area was very beautiful was some of the statements from my testers. The colours worked really well and were not too over powering. The collapsibles were smooth and it was cool that they hid the edit and delete buttons. Search function worked well per user and everyone was happy with all functionaility and navigation within their User EnVINYLoment .... Am I getting ye yet?

* **Result**  
I think the overall user environment works well and the navigation is straightforward and easy to understand. Again, I'll raise the point I've made a few times that the Admin vinyl collection format is probably a lot better functionality ways than the user vinyl collection page. I designed the user one first and I really like it so that's why it stayed. It's basic but visually more appealing for me. I love the admin one for ease of use and you can locate your genre collection with one click using the tabs.

* **Verdict**  
Overall, the user experience was very positive and the special selected few who tested my admin section said it was awesome and easy to use too. Again, I think the blend of colours with my background image for the user vinyl collection page works so good that I couldn't change it to a Bulma format. 



### A Record Of Records

#### User Story : I want to be able to know what vinyl I have collected over the years

* **Plan**  
Maybe it's just me that has an issue with keeping track of my vinyl but I know I have mates that are like me. Vinyl everywhere and they 
generally don't know how many they have, what genre they are or what year they came out. I have seen some really well organised vinyl but these were
basically like alphabetically but by genre. I just want the user to have a simple database of all their vinyl, that they can call upon using my application.
The hard part is adding all the vinyl at the start but once it's done .... it's done !  
I wish there was an easier way like scanning the barcode or something but some of these vinyls are pretty oldish and I honestlty don't know if the barcode would 
work or not. I'm now kinda intrigued to see if it would work anyway for possible a future add on :) I'll come back to that one and let you know sure !
The point being that I want the user to be able to add, delete, lookup and edit any of their own personal vinyl collection as and when required.
The database will store the name, the artist, the genre, the label, a brief description and the release year. 
I may add admin access where they can add new catagories to the databases and edit user profiles etc. You may wonder why a user can't do this for themselves but
I just want the admin to do it for the purposes of this project. In production, you could write the code to allow a user the ability to add an extra 3 
personal database fields with a certain amount of characters per field, make it a little more personal to the user :)
Anyway, it's a simple database that the user can salivate over anytime or anywhere .... as long as they have a computer or mobile device ... with internet of course ha ha !


* **Implementation**  
Each user has the ability to add vinyl with the add vinyl form. Once the user fills the correct details out that match my validation then this form data is passed into the ```add_vinyl()``` function where it adds this new vinyl to the database.
I added the *secret* code of ```"owner": session["user"]``` to the document so that I can utilise this to display the users own vinyl later on. This data is inserted into the Mongodb database and my standard flash message makes an appearance as usual. I'm kind of thinking about added the Flash Gordon sound clip eveytime it pops up .... Flash !!! Woooo-ho .... Defender Of The Universe !!! Ha ha, I just googled that clip to make sure it was right, still not sure by the way but did you know that Ming The Merciless, Flash Gordons evil arch nemisis was actually from a planet called ***MONGO*** ..... sure you couldn't write it, could ye !!! That's one of them fate thingys for sure ... love it !
Sorry, got off track there for a minute with my Ming Moment, so once the user adds some vinyl they will see their My Vinyl collection getting bigger.
As I said above about the secret code, I use ```{% if session.user|lower == vinyl.owner|lower %}``` in the users main vinyl page html to only allow the current user in session to only see their own vinyl and no one elses (unless you're admin). Within their Vinyl Collection environment they can see all their vinyl and they have the ability to edit and delete each vinyl also. 
They will be able to edit their vinyl by clicking the edit button which calls the ```edit_vinyl()``` function and passes the vinyl id of the chosen vinyl into it. The function then populates the edit_vinyl_form for the user to edit. Once the user makes their changes they can submit the changes back to the ```edit_vinyl()```function which updates the vinyl's document and redirects them to the edit vinyl form again. A cancel will take them back to their vinyl collection where the changes will have been updated too. 
The user has the option to delete a vinyl from their collection too. Once they choose to delete one, the delete confirmation modal is called for where I double check that they (the user in bold) wants to delete the vinyl (added name of vinyl in bold too). Once the user, selects to confirm delete then ```delete_vinyl()``` function is called for where the vinyl id is passed to. This function then deletes the document asscociated with the passed vinyl id and redirects the user to their vinyl collection again, not forgetting about the wee flash message. Here the user can see that their vinyl has been deleted from the list too. 
I know the user vinyl interface is again pretty basic but this was the first thing I developed and as I got to use Bulma, I realised I could have used a lot more of it's components. Honestly, as basic as it looks, I still love it because I created it from the W3 Schools collapsibles and made it my own. I know it can  be made better but for me it just suits this wee project.

* **Test**  
My testers, fakers and I .... now that really does sound like a Hollywood comedy classic ! Anyway, we all added various vinyl and tested the validation and all worked well. The vinyl form data was easy to fill out and once saved, it gets stored within the Vinyl collection in MongoDB. The user or admin can then access this document to do what ever they want to it but within the legality of the CRUD functionality. All worked well with no issues and each user could only see the vinyls they had added.

* **Result**  
Very happy with the results. All testers added their own vinyls with no issues and had access to them from their vinyl collection page. The user could search through their vinyl collection for vinyl that matched their search criteria. All worked perfectly and the reset buttons reset the search function. The admin tabs are cool in that you can you hit a genre and it filters the collection instantly. This would deffo be an add-on for the user at a later date as it's functionality is very useful.

* **Verdict**  
Overall, very happy again ... and that's coming from someone who is generally always happy and a little hyper !! The shock ... the horror ... I hear you say ... RaVeR76 HYPER ... Neeeeevvvvvveeeeeeerrrrrrr !!!
Love it all so there .... 



### Finding Nemo 

#### User Story : I want to list my vinyl collection by genre or year which are the most important aspects as a DJ .... (or by any attribute possibly)

* **Plan**  
I want the user to be able to search through their personal vinyl collection by genre or release year at the very least but possibly more.
Although I said in the title that this would be good for a DJ, it would still be a great option for any vinyl enthusiast .... the ablity to search their
collection. Why, you may ask? Well, I'll give you my main reason .... duplication !!!   
The amount of times I have bought a vinyl or even a CD that I already feckin had is criminal, although the sound is amazing with two identical tunes playing on the decks
and the beats are cancelling each other out and all. It creates so many emotions when you realise your mistake .... anger, this cost me money .... laughter, can't believe I was so stupid .... worry, jeez my memory is so awful .... happiness, the 90s was so unbelievably awesome and you felt free ..... laughter again, cause I realise that I can't remember what I watched an hour ago on TV but I can remember the 90s :)
So for me to check if you already have that vinyl you are watching on ebay or Discogs would be a good reason.
Also music has changed through the ages so maybe the user is in the mood for a 70s themed evening and isn't sure what 70s songs they have. 
Alexa aka My Vinyl Answer ... what list of vinyls have I from the 1970's? BANG! Search code activated and VOILA !!! ... Your list of 70s classic at your fingertips.


* **Implementation**  
I stated some sort of search function was required and that the DJ ones were important. I think at the start fo this project I was possibily aiming down the DJ route again but as it developed I thought it would be great for all vinyl enthusists not just DJs.
Moving on, I added a little search bar above the users vinyl collection with a reset button and a search button for submitting the input to the ```vinyl_search()``` function. Wthin here, it searches through the vinyl for the matching criteria and then displays the matching vinyls. I set up a collection index (query) using the vinyl_name, genre_name, vinyl_artist, release_year and owner as these would be the main searching points I felt. So basically, the user can search all their vinyl as long as it matches the required query fields. If not then a **No Results Found** message is displayed. 
The user can also reset the page so that it goes back to there full collection. Again it's pretty basic but as my knowledge gets better so will the search functions.  
In Admin access I use a Bulma panel to display all vinyl and I think it looks quite well. You may wonder why not use this format for the user vinyl collection? Like I said before as I got used to Bulma moreso at the admin part plus I loved the original authenticity of the users vinyl collection format too so didn't want to change it at this late stage. For me, the users looks more appealing than the admin one to be honest. Anyway, the admin has basically the same display functions and search functions as the user, only I added some panel tabs for quicker search functionality. I created a function for each genre that when selected it displays all vinyl associated with that genre. Don't get me wrong, I know there is probably a simpler method that uses less code to do all five functions in one ... but unfortunately I don't have time on my side at this moment in time so this works for me and I can look at simplifying it at a later date. I'm still super happy I got it working so well, mind you :)

* **Test**  
We all tested this as users using the search box with our user vinyl collection. I told the users what they could search for as there were two areas that weren't covered .... vinyl description and vinyl label. I covered the rest within my index set up. All worked well within the user environment and it is pretty simplistic to be honest. The admin search functionality has a little more oomph to be fair and is very user friendly. I really loved using Bulma for the first time ... just took me a wee while to get used to it. 

* **Result**  
All search functionality worked well across all users and admin. Any searches carried out across the key areas within the query where displayed and when no searches where found, a message was displayed to say *No Results Found*. 

* **Verdict**  
Very happy with the search functions and everything works as planned.




### Rate My Plate .... I Mean Vinyl

#### User Story : I want to be able to rate my vinyl as they are not all as good as the next one

* **Plan**  
I really want a five star system but this may add too much complexity to my overall code .... I will give it a try though so do not panic but worse case scenario, 
I'll add some sort of one to five rating either by radios or by a simple inputting of a number. This will get added to the vinyl database along with any other information you've added or edited. You know sometimes you could be in that 5 star mode where you want all the tunes to be banging or maybe you want to hear some of the more messed
up tuneage that you bought by lowering your standards and selecting the one star-ers. The more I talk about this project the more I wish I could add the songs as well and play them on your device ... but I'm oldskool and so is vinyl, fortunately !!!
Anyway, the main point is that some of my vinyl tunes are so beautiful, so euphoric and bring back so many good memories to me that it would bring a tear to a glass eye.
On the other hand though .... I have some vinyl tunes that the devil himself would call sadistically sh!t to be quite honest.


* **Implementation**  
Honesty alert ! I just didn't have the time to implement this so I'll have to add this to the *features to be implemented* section up above. I really wanted this as it would be a cool feature but again this may be more from a DJ perspective again. As a DJ you want to play all the 5 star tunes and if ever a 1 star slipped into that set then the dancefloor would come crashing down round them .... and we wouldn't want that. Anyways, sorry but that's one that will have to be looked at in the future.

* **Test**  
Nothing to test at present

* **Result**  
No results at present

* **Verdict**  
You learn that while you spend more time trying to get some other piece of code right ... others may not happen !


### You are here -->o

#### User Story : I want the website to be easy to use

* **Plan**  
I want the user to be able to move from page to page with ease. I want an easy to use database system that is understandable just from the layout.
I am going to use the framework Bulma for assisting with my layout and css. I have used Bootstrap in my first two projects so under direction from my legendary mentor, I will be utilising The Bulma Framework. 
It looks pretty awesome and will deffo have it's challenges, as did Bootstrap to be fair but I'm here to learn and become a better coder every day :)
I have so many great ideas but I deffo lack knowledge and lack time unfortunately ..... I do know this will get better over time, with constant developing and total commitment.
I want the website to work on all devices which I believe Bulma will be a great help with. I want the user to be able to freely navigate to where ever they want but within the confines of **My Vinyl Answer**, of course !


* **Implementation**  
As I have mentioned before that as I progressed through this project I believe I got a little better at python, flask, jinja and bulma so as you see in the admin section I deffo utilise the Bulma framework for this. Navigation is pretty simple and I utilise the Bulma Logo Navbar for my pages. I designed the logo in Paint and Paint 3D, using the Bubble font I got for my MS2 project. I added a vinyl image and there ye go ... a wee logo ! I invert the colour in my CSS as the logo is black and I wanted my navbar to be black eventually. I think it works quite well as a white (black inverted) logo on a black navbar. 
From the navbar the non-signed-in user has a selection of *home*, *about*, *signup* or *login* to navigate to. Although, *home* is their original starting point anyway. Once logged in the user has the options of *profile*, *my vinyl*, *add vinyl* and *logout* which the navigation to and what they do, is pretty much self explanatory.
The admin user only has the *manage site* and *logout* options as I felt this is all they need as an admin. Within here they can navigate to various sections as regards the structure of the whole database and do various admin kinda things. I added some small back buttons to make the admin section navigation a little easier so they wouldn't have to always go back to the main manage site page everytime. 
Overall I think the navigation works well.  
I have now added better back buttons and added the various collection names to the admin navbar for easier navigation.
Overall I think the navigation works weller ha ha, better for sure. 

* **Test**  
 Between my test users and myself, we have tested the navigation, the sign ups, the log ins, the forms, the searching, and most importantly the CRUD functionality. Everything worked really well and as planned. All links worked as they should and all pages displayed the correct information that was requested. Obviously, it's fairly basic but it deffo has the basis to build apon for the future.

* **Result**  
Everything worked accordingly and not issues or bugs whatsoever. Very happy with the feedback from the users and they were all very happy with overall feel of My Vinyl Answer.

* **Verdict**
I'm very happy again .... I'm like a wee Chesire Cat sitting here typing my results and user feedback up. Nearly there though so fingers crossed you like it too.


### Describe Me In Five Words

#### User Story : I want to possibly add a description or some specific notes attached to each vinyl, if required

* **Plan**  
I want the user to be able to add a small description about each specific vinyl. Whether that's a few words about a song on it or the condition of the vinyl itself.
For example, this is an Ibiza style trance tune or this is happy hardcore at it's finest, and it's always good to know if there is a small scratch, some warping 
or possibly some sleeve damage too. This will also be useful information if you are ever looking to sell a vinyl on Discogs (Disclaimer - other vinyl sales websites are available) and you will probably have the main information already in My Vinyl Answer. Although selling vinyl should be made a criminal offence to be fair .... but that would mean I wouldn't have been able to buy any .... which would mean I have lost my passion !!! Okay scrap that, I meant to say selling vinyl should be a crime .... unless you are selling to me, ha ha, much better :)


* **Implementation**  
This was quite simple to be honest. I just added a textarea input to the add vinyl form so the user could add anythng they wanted within this description.
This description will then be stored in the vinyls document along with all the other form data for future referencing by the user or admin.
Nothing really else much more to say on this one to be fair.

* **Test**  
All users and myself like this added feature. It allows the user to add a few things about the vinyl itself and not just as regards the tune. They all said it would be useful if they were going to sell it to have the details readily available. 

* **Result**  
Simple text area for adding some descriptive infomation about the vinyl. All worked really well and most users wrote pleasantries with in this description box, during testing.

* **Verdict**
All in all, a simple user story with a happy ending ... like in a fairy tale or a romatic comedy ... and let's be honest, who doesn't love a Happy Ending ???


### You Spent Our Life Savings On A Vinyl Job Lot

#### User Story : I want to be able to add as many vinyls as I want

* **Plan**  
I want the user to be able to add as much vinyl as they want and with total ease.
The user will be able select this option from the navbar once they have logged in or registered.
I will entail a simple form with the required inputs for the user to fill out.
They can then submit the new vinyl information for storing in their personal accessible database. I will then flash up a notification to say that they have been successful
with their vinyl collection incrementation and redirect back them to their **My Vinyl** page .... simples !

* **Implementation**  
It basically does what it says on the tin so to speak. The user has the option from the navbar to select **add vinyl** once this is selected, the add vinyl page is opened where the add a vinyl form is located. The user fills the form out meeting the validation criteria set by me such as minimum characters. I added the scrolling year just to make it easier for the user to input this. The information required is the basic info of a vinyl. 
Once the user hits the add thy vinyl button (submit) the ```add_vinyl()``` function is initiated and within this function, the added form data is collected into a dictionary called vinyl. This dictionary is then inserted as a new document within my vinyls collection in the database. Pop goes my wee flash message and the user is returned to their vinyl page with the new addition to the family on full view .... awwwww, it's a beautifull baby Techno !
I could maybe have made the overall design of the form a little smaller so that it would fit on a large screen without scrolling but that's just a minor detail, overall I still think it's cool and this is the *CREATE* functionality for the user.

* **Test**  
Once the users were logged in or signed up. They had access to **Add Vinyl** where they could fill in the required form to add their own vinyl to build up their collection. They did this with ease. Obviously, my users / testers were predominantly work colleagues who don't generally carry around a bag of vinyl, in the off chance some wee dude from Northern Ireland needs some specific vinyl details added as part of a Python project he has developed for vinyl freaks like him.
Anyway, my users made up some cool names, yet some explicit vinyl names and added them through their user environment. The users were then able to see the added vinyl within their vinyl collection, and again do whatever they want with them, from a CRUD perspective of course. They repeated this a few times and everytime the new vinyl was added with ease.

* **Result**  
All vinyl that was tried was added with no issues. A flash message appears to let the user know that the vinyl has been added to their collection. The user can repeat this task over and over again to build up their vinyl collection.

* **Verdict**
Again, super happy with the results and the user feedback. Everyones vinyl got added and they performed CRUD functions on them with ease. Powerful stuff I say ... powerful stuff !


### The Vinyl Edit Before It Goes To Press

#### User Story : I want to edit any vinyl info if I want

* **Plan**  
I want the user to be able to edit any vinyl information on any individual vinyl document in the database. They will be able to access the **Edit Vinyl** page from the 
**My Vinyl** page by clicking the edit button hidden within each of the vinyls collapsibles. Once on the Edit Vinyl page the user will have access to a pre-loaded form with the current vinyl information already filled in. The user can then edit whatever section they want and when they are happy, they can submit again to the database the edited vinyl info. Once this is complete I will redirect them back to their **My Vinyl** page again where they can check on their current updated vinyl. I'm just thinking that if the user has a large collection and they edit after scrolling down through a lot of them, if they decide to edit at this point, will a redirection send the user back to the top of the list??? I'll have to think about this one and test to see what happens :)

* **Implementation**  
Very similar to the add vinyl function mentioned above. Although, the add vinyl has it's own wee slot in the navbar the edit button is hidden behind each collapsible. The user has to click onto the tune they want to edit or delete. When they select the edit button, the ```edit_vinyl()``` function is activated and the selected vinyl id is passed to it. On the first instance the function finds the genres, the session user and the vinyl data. It then passes these to the edit vinyl page which populates the form for the user to edit. I utilised the add vinyl form as they are basically exactly the same. After the user has finished editing their vinyl they will then submit the form by pressing the *Edit Vinyl* button. This calls the ```edit_vinyl()``` function again but this time we are **POSTING** the form data for updating within the database. The obligatory flash message makes another appearance and the user is redirected to the edit vinyl page again. They can hit cancel to go back to their vinyl collection and see the changes that were made.  
I added some admin changes so that if you are admin you get redirected to a card that displays all the vinyl information and from here you can move onto edit or delete the vinyl. I had to do this as I was using the Bulma panel format and wanted to keep it this shape instead of adding two buttons to it, I created the vinyl card for pop upping and offering the required options.... clever I know ! 
I did encounter an annoying bug with this one tbh and it was the fact as admin the *owner* field kept getting wrote over as *admin* if I was logged in as admin and *none* if I left it out, but I talk about this in the bugs section.
Again, I am happy with overall edit vinyl functionality and this is the *UPDATE* functionality for the user therefore covered.

* **Test**  
Very similar to the add function above and the delete function below. Once the users add some vinyl then they tested the edit vinyl functionality. They all loved the fact the edit and delete buttons were hidden within the collapsible, they said it was cool (Sounds like I work with a bunch of hippies ha ha). All worked well and they could edit any field they wanted. Once they went back to their vinyl collection, they could see their vinyl with it's updated information. All worked well with no issues. I just had the admin issue with overwritting the vinyl owner value with admin but I rectified this and I tell all in a new explosive section within BUGS, called **I Vaunt All Zee Vinyl** ... bet you the excitement is killing you my little project marker person :) You know, these crap jokes are mostly for your benefit and maybe offer you a README a little different from the norm so you can smile and have a laugh whilst thinking what a coding genius I am .... plus thinking about me thinking about you as I write my future jokes for ye !!! 
   
* **Result**  
All tests passed and any vinyl tried and edited, the changes were made with no issues. All users were happy with the method and the functionality. The usual wee flash message for good measure. Admin vinyl edit functionality works super well as welly well .... so well, I'm welling up !

* **Verdict**
All worked really well and I am very happy with the user feedback.


### Deletion Will Be My Vinyl Option

#### User Story : I want to delete any vinyl I want (if I sell one personally or on another site)

* **Plan**  
I want the user to be able to delete any vinyl that they want. 
Why would they do that, you may ask? Well maybe they have grew up, unlike me, and they want to have babies, settle down and live a vinyl free life !
Life can be cruel so they will have to sell their vinyl collection .... could be a slow and painful sale were they slip from your grasp in ones and twos ... or it could be a highest bid f'ing wins the f'ing lot :(
Anyhow enough gibber jabber fool, there will therefore be a button of the deletion family required. This delete button will be also hidden within each of the vinyls collapsibles beside the edit button above. Once the user clicks the delete button, I will add some defensive programming to make sure this is what the user wants to do.
This will hopefully eliminate the chance of deleting a vinyl by accident or mistake. Again once the user has completed their vinyl deletion, I will redirect them back to their **My Vinyl** page where their deleted vinyl has been removed and also removed from the database.

* **Implementation**  
Very similar to the above and the above above ha ha. Just like the edit button the delete button is hidden behind the vinyl collapsible. When the user clicks on the the vinyl, it opens up displaying the vinyl info and the two buttons. When the user selects the delete button, the ```confirm_modal()``` function is called for which opens up a confirmation modal which double checks the user want to delete that specific vinyl. I passed the user and the vinyl to the modal so that I could ask the user personally and emphasize the vinyl name to them as well before the continue on with the deletion. The user can cancel at this point were they will be be redirected back to their vinyl collection through the ```my_vinyls()``` function. If the user continues on and presses the delete button in the confirmation modal then the ```delete_vinyl()``` function kicks in. The vinyl id is passed into the function for some unadulterated and never to be seen again deletion. The vinyl document is removed from the database and wee flashy mcflash magically appears again. Just so you know, I added the wee close down x in the corner as you can probably tell the flashes were getting on my nerves with testing and testing bits of code over again and again and again. So that needed to have an option to close down ha ha !
Once deleted the user gets directed to the their vinyl collection again or if admin, they get directed to their vinyl list and therefore the admin all vinyl collection.
Again, I am happy with overall delete vinyl functionality and this is the *DELETE* functionality for the user therefore covered.

* **Test**  
Similar to the add and edit functions mentioned above. The users deleted numerous vinyls as did I. They loved the fact it was hidden along with the edit button. They also loved the dark screen thingy as they called it or a **modal** as we know it, that made sure the were making the correct life choice before deleting their vinyl. Once the user crossed that line their vinyl gets removed from the collection and never to be seen again .... unless that specific user re-enters that exact same information again ... then I suppose you can say it's the same so therefore technically it can be seen again .... sorry, well until that happens it's never to be seen again.

* **Result**  
All users tested this functionality and it worked very well. The admin deletion worked perfectly too. And if I wasn't sure about performing the deletion in the first place with the confirmation modal, the user gets a flash message to confirm that the deletion did in fact take place. All corners covered by this boy ... as I rave to cheesy euro pop and type this work of art up, moi README :)

* **Verdict**
Deletion functionality worked for all users and all admin tests. Very happy with this and the CRUD functionality overall. 



### **Validation Checks**

All my html passed all the checks at [W3C HTML Validation Service](https://validator.w3.org/). The only issue being that I had used an ID twice on my user vinyl page when grouping and centering the two sets of buttons. I just changed these to classes so both will work with no issues. Apart from that, it was all jinja logic errors and the fact most of my html didn't have any header information.
All my CSS passed all checks at [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) with no errors what so ever.


### **User Questionnaire And Overall Feedback**

Over the previous two projects, I've seen the necessity for user feedback and user testing. In the first project I was really shy if the truth be told so I didn't really show my project off or let people see it. This also affected my final score which I didn't realise was a major attributory to a decent score. With my last project, the JS one, I annoyed people with testing it as I wanted to the get it right. The user feedback from that was awesome and very encouraging so I set out to get the same people, work colleagues, friends and family, to test my new project. I made a questionnaire of general questions, for them to fill out as they navigate around the site. I let a few of them try the admin access as I needed some testing and verification of that code too. The questionnaire can be found below:

[User / Admin Questionnaire](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/user_questionnaire.pdf)

The overall user / admin feedback from the questionnaire was very encouraging too.... 
And don't be thinking as they fill in the blanks, I'm standing behind them with a large hunting knife whispering into their ear "I know where you live ... princess" so I get better results .... I wanted them to dig deep, try things, mess around and see if they could find anything wrong.
This is how you progress and if you cannot take critique then you're in the wrong business .... sounds like a famous line from a Hollywood movie !
Anyways, the main points were as follows:

- The site looks really awesome and the deck backdrop was cool 
- The colours fit in well with the image
- The navigation was smooth and very easy to follow
- All links worked with no issues 
- Flash messages were in abundance ha ha
- Validation & requirements were all working good
- User CRUD functions working with no issues
- Admin CRUD functions working with no issues
- Everything looked good on mobile too

All in all, I am very happy with the user feedback and apart from the general lad banter, everyone though it was an amazing wee app that worked very well.
Although they did say it wasn't as good as my MS2 project, my wee game, because there was no legendary status with my MS3 project ha ha.
Overall, I am extremely happy with the results and all the feedback within my questionnaires.


[Back to Top](#contents)


## **Bugs**
---

### **Blue In The Face**

* **Bug**
Simple one to start off with ....
Couldn't get dropdown border colour to change to my-blue which did my head in tbh . I tried everything but couldn't get it to work ......
until I remembered something !important (pun intended) ..... this solved my issue as the 'select' class was overruling all my tries !!!

* **Fix**
I remembered the **!important** property so used this to solve it by making all the select borders and input borders my-blue.

* **Verdict**
Easy fix to be fair but all works well now.

### **Modal lay-od-lay-od-lay-he-hoo**

* **Bug**
I tried to add jquery for calling the modal when you clicked on the 'delete button' but it wouldn't work.
It worked when I used say a class = p1 but not an id = p1 .... couldn't figure it out for ages .... did my head absolutely in this one ha ha !
Probably a bit of noob code to be honest as well but sure .... it's the joys of gaining experience.

* **Fix**
I realised, eventually, that I was creating id = p1 numourous times as it was within a for loop so therefore it was pissed off because there should only one 'id' and that's why it wouldn't work .... glad I figured it out tbh :)


* **Verdict** 
In the end I settled for calling a modal function which in turn displays the modal page for the user or admin .... but a bug is a bug and I fixed it so might as well share.

### **Modal lay-od-lay-od-lay-he-hoo Two**

* **Bug**
I couldn't get my modal to delete the correct database document and it would just delete the first one in the collection.
The selected vinyl_id wasn't linking to my delete route app.

* **Fix**
I tried a few things but in the end I moved the modal to it's own page and created a route to it when the delete button is pressed and I pass through the vinyl details using vinyl_id. This is so I can display any vinyl details I want plus pass the vinyl_id into the delete vinyl function. When the delete button in the modal is pressed the vinyl gets deleted.

* **Verdict** 
I think this works really well now and by passing in the user also I could confirm with them on a personal level if they really wanted to delete that specific vinyl.

### **Jinja Ninja Not So Logic**

* **Bug**
Spent ages trying to figure out why my users document values would not display on my profile page as per user
I was using jinja logic to display them so should have been simples ... right !

* **Fix**
Well, butt munch here forgot to write the database name with the proper jinja logic value. I was using {{ fullname }} when it should have been {{ users.fullname }}

* **Verdict**
Pretty raging after that tbh but sure .... another learning point noted & will be easier to notice next time !

### **Email Wasn't Playing Ball**

* **Bug**
Another simple one ....
Email validation wasn't working

* **Fix**
I had type="text" instead of type="email"

* **Verdict**
Easy solution

### **Image Not Rights**

* **Bug**
Tried various ways and pieces of code to try get my image centered eveningly in the profile section. I know there is probably a simple solution but I settled on my wee fix.

* **Fix**
I tried putting the image in the middle of 3 columns and making the outer columns set to auto so that the middle column and therefore the image would stay in the middle of the device. It worked so I am happy and that's all that matters ha ha and all users too obviously ... I'm not that selfish ! 

* **Verdict**
This wee fix worked well and solved my bug so life is better for now .... woah stay away from the dark side RaVeR76 !

### **It's Not The Image's Default**

* **Bug**
After a mentor sesh he said it would be good to have a default image in case the users url didn't load. Well I tried various pieces of code and couldn't get anything to work on a user I had made up but didn't have a profile pic url loaded. I tried for ages then after some glorous investigative work figured out he didn't have a profile_pic field in his document which didn't help because I had him made up before I decided to add a profile pic input, to add some flavour to their Envinylonment (if I keep saying it maybe it'll catch on ha ha).

* **Fix**
Once I added this manually to the database the code I had be trying started to work ..... happy yet angry happy yet angry !!! Anyways, I tried another url based image as back-up but while it maybe worked the first time, it was maybe missing on a reload and then back into vision on another reload. Not sure why this was happening to be honest but I didn't want to take any chances so I got a smiley face from my MS1. I edited the Smiley Face image in Paint3D by removing some writing and I also removed the background. I added this to my images folder and using the code ```<img src="image.png" onError="this.onerror=null;this.src='/images/noimage.gif';" />``` I added my jinja link and my default Smiley Face ..... Loads everytime ye boy ye (P.S. please don't come back saying it didn't work for you ..... just lie to me and say *worked dead on RaVeR76 !*)

* **Verdict**
Hopefully it works either way, I really want the user to have their own image but at least if it doesn't work they have a happy smiley face. I think it all depends on you copy the link from the image. Google tells you to share then copy link but this doesn't work for me. If I right click and copy image address and paste that then this works everytime for me.

### **Nobody Likes A Faker**

* **Bug**
I honestly don't know why this keeps happening because with my MS2 a similar UFO (Unidentified Fecking Oversight) happened during my mentor session. 
Last night he showed me his ... screen and my wee project was displaying proudly but I could see two vinyls being displayed. I was like how come there are two vinyls being displayed when you have't even logged in .... mind blown again. With my MS2 his cards would show the actually card underneath before he even turned it whereas on my PC is was perfect. It was a Google vs Safari issue which I couldn't resolve and I thought this was another compatability issue.

* **Fix**
Anyway, Detective RaVeR76 was on the case and after some clever analysing, snooping around, interogating, I found that the culprit was none other than me .... RaVeR76 ! I hadn't added any *Owner* field to their individual collection document within Mongodb so my code I wrote for vinyl only to be displayed by the user would not work. Owner is a hidden field (not for display) that I use to do this and gets added when a new vinyl is added to their collection. Within the jinja for loop, I check that the current user ```session.user``` is the same as the owner ```vinyl.owner``` for each vinyl and if they are, their vinyl's will be displayed on screen.

* **Verdict**
My fix works perfect as I have tried loads of fake users to make sure my code is working. I've that many passwords in my head it's about to explode, should've just used the same one over and over again for test purposes. All fake users display their own vinyl so everything works well. 

### **Vinyls M.I.A.**

* **Bug**
I was refactoring all my code so I was doing it very slowly and in small parts so I didn't create a major headache on a Saturday night.
So when I refactored a part say the modal I would test everything linked to that modal and in fact I would just go through the whole website to make sure it all worked.
Anyway I was testing the edit and delete functions from the vinyls page. I noticed that when I made an edit and clicked the edit button it stayed on the edit vinyl page which is correct but when I went back to the my_vinyl page .... the wee vinyl had did a Hoodini and disappeared ! I was like WTF !
I added more vinyl and kept trying it but yip ... same thing again. I followed the paths between everything and couldn't see anything that was out of place. 

* **Fix**
I did a bit more investigating and went to my Mongodb collections and low n behold, there was all the vinyl that I had been adding. They had passed through the My Vinyl Anwser Bermuda Triangle or something mad-doggy like that.
Only messing, what was happening was that when I created the add_vinyl function, I had added an ```owner``` field to utilise it when displaying the users own vinyl collection. So when the user edited the vinyl they were only editing the original fields, as I had not added ```owner``` to the edit_vinyl function .... D'OH !!!!
To be honest it wasn't really deleting, as you know, it was just deleting the ```owner``` field and when it reloaded the users **My Vinyl** page again, the edited vinyl was just not loaded from the database as it only displays the users *aka owners* vinyl.
So I simply rectified this by adding ```"owner": session["user"]``` to the ```vinyl_edit``` list before updating the database document in MongoDb.

* **Verdict**
The edit function worked perfectly after this error was solved :)

### **Hungry? Have A NavBar !**

* **Bug**
I refactored everything as mentioned above, so I only had the navbar and base to refactor. I did the navbar but had some sizing issues afterwards.
When the navbar was in the base it was covering the whole top part of the page but when I moved it to the components folder and used *Jinja Logic* to link it, it was only covering a smaller section at the top.

* **Fix**
I found that because I had added it to each page in the pages folder using *Jinja Logic* it then became an extension of the base and this extension is sanwiched in it's own container in the base html. Therefore the navbar was a navbar for the container. I therefore removed the main div with container class from the base.html and also the header section. This solved the navbar issue but the rest of the content was wider on each page ha ha .... it never rains but it pours as they say !
Solution for this bug within a bug was to enclose each page in the pages folder within a div with a container class, which I did and everything looks cool again :)

* **Verdict**
All looks good and the navigation bar looks perfect.

### **URL Avin A Laff**

* **Bug**
Profile Issue Again - Didn't realise you could use a ```type="URL"``` for extra validation as I was worried about users just typing jibber jabber fool.
I had tried javascript methods, I was thinking am I going to have to write logic to cover every eventuallity of what the user may or may not type .... this is going to take ages.

* **Fix**
After a little bit of reaearch that wee ```type="URL"``` saved the day. 
It works a treat along with the *required* attribute so the user has to type a valid url before submitting their signup form.
If it doesn't work then it goes to the default pic .... a big raver smiley face :)

* **Verdict**
Very happy with the solution and the results.

### **Moving Folder**

* **Bug**
Off the back of this validation adjustment above, I found another bug that had raised it's ugly wee head, my default pic would not display no matter what.
At first I thought it had some connection with the URL validation so I checked it all, I deleted it also just to see as well but still no Smiley Face. I was beginning to crack up to be honest but I kept going. I checked the database to see if anything was untoward in there but everything looked okay.

* **Fix**
I found the bug by copying my Smiley Face src link and pasting it in over the Jinja expression just to see if it displayed when first called but NO ... it did not either ! What was happening you may ask cause I did too ... well when I was doing my Refacrtoring thing I had moved my profile page into a new pages folder so therefore my default link didn't work no more. I just needed to add a wee ```/``` at the start of the link which solved the problem and everyone who's profile pic url does not work will get a Big Smiley Face instead :)

* **Verdict**
Happy with the solution and it was simple anyway just a silly mistake.

### **Pop A Cap In Your Lock**

* **Bug**
I tried to log in and I couldn't. I tried using my various test login details but none would work. This was just after I had did some button styling so I was like there should be no connection here. It did my head in for about an hour trying to figure it out. I investigated anyway and eventually found the reason.... I had **CAPS LOCK ON !** How annoying yet secretly deceptive, in that I wouldn't have realised that and didn't realise that, hence me delving into my code to find the reason.

* **Fix**
Added some detection for passwords as the user cannot see any input values. I found some cool yet simple code for this in W3Schools and link is in the credit section below.
I also used the Bulma classes of help and is-danger for colour, I removed the red from the W3School example as it overide it.

* **Verdict**
I think it works well and will stop other users from being caught out like me, RaVeR76, the developer himself ha ha !

### **Caps Lock Caps Collapsibles From Collapsing**

* **Bug**
After I added the Caps Lock On code my collapsibles for the users vinyl wouldn't work, it worked when I swapped the position of the JS functions around for them within the js file.

* **Fix**
I tried various test to figure out why it was doing this but I was spending too much time when I had a solution but I'll try come back to it and figure it out.
Think it's to do with the display class but not sure. It was a head melter for sure.

* **Verdict**
Spent too much time on it so just used the solution above which works.

### **Conflicting Functions**

* **Bug**
Dropdown issues -it was the new keyboard it was a complete scud I swear .... I couldn't get my JS to work with two functions, they were conflicting with each other for some reason and I'd spent about 6 hours on the two feckers. It was my Caps Lock On function and my dropdown selector function so I'll blank the Caps On out for a while cause I need to move on.

* **Fix**
I decided to remove the password caps lock script from my main js file and place it on each of the login and signup pages. This solved the problem although I am reluctant to put any script on any of my pages, I have no alternative at the minute as I want both functions to work :)

* **Verdict**
Fix works well and both functions are functioning lol.

### **Super Duper Admin CRUD Box**

* **Bug**
The keyboard is deffo a scud ha ha ..... just spent at least four hard spent evenings probably about 25 hours or so trying to get my all singing all dancing Admin CRUD box working and in the end I've had to give up. I couldn't get the certain functions working together and my JS was playing up again. Really guttted on this one to be honest because I put so much effort in and I couldn't get it right. Suppose it's another hard lesson to take but maybe if I had more time I would've got there in the end. If I have time at the end I will give it another go. But for now I have to move on and get my Admin CRUD simplified :(

* **Fix**
I made a simple manage site page where the admin can navigate to the various collections within the My Vinyl Answer database.
Within each collection the admin can carry out various CRUD functions and various searches. The vinyl panel probably could have been utilised across all collections but I tried using this for my super duper CRUD box and failed so I made a simplier approach for the Genre and User management. I tried the panel again for the vinyl collection only and figured it out. I think it works well but by this time it was too late to go back and change out the other two for panels plus they worked welll anyway withe there individual cards on display.

* **Verdict**
The more I used the Bulma framework the better I got as you can see this within Admin section, the last section I did. The bug is really hard to explain because it was one of them that I just lost control with so had to delete loads of test code etc and get back to were I was before I went into one. I think all admin sections look fine and maybe the all in one admin page will come with an update at a later time.


### **I Vaunt All Zee Vinyl**

* **Bug**
Admin issues when editing a vinyl because it changed the vinyl owner name to admin everytime. I knew why it was doing it but just couldn't find a solution quick enough.

* **Fix**
This simple piece of code ```owner = vinyl.get('owner')``` saved the day. I spent hours on this one as well .... unbelieveable I swear. Once you fix one wee bug another one pops it's ugly head up. I wanted to utilize the edit_vinyl as both admin and a user but the owner key was causing me major headaches as the value was becoming admin then null and I couldn't figure it out for ages but then I found that piece of code, it worked.
Only now when the page returned the flash message had the new name but the page didn't change. I got stuck on this one too. I couldn't figure out how to redirect to function in my app.py and pass an _id too. I had to settle for finding the vinyl & rendering the template again. Sorry if it was not the logical method but I'm still learning and my head is fried at the minute lol !

* **Verdict**
Everything works well now, with a simple solution that took ages to **get** .... pun intended as always my dear :)

### **If Your Name's Not Admin ... You're Not Coming In !**

* **Bug**
I wanted a set up where the user has access to the main pages and admin have access to the manage site pages only. I thought this would be a wee easy one to find and solve but hey ... is coding simple .... not for a noob like me unfortunately. I tried searching through the depths of the internet for such code but that's after I was offered someone's kidney, three pythons and a WW2 Russian Tank .... the web can be so so dark sometimes !
I got there yay me ! All I wanted to do was show certain navbar links to the user and admin just the admin section and then the non loggy in pages when you first arrive :)

* **Fix**
I messed about which the jinja logic on my navigation code but struggled to get it right .... quite a few hours yet again but look ... I have to learn and as painful as it was I got there and it works for me. I had to duplicate the login line of code for admin and a user which may not be the correct way but it works and I need to move on. I just need to redirect my admin to a different page as it still shows their Profile page on first log in :)
One major fact if we are putting honesty on the table that I had my else statement as {else} and not {% else %} which 100% did not help the situation and totally threw me a curve ball but it's done and working the way I want it to !
Now to fix the admin post login link so it's naw Profile 

* **Verdict**
Everything working the way it should and admin now lands on the manage_site page after login login.

### **I *get* It Now**

* **Bug**
Very similar to a wee bug above about the vinyl owner but this time, the users password was disappearing after admin had edited the user.

* **Fix**
I used similar logic to solve another bug mentioned earlier, ```password = users.get('password')``` and then add this *password* to the new dictionary *user_edit*. 

* **Verdict**
The admin can edit the user details apart from their password which now stays the same after the edits are updated.


### **Master Py Thong**

* **Bug**
It was annoying me that whenever a user was logged in and they closed the page down. If they opened that page again they would still be logged in as that user, which let's face facts would not be a great piece of code for, let's say James Bond to get all his missions through. Let's play out a wee scene here .... The Evil Genius says "Well Mr. Bond, I've been expecting yeou" ! James Bond replies "But this is impossible .... how did you know about this top secret mission to capture you ... Master Py Thong". Master Py replies "Well you see Mr. Bond ... you only closed down your super secret webpage but not your browser so I still got your little cookies fool .... mwah ... mwah ... mwah ! 
You get the gist of it anyway.

* **Fix**
I added ```session.clear()``` to the home page function so everytime the website is connection to, it clears the session cookies and therefore displays the home page and start navbar. Before it was the main homepage but with the user logged in navbar.

* **Verdict**
I have tested this through Heroku as well so it all looks good. 


[Back to Top](#contents)

## **Deployment**
---
### Local Deployment
For my project **My Vinyl Answer**, I used Github to create a repository with the Code Institute template as my base, and from here I used [Gitpod](https://www.gitpod.io/) to write all my code. Periodically I would commit my work to git and generally at the same time I would *git push* my code to Github.
I've deployed this project to Heroku for a wee change and set up automatic deployment so when I push to Github, I also push to Heroku.

To clone this project:

1. From the application's repository, click the "code" button and download the zip of the repository.
    Alternatively, you can clone the repository using the following line in your terminal:

    ``` 
    git clone https://github.com/RaVeR76/My-Vinyl-Answer.git
    ``` 
1. Access the folder in your terminal window and install the applications requirements using the following command:

    ```
    pip3 install -r requirements.txt
    ```

1. Sign-in or sign-up to [MongoDB](https://www.mongodb.com/) and create a new cluster
    * Within the Sandbox, click the collections button and after click Create Database (Add My Own Data), I called mine **myVinylAnswer**
    * Set up the following collections: users, genre, vinyl
    * Under the Security Menu on the left, select Database Access.
    * Add a new database user, and keep the credentials secure
    * Within the Network Access option, add IP Address 0.0.0.0

1. In Gitpod or your IDE, create a file containing your environmental variables called env.py at the root level of the application. 
    It will need to contain the following lines and variables:
    ```
    import os

    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")
    os.environ.setdefault("MONGO_URI", "YOUR_MONGODB_URI")
    os.environ.setdefault("MONGO_DBNAME", "DATABASE_NAME")
    os.environ.setdefault("DEBUG", "True")
    ```

    Please note that you will need to update the **SECRET_KEY** with your own secret key, as well as the **MONGO_URI** and **MONGO_DBNAME** variables with those provided by MongoDB.
    To find your MONGO_URI, go to your clusters and click on connect. Choose connect your application and copy the link provided. 
    Don't forget to update the necessary fields like password and database name. 

    If you plan on pushing this application to a public repository, ensure that *env.py* is added to your *.gitignore* file.

1. The application can now be run locally. In your terminal, type the following command 
    ```
    python3 app.py. 
    ```

### To deploy your project on Heroku, use the following steps: 

1. Log in to your Heroku account and create a new app. Choose your region. 
1. Ensure the Procfile and requirements.txt files exist are present and up-to-date in your local repository.  
    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```
1. The Procfile should contain the following line:
    ```
    web: python app.py
    ```

1. Scroll down to the "deployment method" section. Choose "Github" for automatic deployment.
1. From the inputs below, make sure your github user is selected, and then enter the name for your repository. Click "search". When it finds the repo, click the "connect" button.
1. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your env.py (IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME):
    !You shouldn't set the DEBUG variable in under config vars, only in your env.py to prevent DEBUG being active on live website. 

    ```
    IP = 0.0.0.0
    PORT = 5000
    SECRET_KEY = YOUR_SECRET_KEY
    MONGO_URI = YOUR_MONGODB_URI
    MONGO_DBNAME = DATABASE_NAME
    ```

1. Scroll back up and click "Deploy". Scroll down and click "Enable automatic deployment".
1. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
1. In order to commit your changes to the branch, use git push to push your changes.



## **Conclusion**
---

I know I called this My Vinyl Answer so it's therefore mainly about vinyl and stacks of it ha ha, but this could have been further developed so the
user could make up their own personl database for whatever collection they wanted. Obviously, there would be limits put in place so they don't abuse the database ...
nobody likes a db abuser !  
Overall I found python not to bad and really enjoyed it. Don't get me wrong there were times when I thought why won't you work you piece of chip ! It should have panned out differently and there were a few times when I got swallowed up in changes and lost my way. I just needed to take a step back and trace the code through which I learned through time. To be honest, some of the harder python was easiest to conquer and I was like who's the daddy but then again some the easier python twisted my napper and it was like an uppercut from Drago in Rocky 4.  
I know the overall layout could improve and maybe it will in *Version 2* ha ha but I am happy with what I have achieved in the allocated time plus having to learn Python too.
Maybe I should have used all Bulma components which I have for 95% of it but just the user vinyl collection I left the way it is as I love the look and feel of it. 
All in all, there could be a few upgrades in the future but I am super happy with the overall outcome of this project.  
I hope you like it too !

## **Credits**
---

**Code Credits**

* [Collapsible taken from W3SChools](https://www.w3schools.com/howto/howto_js_collapsible.asp)

* [JavaScript for a Bulma select dropdown taken from here](https://github.com/jgthms/bulma/issues/1870)

* [Release year selection code](https://stackoverflow.com/questions/34676752/can-i-use-an-html-input-type-date-to-collect-only-a-year/40662109)

* [Remove autofill from Add Vinyl as turned background blue](https://stackoverflow.com/questions/2338102/override-browser-form-filling-and-input-highlighting-with-html-css)

* [Align edit button within my column](https://stackoverflow.com/questions/7560832/how-to-center-a-button-within-a-div)

* [Delete confirmation modal](https://www.w3schools.com/howto/howto_css_delete_modal.asp)

* [Caps Lock On code taken from W3Schools](https://www.w3schools.com/howto/howto_js_detect_capslock.asp)

* [Got database collection names from this code](https://stackoverflow.com/questions/9805451/how-to-find-names-of-all-collections-using-pymongo)

* [Code for scroll on Admin Vinyl](https://stackoverflow.com/questions/21998679/css-how-to-make-scrollable-list)

* [Added back button code from W3Schools](https://www.w3schools.com/jsref/met_his_back.asp)

* [Background for home page logo taken from here](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_blurred_bg)

* [Code for default image fix taken from here](https://stackoverflow.com/questions/92720/jquery-javascript-to-replace-broken-images?page=1&tab=votes#tab-top)

* [Code for url bug solution](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/url)

* [Bouncing ball code used for my About smiley](https://codeburst.io/tutorial-make-a-bouncing-ball-entirely-with-css-1e7e3c853a50)

* [Favicon Vinyl Image](https://www.pngfind.com/mpng/mRhxxh_vinyl-record-clip-art-hd-png-download/)

* [Debugging Help](https://code-institute-room.slack.com/archives/C7JQY2RHC/p1618992182397900?thread_ts=1618985984.386500&cid=C7JQY2RHC)

**Image Credits**

* Deck Pic -  Photo by James Sutton on Unsplash 

* Vinyl On Floor Pic - Photo by Eric Krull on Unsplash

**Special Shout Outs**

* Firstly to my testers - my family, my work colleagues and Wee Ro .... with the main ones being Scott, Storm & Wee CJ

* My **'patient'** mentor [Simen Daehlin](https://github.com/Eventyret), for helping me develop my coding skills by giving awesome advice and direction :)

* [AnoukSmet](https://github.com/AnoukSmet), for her awesome README & cool website

* Slack for continuous information, help links, tutorials, laughter, support .... I could go on

* [Stackoverflow](https://stackoverflow.com/), useful resource site for finding solutions to many issues I had

**This site is mainly for educational purposes only but chill out and face the Vinyl Frontier**


[Back to Top](#contents)
