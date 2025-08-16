**CSRF** stands for **Cross-Site Request Forgery**. It is a type of **security attack** where a malicious user tricks someone into performing an unwanted action on a website where they are authenticated (logged in).

### What is CSRF?

In simple terms, CSRF allows attackers to send unauthorized requests to a website using the identity and privileges of an authenticated user. This can lead to a wide range of malicious activities, like changing a password, transferring funds, or deleting data without the user's knowledge.

### Example of how a CSRF attack works:

1. **A user is logged into a website** (like a banking site).
2. The user visits a malicious website that contains an **evil link** or **form** that tries to perform an action on the legitimate website (like transferring money).
3. Since the user is already logged in, the website trusts the request (because it has the user's authentication cookies), and it performs the action without the user's consent.

### Why is CSRF a problem?

* If there is no protection against CSRF, a malicious attacker can trick a user into doing things like:

  * Changing account settings.
  * Making purchases.
  * Deleting posts or data.

### CSRF protection in Django:

Django has built-in protection against CSRF attacks to keep your application secure.

#### How Django prevents CSRF attacks:

1. **CSRF Tokens**: Django includes a **CSRF token** in each form submitted to the server. This token is a random string that the server generates when the form is loaded. When the form is submitted, the server checks if the CSRF token sent with the request matches the one it generated. If they don’t match, the request is rejected.

2. **Middleware**: Django automatically checks for CSRF tokens in requests made with methods like `POST`, `PUT`, and `DELETE`. If the token is missing or incorrect, Django will block the request.

### Example of CSRF protection in Django:

#### 1. **Using `{% csrf_token %}` in Templates**:

When creating a form in Django, you need to include `{% csrf_token %}` inside the form tag. This ensures that Django generates a CSRF token and checks it when the form is submitted.

```html
<form method="POST">
    {% csrf_token %}
    <label for="username">Username:</label>
    <input type="text" name="username" id="username">
    <button type="submit">Submit</button>
</form>
```

In the example above:

* `{% csrf_token %}` generates a hidden input field with the CSRF token.
* When the form is submitted, Django checks the CSRF token to make sure the request is valid.

#### 2. **CSRF Protection in Views**:

By default, Django uses middleware to ensure that any view that handles a `POST` request is protected by CSRF validation. If a request does not have a valid CSRF token, Django will return a **403 Forbidden** response.

You don't need to do anything extra for CSRF protection in most cases, but if you want to exempt certain views (like an API endpoint), you can use `@csrf_exempt` decorator:

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):
    # This view won't be checked for CSRF
    return HttpResponse("No CSRF protection here")
```

### Why does Django use CSRF tokens?

* **Protection from malicious sites**: By requiring a CSRF token for all form submissions, Django ensures that only your site can make requests to itself, preventing external malicious sites from tricking a user into making unauthorized requests.
* **Ensures authenticity**: CSRF tokens ensure that requests come from the same user who is interacting with the website, not from an attacker.

### Conclusion:

* **CSRF** is a security vulnerability where attackers can force users to perform unintended actions.
* **Django** provides built-in protection using CSRF tokens that validate the authenticity of requests.
* Always include `{% csrf_token %}` in your forms to keep your app safe from CSRF attacks.

Let me know if you'd like a more detailed explanation or examples!
