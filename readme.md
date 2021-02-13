## Calculator for Stock price valuation

---

### Goal:
* Input historical financial reports, and output the expected stock price
* Automatically choose the optimized prediction method among the implemented ones
* Save predicted data and plots

### Constraints:
* Currently, only annual report mode is supported
* Need at least 4 previous years to make predictions

### Steps:
1. Set up the financial report file at `/data/financial_sheet/annual/`
   * A template is available at `/data/financial_sheet/annual/hw1.csv`

2. Edit `/run_valuation_pipeline.py`
   1. Set up `company` variable corresponding to the report file name
   2. Set up report `mode` (only 'annual' inplemented now)
   3. (Optional) Change the baseline assumptions

3. Execute `/run_valuation_pipeline.py`

---

### Future features:
* Sanity check for the input table formats
* Quarterly report mode
* Add linear regression into prediction methods
* Load uncertainties of stock prices
  * Also, use Monte-Carlo method to generate the variance of the predicted price
  * Scorethe prediction by the range instead of a single data point
* Web crawler: auto-get financial reports
* Add other valuation models
