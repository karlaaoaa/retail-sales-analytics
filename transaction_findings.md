## Transaction Category Findings

- Total original rows: 541,909.
- Cancellation invoice rows: 9,288, with a combined line amount of -£896,812.49.
- Negative quantity rows: 10,624, including 1,336 without cancellation invoice numbers.
- Negative quantity rows without cancellation invoice numbers have a combined line amount of £0.00. This does not establish that they are irrelevant.
- Zero-price rows: 2,515.
- Missing descriptions: 1,454; all also have zero unit prices.
- Negative-price adjustments: 2 rows described as `Adjust bad debt`, with a combined line amount of -£22,124.12.

## Initial Metric Definitions

- **Line amount:** Quantity multiplied by UnitPrice.
- **Ordinary product sales:** Eligible positive-quantity transactions with positive unit prices, excluding confirmed duplicates and accounting adjustments.
- **Returns and cancellations:** Classified separately until their treatment is defined.
- **Customer-level metrics:** Require a usable CustomerID.
- **Net sales:** Not finalized yet; the treatment of returns and cancellations must be documented before calculation.

The original dataset remains unchanged. Cleaning decisions will be applied to a separate analytical dataset.
