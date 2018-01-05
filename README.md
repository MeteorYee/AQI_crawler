# AQI_crawler
A visualized tool for Chinese cities AQI

Is the haze realy severe in China? This tool will help you to see it. All the data is from [here](https://www.aqistudy.cn/historydata/).

## Beijing
<p align="center"><img src="https://github.com/MeteorYee/AQI_crawler/blob/master/pics/bj_1517.png" /><br>Fig 1. Beijing AQI, 2015~2017</p>

<p align="center"><img src="https://github.com/MeteorYee/AQI_crawler/blob/master/pics/bj_17.png" /><br>Fig 2. Beijing AQI, 2017</p>

Throughout the past 3 years, as the figure 1 shows above, Beijing's air condition was being improved gradually. In 2017, the progress is more evident as the figure 2 shows. Then, what about your hometown?

## Usage
### Crawl a city's data
>*python AQISpider.py --city_para %E5%8C%97%E4%BA%AC --city_alias bj --years 2015 2016 2017*<br>

Where the '%E5%8C%97%E4%BA%AC' the parameter from the website link: https://www.aqistudy.cn/historydata/daydata.php?city=%E5%8C%97%E4%BA%AC, which means Beijing. (Note: You may see it as Chinese characters in your browser, but when you copy the link and paste to your editor, you will see this parameter.)

### Visualize it
>*python DataPlot.py --city_name Beijing --city_alias cz --years 2015 2016 2017*<br>

You will see a curve chart like figure 1 and 2.
