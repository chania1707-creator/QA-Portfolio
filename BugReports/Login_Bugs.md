### 🐞 Bug Report: Locked Out User Cannot Login

**Severity:** Medium  
**Environment:** Chrome (latest), Windows 10  

---

### 📌 Steps to Reproduce:
1. Open https://www.saucedemo.com/  
2. Enter username: `locked_out_user`  
3. Enter password: `secret_sauce`  
4. Click "Login"  

---

### ✅ Expected Result:
User should receive clear guidance to unlock the account or contact support.

---

### ❌ Actual Result:
Error message displayed: "Sorry, this user has been locked out."  
No instructions are provided to the user.

---

### 📷 Screenshot:
![Locked user error](./screenshots/locked-user.png)

*Screenshot shows error message displayed after login attempt with `locked_out_user` credentials.*
### 📷 Screenshot:
![Login button bug](./screenshots/login-button-bug.png)

---

### 📝 Notes:
The button appears clickable but does not trigger any action.
