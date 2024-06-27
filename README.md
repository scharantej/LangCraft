### Problem: Displaying a List of Items Using Flask

#### Design
**HTML Files**

1. `index.html`:
   - Purpose: Main page that displays a list of items.
   - Content:
     - Title and heading to display "Items List"
     - Unordered list`<ul>` to display the list of items.
     - Placeholder text for the items, such as`<li>Item 1</li>`.

2. `add_item.html`:
   - Purpose: Page to add a new item to the list.
   - Content:
     - Form with an input field for entering an item name.
     - Submit button to save the item.

**Routes**

1. `@app.route('/')`:
   - Purpose: Renders the `index.html` page and displays the list of items.
   - Function:
     - Retrieves the list of items from a data store (e.g., a database).
     - Renders the `index.html` template with the list of items.

2. `@app.route('/add_item', methods=['POST'])`:
   - Purpose: Receives the submitted form data from `add_item.html` and adds a new item to the list.
   - Function:
     - Retrieves the submitted item name from the form data.
     - Adds the new item to the data store.
     - Redirects the user back to the `index.html` page.