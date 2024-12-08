# deletedScratchFinder
Simple tool that lets you find deleted scratch projetcs.
!!This takes really long even with multithreading as its scraping every scratch project in a range

Usage:
You need your scratch x-token. You get it by going in to the network tab in your browser while looking at a scratch page, reloading the scratch page and finding the request for the actual site (its named as the project id). Click on the headers tab and then if you scroll down there sould be the x-token that you will have to copy and paste into the code in main.py.
## !!The x-token is basically your login information so never tell it to anyone

After that you will need to put a start and stop id for the range of projects and run it. I have implemented multithreading but it still takes a while. In the end it will crash as i am too lazy to fix it but when it finds deleted project it will put the id into a file that will be created.
Note: you can only find deleted projects of your x token (your account (( the account the x token belongs to)) )
