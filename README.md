# Shop Buddy
DeltaHacks 9 Project

by Ben Sun and Sheridan Fong

Technologies: Python, Selenium, blockchain, CSS, HTML, Javascript, Twilio

# Inspiration
Being Asian-Canadian, we had parents who had to immigrate to Canada. As newcomers, adjusting to a new way of life was scary and difficult. Our parents had very few physical possessions and assets, meaning they had to buy everything from winter clothes to pots and pans. Ensuring we didn't miss any sales to maximize savings made a HUGE difference. That's why we created Shop Buddy - an easy-to-use and convenient tool for people to keep an eye out for opportunities to save money without needing to monitor constantly. This means that people can focus on their other tasks AND know when to get their shopping done.

# What it does
Shop Buddy allows users to input links to products they are interested in and what strike price they want to wait for. When the price hits their desired price point, Shop Buddy will send a text to the user's cell phone, notifying them of the price point. Furthermore, to save even MORE time, users can directly purchase the product by simply replying to the text message alert. Since security and transparency are a huge deal these days - especially with retail and e-commerce - we implemented a blockchain where all approved transactions are recorded for full transparency and security.

# How we built it
The user submission form is built on a website using HTML/CSS/Javascript. All forms submissions are sent through requests to the Python Backend served via a Flask REST API. When a new alert is submitted via the user, the user is messaged via SMS using the Twilio API. If the user replies to a notification on their phone to instantly purchase the product, the transaction is performed with the Python Chrome Web Driver and then the transaction is recorded on the Shop Buddy Blockchain.

# Challenges we ran into
The major challenge we faced was connecting the backend to the frontend. We worked with the mentors to help us submit POST and GET requests. Another challenge was testing. Websites have automatic bot detection, so when we tested our code to check prices and purchase items, we were warned by several sites that bots were detected. To overcome this challenge, we coded mock online retailer webpages, that would allow us to test our code.

# Accomplishments that we're proud of
We're proud of completing this project in a group of 2! We both expanded our skillsets to complete Shop Buddy. We are proud of our idea as we believe it can help people be more productive and help newcomers to Canada.

# What we learned
We wanted to learn something new, and we both did. Sheridan learned how to code in JavaScript and do Post and Get requests, and Ben learned how to use Blockchain and code a bot to buy items. Overall, we are very happy to see this project come together.

# What's next for Shop Buddy
Currently, our product can only be used to purchase items from select retailers. We plan to expand our retail customer list as we get used to working with different websites. Shop Buddy's goal is to help those in need and those who want to be more productive. We would focus on companies catering to a wider audience range to meet these goals.
