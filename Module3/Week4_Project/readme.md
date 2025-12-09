# Project Week! 
This is your chance to shine - update the LLM and build new models, then share your results to your GitHub repo.

Right now, I have prepared for you all a souped-up version of the basics `/myscrapers` repo. 

That version of the code scrapes craigslist, uses RegEx and LLMs (Gemini) to the to ETL (we added more fields like `transmission` with LLMs), and then we fit a basic DT model to predict car prices. The results were originally stored on GCS, but now we use GitHub Actions (`sync-data`) to go grab those preds and bring them back for the World to see.

I want you to take things a bit further now - 
* Keep all the scraping logic FIXED for now... we will all use the same dataset...
* Enhance the ETL by the LLM to account for more variables (`color`, `city`, `state`, `zip code`)
* Use hyperparameter tuning (grid search or Optuna or autoML) to fit your model on the previous day's data
* Send the predictions to GitHub Actions (already done)
* Send the permutation importance (all features) and PDP for top 3 features to GitHub (similar to how you are sending .csv) files
* Write an .ipynb that documents how well your model is doing... as the dataset grows, your model should get better and better... trend the results and make a dashboard to show 1) how good your model is (MAE, MAPE, RMSE, BIAS) 2) what's most important (permutation importance) and 3) how is the model using the data, and are the patterns changing over time. 
