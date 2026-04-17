SELECT
  user,
  COUNT(*)                        AS tweet_count,
  SUM(polarity)                   AS positive_tweets,
  COUNT(*) - SUM(polarity)        AS negative_tweets,
  ROUND(AVG(polarity) * 100, 2)  AS pct_positive
FROM tweets_db.tweets
GROUP BY user
HAVING COUNT(*) >= 5          -- solo usuarios con al menos 5 tweets
ORDER BY tweet_count DESC
LIMIT 100;