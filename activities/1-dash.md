# Plotly Dash version of the activities

The Dash application is based on the paralympics data used in COMP0035 tutorials.

In this activity you will:

- Create a Dash page with an HTML layout
- Style the Dash layout using Bootstrap CSS
- Adapt the Dash layout to support responsive styling
- Adapt the Dash layout to allow several chart areas
- Add dropdown selectors and check boxes to the Dash layout

The activity builds towards a single page Dashboard design with the following layout. This uses a 12 column grid layout:

<table>
<tr><td colspan="12">Heading and intro</td></tr>
<tr>
<td colspan="2">dropdown</td>
<td colspan="4">Line chart</td>
<td colspan="2">checkbox</td>
<td colspan="4">Bar chart</td>
</tr>
<tr>
<td colspan="6">Map with event markers</td>
<td colspan="6">card showing event info</td>
</tr>
</table>

The Dash website has a place for developers to
share [examples of their work](https://plotly.com/examples/?_gl=1*180ybt8*_ga*MjEyMzA3NDMxOS4xNjk2MzQwMTcx*_ga_6G7EE0JNSC*MTcwNDkwMDE4NS45LjEuMTcwNDkwMTUyNi4zMy4wLjA.).
I looked at a number of these to help with deciding on the overall page structure. There is a section of examples
called 'Connecting to APIs' that might be of particular relevance to the coursework.

## Check the Dash app runs

There is code to run a [basic Dash app](../src/paralympics_dash/paralympics_dash.py) that displays 'Hello world'. This
is copied from the [Dash tutorial](https://dash.plotly.com/tutorial).

1. `python paralympics_dash/paralympics_dash.py`

   You may need to change the port number if you already have something running on the default port 8050
   e.g. `flask --app paralympics_flask run --debug --port=5050`.

2. Go to the URL that is shown in the terminal. By default, this is <http://127.0.0.1:8050>.
3. Stop the app using `CTRL+C`

## Create a Dash page with an HTML layout

### HTML basics

The basic tag structure for HTML is `<start_tag> some content </end_tag>`. This set of opening tag + content + closing
tag is referred to as an **HTML element**.

A small number of elements only have an opening tag e.g. `<img>`, `<br>`, `<hr>`. There is a list of
these [void elements here](https://developer.mozilla.org/en-US/docs/Glossary/Void_element).

Elements can also have attributes that give additional information. In this course you will mostly use id
e.g. `id="some-name"` and class e.g. `class="some-class"`. `id` is used to locate a particular element on a webpage,
and `class` is used in adding styles to elements (more on these in later sections).

HTML documents start with a document type declaration `<!DOCTYPE html>`. This is required at the start of the document.

The HTML document itself begins with `<html>` and ends with `</html>`

The part that is mostly not visible in the final webpage is between `<head>` and `</head>`. This is typically metadata,
i.e. info about the page.

The part of the HTML document that is visible in the browser is between `<body>` and `</body>`.

A minimal page structure looks like the following:

```html
<!DOCTYPE html>
<!-- This is an HTML comment, you won't see it on the page -->
<!-- Head section -->
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>COMP0034 Introduction to HTML - Basic page structure</title>
</head>
<!-- Body section -->
<body>
<p>Here is some text on a page.</p>
</body>
</html>
```

You can practice using HTML with the optional activity [2-html-intro.md](2-html_intro.md).

### Using HTML in Dash

Dash provides an API, [Dash HTML Components](https://dash.plotly.com/dash-html-components), that "provides pure Python
abstraction around HTML, CSS, and JavaScript.

Instead of writing HTML or using an HTML templating engine, you compose your layout using Python with the Dash HTML
Components module (dash.html)"

The HTML tags supported by Dash are [listed here](https://dash.plotly.com/dash-html-components#full-elements-reference).
You may need to refer to an [HTML reference](https://www.w3schools.com/html/) to know what the tags and their attributes
are; however you
will not write HTML files. You will only use Dash html python functions.

This is an example given in the Dash documentation:

```python
from dash import html

html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ])
])
```

which equates to the following HTML:

```html

<div>
    <h1>Hello Dash</h1>
    <div>
        <p>Dash converts Python classes into HTML</p>
        <p>This conversion happens behind the scenes by Dash's JavaScript front-end</p>
    </div>
</div>
```

HTML elements can have properties such as style (CSS), class (CSS classes which you will see later) and id (to uniquely
identify an element on a page). More on this in a later section.

### Add HTML elements to the Dash layout

The dash app starter code in `paralympics_dash.py` currently looks like this:

```python
# Imports for Dash and Dash.html
from dash import Dash, html

# Create an instance of the Dash app
app = Dash(__name__)

# Add an HTML layout to the Dash app
app.layout = html.Div([
    html.Div(children='Hello World')
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

The HTML to layout the page will be added to the `app.layout =` section of the code.

Add some HTML to the page such as paragraph (html.P), heading 1 (html.H1) and image (html.Img).
These are in the [Dash html components reference](https://dash.plotly.com/dash-html-components).

Images are in the 'assets' folder. To reference these in the `src=` parameter use the `app.get_asset_url()`
function. In the brackets specify the file name and any subdirectory below the 'assets' directory,
e.g. `html.Img(src=app.get_asset_url('bar-chart-placeholder.png'))`

1. Add an H1 heading using html.H1()
2. Add an image using html.Img()

Add any other elements you want to try.

## Style the Dash layout using Bootstrap CSS

### CSS overview

CSS stands for Cascading Style Sheets. It provides styles for HTML elements.

Web browsers apply CSS rules to a document. A CSS **rule** consist of:

- A **selector**, which selects the element(s) you want to style

- A declaration which is a set of **properties** with values

The following CSS rule selects the paragraph tag `p` and makes the font colour red and the text center-aligned.

```css
p {
    color: red;
    text-align: center;
}
```

A set of these CSS rules are called a **stylesheet**.

CSS can be added to HTML elements in 3 ways:

- **Inline**: using the style attribute in HTML elements
- **Internal**: using a `<style>` element in the `<head>` section
- **External**: using an external CSS file e.g. `my_css.css`.

An **Inline style** affects one element only and is defined in the `style'=""` attribute of that HTML element
e.g. `<h1 style="color: blue; background-color: yellow;">Hello World! </h1>`. Avoid using this method as it is much
harder to maintain!

An **internal stylesheet** places CSS inside a `<style>` element contained inside the HTML `<head>` section.

An **external CSS file** is usually the preferred method and is used in most COMP0034 example code. CSS is
written in a separate file with a `.css` extension.
The stylesheet `.css` file is referenced in the `<head>` section of the html using an HTML `<link>`
element.

A little more detail is included in the optional activity [3-css-intro.md](3-css_intro.md)

In Dash you apply an inline style using the style property of an HTML component e.g.:

```python
app.layout = html.Div([
    html.Div(className='row', children='My First App with Data, Graph, and Controls',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
])
```

In most cases you will use an external stylesheet. This can either be a .css file saved in your project file structure,
or .css hosted elsewhere (usually on a CDN). A CDN (Content Distribution Network) is a
distributed group of servers that caches content and typically has several locations near end users. Its aim is to
improve load times; and for those who use it, to reduce the costs of hosting files themselves.

In Dash you do not have an HTML file, so you define the location of the stylesheet (or stylesheets if you have more than
one) and pass this as a parameter to the Dash app instance. This example uses
the [CDN version of Milligram css](https://milligram.io):

```python
# Import packages
from dash import Dash

# Initialize the app using Milligram css
external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout etc...
```

The Dash documentation does not currently cover how to reference a .css file from your project folder. Community posts
suggest you can do it, though it does not appear to be straightforward, so is not included in this tutorial.

### Using open source CSS in Dash

While you can write your own CSS, **for your coursework it is recommended that you use a third party CSS**. Check it has
an open source license, i.e. that you are given permission by its author to use it. Writing your own CSS is not
considered in the mark scheme so writing your own CSS will not improve your marks.

Bootstrap is a popular CSS library that has extensive documentation and support and is used in the course materials for
this reason.

Bootstrap is widely used which some say leads to many sites looking similar, others criticisms include the fact that it
is comprehensive, leading to larger file sizes, and yet you may only want to use a small subset of its features. There
are alternatives to Bootstrap you can explore, try searching `alternatives to Bootstrap`, such as:

- [Pure.css](https://purecss.io/start/)
- [Materialize](https://materializecss.com/getting-started.html)
- [ZURB foundation](https://foundation.zurb.com/)

The [Bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/#quick-start) gives the URL
to access the hosted version.

For Dash, there is an additional
library, [dash bootstrap components](https://dash-bootstrap-components.opensource.faculty.ai), that makes Bootstrap
easier to apply to Dash. This is used in the remainder of the tutorial.

To use the Dash bootstrap components timesheets also
have [themes](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/) that you can apply to achieve a
particular look and feel.

To apply a Boostrap standard them, add the import for dash_bootstrap_components and then reference the theme as the
external stylesheet. The following is the standard Bootstrap look and feel:

```python
from dash import Dash
import dash_bootstrap_components as dbc

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Pass the stylesheet variable to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets)
```

### Activity

1. Add the import: `import dash_bootstrap_components as dbc`
2. Add a bootstrap theme external stylesheet to the paralympics app. You may wish to try a few to see which you like.
3. Run the dash app.

Dash will try to update dynamically when you make changes, so you could experiment with a few different themes without
needing to stop and restart the server.

## Adapt the Dash layout to support responsive styling

### Intro to responsive design

The intent of responsive design is to make web pages look good on all devices: desktop, tablets, and phones. For
example, people are typically used to scrolling websites vertically but not horizontally. So there are techniques to
achieve responsive web design such as resize, hide, shrink, enlarge, move the content.

To create a web page that is responsive:

- Set the viewport
- Use responsive images
- Use responsive text
- Use media queries (apply a different style for different screen sizes)
- Optionally, use a grid layout

The **viewport** is the visible area inside the browser window. A `<meta>` viewport element gives the browser
instructions on how to control the page's dimensions and scaling. This gives the browser instructions on how to control
the page's dimensions and scaling. For example the following code would be placed in the `<head>` section of a html
document.

```html

<meta name="viewport" content="width=device-width, initial-scale=1">
```

- `width=device-width` sets the width of the page to follow the screen-width of the device (varies depending on the
  device).
- `initial-scale=1` sets the initial zoom level when the page is first loaded by the browser.

To use Bootstrap in a responsive way, the minimum you need is:

1. Include the `<meta>` tag in the `<head>` to set the page width to the device
   `<meta name="viewport" content="width=device-width, initial-scale=1">`.
2. Wrap the page contents in an HTML `<div>` tag that has a container CSS class. Bootstrap offers two container classes:
    - `.container` class provides a responsive fixed width container
    - `.container-fluid` class provides a full width container, spanning the entire width of the viewport

As you don't have an HTML file in Dash then to pass in tags that would usually be the head section, you pass them to the
Dash app object. You did this with the stylesheets in the earlier activity.

The code to add the <meta> tag to the head section is as follows:

```python
from dash import Dash
import dash_bootstrap_components as dbc

# Define a variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Define a variable that contains the meta tags
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Pass the stylesheet and meta_tag variables to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
```

To wrap the entire page content in a div that applies one of bootstrap's container classes, use the dbc.Container()
component:

```python
import dash_bootstrap_components

app.layout = dash_bootstrap_components.Container(
    # The rest of the html contents can go here
)
```

You can wrap individual elements in Containers rather than the entire page. The above is just one approach.

Other responsive aspects to consider, such as images and text size, are briefly covered
in [4-responsive_intro.md](4-responsive_intro.md).

### Update the paralympics Dash app layout to a responsive design

1. Add a variable that defines a meta tag
2. Pass the meta tag variable to the Dash app constructor
3. Wrap the layout in a dbc.Container() components
4. Check the updated Dash app in a browser

## Use the Bootstrap grid system to structure the paralympics Dash app

Before starting, remove any of the HTML elements you added inside the layout such as H1, P, Img etc. in an earlier
activity.

### Overview

This is the most challenging part of the tutorial.

Use the skills you just learned for the HTML components and Dash Bootstrap Components to create a layout that is similar
to the following.

This uses a grid layout that logically divides the page into 4 rows, where each row spans a width that can be divided
into 12.

Each column in a row can span 1 or of the 12 divisions. So if there are 3 equal columns then each column would have a
width of '4' (as 3 x 4 = 12).

<table>
<tr><td colspan="12">12 cols: Heading and intro</td><tr>
<tr>
<td colspan="2">2 cols:<br>dropdown</td>
<td colspan="4"></td>
<td colspan="2">2 cols, offset by 4 cols:<br>checkbox</td>
<td colspan="4"></td>
</tr>
<tr>
<td colspan="6">6 cols: Line chart</td>
<td colspan="6">6 cols: Bar chart</td>
</tr>
<tr>
<td colspan="6">6 cols: Map with event markers</td>
<td colspan="6">6 cols: card showing event info</td>
</tr>
</table>


You can write all the code by adding it to the layout. However, to break up the code to try and make it easier to read,
in the following steps each row and cell is defined in as separate variable, then the variables will be referenced from
the app.layout.

You may wish to refer to the following to complete this activity:

- [Dash bootstrap components layout documentation](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/)
- [Dash tutorial on styling](https://dash.plotly.com/tutorial#styling-your-app)
- [Bootstrap grid documentation](https://getbootstrap.com/docs/5.0/layout/grid/)

### 1. Define the layout

The layout described above has 3 rows and a varying number of columns within each row.

The following code provides a skeleton for the columns in the rows with the widths. The `children=[]` is where you will
place the children of an element. The full syntax is `children=[]`though if this is placed as the first parameter in the
brackets then the `children=` can be omitted, so you will often just see `[]`. So, for a row `dbc.Row([])` the '
children' are the columns in that row. For the columns, `dbc.Col([])` in a row, the children will be the selectors,
charts, text etc.

The first row has a single column that spans the entire width. You can either specify the column width as 12 or omit the
width as it will then default to fit the available space.

Add the code `paralympics_dash.py`. The use of variables for each row is just to breaks the code down, so it may be
easier to read. This does not affect the code functioning, you can place it all inside `app.layout` if you prefer.

```python
import dash_bootstrap_components as dbc

row_one = dbc.Row([
    dbc.Col([]),
])

row_two = dbc.Row([
    dbc.Col(children=[], width=2),
    dbc.Col(children=[], width={"size": 2, "offset": 4}),  # 4 'empty' columns between this and the previous column
])

row_three = dbc.Row([
    dbc.Col(children=[], width=6),
    dbc.Col(children=[], width=6),
])

row_four = dbc.Row([
    dbc.Col(children=[], width=6),
    dbc.Col(children=[], width=6),
])

app.layout = dbc.Container([
    row_one,
    row_two,
    row_three,
    row_four
])
```

If you run the app now you will see a blank page. The rows and columns provide structure, however there is no content
yet.

### 2. Add the contents to the rows

The content includes HTML tags from Dash html such as paragraph (html.P), heading 1 (html.H1) and image (html.Img).
These are in the Dash html reference.

Images are placed in the 'assets' folder. To reference these in the `src=` parameter use the `app.get_asset_url()`
function. In the brackets specify the file name and any subdirectory below the 'assets' directory. You will see examples
in the code below.

The dropdown and checkbox can either be Dash Boostrap components (dbc) style so dbc.Select() and dbc.Checklist(); or
Dash core components (dcc).

[DBC components reference](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/input/)
[Dash Core Components reference](https://dash.plotly.com/dash-core-components/dropdown).

#### Row 1

The first row has a heading level 1 with the app name and a paragraph with some descriptive text (lorem ipsum
placeholder for now). You can write what you wish or copy the text below. Place these inside the `children=[]` of the
column in row one.

```python
html.H1("Paralympics Data Analytics"),
html.P(
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida. Fusce efficitur posuere metus posuere malesuada. ")
```

#### Row 2

The second row has:

- column 1: contains
  an [input of type select](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/input/) (a
  dropdown).
- column 2: will have a line chart.
- column 3: contains
  an [input of type checklist](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/input/)
- column 4: contains a bar chart.

```python
# Column 1 children
dbc.Select(
    options=[
        {"label": "Events", "value": "events"},  # The value is in the format of the column heading in the data
        {"label": "Sports", "value": "sports"},
        {"label": "Countries", "value": "countries"},
        {"label": "Athletes", "value": "participants"},
    ],
    value="events",  # The default selection
    id="dropdown-input",  # id uniquely identifies the element, will be needed later for callbacks
),

# Column 2 children
# className="ing-fluid" is a pure Bootstrap class and prevented the image spanning the next column
html.Img(src=app.get_asset_url('event-chart-placeholder.png'), className="img-fluid"),

# Column 3 children
html.Div(
    [
        dbc.Label("Select the Paralympic Games type"),
        dbc.Checklist(
            options=[
                {"label": "Summer", "value": "summer"},
                {"label": "Winter", "value": "winter"},
            ],
            value=["summer"],  # Values is a list as you can select 1 AND 2
            id="checklist-input",
        ),
    ]
)

# Column 4 children
html.Img(src=app.get_asset_url('bar-chart-placeholder.png'), className="img-fluid")
```

#### Row 3

The third row has:

- column 1: a map visualisation with markers for events
- column 2: a card that displays details for a selected paralympic event, this will be dynamically generated when the
  event is clicked on

```python
# Column 1 children
html.Img(src=app.get_asset_url('map-placeholder.png'), className="img-fluid")

# Column 2 children
dbc.Card(
    [
        dbc.CardImg(src="assets/logos/1960_Rome.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("TownName 2026", className="card-title"),
                html.P(
                    "Highlights of the paralympic event will go here. This will be a sentence or two.",
                    className="card-text",
                ),
                html.P(
                    "Number of athletes: XX",
                    className="card-text",
                ),
                html.P(
                    "Number of events: XX",
                    className="card-text",
                ),
                html.P(
                    "Number of countries: XX",
                    className="card-text",
                ),
            ]
        ),
    ],
    # style={"width": "18rem"},
)
```

Run the app and check it displays as you expected. I'm no designer, the design could be improved!

### The end

Well done on reaching the end of the activities! You have now built a dashboard layout. Next week you will learn how to
create and add charts.

### Multi-page dashboard (optional for those that have a multipage layout)

To create a multi-page Dashboard see the [Dash tutorial](https://dash.plotly.com/urls)
and [dbc.Navbar()](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/).

There is a modified version of the paralympics app in week 7 starter code that divides the app into two pages.

The changes made:

1. Create a new file called paralympic_app.py
2. Move the code to create and run the Dash instance out of the original file to this new file.
3. Modify the creation of the app to include `use_pages=True`
   e.g. `app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags, use_pages=True)`
4. Rename the original file to 'map.py'
5. Make a copy of 'map.py' and name it 'charts.py'
6. Delete the code to create row_two and its selectors from map.py and remove it from the layout also
7. Delete the code to create row_three and the card from charts.py and remove it from the layout also
8. Add the import `from dash import register_page, get_asset_url` to map.py and charts.py
9. Add code at the start of `charts.py` to register the page on the
   app: `register_page(__name__, name='Charts', title='Charts')`
10. Add code at the start of `events.py` to register the page on the
    app: `register_page(__name__, name='Events', title='Events', path="/")` this sets the Events page to be the home
    page
11. In `map.py` and `charts.py`, change any `app.get_asset_url` to `get_asset_url` otherwise you will get circular
    import
    issues.
12. In `map.py` and `charts.py`, change `app.layout=` to `layout=`
13. In `paralympics_app.py` add an `app.layout` section as below. This adds a menu (navbar) and a container where the
    other pages content will be displayed. The code is adapted from the Dash multi-page app documentation and the Dash
    Bootstrap Components navbar documentation.

    ```python
    # From https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Event Details", href=dash.page_registry['pages.events']['path'])),
            dbc.NavItem(dbc.NavLink("Charts", href=dash.page_registry['pages.charts']['path'])),
        ],
        brand="Paralympics Dashboard",
        brand_href="#",
        color="primary",
        dark=True,
    )

    app.layout = html.Div([
        # Nav bar
        navbar,
        # Area where the page content is displayed
        dash.page_container
    ])
    ```
14. Run the app from paralympics_app.py. You should have two pages and a clickable menu bar.

## Final code for the single page app

```python
# This version is after the final activity in week 7
from dash import Dash, html
import dash_bootstrap_components as dbc

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap
# components (dbc)
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Define a variable that contains the meta tags
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Pass the stylesheet variable to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Variables that define the three rows of the layout
row_one = html.Div(
    dbc.Row([
        dbc.Col([html.H1("Paralympics Dashboard"), html.P(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida. Fusce "
            "efficitur posuere metus posuere malesuada. ")
                 ], width=12),
    ]),
)

row_two = html.Div(
    dbc.Row([
        dbc.Col(children=[dbc.Select(id="type-dropdown",
                                     # id uniquely identifies the element, will be needed later
                                     options=[
                                         {"label": "Events", "value": "events"},
                                         # The value is in the format of the column heading in the data
                                         {"label": "Sports", "value": "sports"},
                                         {"label": "Countries", "value": "countries"},
                                         {"label": "Athletes", "value": "participants"},
                                     ],
                                     value="events"  # The default selection
                                     ),
                          ], width=2),
        dbc.Col(children=[
            html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=4),
        dbc.Col(children=[
            dbc.Checklist(
                options=[
                    {"label": "Summer", "value": "summer"},
                    {"label": "Winter", "value": "winter"},
                ],
                value=["summer"],  # Values is a list as you can select both winter and summer
                id="checklist-input",
            ),
        ], width=2),
        dbc.Col(children=[
            html.Img(src=app.get_asset_url('bar-chart-placeholder.png'), className="img-fluid"),
        ], width=4),
    ], align="start")
)

row_three = html.Div(
    dbc.Row([
        dbc.Col(children=[
            html.Img(src=app.get_asset_url('map-placeholder.png'), className="img-fluid"),
        ], width=8),
        dbc.Col(children=[
            dbc.Card(
                [
                    dbc.CardImg(src=app.get_asset_url('logos/2022_Beijing.jpg'), top=True, style={"width": "200px"}),
                    dbc.CardBody(
                        [
                            html.H4("TownName 2026", className="card-title"),
                            html.P(
                                "Highlights of the paralympic event will go here. This will be a sentence or two.",
                                className="card-text",
                            ),
                            html.P(
                                "Number of athletes: XX",
                                className="card-text",
                            ),
                            html.P(
                                "Number of events: XX",
                                className="card-text",
                            ),
                            html.P(
                                "Number of countries: XX",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "18rem"},
            )

        ], width=4),
    ], align="start")
)

# Add an HTML layout to the Dash app.
# The layout is wrapped in a DBC Container()
app.layout = dbc.Container([
    row_one,
    row_two,
    row_three,
])

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)
    # Runs on port 8050 by default. If you have a port conflict, add the parameter port=   e.g. port=8051
```