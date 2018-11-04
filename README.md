# European refugee crisis: interplay of power between politics, media and citizens

# Abstract
In last decades because of the rising poverty and conflicts in developing regions such as Maghreb(Sub-Saharan Africa), Latin America and Middle East the immigration to Europe had been steadily increasing. In recent years, this tendency was accelerated by the starting of the revolutions and civil wars in Arab countries - so called Arab Spring and reached the crisis level (https://en.wikipedia.org/wiki/European_migrant_crisis). 

In our report, we want to explore the emergence of this refugee crisis topic. Usually, politics, media and people's oponion influence each other theoretically. However, the time series data gives us a chance to study the causility of those three. For example, maybe the refugee crisis topic first arses with people's oppnion, then is followed by politics then media. Maybe it's opposite. 

To study this, we conduct a analysis on extracting the time evolution (from January 1st 2015 to December 31st 2017) of politic approach, news media coverage and people's oponio by searching the key words or sentiment analysis related to refugee crisis on Global Database of Events, Language, and Tone (GDELT), Twitter database, Wikipedia etc.

# Research questions
What's the approaches of the European Union, goverments to this refugee crisis with the time?

What's the attitude of medias to this refugee crisis with the time?

What's the people's oponion about this refugee crisis with time?

What's the time order of politics, media, citizens? How do they influence each other?

# Dataset
**Global Database of Events, Language, and Tone (GDELT)** The dataset monitors and analyses news articles around the world from 1979 to present. It is important to mention that the dataset consists of two versions: the GDELT Knowledge Graph and the GDELT Event Database. We will use the simple sentiment algorithm of GDELT which is already precalculated and referred to 'tone' metadata on the dataset. Sentiment scores range from -100 to +100, where 0 is neutrality. However most of the news and events range from -10 to +10.

**Twitter dataset**: We will use 2017 Twitter dataset to analyze the reaction of the people to the refugees in their countries and policies of their governments towards them. We are planning to use sentiment algorithm to detect that tweets are negative, positive or neutral. Since we can detect the language of the tweets, we can discover the different tendencies between the languages, thereby more generally countries.

**Wikipedia** and **UNHCR's database**: After dealing with textual descriptions, we are planning extract the numerical data about the refugee crisis for the statistics from Wikipedia tables and UN Refugee Database(UNHCR).

# A list of internal milestones up until project milestone 2
**4th of November** 
  - Explore the structure of the data, and create Github repo, and write the README.md
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

# Questions for TAa
Is it okay to use external datasets like UNHCR?
Can we use unofficial/official polls related to people's opinion towards refugees?
