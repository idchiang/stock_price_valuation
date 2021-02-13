import os
import platform
from datetime import date
from shutil import rmtree
import numpy as np
import pandas as pd
from src.make_derivations import derive_quant
from src.make_predictions import make_pred
from src.make_summary import make_sum

# Step 0: Set up the financial report file "X.csv"
#      Annual repot dir: ./data/financial_sheet/annual/
#      Annual repot template: ./data/financial_sheet/annual/hw1.csv

# Step 1: Set up company name "X" (corresponding to the report file name)
company = 'hw1'

# Step 2: Set up report mode (only 'annual' inplemented now)
mode = 'annual'

# Step 3: Change the baseline assumptions (optional)
#      ('const', X): set to value X
#      ('last', N): set to the value of the last period
#      ('avg', N): set to the average of previous N periods
baseline_assumptions = {
  'revenue_yoy_growth_rate': ('avg', 3),
  'gross_margin': ('avg', 4),
  'other_expenses': ('last', 1),
  'tax_rate': ('last', 1),
  'share_outstanding': ('last', 1),
  'pe_ratio': ('const', 20)
  }

# Step 4: Setting done. Please execute the pipeline.

print('#######################################################')
print('########            Pipeline starts            ########')
print('#######################################################')

# Definition and sanity check
mode = 'annual'  # only annal now
company = 'hw1' if not company else company
dir_root = os.getcwd()
dir_annual = dir_root + '/data/financial_sheet/annual/'
dir_quarterly = dir_root + '/data/financial_sheet/quarterly/'
dir_report = dir_root + '/results/' + company + '_' + mode + '_' + \
    date.today().strftime("%Y%m%d") + '/'
if platform.system() == 'Windows':
    dir_annual = dir_annual.replace('/', '\\')
    dir_quarterly = dir_quarterly.replace('/', '\\')

# Load report
if mode == 'annual':
    filepath = dir_annual + company + '.csv'
    assert os.path.isfile(filepath), 'Error: file ' + company + \
        '.csv' + ' does not exist.'
    df = pd.read_csv(filepath, comment='#')
else:
    assert False, 'Error: mode ' + mode + ' not implemented yet.'
# Load report -- Derive quantities and sort the columns
s = df.iloc[-1].copy()
for key in s.keys():
    if key == 'year':
        s[key] += 1
    else:
        s[key] = np.nan
df = df.append(s, ignore_index=True)
df = derive_quant(df)

# Print pipeline run info
print('\n' +
      '# Company name:', company, '\n' +
      '# Report mode:', mode, '\n' +
      '# Report file:', filepath, '\n')

# Make predictions
print('...Making predictions')
df_pred_base, assumptions_base = \
    make_pred(df, init_row_idx=4, pred_mode='baseline')
df_pred_opt, assumptions_opt = \
    make_pred(df, init_row_idx=4, pred_mode='optimize')

# Evaluate results. Plots.
print('...Generating reports')
if os.path.isdir(dir_report):
    rmtree(dir_report)
os.mkdir(dir_report)
df.to_csv(dir_report + 'data_true.csv')
df_pred_base.to_csv(dir_report + 'prediction_baseline.csv')
df_pred_opt.to_csv(dir_report + 'prediction_optimized.csv')
assumptions_base.to_csv(dir_report + 'assumptions_baseline.csv')
assumptions_opt.to_csv(dir_report + 'assumptions_optimized.csv')
make_sum(df, df_pred_base, df_pred_opt, dir_report)

print('\n' +
      '# Results saved at', dir_report)

# Closing
print('\n' +
      '# Pipeline executed successfully')
