---
title: :filled Selector
entry_name: filled
entry_type: selector
category: selectors
layout: default
---

# :filled Selector

**Selector:** `:filled`

Selects all elements with a filled value.

## Description

filled means any value, but not only whitespace. The implementation does a check like this: `jQuery.trim(value).length > 0`

## Usage


## Examples

Finds input elements with a non-whitespace value.

```javascript
$( "input:filled" ).css( "background-color", "#bbbbff" );
```

```html
<div>Mouseover to see the value of each input</div>
  <input value="" title='""'>
  <input value="   " title='"   "'>
  <input value="abc" title='"abc"'>
```
