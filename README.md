## Inspiration
Cassava leaves are the **2nd largest carbohydrate source in Africa**, and heavily dependant on as a security crop by African farmers. But there is a problem! Numerous diseases are spreading from crop to crop, costing farmers up to **$1 billion every year in wasted crops** due to disease. This ultimately leads to increased poverty rates and people going hungry.

## What it does
But we have created a solution to tackle this problem. CASSAVEA is a web app created to easily detect these diseases and helps the farmer **limit the spread** while providing helpful feedback on how they can combat this. The process is quick and easy, simply choose your crop, and take or upload a picture and **instantly receive statistics for the image**. If you want a more detailed experience, CASSAVEA also returns the probabilities of each disease for the plant.

## How we built it
First, we tackled the core of the project which was the **machine learning algorithm**. We knew this would take a long time to train so we made sure to complete it first. This algorithm was created with **TensorFlow, Pandas and MatPlotLib**, using a dataset collected from Kaggle. Before going ahead with the model we also decided to use data analysis with **R** to make sure it was a fit for our project. We then decided to each work on our specialities, creating the prototype with **Figma initially**, then turning this prototype to reality with **HTML, CSS and advanced JavaScript**. For the back-end, we decided to use **Flask**, as it was easy to send and receive data from the model. The web app was deployed using **Docker** and **AWS**, as we received credits to use.

## Challenges we ran into
The main challenge we ran into was the machine learning algorithm, as we knew it would take a **long time to train** in order to be effective. How we managed to solve this problem was by using **data analysis** with R to review and graph the data, and by testing various sizes of datasets we were able to predict the optimal number of epochs so that the model would not underfit nor overfit.

Another challenge we came across was connecting all these stages together, especially sending and receiving data from the model. We solved this problem by creating a **REST API** so that we can limit the time between sending and receiving the model, so the user has a faster time to receive the data.

## Accomplishments that I'm proud of
As a team, we knew coordination would be a challenge as we are an **international team** from 3 different continents and hence, **3 extreme different time zones**. We stepped up to the challenge and made it work, by delegating each person with tasks of equal work, we managed to lower the workload all while keeping **good communication** all while being up to 7 hours apart. Another accomplishment was the model accuracy, we trained our model to 80% accuracy, which for our large dataset and multiple classifications, was quite a good result. Especially as we only had a fixed amount of time for the model to train.

## What we learned
This was also our **first time as a team using Figma**, and we quickly adapted to it and learned in a short time period. We also improved our understanding of Docker. Only one person in the team had any experience with using **Docker and AWS**, but we all made it a priority to learn. 

## What's next for CASSAVEA
We realise that the scope of this technology is much larger than just cassava plants. We look to **implement more plants in the future**, to help minimise hunger and **fight poverty**. We also understand that not all farmers in this situation have no access to the internet and a mobile phone. This could be an external factor out of our control but we are thinking of ways to solve this. It is also clear that gaining users in this field of technology would be difficult, but by **working with charities** and other organisations, we think that this can reach the right people and ultimately help save lives!
