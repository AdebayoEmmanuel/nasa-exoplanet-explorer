# NASA Exoplanet Explorer

My Very Eyes Must Just See Under Nine…?

## Team:

Emmanuel Adebayo: I am taking on the full stack role as I am doing this project solo because of the time constraint involved since the end of my deferment period.

## Technologies:

### Client side:

- HTML, CSS, JavaScript frontend (for fast development).
- Alternatively: I can use React with Headless components and fast page generation tools like Vercel’s v0.dev. If there is sufficient time to adapt my project to use React, I would love to explore this.

### Server side:

- Python serverless function to parse fetched CSV data and convert them to JSON, return the JSON representation to the client.
- Alternative to this would have been to use JavaScript on the client side after fetching the data, but I don’t want to be doing client side processing. I believe it is more efficient, reliable and scalable to run data processing logic using serverless functions.
- Another reason why I picked python is because it is a better language for file manipulation (or should I say I have become conversant with using Python for file processing thanks to all the ALX tasks 😒😊).

### Storage:

- I intend to use the client storage indexDB to store converted JSON for faster loading and to only make API call to NASA’s archive if the file is not present on the client’s local storage (let's say the data was cleared) [IndexedDB API](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API).
- This is not an alternative, but I just want to point out that I will be using regular file storage for the dev environment, after sufficient test, I will switch to indexDB.

## Challenge:

- Since 1992 over 5,000 exoplanets have been discovered outside our solar system and I am only just finding out about it (thanks to this project😊). The United States National Aeronautics and Space Administration (NASA) maintains a publicly accessible archive of the data collected on these in comma separated value (CSV) format. I plan on fetching this data, modifying the structure(from comma delimited CSV to JSON) using some backend python code hosted on a serverless function and some indexer logic to store and retrieve the data efficiently.
- The objective of the NASA Exoplanet Explorer app is to make this data available for simple queries by its users. This project is based on this open source idea: [NASA Exoplanet Query](https://github.com/florinpop17/app-ideas/blob/master/Projects/3-Advanced/NASA-Exoplanet-Query.md).
- I have decided to chain the project idea suggested in the open source repo above with a different open source project idea which is aimed at creating an app that converts CSV to JSON format. [CSV2JSON App](https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/CSV2JSON-App.md).
- The Idea is to create an archive explorer that users can use to query the archive and efficiently retrieve details about exoplanets discovery.
- This project would only download the CSV of all exoplanets from 1992 till date (dataset of more than 5000 planets and details about them). [NASA Exoplanet Archive](https://exoplanetarchive.ipadc.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS)
- This project does not intend to mirror NASA’s archive nor aim to act as a replacement, it is only an aggregator of confirmed planets data, downloaded over a fetch API call, modified into JSON by serverless python codes and queried using efficient search algorithms.
- This project’s tagline has a sentimental meaning as it was motivated by the fact that there are more planets outside our solar system. The tagline used to be an analogy for the planets in our solar system and was how I learned about the planets back in secondary school.

## Risks:

- I have to find a way to implement a means of efficiently loading the exoplanet CSV data obtained from NASA to minimise any delays when the application starts. I am currently considering indexDB for this, I will have to review the docs properly to figure out how I can use this.
- I have to utilise a data structure and search mechanism that minimises the time required to query the exoplanet data and display the results. [Big O Notation](https://en.wikipedia.org/wiki/Big_O_notation), [CSV2JSON](https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/CSV2JSON-App.md).
- I will need to review the Exoplanet Archive documentation to understand the format of the data fields. [Exoplanet](https://en.wikipedia.org/wiki/Exoplanet), [NASA Exoplanet Archive](https://exoplanetarchive.ipadc.caltech.edu/docs/program_interfaces.html).
- One potential blocker I am seeing is the gap between sending CSV to Backend, having it processed and sending it back to the client as JSON. It may be tricky and potentially unsafe to keep an http connection open long enough for this, so I am thinking of using something like server sent events [Server Sent Events](https://medium.com/@tahsinkheya/server-sent-events-using-python-flask-and-react-js-e564e03b03e9) for this.

## Infrastructure:

### Client side:

- The frontend will be hosted as a static web app either on Azure (I have sufficient cloud credits although there is a free tier I can take advantage of) or alternatively, if I can make GitHub pages work, or explore free options with vercel.

### Serverside:

- Serverless cloud function deployed to Azure or alternatively, I can deploy an API to a Docker container hosted on any of my ALX sandboxes that will expose endpoints for the client app and do my server side data processing and sending of JSON back to the client. Issue with this option is scaling, Serverless functions scale better.

## Existing Solutions:

- Like I mentioned in earlier section, this project does not aim to replace NASA’s archive but builds on these open source projects: [NASA Exoplanet Query](https://github.com/florinpop17/app-ideas/blob/master/Projects/3-Advanced/NASA-Exoplanet-Query.md) and [CSV2JSON App](https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/CSV2JSON-App.md) to build a system that aggregates the data from the CSV file containing details of the exoplanets, load it unto the backend infrastructure for data modification and implementing efficient search algorithm to allow user to query this data set efficiently.
- To improve efficiency, this project is focusing on best practices on using local storage and client side programming, strong consideration to storing the data as JSON on the back end and an algorithm to query the JSON file and fetch user’s queries. The ultimate consideration for efficiency is the decision to use indexDB so the client doesn't have to make fresh API calls to the archive and even would not have to do new backend data processing every time as long as the indexed data exists.
