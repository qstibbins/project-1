---
From TikTok to Top Charts
---
Analyzing its Influence on Spotify & YouTube Trends

## Introduction
##### TikTok has become a major force in shaping modern culture. Songs that gain traction on the platform can experience explosive popularity. TikTok’s algorithm-driven nature allows snippets of songs to spread rapidly. This cycle has made TikTok a key player in music discovery, with many artists using the platform to reach wider audiences. 
##### Given its impact, we wanted to explore whether TikTok’s influence translates into true streaming success. Does a song’s popularity on TikTok lead to proportional growth on Spotify or Youtube, or do viral moments fade without long-term impact? To answer this question, we analyzed data across these platforms, comparing TikTok engagement with streaming performance to determine whether going viral truly drives success.
## Data Overview (Merge and Clean)
##### Step 1: File Preparation - Converted the original Excel file to a CSV format for easier processing.
##### Step 2: Selecting Relevant Data - Chose only the necessary columns for our analysis and renamed columns for clarity and easy reference.
##### Step 3: Handling Missing Data - Counted the number of rows before cleaning and removed rows containing NaN (missing values), and then recounted to ensure data integrity.
##### Step 4: Data Type Verification & Conversion - Checked data types to confirm compatibility for analysis. Converted numerical columns (Spotify streams & TikTok views) to numeric format.
## Analysis of All Data
##### Typically when making a marketing budget or campaign, the goal is to aim for the top spots in the charts for the most visibility and return on investment. This means it is important to understand the overall market for a particular platform, but more importantly understand top chart trends for the platform before investing. When we initially looked at the data, we were under the assumption that TikTok would be leading the trends in what songs became popular, but as we reviewed the data, we saw that other platforms were more predictive. Starting with Spotify data, we see here that using TikTok Likes VS All Time Rank, TikTok’s correlation was opposite to predictive, whereas flipping the control to Spotify All Time Rank shows a stronger and more evenly distributed trend. 
![image 8](https://github.com/user-attachments/assets/26a90ff2-520e-4c9b-9096-e37095890459)
## Weak Correlation Between TikTok and Streaming Success
##### The scatterplots analyzing the relationship between TikTok engagement (likes and views) and streaming performance (on Spotify and YouTube) show an extremely weak correlation across all comparisons. Each linear regression line has a near-zero rate of change, indicating that TikTok engagement has little to no direct impact on streaming success.
![image 3](https://github.com/user-attachments/assets/67da8da0-a606-4f25-975d-c3c38d8f1ac7)
## Data Distribution and Trends
##### Across all scatterplots, there is a clear concentration of data points near the origin (0,0), where both TikTok engagement and streaming metrics are relatively low. This suggests that many songs with low TikTok views also have low Spotify streams. However, some data points are scattered along the Spotify stream axis, demonstrating that certain songs can achieve high streaming numbers despite low TikTok engagement.
![image 4](https://github.com/user-attachments/assets/0583d735-9466-4139-93e9-8f4a961b6516)
## Switching the Control: Spotify as the Baseline
##### With Spotify as the control, the relationship between streams and TikTok views presents a different picture compared to using TikTok as the baseline. The scatterplots show a slight upward trend, indicating that as Spotify streams increase, TikTok views also tend to rise. However, the r² value remains bel![image 8](https://github.com/user-attachments/assets/dd1157e6-3a20-4c0b-a752-84c498b74ff6)
ow 0.1, suggesting a weak correlation. This means that a song’s success on Spotify does not strongly predict its virality on TikTok.![image 8](https://github.com/user-attachments/assets/ff4b0026-75e6-4ba2-af91-c56edfa675ec)

#### Differences in Data Spread
##### A key difference emerges in the distribution of data. When TikTok was the control, data points were more concentrated, showing that TikTok hits experienced varying levels of success on Spotify. Now, with Spotify as the control, TikTok views display a much wider spread. While some songs perform well on both platforms, the relationship is inconsistent, highlighting that streaming success does not guarantee TikTok virality.
#### Challenging Assumptions
##### Overall, this new scatterplot challenges the assumption that TikTok is the primary driver of Spotify success. A song can thrive on Spotify without needing to go viral on TikTok, suggesting that long-term streaming performance may be influenced by other factors beyond TikTok trends.
![image 5](https://github.com/user-attachments/assets/009d597d-cc5a-4121-84d3-6ff08fa2446a)
## Comparing Top 10 Rankings
##### The percentage bar graphs reveal a consistent trend: a song’s popularity on TikTok does not always translate to proportional success on Spotify. For instance, a song ranked #8 on TikTok reaching #1 on Spotify suggests that virality on TikTok does not guarantee streaming dominance. This highlights how some songs thrive within TikTok trends but may not have lasting appeal for full-length listening, while others achieve streaming success without widespread TikTok engagement.
![image 6](https://github.com/user-attachments/assets/6fa54bad-d49b-40d2-88cc-26bc3405db1b)
### TikTok’s Unpredictable Virality
##### In contrast, TikTok engagement is far more unpredictable, with certain songs experiencing sharp spikes in views. This suggests that TikTok favors bursts of virality driven by trends, rather than the gradual, consistent success seen on Spotify.
## Analysis of heatmaps
#### Correlation Between Platforms
##### Strong correlations exist between *YouTube Views*, *Spotify Streams*, and *Playlist Reach*, suggesting songs that perform well on one platform tend to perform well on others.
##### TikTok Likes have *weak* or *negative correlations* with streaming and playlist metrics, **suggesting TikTok popularity doesn’t always translate into high Spotify or YouTube engagement**.
#### Platform-Specific Trends
##### In smaller datasets (Top-10, Top-25), *YouTube* and *Spotify* metrics show very high correlations, but as the dataset expands (Top-500), these correlations weaken, implying that mainstream hits are more universally popular across platforms, while lesser-known songs have more variable engagement.
##### TikTok Posts and Views are highly correlated, but their relationship with streaming metrics weakens as the dataset size increases.
#### Playlist Influence on Streams
##### Spotify Playlist Count and Playlist Reach are consistently correlated with Spotify Streams, suggesting that placement in multiple playlists strongly impacts streaming numbers.
![image 7](https://github.com/user-attachments/assets/1df9b436-480c-433f-8868-550cc51b010c)
## Final takeaways
#### TikTok Influence
##### While TikTok Views and Posts show a strong internal correlation, their impact on Spotify Streams is inconsistent across dataset sizes. In smaller datasets, TikTok engagement might appear more influential on streaming performance, but in larger datasets, the effect diminishes.
#### Virality vs. Longevity
##### TikTok success (Likes, Views, and Posts) does not strongly correlate with long-term streaming success, meaning viral moments don’t always convert into sustained listens.
#### Playlisting Matters 
##### Songs with strong playlist placements (Reach & Count) tend to perform well on streaming platforms, highlighting the importance of playlist curation for long-term success.
