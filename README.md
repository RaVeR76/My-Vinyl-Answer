# **My-Vinyl-Answer**
 
***HERO IMAGE OR WEBSITE DISPLAY IMAGE***
 

## **Project Goals**

I'm a DJ (mainly a Bedroom one though .... see my MS1 project ha ha) & have been DJing for 25 years. I do it because I love the music, I love the people and I love the feeling of making people smile through the freedom of my sets :)
I have hundreds of records, aka Vinyl, which I have been collecting from the mid 90s to now and I am still buying them .... it's like an addiction to be honest !
I've tried to attend V.A. classes (Vinyl Anonymous) but they will never change me so I may just try to keep track of what I am buying and why .....
This is were my idea for a project comes from. I don't know how many records I have, I don't know what genre they are when I look at them, obviously I know some like the classics, but the majority I need to play before I can ascertain what genre they are. The amount of times I have went through my whole record selection to try and get some sort of order and organistaion is completely criminal and so time consuming it's unreal. 
Again, this is were my project comes in ! I want to have a once and for all list of my personal vinyl and as much information per record as possible which I can search and hopefully help my keep track of .... I may even add a random function to help me select some cool SETS to play from the various Genres I have :)


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
* 


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
About half way in to this project whilst I love the colours above I just thought the overall website looked a bit boring and plain. so I jumped on the Google Image train to trans-central and searched for some free vinyl images I could use to revamp this project. I found a few and tried them but then I came across the reddish blueish vinyl on the deck one and I thought that's it there. I placed it as my body background and fell in love. The issue was my wee colours above were close but not close enough. I still use them for borders, buttons and my vinyl collasibles because they still fitted beautifully there but for the headers and titles then didn't. 
So I used an online site called [Image Color Picker](https://imagecolorpicker.com/en) to select some colours from my image .... the red and the blue to be precise and using them with the image as a backdrop works really well throughout website, in my opinion but who's to say I'm right ... eh ! I do and it looks cool as feck .... alright ha ha !
That's the story behind the colour changes but I had to, just to spice a little life into the visual aspect of the site.
P.S. I'm not sure if I am to change the orginal colours out or keep them up as these were my intial thoughts but the Smoky Black is the only O.G. left from the orginal line up.  

[Back to Top](#contents)

## **Wireframes**
---
The software that I used for my wireframes was Balsamiq. This was the third time I used this software & it was deffo a lot easier to understand what you need to do. The software allows you design the basic layout of your website on devices such as a desktop, tablet and mobile. They are just simple 2D sketches but I now understand how important these really are :) 
I think my wireframes look good & deffo give me a great starting point for the design process !

Anyway, you can have a wee look at my wireframes below:

- [Mobile Home Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/mobile-home.pdf)

- [Mobile About Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/mobile-about.pdf)

- [Mobile Login Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/mobile-login.pdf)

- [Mobile Register Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/mobile-register.pdf)

- [Mobile My Vinyl Collection Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/mobile-myvinylcollection.pdf)

- [Tablet Home Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/tablet-home.pdf)

- [Tablet About Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/tablet-about.pdf)

- [Tablet Login Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/tablet-login.pdf)

- [Tablet Register Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/tablet-register.pdf)

- [Tablet My Vinyl Collection Wireframe](https://github.com/RaVeR76/My-Vinyl-Answer/raw/master/wireframes/tablet-myvinylcollection.pdf)

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
* 


### **Features To Be Implemented**

Share list with other users for possible sales or swaps if duplicates
5 star ratings or something


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
- [Bulma](https://bulma.io/)
- [jQuery](https://jquery.com/)
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
I want the user to have the ability to register for My Vinyl Answer so they can log in anytime in the future with ease.
I will create a register form where they will have to input their full name, a username, a email address and a password. 
There will be a Sign Up button available which will POST the data to the database. 
I will add some defensive programming so that usernames will not be duplicated. I will check to see if the new username already exists in the database and if so flash up a an alert but if not then render their profile page. This will be populated with the information they just input and also a welcome message will appear ... obviously I will not be displaying their **password** within their profile or anywhere in fact ha ha !



* **Implementation**  
I created a simple *Sign up* page which has a simple form made from Bulma components. Onve the new user fills these in and hits the button. My ```signup ()``` function
kicks into action and checks if the username exists, if so let the user know by a wee flash message and return them to the signup page.
If the user doesn't exist then I take their filled in data and store it in a dictionary I called *signup* which I then *insert* into the Mongo Database. I also add the username to the session cookies for utilising whilst they are logged in. Let's not forget my wee flash message to welcome them to my website and  then send them to their profile page.
I added an input for a the user to add a url of a pic they can use as a profile pic. It works ,ost of the time if the truth be told but it's not perfect at present. Google images says to share the image and then copy the link this way but i find this down't work. If you find the image then right click and copy image addreess then this works for me. ANyways, I've added like a big smiley raver face as a default image so no one should be left with blank image or broken link.
I added validation to all inputs and added some requirements like min lengths or @ for the email.
Password will be encripted by using hash method through the **werkzeug.security** utlity ..... generate_password_hash for generating and check_passowrd_hash for, well you've guessed it ... checking ha ha ! So basically your wee password is taken and mashed, hashed, bashed up and stored in the database and when you login it becomes unbashed, unhashed and unmashed so that it can be compared with the login password at the login stage. 
That's the basic terms of it anyway .... all this hash talk is making me ***salivate*** to be honest, so let's move on quickly.
I also added some Caps Lock code for super cool effect because if the truth be told, I sat for about an hour one evening trying to figure out why my login wasn't working and it was because i had Caps Lock on. You're thinking but should you not have noticed this at the username part ... well no is the answer because I was always clicking the selection from my input pop down history thingy so was never actually inputting my username. Anyway, that's the truth behind the reason why I have a Caps Lock check on the password entries.
Finally, I had to put the Javascript for Caps Lock function on each password page because when it was in my main js file, it conflicted with the users vinyl collapsible but this was a bug which I'll talk about in the bugs section.

* **Test**  


* **Result**  


* **Verdict** 




### EnVINYLoment Tut Tut

#### User Story : I want to be able to login so I can have my own personal environment or enVINYLoment as I like to call it (sorry that was bad)

* **Plan**  
I want to create a website that is unique to each person and allows them to feel welcome everytime they log on.
The user will first have to sign up with some basic details which will be added to their personal user database.
After this, each user will have a personal username which will be one of a kind, as I will add code to eliminate duplication.
They will have access to their own vinyl collection which they will have to build from scratch themselves obviously, unless I'm
some kinda vinyl stalker who knows what each user has in their record boxes or attics !
I may possibly add some sort of a simple profile pic code that the user can utilise to add a URL link for their profile pic (save db space plus keeps it simple)

In production, you could probably give the user the ability to delete their profile if they wanted to but I will add Admin Access to the website
for the ability to delete users.

* **Implementation**  
Ok so like I said above, the user signs up for the first time then they have access to their personal space moving forward. They can then use the simple login page for future logins. All they need here is their unique username and password. These two pieces of info are then passed to the ```login()``` function which basically checks the login combo against the database. If the user is unknown it will flash a generic error message and redirect to the login page again. If the user is known then it checks the users password using the hash method mentioned previously. If the password is incorrect it will flash the generic message and redirect the user to the login page yet again. 
Now after all them mind challenging tests that if the user gets their username right and the correct password is entered ... they will then be accepted into their own wee world of My Vinyl Answer :) 
Within the realms of My Vinyl ANswer they will first see their profile page then they will have acess to their personal vinyl collection ... obviously once they build it up over time. They will have access to the add vinyl form where they can start to build their collection. Finally a logout option. I know it's pretty basic for the user but it's got the potential to expand and be much better. Time constraints and lack of knowledge at this stage but as the project progresses, I think you'll see it gets better as I utilise Bulma a lot more as in the Admin secton.

* **Test**  


* **Result**  


* **Verdict**  




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
They will be able to edit their vinyl by clicking the edit button which calls the ```edit_vinyl()``` function and passes the vinyl id of the chosen vinyl into it. The funsction then populates the edit_vinyl_form for the user to edit. Once the user makes their changes they can submit the changes back to the ```edit_vinyl()```function which updates the vinyl's document and redirects them to the edit vinyl form again. A cancel will take them back to their vinyl collection where the changes will have been updated too. 
The user has the option to delete a vinyl from their collection too. Once they choose to delete one, the delete onfirmation modal is called for where I double check that they (the user in bold) wants to delete the vinyl (added name of vinyl in bold too). Once the user, selects to confimr delete then ```delete_vinyl()``` function is called for where the vinyl id is passed to. This function then deletes the document asscociated with the passed vinyl id and redirects the user to their vinyl collection again, not forgetting about the wee flash message. Here the user can see that their vinyl has been deleted from the list too. 
I know the user vinyl interface is again pretty basic but this was the first thing i developed and as I got to use Bulma, I realised I could have used a lot more of it's components. Honestly, as basic as it looks, I still love it because I created it from the W3 Schools collapsibles and made it my own. I know it can  be made better but for me it just suits this wee project.

* **Test**  


* **Result**  


* **Verdict**  




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
I stated some sort of search function was required and that the DJ ones were important. I think at the start fo this project I was possibily aiming done the DJ route again but as it developed I thought it would be great for all vinyl enthusists not just DJs.
Moving on, I added a little search bar above the users vinyl collection with a reset button and a search button for submitting the input to the ```vinyl_search()``` function. Wthin here, it searches through the vinyl for the matching criteria and then displays the matching vinyls. I set up a collection index (query) using the vinyl_name, genre_name, vinyl_artist, release_year and owner as these would be the main searching points i felt. So basically, the user can search all their vinyl as long as it matches the required query fields. If not then a **No Results Found** message is displayed. 
The user can also reset the page so that it goes back to there full collection. Again it's pretty basic but as my knowledge gets better so will the search functions.

In Admin access I use a Bulma panel to display all vinyl and I think it looks quite well. You may wonder why not use this format for the user vinyl collection? Like I said before as I got used to Bulma moreso at the admin part plus I loved the original authenticity of the users vinyl collection format too so didn't want to change it at this late stage. For my the users looks more appealing than the admin one to be honest. Anyway, the admin has basically the same display functions and search functions as the user, only I added some panel tabs for quicker search functionality. I created a function for each genre that when selected it displays all vinyl associated with that genre. Don't get me wrong, I know there is probably a simpler method that uses less code to do all five functions in one ... but unfortunately I don't have time on my side at this moment in time so this works for me and I can look at simplifying it at a later date. I'm still super happy I got it working so well, mind you :)

* **Test**  


* **Result**  


* **Verdict**  





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


* **Result**  


* **Verdict**  



### You are here -->o

#### User Story : I want the website to be easy to use

* **Plan**  
I want the user to be able to move from page to page with ease. I want an easy to use database system that is understandable just from the layout.
I am going to use the framework Bulma for assisting with my layout and css. I have used Bootstrap in my first two projects so under direction from my legendary mentor, I will be utilising The Bulma Frameowrk. 
It looks pretty awesome and will deffo have it's challenges, as did Bootstrap to be fair but I'm here to learn and become a better coder every day :)
I have so many great ideas but I deffo lack knowledge and lack time unfortunately ..... I do know this will get better over time, with constant developing and total commitment.
I want the website to work on all devices which I believe Bulma will be a great help with. I want the user to be able to freely navigate to where ever they want but within the confines of **My Vinyl Answer**, of course !


* **Implementation**  
As I have mentioned before that as I progressed through this project I believe I got a little better at python, flask, jinja and bulma so as you see in the admin section I deffo utilise the Bulma framework for this. Navigation is pretty simple and I utilise the Bulma Logo Navbar for my pages. I designed the logo in Paint and Paint 3D, using the Bubble font I got for my MS2 project. I added a vinyl image and there ye go ... a wee logo ! I invert the colour in my CSS as the logo is black and I wanted my navbar to be black eventually. I think it works quite well as a white (black inverted) logo on a black navbar. 
From the navbar the non-signed-in user has a selection of *home*, *about*, *signup* or *login* to navigate to. Although, *home* is their original starting point anyway. Once logged in the user has the options of *profile*, *my vinyl*, *add vinyl* and *logout* which the navigation to and what they do, is pretty much self explanatory.
The admin user only has the *manage site* and *logout* options as I felt this is all they need as an admin. Within here they can navigate to various sections as regards the structure of the whole database and do various admin kinda things. I added some small back buttons to make the admin section navigation a little easier so they wouldn't have to always go back to the main manage site page everytime.
Overall I think the navigation works well.

* **Test**  


* **Result**  


* **Verdict**



### Describe Me In Five Words

#### User Story : I want to possibly add a description or some specific notes attached to each vinyl, if required

* **Plan**  
I want the user to be able to add a small description about each specific vinyl. Whether that's a few words about a song on it or the condition of the vinyl itself.
For example, this is an Ibiza style trance tune or this is happy hardcore at it's finest, and it's always good to know if there is a small scratch, some warping 
or possibly some sleeve damage too. This will also be useful information if you are ever looking to sell a vinyl on Discogs (Disclaimer - other vinyl sales websites are available) and you will probably have the main information already in My Vinyl Answer. Although selling vinyl should be made a criminal offence to be fair .... but that would mean I wouldn't have been able to buy any .... which would mean I have lost my passion !!! Okay scrap that, I meant to say selling vinyl should be a crime .... unless you are selling to me, ha ha, much better :)


* **Implementation**  
This was quite simple to be honest. I just added a textarea input to the add vinyl form so the user could add anythng they wanted within this description.
This discription will then be stored in the vinyls document along with all the other form data for future referencing by the user or admin.
Nothing really else much more to say on this one to be fair.

* **Test**  


* **Result**  


* **Verdict**



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
I could maybe have made the overall design of the form a little smaller so that it would fit on a large screen without scrolling but that's just a small detai, overall I still thnk it's cool and this is the *CREATE* functionality for the user.

* **Test**  


* **Result**  


* **Verdict**



### The Vinyl Edit Before It Goes To Press

#### User Story : I want to edit any vinyl info if I want

* **Plan**  
I want the user to be able to edit any vinyl information on any individual vinyl document in the database. They will be able to access the **Edit Vinyl** page from the 
**My Vinyl** page by clicking the edit button hidden within each of the vinyls collapsibles. Once on the Edit Vinyl page the user will have access to a pre-loaded form with the current vinyl information already filled in. The user can then edit whatever section they want and when they are happy, they can submit again to the database the editted vinyl info. Once this is complete I will redirect them back to their **My Vinyl** page again where they can check on their current updated vinyl. I'm just thinking that if the user has a large collection and they edit after scrolling down through a lot of them, if they decide to edit at this point, will a redirectiion send the user back to the top of the list??? I'll have to think about this one and test to see what happens :)

* **Implementation**  
Very similar to the add vinyl function mentioned above. Although, the add vinyl has it's own wee slot in the navbar the edit button is hidden behind each collapsible. The user has to click onto the tune they want to edit or delete. When they select the edit button, the ```edit_vinyl()``` function is activated and the selected vinyl id is passed to it. On the first instance the function finds the genres, the session user and the vinyl data. It then passes these to the edit vinyl page which populates the form for the user to edit. I utilised the add vinyl form as they are basically exactly the same. After the user has finished editing their vinyl they will then submit the form by pressing the *Edit Vinyl* button. This calls the ```edit_vinyl()``` function again but this time we are **POSTING** the form data for updating within the database. The obligatory flash message makes another appearance and the user is redirected to the edit vinyl page again. They can hit cancel to go back to their vinyl collection and see the changes that were made.

I added some admin changes so that if you are admin you get redirected to a card that displays all the vinyl information and from here you can move onto edit or delete the vinyl. I had to do this as I was using the Bulma panel format and wanted to keep it this shape instead of adding two buttons to it, I created the vinyl card for pop upping and offereing the required options.... clever I know ! 
I did encounter an annoying bug with this one tbh and it was the fact as admin the *owner* field kept getting wrote over as *admin* if i was admin and *none* if i left it out but I talk about this in the bugs section.
Again, I am happy with overall edit vinyl functionality and this is the *UPDATE* functionality for the user therefore covered.

* **Test**  


* **Result**  


* **Verdict**



### Deletion Will Be My Vinyl Option

#### User Story : I want to delete any vinyl I want (if I sell one personally or on another site)

* **Plan**  
I want the user to be able to delete any vinyl that they want. 
Why would they do that, you may ask? Well maybe they have grew up, unlike me, and they want to have babies, settle down and live a vinyl free life !
Life can be cruel so they will have to sell their vinyl collection .... could be a slow and painful sale were they slip from youir grasp in ones and twos ... or it could be a highest bid f'ing wins the f'ing lot :(
Anyhow enough gibber jabber fool, there will therefore be a button of the deletion family required. This delete button will be also be hidden within each of the vinyls collapsibles besdie the edit button above. Once the user clicks the delete button, I will add some defensive programming to make sure this is what the user wants to do.
This will hopefully eliminate the chance of deleting a vinyl by accident or mistake. Again once the user has completed their vinyl deletion, I will redirect them back to their **My Vinyl** page where their deleted vinyl has been removed and also removed from the database.

* **Implementation**  


* **Test**  


* **Result**  


* **Verdict**



### ADMIN SHIT NEEDS ADDED HERE AND AT USER STORIES OOSSIBLY

#### User Story :

* **Plan** 


* **Implementation**  


* **Test**  


* **Result**  


* **Verdict**




[Back to Top](#contents)

## **Bugs**
---

### **Bug Title**

* **Bug**


* **Fix**


* **Verdict** 




### **User Story Title**

#### User Story : 

* **Plan**  


* **Implementation**  


* **Test**  


* **Result**  


* **Verdict**  


[Back to Top](#contents)

## **Bugs**
---

### **Bug Title**

* **Bug**


* **Fix**


* **Verdict** 



[Back to Top](#contents)

## **Deployment**
---


## **Conclusion**
---

I know I called this My Vinyl Answer so it't therefore mainly about vinyl and stacks of it ha ha, but this could have been further developed so the
user could make up their own personl database for whatever collection they wanted. Obviously, there would be limits put in place so they don't abuse the database ...
nobody likes a db abuser !

Some of the harder python was easiest to conquer and I was like who's the daddy but then again some the easier python twisted my napper & was like an uppercut from Drago in Rocky 4.


## **Credits**
---

Collapsible taken from W3SChools

 JavaScript for a Bulma select dropdown taken from here - https://github.com/jgthms/bulma/issues/1870

Couldn't get dropdown border colour to change to my-blue which did my head in tbh . I tried everything but couldn't get it to work ......
until I remembered something !important (pun inteneded) ..... this solved my issue as the 'select' class was overruling all my tries !!!

https://stackoverflow.com/questions/34676752/can-i-use-an-html-input-type-date-to-collect-only-a-year/40662109 - Release Year Selection Code

https://stackoverflow.com/questions/2338102/override-browser-form-filling-and-input-highlighting-with-html-css - Remove Autofill from Add Vinyl As turned background blue

https://stackoverflow.com/questions/7560832/how-to-center-a-button-within-a-div - Align Edit Button with in my column

https://www.w3schools.com/howto/howto_css_delete_modal.asp - Delete Confirmation Model


tried to add jquery for calling the modal when you clicked on the 'delete button' but it wouldn't work.
It worked when I used say a class = p1 but not an id = p1 .... couldn't figure it out for ages .... did my head absolutely in tnh
but then i realised I was created id = p1 numourous times as it was within a for loop so therefore it was pissed off because there should only one 'id' & thats why it wouldn't work .... glad I figured it out tbh :)



I couldn't get my modal to delete the correct db file & it would just delete the first one in the list.
The selected vinyl_id wasn't linking to my delete route.
SO I moved the modal to it's own page & created an app.route to it when the delete button is pressed.
ANd I pass through the vinyl details using vinyl_id.
so I can display any vinyl details I want plus pass the vinyl_id onto the delete route.



Spent ages trying to figure out why my users database values would not display on my profile page as per user
I was using jinja logic to display them but forgot to write the database name with each value i.e. {{ fullname }} should have been {{ users.fullname }}
Pretty raging after that tbh but sure .... another learning poiunt noted & will be easier to notice next time !


email validation wasn't working .... I had type="text" instead of type="email"


I'm just thinking that if the user has a large collection and they edit after scrolling down through a lot of them, if they decide to edit at this point, will a redirectiion send the user back to the top of the list??? I'll have to think about this one and test tio see what happens :)


Couldn't figure out how to get the profile pic in the middle of the form. So tried putting the image in the middle of 3 columns.
And making the outer columns set to auto so that the middle column and therefore the image would stay in the middle of the device !


After a mentor sesh he said it would be good to have a default image in case the users url didn't load. well I tried various pieces of caode and couldn't get anything to work on a user I had made up but didn't have a profile pic url loaded. I tried for ages then realised he didn't have a profile_pic field in his database which didn't help because I had him made up before I decided to add a profile pic for to add to their Envinylonment (if I keep saying it maybe it'll catch on ha ha). Once I added this manually to the database the code I had be trying started to work ..... happy yet angry happy yet angry !!! Anyways, I tried have another url based image as back-up but while it maybe worked the first time, it was maybe missing on a reload and then back into vision on another reload. Not sure why this was happening to be honest but I didn't want to take any cvhances so I got a smiley face from my MS1. I edited Smiley Face image in Paint3D by removing some writing and I also removed the background. I added this to my images folder and using the code ```<img src="image.png" onError="this.onerror=null;this.src='/images/noimage.gif';" />``` I added my jinja link and my default Smiley Face ..... loads everytime ye boy ye (P.S. please don't come back saying it didn't work for you ..... just lie to me and say *worked dead on RaVeR76 !*)
https://stackoverflow.com/questions/92720/jquery-javascript-to-replace-broken-images?page=1&tab=votes#tab-top


I honestly don't know why this keeps happening because with my MS2 a similar UFO (Unidentified Fecking Oversight) happened during my mentor session. 
Last night he showed me his ... screen and my wee project was displaying proudly but I could see two vinyl being displayed. I was like how come there are two vinyls being diaplayed when you have't even logged in .... mind blown again. With my MS2 his cards would show the actually card underneath before he evn turned it whereas on my PC is was perfect. It was a Google vs Safari issue which I couldn't resolve and I thought this was another compatability issue. Anyway, Detective RaVeR was on the case and after some clever analysing, snooping around, interogation, I found that the culprit was none other than me .... RaVeR ! I hadn't added any *Owner* field to their individual collection document within Mongodb so my code I wrote for vinyl only to be displayed by the user would not work. Owner is a hidden field (not for display) that I use to do this and gets added when a new vinyl is added to their collection. Within the jinja for loop, I check that the current user ```session.user``` is the same as the owner ```vinyl.owner``` for each vinyl and if they are, their vinyl's will be displayed on screen.



I was refactoring all my code so I was doing it very slowly & in small parts so i didn't create a major headache on a Saturday night.
SO when I refactored a part say the modal i waould test everything linked to that modal and in fact I would just go through the whole website to make sure it all worked.
Anyway I was testing edit and delete from the vinyls page. I noticed that the when I made an edit and clicked the edit button it stayed on the edit vinyl page which is correct but when O went back the my vinyl page .... the wee vinyl had did a Hoodini and disappeared ! I was like WTF !
So I added more vinyl and kept trying it but yip ... same thing again. I followed the paths between everything and couldn't see anything that was out of place. 
I did a bit more investigating and went to my Mongodb collections and low n behold, there was all the vinyl that I had been adding. They had passed through the My Vinyl Anwser Bermuda Triangle or something mad-doggy like that.
Only messing, what was happening was that when I created the add_vinyl function, I had added an ```owner``` field to utilise it when displaying the users own vinyl collection. So when the user edited the vinyl they were only editing the original fields, as I had not added ```owner``` to the edit_vinyl function .... D'OH !!!!
To be honest it wasn't really deleting, as you know, it was just deleting the ```owner``` field and when it reloaded the users **My Vinyl** page again, the edited vinyl was just not loaded from the database as it only displays the users *aka owners* vinyl.
So I simply rectified this by adding ```"owner": session["user"]``` to the ```vinyl_edit``` list before updating the database document in MongoDb.
The edit function worked perfectly after this error was solved :)


I refactored everything as mentioned about so I only had the navbar & base to refactor. Did the navbar but had some sizing issues afterwards.
When the navbar was in the base it was covering the whole top part of the page but when I moved it to the components folder & used jinja logic to link it, it was only covering a smaller section. I found that becoasue I had added it to each page in the pages folder using Jinja logic it then becasme an extension of the base and this extension is sanwiched in it's own continer in the base html. Therefore the navbar was a navbar for the container. I therefore removed the main div with container class from the base.html and also the header section. This solved the navbar issue but the rest of the content was wider on each page ha ha .... it never rains but it pours as they say !
Solution was to enclose each page in the pages folder within a div with a container class, which I did and everything look scool again :)


Profile Issue Again - Didn't realise you could use a type="URL" for extra validation as I was worried about users just typing jibber jabber fool.
I had tried javascript methods, I was thinking am I going to have to write logic to cover every eventuallity of what the user may or may not type .... this is going to take ages. After a little bit of reaearch that wee type="URL" aved the day. 
It works a treat alomg with the *required* attribute so the user has to type a valid url before submitting their signup form.
```https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/url```
If it doesn't work then it goes to the default pic .... a big raver smiley face :)

Of the back of this validation adjustment, I found another bug that had raised it's ugly wee head, my default pic would not display no matter what.
at first I thought it had some connection with the URL validation so i checked it all, I deleled to see as well but still no Smiley Face. I was beginning to crack uo to be honest but I kept going. I checked the database to see if anything was untoward in there but everything looked okay. I foujd the bug by copying my Smiley Face src link and pasting it in over the Jinja expression just to see if it displayed when first called but NO ... it did not either ! What was heppening you may ask cause I did too ... well when I was doing my Refacrtoring thing I had moved my profile page into a new pages folder so therefore my default link didn't work no more. I just needed to add a wee ```/``` at the start of the link which solved the problem and everyone who's profile pic url does not work will get a Big Smiley Face instead :)



Nervous about getting the debugging wrong cause all you hear is you'll FAIL FAIL FAIL !!! ... if you leave it on. 
So I researched a bit just to make sure I get it right as I dinny wanna FAIL ! I found this on our very own Slack 
https://code-institute-room.slack.com/archives/C7JQY2RHC/p1618992182397900?thread_ts=1618985984.386500&cid=C7JQY2RHC plus advice from my mentor.
He said you could call the Debug value anything you wanted in the ```env.py``` as long as it's a string so I think I had *CritterFace* at a time and also *DeCrittering* but I just settled on a simple *True* ha ha.



I tried to log in and I couldn't. I tried using my various test login details but none would work. This was just after I had did some button styling so I was like tghere should be no connection. I investigated anyway and eventually found the reason.... I had CAPS LOCK ON ! How annoying yet secretly deceptive in that I wouldn't have realised that and din't realise that hence me delving into my code to find the reason.
Solution - add some detection for passwords as the user cannot see any input values. I found some cool yet simple code for this in W3Schools, link shown below :
https://www.w3schools.com/howto/howto_js_detect_capslock.asp
I also used the Bulma classes of help and is-danger for colour, I removed the red from the W3School example as it overide it.
I think it works well and will stop other users from being caught out like the developer himself ha ha !


After I added Caps Lock On code my collapsibles wouldn't work, it worked when I swapped the position of the JS code for them around.
I tried various test to figure out why it was doing this but I was spending too much time when I had a solution but I'll try come back to it & figure it out.
Think it's to do with the display class but not sure. It was a head melter for sure.


dropdown issues -its this new keyboard its a scud .... I can't get my JS to work with two functions, they are conflicting with each other for some reason & i've spent about 6 hours on the bastardo. It's my Caps On function and my dropdown selector function so I'll blank the Caps On out for a while cause I need to move on.
I decided to remove the password script from my main js file and place it on each of the login and signup pages. This solved the problem although I am reluctant to put any script on any of my pages, I hab=ve no alternative at the minuate as I want both functions to work :)


The keyboard is deffo a scud ha ha ..... just spent at least four hard spent evenings probably about 25 hours or so trying to get my all singing all dancing Admin CRUD box working and in the end I've had to give up. I couldn't get the certain functions working together and my JS was playing up again. Really guttted on this one to be hnest beacuse I put so much effort in and I couldn't get it right. Suppose it's another hard lessin to take but maybe if I had more time I would've got there in the end. If I have time at the end I will give it another go. But for now I have to move on and get my Admin CRUD simplified :(


got database collection names from this code
https://stackoverflow.com/questions/9805451/how-to-find-names-of-all-collections-using-pymongo



Code for scroll on Admin Vinyl 
https://stackoverflow.com/questions/21998679/css-how-to-make-scrollable-list



BUG - Admin issues when editing a vinyl, it changed the vinyl owner name to admin 
Still trying to gigure this shit housery out
This mofo ```owner = vinyl.get('owner')``` saved the day. I spent hours on this one as well .... unbelieveable I swear. Once you fix one wee bug another pops it's ugly head up. I wanted to utilize te edit_vinyl as both admin & a user but the owner key was causing my major headaches as the value was becoming admin then null & I couldnt figure it out for ages but then i found that piece of code, it worked.
Only now when the page returned the flash message had the new name but the page didn't change. I got sstuvk on this one too. I coundn't figure out how to redirect to fucntion in my app.py and pass an _id too. I had to settle for finding the vinyl & redering the template again. Sorry if it was not the logical method but I'm still learning & my head is fried at the minute lol !




Admin Rights - I thought this would be easy to find and solve but hey ... is coding simple .... not for a noob like me
I tried searching through the depths of the internet for such code but that's after I was offered someones kidney, 3 prostitutes & a WW2 Russian Tank .... the web can be so dark sometimes !
I got there yay me ! All I wanted to do was show certain navbar links to the user & admin just the admin section & then the non loggy in pages when you first arrive :)
I messed about which the jinja logic on my navigation code but struggled to get it right .... quite a few hours yet again but look ... I have to learn and as painful as it was I got there and it works for me. I had to duplicate the login line of code for admin and a user which may not be the correct way but it works and I need to move on. I just need to redirect my admin to a different page as it still shows there Profile page on first log in :)
One major fact if we are putting hinesty on the table that I had my else staement as {else} and not {% else %} which 100% did not help the situation and totally threw me a curve ball but it's done and working the way I want it too !
Now to fix the admin post login link so it's naw Profile 

 
https://www.w3schools.com/jsref/met_his_back.asp
Added back button code from W3Schools


https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_blurred_bg
background for home page logo taken from here  


passowrd issues when admin editing user - had to add some code to copy users passord & add it to new edited user so it wouldn't get wiped :)



Bouncing Animation - https://stackoverflow.com/questions/59135939/how-to-make-an-icon-move-up-and-down-with-css-animation

Vinyl On Floor Pic - Photo by Eric Krull on Unsplash

Vinyl Upright & Headphones Pic - Photo by blocks on Unsplash
  
Deck Pic -  Photo by James Sutton on Unsplash 

Vertical Vinyl - Photo by David Grandmougin on Unsplash

Store Vinyl For Sale - Photo by Valentino Funghi on Unsplash

[Back to Top](#contents)
