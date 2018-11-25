# European refugee crisis

# Abstract
In last decades because of the rising poverty and conflicts in developing regions such as Maghreb(Sub-Saharan Africa), Latin America and Middle East the immigration to Europe had been steadily increasing. In recent years, this tendency was accelerated by the revolutions and civil wars in Arab countries - so called Arab Spring and reached the crisis level (https://en.wikipedia.org/wiki/European_migrant_crisis). 

In our report, we want to foucs on the topic of the refugee. To do so, first we start with exploring how the immigration in Europe changes by visulizing UNHCR's database. After getting a quantized results of the refugee's immigration, we want to get the oponion from different countries. we will look at the meadia's oponion and the origin of media by the year and the event related to refugee.

Further, it's also interesting we could classify the events and get the different categories of events. We could try to visualiza the location that most related to those categories and the oponion related to those categories.

In general, we want to explore the refugee cirsis in European and how the oponion changed with the time and the different events happend.


# Research questions
How is the refugee's immigration changes in European countries with the time?

How is the distribution of origin of media sources related to the refugee events?

How is the the meida's oponion change with time?

Clustering the events and see how the oponion change with the different categories of the events.



# Dataset
**Global Database of Events, Language, and Tone (GDELT)** The dataset monitors and analyses news articles around the world from 1979 to present. It is important to mention that the dataset consists of two versions: the GDELT Knowledge Graph and the GDELT Event Database. We will use the simple sentiment algorithm of GDELT which is already precalculated and referred to 'tone' metadata on the dataset. Sentiment scores range from -100 to +100, where 0 is neutrality. However most of the news and events range from -10 to +10.

**Twitter dataset**: We will use 2017(hope 15 and 16 as well) Twitter dataset to analyze the reaction of the people to the refugees in their countries and policies of their governments towards them. We are planning to use sentiment algorithm to detect that tweets are negative, positive or neutral. Since we can detect the language of the tweets, we can discover the different tendencies between the languages, thereby more generally countries.

**Wikipedia** and **UNHCR's database**: After dealing with textual descriptions, we are planning extract the numerical data about the refugee crisis for the statistics from Wikipedia tables and UN Refugee Database(UNHCR).

# A list of internal milestones up until project milestone 2

**4th of November** 
  1. Explore the structure of the data
  2. Create Github repo, and write the README.md
  
**11th of November** 
  1. Get the feedback from TAs and discuss our future plans with them. 
  2. Process and perform the GDELT dataset
  3. Extract the useful information and analyze the sentiment over the time period. 
  4. Start to analyze the Twitter data.
  
**18th of November**
  1. Process and perform the Twitter dataset
  2. Analyzing the sentiment over different coutries(try to do two or more languages). 
  3. Try to connect the results and explore the relationship with media. 
  4. Collect the useful numeric data from Wikipedia and UNHCR and start the visualization.
  
**25th of November** 
  1. Finish the visualization. 
  2. The final retouches. 
  3. Explore the methods for data story or just paper.

# Questions for TAs
Is it okay to use external datasets like UNHCR?

Can we use unofficial/official polls related to people's opinion towards refugees?

Can you help to get sentiment analysis toolkit for multiple languages(such as Google NLP Toolkit) or we should deal with ourselves?

Is it possible to provide tweets in much broader time span?(at least 2015 and 2016)
