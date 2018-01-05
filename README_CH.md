# AQI_crawler
一个对于中国城市 AQI（空气质量指数）的可视化工具

中国的雾霾真的很严重吗？这个工具会帮你看到。所有的数据来源于[这里](https://www.aqistudy.cn/historydata/)。

## 北京
<p align="center"><img src="https://github.com/MeteorYee/AQI_crawler/blob/master/pics/bj_1517.png" /><br>Fig 1. Beijing AQI, 2015~2017</p>

<p align="center"><img src="https://github.com/MeteorYee/AQI_crawler/blob/master/pics/bj_17.png" /><br>Fig 2. Beijing AQI, 2017</p>

在过去的三年中，如图 1 所示， 北京的空气质量缓步提升。在2017年，进步较为明显，如图 2. 那么，你的家乡情况如何呢？
## 使用
### 爬取一个城市的 AQI 数据
>*python AQISpider.py --city_para %E5%8C%97%E4%BA%AC --city_alias bj --years 2015 2016 2017*<br>

在这里 “%E5%8C%97%E4%BA%AC” 指的是网站链接中的参数: https://www.aqistudy.cn/historydata/daydata.php?city=%E5%8C%97%E4%BA%AC, 该参数指的是 北京。（注意: 在浏览器里可能会看到汉字，但一旦将链接复制粘贴下来，就会是参数的形式。）

### 可视化
>*python DataPlot.py --city_name Beijing --city_alias bj --years 2015 2016 2017*<br>

你会看到像图 1 和 2 的图表。
