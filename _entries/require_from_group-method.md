---
title: require_from_group method
entry_name: require_from_group
entry_type: method
return_type: Boolean
category: methods
layout: default
---

# require_from_group method

Ensures a given number of fields in a group are complete.

## Description

In the options passed to the rule, supply the minimum number of fields within the group that must be complete and a selector to define the group. Then apply this rule to all the fields within the group. The form then cannot be submitted until at least the minimum number have been completed. Part of the additional-methods.js file

## Examples

Within a group of three phone numbers, ensure at least one is complete.

```javascript
$( "#myform" ).validate({
  rules: {
    mobile_phone: {
      require_from_group: [1, ".phone-group"]
    },
    home_phone: {
      require_from_group: [1, ".phone-group"]
    },
    work_phone: {
      require_from_group: [1, ".phone-group"]
    }
  }
});
```

```html
<label for="mobile_phone">Mobile phone: </label>
<input class="left phone-group" id="mobile_phone" name="mobile_phone">
<br/>
<label for="home_phone">Home phone: </label>
<input class="left phone-group" id="home_phone" name="home_phone">
<br/>
<label for="work_phone">Work phone: </label>
<input class="left phone-group" id="work_phone" name="work_phone">
<br/>
<input type="submit" value="Validate!">
```
