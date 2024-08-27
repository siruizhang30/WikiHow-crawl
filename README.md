- [Crawl Wikihow data](#crawl-wikihow-data)
  - [1. Crawl topics](#1-crawl-topics)
  - [2. Crawl pages](#2-crawl-pages)
    - [2.1 Based on topics](#21-based-on-topics)
    - [2.2 Randomly](#22-randomly)
  - [3. Extract content](#3-extract-content)



# Crawl Wikihow data



WikiHow: [Wikihow](https://www.wikihow.com/)



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


<details>
    <summary><b> Example of the structure of topics </b></summary>
root
├─Arts and Entertainment
│  ├─Artwork
│  ├─Books
│  ├─Celebrities
│  ├─Concerts
│  ├─Cosplay
│  └─ ......
├─Cars & Other Vehicles
│  ├─Aviation
│  ├─Boats
│  ├─Cars
│  ├─Cycling
│  ├─Driving Vehicles
│  └─ ......
├─Computers and Electronics
│  ├─Basic Computer Skills
│  ├─Computer Networking
│  ├─Computers
│  ├─Consumer Electronics
│  ├─Hardware
│  └─ ...... 
└─ ......


</details>


csv file includes the following contents:

- topic url
- topic name
- father topics
- topic description

<details>
<summary><b> csv example </b></summary>
<table>  
  <tr>  
    <th>topic-url</th>  
    <th>topic-name</th>  
    <th>father-topics</th>  
  </tr>
  <tr>  
    <td>https://www.wikihow.com/Category:Arts-and-Entertainment)</td>  
    <td>Arts and Entertainment</td>  
    <td>['root']</td>   
  </tr>  
  <tr>
    <th>topic description</th>
  </tr>
  <tr>
  	<td colspan="3">Learn to be well read, become a better artist, and sell your own music with wikiHow's Arts and Entertainment category. Our articles can help you develop talent in multiple areas and be a good entertainer. Check out how-tos on learning ventriloquism, making your own radio show, becoming a professional storyteller, and more.</td>
  </tr>
  <tr>
  	<td> </td>
  </tr>
  <tr>  
    <th>topic-url</th>  
    <th>topic-name</th>  
    <th>father-topics</th>  
  </tr>
  <tr>  
    <td>https://www.wikihow.com/Category:Amusement-and-Theme-Parks</td>  
    <td>Amusement and Theme Parks</td>  
    <td>['root', 'Arts and Entertainment']</td>    
  </tr> 
  <tr>
    <th>topic description</th>
  </tr>
  <tr>
  	<td colspan="3">Learn everything you want about Amusement and Theme Parks with the wikiHow Amusement and Theme Parks Category. Learn about topics such as How to Overcome Your Fear of Roller Coasters, How to Cancel Six Flags Membership, How to Overcome a Fear of Scary Rides, and more with our helpful step-by-step instructions with photos and videos. </td>
  </tr>
   <tr>
  	<td> </td>
  </tr>
  <tr>  
    <th>topic-url</th>  
    <th>topic-name</th>  
    <th>father-topics</th>  
  </tr>
  <tr>  
    <td>https://www.wikihow.com/Category:Art-Collection</td>  
    <td>Art Collection</td>  
    <td>['root', 'Arts and Entertainment', 'Artwork']</td>  
  </tr>  
  <tr>
    <th>topic description</th>
  </tr>
  <tr>
  	<td colspan="3">Learn everything you want about Art Collection with the wikiHow Art Collection Category. Learn about topics such as How to Appreciate Art, How to Sell Thomas Kinkade Paintings, How to Talk About Art, and more with our helpful step-by-step instructions with photos and videos. </td>
  </tr>
   <tr>
  	<td> </td>
  </tr>
  <tr>  
    <th>topic-url</th>  
    <th>topic-name</th>  
    <th>father-topics</th>  
  </tr>
  <tr>  
    <td>https://www.wikihow.com/Category:Automotive-and-Transportation-Businesses</td>  
    <td>Automotive and Transportation Businesses</td>  
    <td>['root', 'Cars & Other Vehicles']</td>  
  </tr> 
  <tr>
    <th>topic description</th>
  </tr>
  <tr>
  	<td colspan="3">Learn everything you want about Automotive and Transportation Businesses with the wikiHow Automotive and Transportation Businesses Category. Learn about topics such as How to Open a Car Wash Business, How to Buy and Sell Cars for Profit, How to Open a Car Dealership, and more with our helpful step-by-step instructions with photos and videos. </td>
  </tr>
   <tr>
  	<td> </td>
  </tr>
  <tr>  
    <th>topic-url</th>  
    <th>topic-name</th>  
    <th>father-topics</th>  
  </tr>
  <tr>  
    <td>https://www.wikihow.com/Category:Audio</td>  
    <td>Audio</td>  
    <td>['root', 'Computers and Electronics']</td>  
  </tr> 
  <tr>
    <th>topic description</th>
  </tr>
  <tr>
  	<td colspan="3">Learn everything you want about Audio with the wikiHow Audio Category. Learn about topics such as How to Fix an Airpods Microphone, How to What Equalizer Settings Are Best for Bass and Other Equalizer Settings Explained, How to Reduce Static Noise in a Microphone, and more with our helpful step-by-step instructions with photos and videos.</td> 
  </tr>
</table>  


</details>


csv file：[CSV file](topics.csv)



## 2. Crawl pages

### 2.1 Based on topics

Based on the topics , crawl page links of each topics

code: [crawl_pages.py](crawl_pages.py) ——> `pages/pages_{topic}.csv` 

merge them to get: [merged_pages.csv](merged_pages.csv)



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

### 2.2 Randomly

Download html files randomly from root path

code: [crawl_random_pages.py](crawl_random_pages.py) ——>  `random_pages-wikihowfun/{content_url.split('/')[-1]}.html`



## 3. Extract content

Use  `trafilatura` to parse the html

```python
import trafilatura
url = "https://www.wikihow.com/Lower-Blood-Pressure"  
  
# Use function trafilatura.fetch_url() to fetch html content of the URL  
html_content = trafilatura.fetch_url(url)  
  
# Use function trafilatura.extract() to get main content from html content  
extracted_text = trafilatura.extract(html_content, include_tables=False, include_formatting=False, include_comments=False)  
  
print(extracted_text)
```

<details>
<summary><b> Output results </b></summary>

```text
This article was medically reviewed by Victor Catania, MD and by wikiHow staff writer, Eric McClure. Dr. Catania is a board certified Family Medicine Physician in Pennsylvania. He received his MD from the Medical University of the Americas in 2012 and completed his residency in Family Medicine at the Robert Packer Hospital. He is a member of the American Board of Family Medicine.
There are 16 references cited in this article, which can be found at the bottom of the page.
wikiHow marks an article as reader-approved once it receives enough positive feedback. In this case, 100% of readers who voted found the article helpful, earning it our reader-approved status.
This article has been viewed 796,245 times.
If you've been diagnosed with high blood pressure (also called hypertension), your doctor has probably suggested making some changes to improve your blood pressure and overall health. Fortunately, there are many ways to naturally lower your blood pressure and make a change. From tweaking your diet and exercise routine to reducing stress, we've got the best expert advice on how to control high blood pressure.
Things You Should Know
- Switch to the DASH diet, which is designed to help lower blood pressure and manage your symptoms.
- Exercise regularly, minimize your alcohol consumption, and manage your stress.
- Consult your doctor and ask about medications to help you lower your overall blood pressure.
Steps
The DASH Diet
-
1Lower your sodium intake by consuming less salt. Many people eat as much as 3,500 mg of sodium per day. The DASH diet, which is short for Dietary Approaches to Stop Hypertension, recommends no more than 2,300 mg of sodium per day. Sodium is in salt, so the best way to reduce your sodium intake is to eat less salt when you cook or order out.[1] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to source
- Season your food without table salt. Do this by not salting meats and not adding salt to the water when you cook rice or pasta.
- Avoid salty snacks and processed food like chips, pretzels, and salted nuts. They often have large amounts of salt added to them. If you do purchase prepared foods, look for low-sodium versions.
- Check the contents of canned food, premixed seasonings, bouillon cubes, canned soups, jerkies, and sports drinks to see if they have salt added to them.
-
2Consume 6-8 servings of whole grains every day. Whole grains are better than processed white rice or processed flour because they have more fiber and nutrients. A serving is a slice of wheat bread, 1 ounce (28 g) of dry cereal, or a ½ cup (19 g) of pasta.[2] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to source
Advertisement
- Buy whole wheat flour and pasta instead of white. Many whole wheat bread products will say on the packaging that they are whole wheat.
- Eat oatmeal or make brown rice if you want a great source of nutrients and fiber.
-
3Load up on fruits and vegetables as snacks and main ingredients. Eat 4-5 servings of fruit and 4-5 servings of vegetables each day. A serving is ½ cup (48 g) of leafy vegetables or a ½ cup (85 g) of cooked vegetables. These are great sources of potassium and magnesium which help to lower your blood pressure.[3] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to source
- Eat a side salad with every meal. Keep them interesting by varying what you put in them. Add a sweet element by throwing in some apple or orange slices. Go easy on the salad dressings, though—they have a lot of salt and fatty oils.
- Incorporate vegetables as a side dish. Instead of cooking pasta, try putting the main dish over a sweet potato or next to a side of squash.
- Snack on fruits and vegetables between meals. Take an apple, banana, carrot, cucumber or green pepper with you to work or school.
- Buy frozen vegetables. If you are worried about having fresh produce go bad before you eat it, frozen vegetables are an excellent choice.
-
4Consume 2-3 low-fat dairy products, like yogurt, every day. Dairy is an important source of calcium and a good way to maintain vitamin D levels. However, it is important to choose dairy products carefully to avoid consuming too much fat and salt. 1 cup is a serving, and you should aim for 2-3 servings per day.[4] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to source
- Cheese is often high in salt, so don’t overdo it.
- When you eat yogurt and drink milk, go for the low-fat or skim varieties. Both are great with whole-grain cereals for breakfast.
-
5Stick with lean meat, poultry and fish. Meats and fish are excellent sources of protein, vitamins, iron and zinc, but some variations can be high in fat and cholesterol. Since fat and cholesterol can clog your arteries, it’s best to not overindulge. Eat no more than 6 servings per day, with 1 serving being an ounce of meat (30 g) or an egg.[5] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to source
- Avoid fatty red meats, like ground beef, ribeye or short rib. When you cook, don’t fry your meats. Healthier alternatives include baking, grilling, or roasting.
- Salmon, herring and tuna are great sources of omega-3 fatty acids. Eating these fish can help control your cholesterol, and they are also high in protein.
- For vegetarians, eating tofu is an excellent meat substitute because it is high in protein.
-
6Cut back on your fat consumption. Fat increases your risk of heart disease. To protect your heart, restrict your fat intake to a maximum of 3 servings per day. A tablespoon (14 g) of butter is a serving.[6] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to source
- Don’t spread butter or mayonnaise on bread. Instead, try using olive oil or ghee.
- Some fats are better than others. Unsaturated natural fats, which are found in things like olives, corn, and fish, are much better than synthetic, saturated, or trans fats.[7] X Research source
- Reduce the amount of oil you cook with. Use skim milk instead of whole milk and avoid heavy cream, lard, solid shortenings, palm and coconut oils.
-
7Supplement your diet with nuts, seeds, and legumes. These ingredients are relatively high in fat, but they also have magnesium, potassium, fiber, and protein. So, the DASH diet calls for 4-5 servings a week. A serving counts as 1/3 of a cup (50 g) of nuts.[8] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to source
- Nuts and seeds make an excellent addition to salads. They’re also just a great snack on their own.
-
8Restrict your sugar consumption, especially if it’s processed. Processed sugars add calories to your diet without providing any nutrients. Reduce your consumption of sweets to, at most, 5 times per week. A serving counts as 1 tablespoon (12 g) of sugar or jelly.[9] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to source
- Artificial sweeteners are always going to be healthier than using sugar, but use them sparingly.
- Some sugars are worse than others. Artificial and added sugars are a lot worse for you than the natural sugars (like fructose) found in fruit and milk.[10] X Trustworthy Source American Heart Association Leading nonprofit that funds medical research and public education Go to source
Lifestyle Changes
-
1Exercise for roughly 75-150 minutes a week to stay healthy. Being physically active can lower your blood pressure by helping to control your weight and manage stress.[11] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to source For the best results try to do 75–150 minutes of physical activity per week.[12] X Trustworthy Source Centers for Disease Control and Prevention Main public health institute for the US, run by the Dept. of Health and Human Services Go to source
- You can choose whatever kind of physical activity you’d like as exercise. Fun options include walking, running, dancing, biking, swimming, or playing sports.
- Do strength training, such as weight lifting, twice a week to maintain bone density and build muscle.
-
2Reduce your alcohol intake. Consuming too much alcohol is bad for your heart, and alcoholic beverages are high in calories that contribute to obesity. You can lower your blood pressure by quitting drinking or drinking only in moderation (i.e. 1 drink a day, or drinking only periodically).[13] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to source
- Men over 65 and women should limit themselves to, at most, one drink per day.
- Men under 65 should have no more than two drinks per day.
- A can of beer, a glass of wine, or a shot of hard liquor all qualify as a drink.
-
3Quit smoking or chewing tobacco if you’re a tobacco user. Tobacco can harden your arteries and make them narrow, which will increase your blood pressure.[14] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to source Secondhand smoke can also cause these effects. If you need help to quit smoking, you might:[15] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to source
- Talk to your doctor or see a counselor.
- Join a support group or call a quitting hotline.
- Ask your doctor about medication or nicotine replacement therapy.
-
4Evaluate your medications and avoid illicit drugs. If you think your medications might be causing high blood pressure, consult your doctor. Your doctor may be able to help you find an alternative that is better for your blood pressure. Don’t stop taking your medications without clearing it with your doctor first.[16] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to source
- Illicit drugs like cocaine, crystal methamphetamine, and speed can increase your blood pressure to a dangerous degree.
- Some birth control pills can raise your blood pressure.
- Many decongestants and cold medications can put stress on your heart if you overuse them.
- Over-the-counter nonsteroidal anti-inflammatory drugs (like ibuprofen) aren’t good for blood pressure over time.
-
5Reduce your overall stress. Constant stress can put a ton of unnecessary strain on your heart and artificially raise your blood pressure—especially if your body experiences the “fight or flight” response frequently. While some stress is an unavoidable part of life, use relaxation techniques to help you deal with it.[17] X Trustworthy Source American Heart Association Leading nonprofit that funds medical research and public education Go to source Try:
- Yoga.
- Meditation.
- Music therapy.
- Deep breathing exercises.
- Positive visualization.
- Progressive muscle relaxation.
Seeing a Doctor
-
1Call emergency responders for a heart attack or stroke. Heart attacks and strokes occur quickly, and you’re at an increased risk if you have high blood pressure. Every minute counts, so call emergency services at the first onset of symptoms.[18] X Research source
- Signs of a heart attack include: pressure or pain the chest, pain in one or both arms, neck, back, jaw, or abdomen, shortness of breath, sweating, nausea, or dizziness.[19] X Trustworthy Source American Heart Association Leading nonprofit that funds medical research and public education Go to source
- Symptoms of a stroke include: drooping face, difficulty speaking or understanding speech, numbness or weakness in an arm, leg, or the face, confusion, vision problems in one or both eyes, dizziness, loss of coordination, or headache.
-
2Go to the emergency room if you have a hypertensive crisis. If you have high blood pressure, monitor it closely and get your blood pressure checked every year at your annual checkup. If your blood pressure gets too high, you may experience a hypertensive crisis, which requires emergency medical care. Go to the ER if you have:[20] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to source
- Headaches that don’t go away.
- Blurred vision or seeing double.
- Frequent nosebleeds.
- Shortness of breath.
- Chest pain, nausea, or vomiting.
-
3Consult your doctor if you aren’t taking blood pressure medication. There are a lot of effective medications out there to help you manage blood pressure, so see your doctor if you aren’t taking anything, get a consult. It is imperative to take the medications following your doctor’s instructions. If you skip doses or don’t take them correctly, they may not be effective. Your doctor may prescribe:[21] X Trustworthy Source National Health Service (UK) Public healthcare system of the UK Go to source
- ACE inhibitors. ACE stands for Angiotensin-converting enzyme. These medications relax your blood vessels. It may give you a cough as a side effect.
- Calcium channel blockers. These medications widen your arteries. Ask your doctor about side effects and interactions.
- Diuretics. These medications reduce your salt levels by helping you urinate more often.
- Beta-blockers. These medications slow your heartbeat and make it less forceful. This is generally a last resort for when other medications and lifestyle changes have not been sufficient.
Foods and Exercises to Lower Blood Pressure
Expert Q&A
-
QuestionI only have a high blood pressure when I see the doctor; do I need to make all these changes?Janice Litza, MDDr. Litza is a Board Certified Family Medicine Physician based in Racine, Wisconsin. With over 25 years of educational and professional experience, she has extensive experience providing full-spectrum Family Medicine, including obstetrics, newborn care, and hospital medicine. She is currently the Residency Program Director for Family Medicine at Ascension. Dr. Litza received her MD from the University of Wisconsin-Madison School of Medicine and Public Health and has completed additional fellowship training in Integrative Medicine through the University of Arizona.
Board Certified Family Medicine PhysicianBoard Certified Family Medicine PhysicianExpert AnswerWe call that “White Coat” hypertension, and are realizing that your blood pressure is likely also going high in other stressful situations, and making healthy changes is important. Sometimes, if it gets very high, even for a short amount of time, it’s best to start daily medication to avoid long-term complications.
-
QuestionHow can I tell my blood pressure?Chris M. Matsko, MDDr. Chris M. Matsko is a retired physician based in Pittsburgh, Pennsylvania. With over 25 years of medical research experience, Dr. Matsko was awarded the Pittsburgh Cornell University Leadership Award for Excellence. He holds a BS in Nutritional Science from Cornell University and an MD from the Temple University School of Medicine in 2007. Dr. Matsko earned a Research Writing Certification from the American Medical Writers Association (AMWA) in 2016 and a Medical Writing & Editing Certification from the University of Chicago in 2017.
Family Medicine PhysicianFamily Medicine PhysicianExpert AnswerThe only way to tell your blood pressure is to have it measured with a sphygmomanometer. If you are having a hypertensive emergency you may have dizziness and CNS symptoms
Tips
-
Caffeine can cause short spikes in blood pressure, but unless you’re on the cusp of a hypertension crisis (in which case you need medical care ASAP), the occasional coffee or tea is probably fine. Ask your doctor to make sure it’s okay to consume caffeine.[22] X Trustworthy Source Mayo Clinic Educational website from one of the world's leading hospitals Go to sourceThanks
References
- ↑ http://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/dash-diet/art-20048456
- ↑ http://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/dash-diet/art-20048456
- ↑ http://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/dash-diet/art-20048456
- ↑ http://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/dash-diet/art-20048456
- ↑ http://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/dash-diet/art-20048456
- ↑ http://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/dash-diet/art-20048456
- ↑ https://www.hsph.harvard.edu/nutritionsource/what-should-you-eat/fats-and-cholesterol
- ↑ https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/dash-diet/art-20048456
- ↑ http://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/dash-diet/art-20048456
- ↑ https://www.heart.org/en/healthy-living/healthy-eating/eat-smart/sugar/sugar-101
- ↑ https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/in-depth/high-blood-pressure/art-20045206
- ↑ https://www.cdc.gov/physicalactivity/basics/adults/index.htm
- ↑ http://www.mayoclinic.org/diseases-conditions/high-blood-pressure/basics/risk-factors/con-20019580
- ↑ http://www.mayoclinic.org/diseases-conditions/high-blood-pressure/basics/lifestyle-home-remedies/con-20019580
- ↑ http://www.mayoclinic.org/healthy-lifestyle/quit-smoking/basics/quitsmoking-action-plan/hlv-20049487
- ↑ http://www.mayoclinic.org/diseases-conditions/high-blood-pressure/basics/causes/con-20019580
- ↑ https://www.heart.org/en/health-topics/high-blood-pressure/changes-you-can-make-to-manage-high-blood-pressure/managing-stress-to-control-high-blood-pressure
- ↑ https://doh.wa.gov/you-and-your-family/illness-and-disease-z/heart-disease/heart-attack/stroke-and-heart-attack-signs-and-symptoms-multiple-languages
- ↑ http://www.heart.org/HEARTORG/Conditions/HeartAttack/WarningSignsofaHeartAttack/Heart-Attack-Symptoms-in-Women_UCM_436448_Article.jsp
- ↑ https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/expert-answers/hypertensive-crisis/faq-20058491
- ↑ http://www.nhs.uk/Conditions/Blood-pressure-%28high%29/Pages/Treatment.aspx
- ↑ https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/expert-answers/blood-pressure/faq-20058543
About This Article
To lower your blood pressure, follow the DASH diet, which is short for Dietary Approaches to Stop Hypertension. Reduce your sodium intake to no more than 2,300 mg each day, since high sodium levels increase your blood pressure, and limit your fat intake to no more than 3 servings each day. In addition, you should eat a diet rich in whole grains, fruits and vegetables, low-fat dairy products, and lean proteins in moderation. These diet changes, along with 75-150 minutes of exercise each week, should help lower your blood pressure. Read on to learn tips from our medical reviewer about the connection between stress and your blood pressure!
Reader Success Stories
-
"The yoga and meditation things helped. Didn't know that you could eat grains, cheers for that."
```
</details>



```python
import trafilatura
from bs4 import BeautifulSoup 

url = "https://www.wikihow.com/Lower-Blood-Pressure"  
  
# Use function trafilatura.fetch_url() to fetch html content of the URL  
html_content = trafilatura.fetch_url(url)  
  
# parser html content
soup = BeautifulSoup(html_content, "html.parser")

other_languages = soup.find("div", attrs={"id": "other_languages"}).find_all("div", attrs={"class": "language_link"})

```



An example to construct zh-en paired data:

code: [crawl_wikihow_data.py](crawl_wikihow_data.py)
