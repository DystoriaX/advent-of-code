# Analysis

## Glossary

- String digit: Sequence of letters that lights up the digit
- Set digit: Set of letters that lights up the digit

## Determining Segment `2` and `5`

We can determine which letters will be mapped to **either** segment `2` or `5` by taking the intersection of string digit 1 and 7. Notice that the string digit of 0, 6 and 9 have the same length. Both 0 and 9 lights up the segment `2` and `5`, only `6` that **does not** light up segment `2`. Hence, if we find a mismatch between the intersection, we can infer which letter maps to segment `2`. We can also determine letter that maps to segment `5`.

From this information alone, we can determine which string digit corresponds to the digit 6. By using the information of which letter maps to segment `2` and `5`, we can determine string digit that corresponds to either 2, 3, or 5 (they have the same length, and yet segment `2` and `5` help us to determine which of them uniquely)

Hence, up to know, we have yet to determine which string digit corresponds to the digit 0 and 9

## Determining Digit 0 and 9

Notice that we can take the intersection of set digit (0 or 9) and 5, since the intersection between 0 and 5 yields 4 elements, whilst 9 and 5 have 5 elements.
