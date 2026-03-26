# Test Cases – SauceDemo

## TC01 – Successful Login
**Steps:**
1. Open https://www.saucedemo.com
2. Enter username: `standard_user`
3. Enter password: `secret_sauce`
4. Click Login

**Expected Result:**  
User is redirected to the products page.

**Screenshot:**
![Products Page](screenshots/products-page.png)

---

## TC02 – Login with incorrect password
**Steps:**
1. Open https://www.saucedemo.com
2. Enter username: `standard_user`
3. Enter incorrect password
4. Click Login

**Expected Result:**  
Error message is displayed.

**Screenshot:**
![Locked User](../screenshots/locked-user.png)

---

## TC03 – Add product to cart
**Steps:**
1. Login to the website
2. Click "Add to cart" on a product

**Expected Result:**  
Product is added to the shopping cart.

**Screenshot:**
![Cart Badge Issue](../screenshots/cart-test.png)
