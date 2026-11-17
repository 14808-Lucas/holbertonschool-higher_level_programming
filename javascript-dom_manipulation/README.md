# JavaScript - DOM Manipulation

Scripts that run in the browser and change a web page through the **DOM (Document Object Model)**: selecting elements, changing their styles, classes and text, creating new elements, reacting to clicks, and loading data from web APIs with the **Fetch API**. The page never reloads; JavaScript updates it in place.

## Learning objectives

- What the DOM is, and how the `document` object gives JavaScript access to the page
- How to select elements with `document.querySelector` and CSS selectors (type, `#id`, `.class`)
- How to change an element's style (`.style`), classes (`classList`) and text (`textContent`)
- How to create elements and add them to the page (`createElement`, `appendChild`)
- How to listen for events with `addEventListener` (`click`, `DOMContentLoaded`)
- How to request data with `fetch` and handle the result with Promises (`.then`)
- Why a script loaded from `<head>` must wait for `DOMContentLoaded`

## Requirements

- Scripts are interpreted in Chrome (version 57.0 or later)
- All files end with a new line
- Code is `semistandard` compliant
- `var` is not used
- The HTML never reloads: every change happens through DOM manipulation

## Testing

Each task comes with an HTML page (`<n>-main.html`) that loads its script.

Check the code style with:

```shell
semistandard *.js
```

## Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-script.js` | Sets the text color of the `header` element to red (`#FF0000`) with `document.querySelector`. |
| 1 | `1-script.js` | Turns the `header` red when the element with id `red_header` is clicked. |
| 2 | `2-script.js` | Adds the class `red` to the `header` when `red_header` is clicked. |
| 3 | `3-script.js` | Toggles the `header` class between `red` and `green` when `toggle_header` is clicked. The header always has exactly one of the two classes. |
| 4 | `4-script.js` | Adds a new `<li>Item</li>` to the `ul.my_list` list each time `add_item` is clicked. |
| 5 | `5-script.js` | Changes the `header` text to `New Header!!!` when `update_header` is clicked. |
| 6 | `6-script.js` | Fetches Star Wars character 5 from the SWAPI and displays its `name` in `#character`. |
| 7 | `7-script.js` | Fetches all Star Wars films from the SWAPI and lists each `title` in `ul#list_movies`. |
| 8 | `8-script.js` | Fetches the French translation of "hello" and displays it in `#hello`. Works when loaded from `<head>` by waiting for `DOMContentLoaded`. |


## Resources

- [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
- [Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)
- [Element](https://developer.mozilla.org/en-US/docs/Web/API/Element)
- [Locating DOM elements using selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Selection_and_traversal_on_the_DOM_tree)
- [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
- [DOM scripting](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting)
- [Network requests](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Network_requests)
- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/What_went_wrong)

## Author

Lucas Fisher - Holberton School
