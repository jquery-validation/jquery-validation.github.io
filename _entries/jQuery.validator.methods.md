---
title: jQuery.validator.methods
entry_name: jQuery.validator.methods
entry_type: method
category: validator
layout: default
---

# jQuery.validator.methods

Object holding all validation methods known to the validator. This can be accessed to override individual methods, while keeping the default messages.

## Examples

Sets a custom email pattern for the built-in email validation rule.

```javascript
$.validator.methods.email = function( value, element ) {
  return this.optional( element ) || /[a-z]+@[a-z]+\.[a-z]+/.test( value );
}
```
