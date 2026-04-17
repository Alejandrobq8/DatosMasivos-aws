SELECT
  hashtag,
  COUNT(*)                       AS frecuencia,
  ROUND(AVG(polarity) * 100, 2) AS pct_positive
FROM tweets_db.tweets
CROSS JOIN UNNEST(
  regexp_extract_all(LOWER(text), '#([a-z0-9_]+)')
) AS t(hashtag)
WHERE text LIKE '%#%'
GROUP BY hashtag
HAVING COUNT(*) >= 10
ORDER BY frecuencia DESC
LIMIT 50;