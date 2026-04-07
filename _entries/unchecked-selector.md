---
title: :unchecked Selector
entry_name: unchecked
entry_type: selector
category: selectors
layout: default
---

# :unchecked Selector

**Selector:** `:unchecked`

Selects all elements that are unchecked.

## Description

Inversion of [:checked](https://api.jquery.com/checked).

## Usage


## Examples

Finds all input elements that are unchecked.

```javascript
function countUnchecked() {
  var n = $( "input:unchecked" ).length;
  $( "div" ).text(n + (n == 1 ? " is" : " are") + " unchecked!" );
}
countUnchecked();
$( ":checkbox" ).click( countUnchecked );
```

```html
<form>
    <input type="checkbox" name="newsletter" checked="checked" value="Hourly" />
    <input type="checkbox" name="newsletter" value="Daily" />
    <input type="checkbox" name="newsletter" value="Weekly" />
    <input type="checkbox" name="newsletter" checked="checked" value="Monthly" />
    <input type="checkbox" name="newsletter" value="Yearly" />
  </form>
  <div></div>
```
