- [Crawl Wikihow data](#crawl-wikihow-data)
  - [1. Crawl topics](#1-crawl-topics)
  - [2. Crawl pages](#2-crawl-pages)



# Crawl Wikihow data



## 1. Crawl topics

Download all first-class and other topics

code:  [Crawl_topics](crawl_topics.py)  ——>  [topics.csv](topics.csv)



WikiHow's data is organized by topics and the topics are hierarchical

<details>
    <summary><b> Example of the structure of topics </b></summary>

│root

└───Arts and Entertainment
│   └───Artwork
│   └───Books
│   └───Celebrities
│   └───Concerts
│   └───Cosplay
│   └─── ......
│   

└───Cars & Other Vehicles
│   └───Aviation
│   └───Boats
│   └───Cars
│   └───Cycling
│   └───Driving Vehicles
│   └─── ......
│   

└───Computers and Electronics
│   └───Basic Computer Skills
│   └───Computer Networking
│   └───Computers
│   └───Consumer Electronics
│   └───Hardware
│   └─── ......
│   

└─── ......

</details>

csv file includes the following contents:

- topic url
- topic name
- father topics
- topic description

<details>
<summary><b> csv example </b></summary>

> | topic url                                                    | topic name                               | father topics                                  | topic  description                                           |
> | ------------------------------------------------------------ | ---------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------ |
> | https://www.wikihow.com/Category:Arts-and-Entertainment      | Arts and Entertainment                   | ['root']                                       | Learn to be well read, become a  better artist, and sell your own music with wikiHow's Arts and Entertainment  category. Our articles can help you develop talent in multiple areas and be a  good entertainer. Check out how-tos on learning ventriloquism, making your  own radio show, becoming a professional storyteller, and more. |
> |                                                              |                                          |                                                |                                                              |
> | https://www.wikihow.com/Category:Amusement-and-Theme-Parks   | Amusement and Theme Parks                | ['root', 'Arts and Entertainment']             | Learn everything you want about Amusement and  Theme Parks with the wikiHow Amusement and Theme Parks Category. Learn about  topics such as How to Overcome Your Fear of Roller Coasters, How to Cancel  Six Flags Membership, How to Overcome a Fear of Scary Rides, and more with  our helpful step-by-step instructions with photos and videos. |
> | https://www.wikihow.com/Category:Art-Collection              | Art Collection                           | ['root', 'Arts and Entertainment',  'Artwork'] | Learn everything you want about Art  Collection with the wikiHow Art Collection Category. Learn about topics such  as How to Appreciate Art, How to Sell Thomas Kinkade Paintings, How to Talk  About Art, and more with our helpful step-by-step instructions with photos  and videos. |
> |                                                              |                                          |                                                |                                                              |
> | https://www.wikihow.com/Category:Automotive-and-Transportation-Businesses | Automotive and Transportation Businesses | ['root', 'Cars & Other Vehicles']              | Learn everything you want about Automotive  and Transportation Businesses with the wikiHow Automotive and Transportation  Businesses Category. Learn about topics such as How to Open a Car Wash  Business, How to Buy and Sell Cars for Profit, How to Open a Car Dealership,  and more with our helpful step-by-step instructions with photos and videos. |
> | https://www.wikihow.com/Category:Audio                       | Audio                                    | ['root', 'Computers and Electronics']          | Learn everything you want about Audio with  the wikiHow Audio Category. Learn about topics such as How to Fix an Airpods  Microphone, How to What Equalizer Settings Are Best for Bass and Other  Equalizer Settings Explained, How to Reduce Static Noise in a Microphone, and  more with our helpful step-by-step instructions with photos and videos. |
>
</details>


csv file：[CSV file](topics.csv)



## 2. Crawl pages

Based on the topics , crawl page links of each topics

code: [crawl_pages.py](crawl_pages.py) ——> [merged_pages.csv](merged_pages.csv)



csv file includes the following contents:

- topic url
- topic name
- wikihow url
- wikihow name
- wikihow expert : whether writen by wikihow expert ;
- wikihow cover url : cover image url



csv file example:

| topic url                                               | topic name             | wikihow url                                                | wikihow name                              | wikihow expert | wikihow cover url                                            |
| ------------------------------------------------------- | ---------------------- | ---------------------------------------------------------- | ----------------------------------------- | -------------- | ------------------------------------------------------------ |
| https://www.wikihow.com/Category:Online-Role-Playing    | Online Role Playing    | https://www.wikihow.com/Beat-Sans-in-Undertale             | How to Beat Sans in Undertale             | FALSE          | https://www.wikihow.com/images/thumb/8/83/Beat-Sans-in-Undertale-Step-8.jpg/-crop-375-300-375px-nowatermark-Beat-Sans-in-Undertale-Step-8.jpg |
| https://www.wikihow.com/Category:Cleaning-Up-After-Dogs | Cleaning Up After Dogs | https://www.wikihow.com/Get-Dog-Urine-Smell-out-of-Carpets | How to Get Dog Urine Smell out of Carpets | TRUE           | https://www.wikihow.com/images/thumb/e/e7/Get-Dog-Urine-Smell-out-of-Carpets-Step-16-Version-2.jpg/-crop-375-300-375px-nowatermark-Get-Dog-Urine-Smell-out-of-Carpets-Step-16-Version-2.jpg |
| https://www.wikihow.com/Category:Technology-Hacks       | Technology Hacks       | https://www.wikihow.com/Hack                               | How to Hack                               | FALSE          | https://www.wikihow.com/images/thumb/f/f6/Hack-Step-14.jpg/-crop-375-300-375px-nowatermark-Hack-Step-14.jpg |



## 3. Extract content



