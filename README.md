# Stock Web Scraper
## Description
Scrapes list of stocks, scrapes their details from Yahoo finance (if applicable) and outputs as a CSV
## Requirements
<ul>
  <li>Requests</li>
  <li>Beautiful Soup 4</li>
  <li>Pandas</li>
</ul>

## Limitations
Some stocks are skipped as they do not exist on Yahoo finance, could look at using other data pools as well and comparing results.
For everyday use by other investment staff, csv files may be difficult to use, importing this file to excel and then passing it on would be a better alternative.