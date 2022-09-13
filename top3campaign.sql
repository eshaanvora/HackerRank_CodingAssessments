SELECT revenue - expenses as profit,
  (SELECT name
  FROM companies
  WHERE companies.id = campaigns.company_id)
FROM campaigns
ORDER BY profit DESC
WHERE profit > 0
LIMIT 3;
