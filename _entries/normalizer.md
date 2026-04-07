---
title: normalizer
entry_name: normalizer
entry_type: method
return_type: String
category: methods
layout: default
---

# normalizer

Prepares/transforms the elements value for validation.

## Description

Transform the value of an element and the result for validation instead of the initial value. The normalizer can be defined global to all elements or local to only one element. With that said, the local normalizer will only run for the element for which it was defined. The global normalizer will run for all validated elements. This normalizer can be then overrided for each element, as needed, by attaching one to it. This way only the local one will run for that element, and the global one will run for others. Note that this method: Has been available since version 1.15.0 Doesn't change the elements' value, it only changes the value used for validation. Gets the value passed as argument, and "this" within it references the corresponding DOMElement. For versions between 1.15.0 and 1.17.0, it must return a string value. And as of 1.17.1, it can return any value including null and undefined.

## Usage

**value** *(String)*

The value of the element.

## Examples

### Example 1

Makes "field" required and use a normalizer to trim its value before validating

```javascript
$( "#myform" ).validate( {
  rules: {
    field: {
      required: true,
      normalizer: function( value ) {
        // Trim the value of the `field` element before
        // validating. this trims only the value passed
        // to the attached validators, not the value of
        // the element itself.
        return $.trim( value );
      }
    }
  }
} );
```

```html
<label for="field">Required: </label>
<input class="left" id="field" name="field">
<br/>
<input type="submit" value="Validate!">
```

### Example 2

Makes "url" required and use a normalizer to append 'http://', if not present, to the value of the "url" element before validating

```javascript
$( "#myform" ).validate( {
  rules: {
    url_input: {
      required: true,
      url: true,
      normalizer: function( value ) {
        var url = value;

        // Check if it doesn't start with http:// or https:// or ftp://
        if ( url && url.substr( 0, 7 ) !== "http://"
            && url.substr( 0, 8 ) !== "https://"
            && url.substr( 0, 6 ) !== "ftp://" ) {
          // then prefix with http://
          url = "http://" + url;
        }

        // Return the new url
        return url;
      }
    }
  }
} );
```

```html
<label for="url_input">url: </label>
<input class="left" id="url_input" name="url_input">
<br/>
<input type="submit" value="Validate!">
```

### Example 3

Using a global normalizer in conjunction with a local one

```javascript
$( "#myform" ).validate( {
  // This global normalizer will trim the value of all elements
  // before validatng them.
  normalizer: function( value ) {
    return $.trim( value );
  },
  rules: {
    username: {
      required: true
    },
    url_input: {
      required: true,
      url: true,

      // We don't need to trim the value of this element, so we overrided
      // the global normalizer in order to append 'http://' to the url value
      // if doesn't already.
      normalizer: function( value ) {
        var url = value;

        // Check if it doesn't start with http:// or https:// or ftp://
        if ( url && url.substr( 0, 7 ) !== "http://"
            && url.substr( 0, 8 ) !== "https://"
            && url.substr( 0, 6 ) !== "ftp://" ) {
          // then prefix with http://
          url = "http://" + url;
        }

        // Return the new url
        return url;
      }
    }
  }
} );
```

```html
<label for="username">Required: </label>
<input class="left" id="username" name="username">
<br/>
<label for="url_input">url: </label>
<input class="left" id="url_input" name="url_input">
<br/>
<input type="submit" value="Validate!">
```
