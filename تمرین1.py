Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # گرفتن نمره از کاربر
... score = float(input("نمره دانشجو را وارد کنید: "))
... 
... # تبدیل نمره به مقدار کیفی
... if score > 90:
...     print("عالی")
... elif score > 70:
...     print("خوب")
... elif score > 50:
...     print("متوسط")
... else:
...     print("مردود")
