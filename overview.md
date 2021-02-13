**Stock price Calculator**

---

Goal:
* Input previous financial reports, and output the expected stock price

Constraints:
1. Need at least 4 previous years

Current Tasks:
* Petia's plot: matplotlib can plot text beside the plot! combine text & figure together https://stackoverflow.com/questions/42435446/how-to-put-text-outside-python-plots
Karl's BEAST code https://github.com/BEAST-Fitting/beast/blob/master/beast/plotting/plot_indiv_fit.py
* Report
 * A dir for saving reports.
  * subdir name: company + date
 * Plot: selected quantities vs. year
 * three data: [true, base, opt]
 * label RMSE
 * label opt models
 * Save both predicted dfs
 * Print output directory
* For HW: generate a table for [true, base, opt] for 2019
* Back to notion: build a github repository; write the (notion) report for submission.

---

Future improvements:
* Check input table formats

Future features:
* Quarterly
* Regression (more like quarterly)
* Uncertainties and Monte-Carlo
* Scoring by price range
* Web crawler: auto-update financial repotrs
* Execute all
* Add other valuation models