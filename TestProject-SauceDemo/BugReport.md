# Bug Report – SauceDemo

## Bug ID
BR-001

## Summary
Cart badge does not update after removing a product.

## Environment
| Parameter | Value |
|-----------|-------|
| Browser   | Google Chrome |
| OS        | Windows 11 |
| URL       | https://www.saucedemo.com |

## Steps to Reproduce
1. Open https://www.saucedemo.com
2. Login with:
   - Username: `standard_user`
   - Password: `secret_sauce`
3. Add a product to the cart
4. Remove the product from the cart

## Expected Result
Cart icon should show 0 items.

## Actual Result
Cart badge still displays 1 item.

## Severity
Medium

## Priority
High

## Screenshot
![Cart Badge Issue](screenshots/cart-test.png)
