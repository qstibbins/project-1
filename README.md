# Spotify Exploration

## Introduction

TikTok has become a major force in shaping modern culture. Songs that gain traction on the platform can experience explosive popularity. TikTok’s algorithm-driven nature allows snippets of songs to spread rapidly. This cycle has made TikTok a key player in music discovery, with many artists using the platform to reach wider audiences. 

Given its impact, we wanted to explore whether TikTok’s influence translates into true streaming success. **Does a song’s popularity on TikTok lead to proportional growth on Spotify or Youtube, or do viral moments fade without long-term impact?** To answer this question, we analyzed data across these platforms, comparing TikTok engagement with streaming performance to determine whether going viral truly drives success. 

## Data Overview (Merge and Clean)

## Analysis of All Data

## Breakdown of Top 500 TikToks

![][image1]

#### Weak Correlation Between TikTok and Streaming Success

The scatterplots analyzing the relationship between TikTok engagement (likes and views) and streaming performance (on Spotify and YouTube) show an extremely weak correlation across all comparisons. Each linear regression line has a near-zero rate of change, indicating that TikTok engagement has little to no direct impact on streaming success.

![][image2]

#### Data Distribution and Trends

Across all scatterplots, there is a clear concentration of data points near the origin (0,0), where both TikTok engagement and streaming metrics are relatively low. This suggests that many songs with low TikTok views also have low Spotify streams. However, some data points are scattered along the Spotify stream axis, demonstrating that certain songs can achieve high streaming numbers despite low TikTok engagement.

## Switching the Control: Spotify as the Baseline

![][image3]

With Spotify as the control, the relationship between streams and TikTok views presents a different picture compared to using TikTok as the baseline. The scatterplots show a slight upward trend, indicating that as Spotify streams increase, TikTok views also tend to rise. However, the r² value remains below 0.1, suggesting a weak correlation. This means that a song’s success on Spotify does not strongly predict its virality on TikTok.

#### Differences in Data Spread

A key difference emerges in the distribution of data. When TikTok was the control, data points were more concentrated, showing that TikTok hits experienced varying levels of success on Spotify. Now, with Spotify as the control, TikTok views display a much wider spread. While some songs perform well on both platforms, the relationship is inconsistent, highlighting that streaming success does not guarantee TikTok virality.

#### Challenging Assumptions

Overall, this new scatterplot challenges the assumption that TikTok is the primary driver of Spotify success. A song can thrive on Spotify without needing to go viral on TikTok, suggesting that long-term streaming performance may be influenced by other factors beyond TikTok trends.

## TikTok vs. Spotify: Comparing Top 10 Rankings

![][image4]

The percentage bar graphs reveal a consistent trend: a song’s popularity on TikTok does not always translate to proportional success on Spotify. For instance, a song ranked \#8 on TikTok reaching \#1 on Spotify suggests that virality on TikTok does not guarantee streaming dominance. This highlights how some songs thrive within TikTok trends but may not have lasting appeal for full-length listening, while others achieve streaming success without widespread TikTok engagement.

#### Differences in Success Patterns

![][image5]

Analyzing Spotify streams as the control reveals key differences in how music performs across platforms. On Spotify, the top ten songs show a steady decline in streams, from 13.9% at \#1 to 7.3% at \#10, indicating that success is driven by sustained listening habits rather than sudden spikes.

#### TikTok’s Unpredictable Virality

In contrast, TikTok engagement is far more unpredictable, with certain songs experiencing sharp spikes in views. This suggests that TikTok favors bursts of virality driven by trends, rather than the gradual, consistent success seen on Spotify.

## Heat map

![][image6]

![][image7]

![][image8]

### Analysis of heatmaps

#### Correlation Between Platforms

* Strong correlations exist between \*YouTube Views\*, \*Spotify Streams\*, and \*Playlist Reach\*, suggesting songs that perform well on one platform tend to perform well on others.  
* TikTok Likes have \*weak\* or \*negative correlations\* with streaming and playlist metrics, \*\*suggesting TikTok popularity doesn’t always translate into high Spotify or YouTube engagement\*\*.

####  Platform-Specific Trends

* In smaller datasets (Top-10, Top-25), \*YouTube\* and \*Spotify\* metrics show very high correlations, but as the dataset expands (Top-500), these correlations weaken, implying that mainstream hits are more universally popular across platforms, while lesser-known songs have more variable engagement.  
* TikTok Posts and Views are highly correlated, but their relationship with streaming metrics weakens as the dataset size increases.

#### Playlist Influence on Streams

* Spotify Playlist Count and Playlist Reach are consistently correlated with Spotify Streams, suggesting that placement in multiple playlists strongly impacts streaming numbers.

## Final takeaways

#### TikTok Influence

* While TikTok Views and Posts show a strong internal correlation, their impact on Spotify Streams is inconsistent across dataset sizes. In smaller datasets, TikTok engagement might appear more influential on streaming performance, but in larger datasets, the effect diminishes.  
* Further research into other factors and artist characteristics impacting popularity (i.e. \- social media engagement, age, sex, gender, genre) could yield stronger correlational data or even causational explanations for an artist's popularity. \- (copy/pasted from Dina’s analysis)   
* The *correlation coefficient* of ***\-0.0470*** between *TikTok Likes* and *Spotify Popularity* indicates there is a **weak correlation** between these two factors. With the value being so close to 0 and in the negative, there is a **slight tendency** for Spotify Popularity to decrease as TikTok likes increase and vice versa. Still, it is not a significant enough correlation for it to matter when anticipating artist popularity. The near zero correlation also suggests these are two completely independent variables. \- (copy/pasted from Dina’s analysis) 

#### Virality vs. Longevity

* TikTok success (Likes, Views, and Posts) does not strongly correlate with long-term streaming success, meaning viral moments don’t always convert into sustained listens.

#### Playlisting Matters 

* Songs with strong playlist placements (Reach & Count) tend to perform well on streaming platforms, highlighting the importance of playlist curation for long-term success.

#### Platform Synergy in Big Hits

* **Top-10** and **Top-25** songs show **stronger cross-platform correlations**, while lower-ranked songs (Top-500) exhibit more diverse success patterns.

\- Something to said about recency ranking, what stands the test of time?

## Where we would go with more time \- API

* Try looking at this across random samples within the dataset (as opposed to just top-500, top-10, etc.)  
* Find a reliable API for gathering additional song metadata and metrics like genre, danceability, etc.  
  * Much of the Spotify API was deprecated at the end of 2024, depriving us of much of the desired data  
* Expand study to include other major streaming platforms such as Apple Music
