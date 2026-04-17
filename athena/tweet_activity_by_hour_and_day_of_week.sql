SELECT
  hour,
  day_of_week,
  COUNT(*)                                    AS total_tweets,
  ROUND(AVG(polarity) * 100, 2)              AS pct_positive,
  COUNT(*) * 100.0 / SUM(COUNT(*)) OVER ()   AS pct_of_total
FROM tweets_db.tweets
GROUP BY hour, day_of_week
ORDER BY total_tweets DESC
LIMIT 50;