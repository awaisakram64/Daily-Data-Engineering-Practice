SELECT browser, DATE(pageview_time) AS day, COUNT(*) AS views
FROM web_traffic
GROUP BY GROUPING SETS (
  (browser, DATE(pageview_time)),
  (browser),
  (DATE(pageview_time))
);