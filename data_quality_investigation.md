# Data Quality Investigation

## Dataset
UCI Online Retail dataset, containing 541,909 original transaction lines.

## Findings
- 5,268 exact duplicate rows were identified (approximately 0.97% of the dataset).
- Removing exact duplicates reduces the row count to 536,641.
- The preliminary total of `Quantity × UnitPrice` decreases by £21,740.98 after deduplication.
- 10,624 rows have negative quantities. Of these, 9,288 have cancellation invoice numbers and 1,336 do not.
- 2,515 rows have zero unit prices.
- Two rows have negative unit prices and are described as `Adjust bad debt`.
- CustomerID and Description contain missing values.

## Provisional Cleaning Rules
1. Preserve the original raw dataset unchanged.
2. Remove exact duplicate rows from the analytical dataset, documenting this as a cleaning assumption.
3. Investigate negative quantities separately from cancellation invoice numbers.
4. Flag zero-price transactions rather than automatically deleting them.
5. Retain and separately classify the two bad-debt adjustments; exclude them from ordinary product-sales revenue unless the chosen metric explicitly includes adjustments.
6. Do not automatically discard rows with missing CustomerID. They may still contribute to overall sales analysis.
7. Investigate missing descriptions before deciding whether those records should be excluded from product-level analysis.

## Metric Definition
`LineAmount = Quantity × UnitPrice`

This is a preliminary line-level amount, not the final sales revenue measure. Cancellation, return, and adjustment treatment must be defined before final revenue is calculated.


Here is the rule set I recommend documenting for now.
Data issue	Provisional rule
Exact duplicate rows	Remove from the analytical dataset, documenting the assumption
Missing CustomerID	Retain for overall sales metrics; exclude from customer-specific analysis
Missing Description and zero price	Flag and exclude from ordinary product-sales revenue
Zero unit price	Investigate and flag; do not automatically delete every such row
Negative quantity	Classify separately for return/cancellation analysis
Cancellation invoice (InvoiceNo begins with C)	Classify as a cancellation; investigate separately from other negative quantities
Negative unit price with Adjust bad debt	Classify as an accounting adjustment, not ordinary product sales