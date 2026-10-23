# Initial Data Exploration — Online Retail

## Dataset overview

- **Source:** UCI Machine Learning Repository — Online Retail
- **Original records:** 541,909
- **Columns:** 8
- **Period:** December 1, 2010 – December 9, 2011

## Initial findings

- Missing `CustomerID`: 135,080 rows.
- Missing `Description`: 1,454 rows.
- Exact duplicate rows: 5,268.
- Quantity and unit price contain extreme values that require investigation.
- `CustomerID` is represented as a floating-point value and may need a more appropriate database type.

## Next investigations

- Determine the frequency of negative and zero quantities and prices
    - negative quantities: 106624
    - zero quantities: 0
    - negative prices: 2
    - zero prices: 2515
- Investigate cancellation invoice numbers.
    - 9288
- Inspect duplicate records before deciding how to handle them.
    - At the beginning I thought that the duplicates where same purchases made by customers in different dates or times however since the invoice data always matches I believe that the duplicates must be removed because they don't seem to be real significant data and just double incorrect information.
- Establish business rules before calculating final sales metrics.
    - a sale is a row that doesn't have any null values and the unit price and quantity are positive
    - a return is a row that starts with C in InvoiceNo and the quantity is negative
    - duplicate rows must be eliminated
    - rows with missing description and unitprice must be eliminated because we don't know what is happening
    - the two rows with negative unitprice stay because in the description it says "Adjust bad debt" 

## Important decision

The original dataset must remain unchanged. All cleaning and transformations will be applied to a separate analytical table.
