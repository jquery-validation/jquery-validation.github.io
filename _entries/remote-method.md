---
title: remote method
entry_name: remote
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# remote method

Requests a resource to check the element for validity.

## Description

The serverside resource is called via jQuery.ajax (XMLHttpRequest) and gets a key/value pair corresponding to the name of the validated element and its value as a GET parameter. The serverside response must be a JSON string that must be `"true"` for valid elements, and can be `"false"`, `undefined`, or `null` for invalid elements, using the default error message. If the serverside response is a string, eg. `"That name is already taken, try peter123 instead"`, this string will be displayed as a custom error message in place of the default. For more examples, take a look the [marketo demo](//jqueryvalidation.org/files/demo/marketo) and the [milk demo](//jqueryvalidation.org/files/demo/milk/).

## Usage

**options** *(Object)*

For the URL of the resource to request for serverside validation (String) or options to fully customize the request, see [jQuery.ajax](https://api.jquery.com/jQuery.ajax) for details. These options deep-extend the defaults (`dataType:"json", data:{nameOfTheElement:valueOfTheElement}`). Any options you provide will override the defaults.

## Examples

### Example 1

Makes the email field required, an email and does a remote request to check if the given address is already taken.

```javascript
$( "#myform" ).validate({
  rules: {
    email: {
      required: true,
      email: true,
      remote: "check-email.php"
    }
  }
});
```

### Example 2

Makes the email field required, an email and does a remote request to check if the given address is already taken. In addition, the http method is set to "post" and the username is sent alongside the email address.

```javascript
$( "#myform" ).validate({
  rules: {
    email: {
      required: true,
      email: true,
      remote: {
        url: "check-email.php",
        type: "post",
        data: {
          username: function() {
            return $( "#username" ).val();
          }
        }
      }
    }
  }
});
```
