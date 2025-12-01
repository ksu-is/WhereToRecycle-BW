Nov 7, 2025
-[ x ] Joined KSU-IS github group
-[ x ] Created WhereToRecycle-BW repository in KSU-IS group
-[ x ] Created description for app in read.me file and committed changes
-[ x ] Cloned and Evaluated flask repository code
The code has a lot of comments, but much of the code is still confusing for me, since I'm such a beginner at coding.
-[ x ] Evaluated Sort-Smart-Advanced-Waste-Management-System repository
They used python and flask for their backend code. In this app, the user inputs a picture of the item they want to recycle and also inputs the city’s name. In my app, I want the user to input the name of the item to recycle and the zip code or city’s name. This is from their repository:

Backend
Developed in Python using Flask
Hosts the ML model and processes image classification requests
Exposes RESTful API endpoints for classification, guidelines, and location-based queries

They also list recycling guidelines for each category, and I would like to have something similar, with information on each item and the importance and local impact of recycling. The rest of the app is not in python, so I'll try to understand which parts I can use for the location input and recycling info.

Sprint 2:
-[ x ] Make at least 6 small updates in repository and commit changes
-[ x ] Do this in Github Desktop
-[ x ] Each commit should include a comment that explains what you did. The comment must be specific.
-[ x ] Track your progress on planned and emerging tasks in your projectroadmap.md document.

Sprint 3:
-[ x ] Make at least 6 small updates in repository and commit changes
-[ x ] Do this in Github Desktop
-[ x ] Each commit should include a comment that explains what you did. The comment must be specific.
-[ x ] Create a PowerPoint slide introducing your project and upload it.
Include this information:
-[ x ] List your project team members.
-[ x ] Show the title of your project.
-[ x ] Show a tag line that introduces the main concept of what it does/will do.
-[ x ] Show 1-2 screenshots or pictures demonstrating the idea or parts (optional) Each person must upload a PPT slide in D2L. Each team must ensure there is a copy in their Github repository so that future coders can quickly grasp the idea.

Nov 15, 2025
I've been a bit overwhelmed this week figuring out where to start. I've been researching how to create an app with flask on Github to help understand what I need to do to start, but I haven't found anything helpful (except from our class). I figured out how to start the code by creating a file called app.py in the WhereToRecycle-BW repository in VSCode. I read over the information on D2L about importing modules, but flask isn't importing, so I'm re-watching the Project Demo: Flask video to get it started.
I was able to successfully install flask after re-watching the Project Demo: Flask video from class. Now I am figuring out how to create the app. I think I can just create a website that links users to recycling websites and gives them information on recycling. It takes a lot of time to research to figure out the details of how to create an app.

Nov 17, 2025
After watching the Demo Project: Flask video, I evaluated the script.py file and researched on the internet to understand what code to use to create a web app with Flask. I copied and pasted from the script.py file and got the app running. I created a folder called templates and added a WhereToRecycle.html page.

Nov 22, 2025
I had to redo the app.py file, because for some reason it was empty. I changed the home page to link to the WhereToRecycle.html file. I added some content and a photo to the top. I also added a link to the earth.911.com website, where users can find information on where to recycle items based on the item name and zip code input.
I moved the recycling symbol photo to the top and placed a recycling center photo under recycling definition content. I also added content of a sentence explaining to the user to click the link and be taken to earth.911.com where they can put in the name of the item and their zip code to find where to recycle the item.
I have the basic functionality of the app completed with the link to the earth.911.com website. I want to add more content on why recycling is important.
I thought I would need to create the link to the external website with HTTP requests to an external API, but I was able to create the link with the html webpage.
I've made commits for my changes in Github Desktop to satisfy the requirements of Sprint 2.

Nov 24, 2025
I added two links for epa.gov where users can find information on recycling and how to recycle items. I also changed the earth.911.com link to say where to recycle items SEARCH instead of having a sentence above the link saying to click the link for the search. I researched copyright for the epa.gov website, and the information on epa.gov is public domain. I'm glad to know I can put information about recycling on my app's webpage.

I realized none of my projectroadmap.md comments were committed, so I copied and pasted them all on VSCode today, and just added the dates of each.

Nov 29
I am researching again about http requests and using an api to link an input box on my app with an external website to input an item and return information to the user on where to recycle the item. I found coding information on Copilot Search to create the input box with flask forms, create the html page with the form's data, and create the api request. The website is called earth911.com. It requires me to get permission from the website to create an api to their website. I haven't gone through the process to try and get permission, because my app is just a project assignment and not going to be a real app, so I'm assuming they will say no.That's why I just have a link from my app to the website, so the user can just enter the item directly on earth911.com's input box.

Nov 30
I'm making the webpage look better by providing information to the user on recycling. I replaced a picture with a paragraph of recycling info on the webpage. I tried to use a different branch to try it out but it wouldn't seem to run without being committed to the main branch. I realized it wasn't running because I was trying to run the .html file instead of the .py file. My mistake.
I then added h4 styling to css and added recycling info from the epa.gov website to WhereToRecycle.html. The webpage looks a lot better, and the user can get information on recycling before they click the link to search for where to recycle their item.

Dec 1
I deleted one link to the epa.gov recycling basics and benefits webpage, because I put the info from the page on my app webpage. The info is public domain. I added some more recycling info from the epa.gov website to WhereToRecycle.html. 
I finished the app, and it looks good. A user would find valuable information and links to reputable websites where they can learn where and how to recycle items they're interested in recycling.
I updated the Sprint 3 check boxes to show I've completed all of Sprint 3, including the PowerPoint Splash Screen slide. 

I noticed the title of one of the website links was not accurate and some words needed to be capitalized, so I updated the WhereToRecycle.html webpage, took a new screenshot, and updated the PPT slide. I uploaded a new slide on D2L and on the GitHub repository.