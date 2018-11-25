# European refugee crisis

# Abstract
In last decades because of the rising poverty and conflicts in developing regions such as Maghreb(Sub-Saharan Africa), Latin America and Middle East the immigration to Europe had been steadily increasing. In recent years, this tendency was accelerated by the revolutions and civil wars in Arab countries - so called Arab Spring and reached the crisis level (https://en.wikipedia.org/wiki/European_migrant_crisis). 

In our report, we want to foucs on the topic of the refugee. To do so, first we start with exploring how the immigration in Europe changes by visulizing UNHCR's database. After getting a quantized results of the refugee's immigration, we want to get the oponion from different countries. we will look at the meadia's oponion and the origin of media by the year and the event related to refugee.

Further, it's also interesting we could classify the events and get the different categories of events. We could try to visualiza the location that most related to those categories and the oponion related to those categories.

In general, we want to explore the refugee cirsis in European and how the oponion changed with the time and the different events happend.


# Research questions
How is the refugee's immigration changes in European countries with the time?

Which countries are the most important refugee destinations?

How are refugee movements associated with news?

How is the distribution of origin of media sources related to the refugee events?

What are the differences between Eastern and Western European countries' approach towards refugees?

How political state of country is related to its media coverage towards refugees?

How is the the media's oponion change with time?

Which important events(like Istanbul, Paris bombing, other terrorist attacks) are vital in tone of media coverage?
(https://en.wikipedia.org/wiki/Timeline_of_the_European_migrant_crisis)

# Dataset
**Global Database of Events, Language, and Tone (GDELT)** The dataset monitors and analyses news articles around the world from 1979 to present. It is important to mention that the dataset consists of two versions: the GDELT Knowledge Graph and the GDELT Event Database. We will use the simple sentiment algorithm of GDELT which is already precalculated and referred to 'tone' metadata on the dataset. Sentiment scores range from -100 to +100, where 0 is neutrality. However most of the news and events range from -10 to +10.

**Wikipedia** and **UNHCR's database**: After dealing with textual descriptions, we are planning extract the numerical data about the refugee crisis for the statistics from Wikipedia tables and UN Refugee Database(UNHCR).

# Milestone 2 
For milestone 2, we extract the data - GDELT Events and Mentions from the cluster and use important information from UNHCR database. We explore the data based on time and countries over average tone and number of events and visualize many maps based on those information. They will be important in our future visualizations for milestone 3.

We saved all results in our local machine as parquet file. Also for maps you can look the exporting html(data_exploration.html) of our main notebook.

# For milestone 3

- We will cluster the countries and the sites based on the average tone and their approach.
- We will analyze important events which are effective in tone of the media coverage.
- We will visualize more user-friendly maps which illustrates all flows of refugee from North Africa or Middle East to Western Europe.
