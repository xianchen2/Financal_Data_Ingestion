SELECT name,
         MAX(high),
         SUBSTRING(ts,
         12,
         2) AS hour
FROM "stockprices"."25"
GROUP BY  name, SUBSTRING(ts, 12, 2)
ORDER BY  name, SUBSTRING(ts, 12, 2) 