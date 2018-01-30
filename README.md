# CORDIS-DB-EU-Projects-Scraper

This project aims to download information from the news section of [CORDIS DB](http://cordis.europa.eu/home_en.html).

### Goals

* Conduct statistical/ling analyses
* Data-Journalism

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

First clone ```git clone https://github.com/poltys/CORDIS-DB-News-Scraper```

You will have to install Scrapy (and needed dependencies) in order to use it.

You can run ```sh install-dependencies.sh``` or ```pip install --user Scrapy```

### How to use

Run ```scrapy crawl basic -o "filename"."extension"```.

If you want to download information about a specific project you will have to change the following ```start_urls = ['http://cordis.europa.eu/news/rcn/%d_en.html' %(n) for n in range(128792, 128793)]``` in ```spiders/basic_spider.py```.

### Data Sample

Scrapy gives you the opportunity to download your data in different formats: csv, jl, json, xml.
```
[{
  "Article": ["A simple kitchen stable that is cheap, accessible and easy to use has the potential to save lives, as a recent study has demonstrated. Labour fails when contractions are not strong enough and treatment with oxytocin is usually the next step. If that doesn\u2019t work then a Caesarean section can be the solution.", "But in rural environments in developing countries these may not be options and if a C-section can be carried out at all, there may be complications. The World Health Organisation explains that almost all maternal deaths (99 %) occur in developing countries and that the risk of maternal mortality is highest for adolescent girls under 15 years old. Complications in pregnancy and childbirth is a leading cause of death among adolescent girls in developing countries.", "A simple sachet of sodium bicarbonate from the corner shop could help women give birth naturally", "A study just conducted, involving 200 women, found that, when dissolved in water, bicarbonate of sodium enables between 17 and 20 % of women having slow or difficult labours to give birth naturally, without harming their babies. ", "Professor Susan Wray, from the University of Liverpool, and a team of researchers at the Karolinska Institute in Sweden, gave bicarbonate of soda to 100 women in labour experiencing difficulties, as well as oxytocin. Another 100 women were treated with just oxytocin. The results, published in the journal of Maternal-Fetal & Neonatal Medicine, found those who had bicarbonate of soda increased their chances of a vaginal delivery.", "\u2018The study was conducted with clinical colleagues in Sweden, and there at the corner shop you can buy this as an antacid, it really is low rent,\u2019 said Prof Wray.", "Why sodium bicarb?", " on BBC Radio 4\u2019s Today Programme, Prof Wray explained that studies at the University of Liverpool had found that the levels of acidity in the blood surrounding the uterus of women suffering a failure to progress in labour was significantly higher than any other group. ", "Prof Wray and her team hypothesised that if they could neutralise that acid in these women, that would help them to have a normal, spontaneous vaginal delivery and avoid the surgery. Without knowing which group they were in, one group received oxytocin alone, while the other had bicarbonate of sodium to in the hope of neutralising the acid in their uterus, then oxytocin one hour later.", "Describing the outcome as \u2018amazing\u2019, Professor Wray added, \u2018We were able to significantly increase the number of women having a spontaneous delivery, avoiding the emergency Caesarean section. Not by just a few percent, but by around 17-20 %.\u2019", "She stressed that the study was a small, randomised controlled study. \u2018But nevertheless we had 100 women in each of the two groups of our study and that was sufficient to rule out confounding factors like differences in BMI.\u2019 ", "A simple solution to an urgent problem could be on the way ", "If the work they carried out with the cohort of 200 is replicable, the researchers could have proven a way to reduce maternal mortality and suffering using a very cheap, shop floor medication and kitchen cabinet staple.  The team are really keen to replicate the results in more centres, but what Prof Wray is really looking forward to doing is getting one branch of the study up and running in sub-Saharan Africa. Liverpool has good links with hospitals in Uganda and Malawi, for example. ", "\u2018In those low resource settings I\u2019m sorry to say that women still die in large numbers in childbirth and this failure to progress is one of the reasons. So if those women could have this as a treatment, avoid surgery which, in any case may not be available to them or when it is, it\u2019s not without significant risk, that would be just wonderful. Because you don\u2019t need to keep this in the fridge, don\u2019t need electricity\u2026 it\u2019s so exciting.\u2019"],
  "Teaser": ["Lack of access to a caesarean section, or complications arising from one, accounts for many deaths in developing countries, but now a team of scientists has identified that a simple drink of bicarbonate of soda could make all the difference."],
  "Countries": ["United Kingdom"],
  "Title": ["Trending Science: Bicarbonate of soda could spare women in developing countries the need and risk of a caesarean section"]
}]
```

## TODO

* Update ```install-dependencies.sh```
* Clean ```basic_spider.py```
* Add Cron jobs
* Add pipelines

## Author

* **Simon Hardy** - *Initial work* - [poltys](https://github.com/poltys)

## License

This project is licensed under the MIT [License](LICENSE)
