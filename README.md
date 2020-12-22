# Machine-Learning-for-Statistical-Arbitrage-Using-News-Media-to-Predict-Currency-Exchange-Rates

<h3>Abstract</h3>
We explore the application of Machine Learning for predicting bilateral Foreign Exchange Rates utilizing the sentiment from news articles and prominent macroeconomic indicators. Using a random forest regressor, we were able to predict foreign exchange rates with an average error of 7.8%. In addition, news articles were an important feature in the majority of these random forest regressions. The novelty of our project relies on utilizing the Latent Dirichlet Allocation to cluster news articles into topics and further understand the semantic meanings behind each topic and applying it to foreign exchange rates.

<h3>Task</h3>
We explore the application of Machine Learning for predicting bilateral Foreign Exchange Rates utilizing the sentiment from news articles and prominent macroeconomic indicators.

<h3>Solution</h3>
<ul>
  <li>Use news article sentiment to predict FER.</li>
  <li>Collect and Cluster news articles from past 40 years.</li>
  <li>Used proportion of articles per year falling in each cluster as an indication of sentiment to predict the next year’s exchange rate.</li>
</ul>

<h3>Source</h3>
<a href="https://developer.nytimes.com">1.New York Times API for Articles</a><br>
<a href="https://data.oecd.org/conversion/purchasing-power-parities-ppp.htm">2.PPP - Purchasing Power Parities Dataset</a><br>
<a href="https://data.oecd.org/price/inflation-cpi.htm">3.Inflation Rates data</a><br>
<a href="https://data.worldbank.org/indicator/pa.nus.fcrf">4.Foreign Exchange Rates</a><br>
<a href="https://data.oecd.org/gdp/gross-domestic-product-gdp.htm">5.GDP - Gross Domestic Product</a><br>

<h3>Steps of Proposed System</h3>
<ol>
  <li>Information Gathering</li>
  <li>Planning</li>
     <ul>
       <li>Exploratory Data Analysis.</li>
       <li>Modelling.</li>
       <li>Performance of Model.</li>
       <li>Model Comparison.</li>
       <li>Feature Importance.</li>
       <li>Dicussion</li>
       <li>Conclusion & Future Enhancement</li>
     </ul>
  <li>Design</li>
  <li>Implementation</li>
  <li>Results</li>
  <li>Deployment</li>
</ol>

<h3>Design(Workflow)</h3>
<img src="https://github.com/Technocolabs100/Machine-Learning-for-Statistical-Arbitrage-Using-News-Media-to-Predict-Currency-Exchange-Rates/blob/main/models/Workflow-Design.jpg" >

<h3>Result</h3>
<img src="https://github.com/Technocolabs100/Machine-Learning-for-Statistical-Arbitrage-Using-News-Media-to-Predict-Currency-Exchange-Rates/blob/main/Output%20Images/Avg-prediction-error.jpg"><br>
<img src="https://github.com/Technocolabs100/Machine-Learning-for-Statistical-Arbitrage-Using-News-Media-to-Predict-Currency-Exchange-Rates/blob/main/Output%20Images/Feature-Importance.jpg"><br>
<img src="https://github.com/Technocolabs100/Machine-Learning-for-Statistical-Arbitrage-Using-News-Media-to-Predict-Currency-Exchange-Rates/blob/main/Output%20Images/Model-error.jpg">

<h3><a href="https://currencyrates-final-ummeathiya.herokuapp.com/">Deployment Link</a></h3>

![alt text](https://github.com/Technocolabs100/Machine-Learning-for-Statistical-Arbitrage-Using-News-Media-to-Predict-Currency-Exchange-Rates/blob/main/Deployment/screencapture-currencyrates-final-ummeathiya-herokuapp-FER-2020-12-22-16_40_51.jpg?raw=true)
