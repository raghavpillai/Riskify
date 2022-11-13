## Inspiration

As Chinese military general Sun Tzu's famously said: "Every battle is won before it is fought." This phrase implies that planning and strategy win wars. Similarly, successful traders commonly quote the phrase: "Plan the trade and trade the plan." Just like in war, risk planning and assessment can often mean the difference between success and failure. This was the foundation behind Riskify, which allows for intricate, yet accessible risk assessment for portfolios. 


## What it does

Riskify takes into account various different factors, including several different types of portfolio categories, economic conditions, regulation and several other factors. We either build a new portfolio with regard to the user's designated risk tolerance, or show them information on their pre-existing portfolio. This allows users to see their possible returns on higher risk levels, while also being able to see their more safe estimates in low risk assessments.

We calculate the user's return using an arithmetic average rate of return calculation, as well as taking into account inflation and market factors to determine an estimate of their returns in the future. We also simulate future portfolio category return rates using our Monte Carlo simulation, allowing for a fine estimation of growth over an extended period of time. 

Risk analysis is done using historical data for several different portfolio categories, and we built Monte Carlo simulation to determine probability of risk in the user's portfolio.  We pair this with a Conditional value-at-risk (CVaR) calculation to get an accurate risk assessment for the user's portfolio. 


## How we built it

Riskify's frontend is built using React. The backend is written in Python, utilizing Flask for API delivery. We used numpy and pandas to write our Monte Carlo simulation.
