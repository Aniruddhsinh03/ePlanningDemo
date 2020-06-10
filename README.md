# ePlanningDemo

This is a Scrapy project to scrape eplanning website and extract agent details from  http://eplanning.ie/.

This project is only meant for educational purposes.

## Selection 

Main Site


![Image of MainSite](https://github.com/Aniruddhsinh03/ePlanningDemo/blob/master/screemshots/1.jpg)

Country Url Selection


![Image of MainSite](https://github.com/Aniruddhsinh03/ePlanningDemo/blob/master/screemshots/2.jpg)

Select Received Application


![Image of ReceivedApplication](https://github.com/Aniruddhsinh03/ePlanningDemo/blob/master/screemshots/3.jpg)

Form Request Data


![Image of FormRequestData](https://github.com/Aniruddhsinh03/ePlanningDemo/blob/master/screemshots/4.jpg)

Application URL


![Image of MainSite](https://github.com/Aniruddhsinh03/ePlanningDemo/blob/master/screemshots/5.jpg)

New Page URL


![Image of MainSite](https://github.com/Aniruddhsinh03/ePlanningDemo/blob/master/screemshots/6.jpg)

Select Agent Button


![Image of MainSite](https://github.com/Aniruddhsinh03/ePlanningDemo/blob/master/screemshots/7.jpg)

Select Agent Data


![Image of MainSite](https://github.com/Aniruddhsinh03/ePlanningDemo/blob/master/screemshots/8.jpg)









## Extracted data

This project extracts Agent Data.
The extracted data looks like this sample:

     {
      "name": "  Sean Boyle Architects",
      "address": [
      "Unit 3, Second Floor",
      "Donohoe Building, Kennedy Centre",
      "Kennedy Road, Navan",
      "Co. Meath "
      ],
      "phone": "046 9023797 ",
      "fax": " ",
      "email": "info@boylearchitects.ie",
     "url": "http://www.eplanning.ie/MeathCC/AppFileRefDetails/aa200649/0"
     }


## Spiders

This project contains one spider and you can list them using the `list`
command:

    $ scrapy list
    eplanningSpider

Spider extract the data from ePlanning Site.




## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl eplanningSpider

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl eplanningSpider -o output.json
