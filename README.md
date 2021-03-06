## Air Quality Prediction of Delhi
![Python 3.6](https://img.shields.io/badge/Python-3.6-brightgreen.svg)

**Link : https://air-quality-predictor.herokuapp.com/**

## Table of Content
 * [Demo](#demo)
 * [Motivation](#motivation)
 * [Data Collection](#data-collection)
 * [EDA and Feature Engg](#eda-and-feature-engg)
 * [Model Building](#model-building)
 * [Deployment](#deployment)
 * [Technologies Used](#technologies-used)
 * [To Do](#to-do)
 * [License](#license)

## Demo

## Motivation
Many website available on the internet does not predict the future air quality index given current date AQI the aim of the app is to predict AQI of locality based on certain factors. Air pollution can cause both short term and long term effects on health and many people are concerned about pollution in the air that they breathe.

## Data Collection
I couldn't find any relevant dataset for this purpose so I decided to scrape the climate data from  **[this website](https://waqi.info/)** using **Selenium and Beautiful Soup** which were really helpful. You can find the code for scraping **[here](https://github.com/nakul1010/Air-Quality-Index/tree/master/scraping)** and to combine all data **[here](https://github.com/nakul1010/Air-Quality-Index/blob/master/scraping/Extract_combine.py)**.

## EDA and Feature Engg
![png](readme_resources/air_pollutants_and_amount_in_atmosphere.png)
* From the pie chart it is clear that all most 50% of air pollutant is from PM2.5(Particulate Matter) more info can be found out **[here](https://en.wikipedia.org/wiki/Particulates)**. So the dependent feature was consider as PM2.5 . 
* Valuable insights such as **air quality deterioration during Winter seasons** and how much effective was **odd even formula** by Delhi Government can be found out with the help of charts in this **[folder](https://github.com/nakul1010/Air-Quality-Index/tree/master/readme_resources)**.

![png](readme_resources/feature_score.png)
* With the help of **correlation matrix & ExtraTreesRegressor algorithm** important and correlated features were able to identify.
* As in the pie chart SLP(Atmospheric pressure at sea level) is the most important feature for air quality index.

## Model Building
<table>
    <tr>
        <td>Sr no.</td>
        <td>Algorithm</td>
        <td>RMSE</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Linear Regression</td>
        <td>56.79</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Decision Tree</td>
        <td>56.31</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Random Forest</td>
        <td>41.53</td>
    </tr>
    <tr bgcolor=#123456>
        <td>4</td>
        <td>XGBoost</td>
        <td>36.70</td>
    </tr>
</table>

**The Jupyter Notebooks of Algorithms can be found out [here](https://github.com/nakul1010/Air-Quality-Index/tree/master/models)**

## Deployment
* The app was deployed in heroku which is **Platform as a Service(PaaS)**.
* Set the environment variable on Heroku as mentioned in _STEP 1_ in the __Run__ section. [[Reference](https://devcenter.heroku.com/articles/config-vars)]
 ![](https://i.imgur.com/TmSNhYG.png)

* Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
├── models 
│   ├── DecisisionTreeRegressor.ipynb
│   ├── LinearRegression.ipynb
│   ├── RandomForestRegressor.ipynb
│   └── Xg_Boost.ipynb
├── readme_resources
├── static
│   ├── style.css
│   ├── logos    
├── templates
│   ├── index.html
│   ├── result.html   
├── weights 
│   ├── DecisisionTreeRegressor.pkl
│   ├── LinearRegression.pkl
│   ├── RandomForestRegressor.pkl
│   └── Xg_Boost.pkl
├── LICENSE
├── Procfile
├── README.md
├── app.py
├── requirements.txt
```

## Technologies Used
[<img target="_blank" src="https://twilio-cms-prod.s3.amazonaws.com/images/scikit-learn.width-808.png" width=200>](https://scikit-learn.org/stable/)  [<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org)
[<img target="_blank" src="https://seekvectorlogo.net/wp-content/uploads/2018/12/heroku-vector-logo.png" width=200>](https://devcenter.heroku.com/categories/reference)[<img target="_blank" src="https://funthon.files.wordpress.com/2017/05/bs.png?w=772" width=200>](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## To Do
* Add more cities like Mumbai,Pune and Bengaluru where Air Pollution is a taboo.
* Add a vizualization chart to display the predictions.
* Convert the app to run without any internet connection, i.e. PWA.

## License
[![Apache license](https://img.shields.io/badge/license-apache-blue?style=for-the-badge&logo=appveyor)](http://www.apache.org/licenses/LICENSE-2.0e)

Copyright 2020 Nakul Amate

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

