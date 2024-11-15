from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """  Elon Musk, the world’s richest person, will be taking on an official role to try to help President-elect Donald Trump make government more efficient. It will add yet another responsibility to an ever-growing to-do list for the increasingly distracted CEO and business leader.

Musk, chief executive of Tesla and SpaceX, owner of X and CEO of other ventures, including Neuralink, xAI and the Boring Company, is already a busy guy. Even if the Trump job is just a side hustle (the announcement said it’s kind of an advisory gig), it’s one more thing for Musk to do that isn’t running the world’s most valuable car company.

But here’s the thing: Musk’s recent distractions may not ultimately matter for his (many) businesses. And there’s actually a strong case to be made that they’re paying off for investors.

Tesla, Musk’s most valuable company, in recent years has struggled to maintain its dominance of the electric vehicle market. Sales slowed as Tesla faces increased competition on both the higher end and lower end of the market, and Tesla was recently overtaken by Chinese rival BYD for EV sales. Meanwhile, Tesla has faced numerous federal investigations over its self-driving technology, and the company’s long-promised autonomous “Cybercab” announcement last month included a number of pie-in-the-sky promises that sounded like a lot of fluff – even coming from notorious over-promiser Musk.

But, for Tesla investors, that’s all been in the rear view mirror over the past week. Tesla’s (TSLA) stock has surged 31% since Election Day, because investors believe that Musk’s influence in Trump’s government will usher in an era of deregulation – particularly in key industries and technologies that could benefit the company.

“The benefits of Musk’s involvement in Trump’s government outweigh the negatives,” said Dan Ives, an analyst at Wedbush Securities. “Tesla investors want Musk more involved in the Trump White House – not less – because of his influence on advancing AI, China tariffs and fast-tracking autonomous driving regulations.”

Musk, Tesla’s largest individual shareholder, has personally reaped the rewards of the stock’s surge. He’s $55 billion richer today than he was on Election Day, according to Bloomberg’s Billionaires Index.

Trump has stated his disdain for electric vehicles, but that ultimately may not matter much for Tesla – in fact, eliminating tax credits may help Tesla by reducing competition that relies more heavily on them to boost sales demand. Also, multiple federal investigations of Tesla’s self-driving technology could vanish, Ives said.

Meanwhile, SpaceX continues to keep a leg (and entire astronauts) up on the competition, and an era of deregulation under Trump could similarly help the company. SpaceX’s valuation reportedly topped an astounding $200 billion earlier this year, according to Bloomberg, and after a Boeing snafu with its Starliner, SpaceX had to come rescue astronauts stranded by its crippled rival. And the company is now catching rocket boosters out of the air with “chopsticks.”

X, by contrast, has clearly struggled under Musk – it has lost 80% of its value, according to Fidelity, as advertisers flee the social network that has become a free-for-all for hate speech and conspiracy theories. But that’s not because Musk has been distracted – if anything, participation on X has become Musk’s primary focus, with constant posts espousing his increasingly right-wing views.

But, ironically, Musk’s controversial – and expensive – $44 billion purchase of then-Twitter (now X) in 2022 set in motion his descent into the MAGA rabbit hole – and ascent in Trumpworld that propelled him to a role in which he has the next president’s ear. And that has given Tesla a valuation north of $1 trillion. It’s one of just nine companies on the stock market with a 13-figure valuation.

Ives called Musk’s path a “Twilight Zone jigsaw puzzle.”

“It’s a ride that feels like it’s just starting,” Ives noted.

Of course, that’s if Trump and Musk remain on good terms. Trump has a long list of former allies who fell out of favor for one reason or another. And no matter how much power and influence Musk could yield, Trump will hold the ultimate trump card: He’ll be president. 
"""
print(summarizer(ARTICLE, max_length=230, min_length=30, do_sample=False))
