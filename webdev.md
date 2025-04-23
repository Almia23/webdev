# WebDev Lab

## Lab 1

Q1 Table and Image Animation

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Table and Image Animation</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script>
    $(document).ready(function(){
      // Apply alternate row colors
      $("tr:odd").css("background-color", "#ddd");
      $("tr:even").css("background-color", "#fff");
      
      // Animate container from right to left on button click
      $("#moveBtn").click(function(){
        $("#container").animate({ left: "0px" }, 2000);
      });
    });
  </script>
</head>
<body>
  <button id="moveBtn">Move</button>
  <div id="container" style="position:relative; left:500px;">
    <table border="1">
      <tr>
        <td>Row1 Cell1</td>
        <td>Row1 Cell2</td>
        <td>Row1 Cell3</td>
      </tr>
      <tr>
        <td>Row2 Cell1</td>
        <td>Row2 Cell2</td>
        <td>Row2 Cell3</td>
      </tr>
      <tr>
        <td>Row3 Cell1</td>
        <td>Row3 Cell2</td>
        <td>Row3 Cell3</td>
      </tr>
    </table>
    <br>
    <img src="https://via.placeholder.com/150" alt="Placeholder Image">
  </div>
</body>
</html>
```

Q2 Calculator

```html
<!DOCTYPE html>
<html>
<head><script src="../jquery-3.7.1.min.js"></script></head>
<body>
  <input id="n1"><input id="n2">
  <button onclick="calc('+')">+</button>
  <button onclick="calc('-')">-</button>
  <button onclick="calc('*')">*</button>
  <button onclick="calc('/')">/</button>
  <div id="res"></div>
  <script>
    function calc(op){
      let a = +$('#n1').val(), b = +$('#n2').val();
      $('#res').text(eval(`${a}${op}${b}`));
    }
  </script>
</body>
</html>
```

Q3 Birthday Card

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Birthday Card</title>
  <!-- jQuery -->
  <script src="../jquery-3.7.1.min.js"></script>
  <script>
    $(document).ready(function(){
      $("#updateBtn").click(function(){
        // Read values from controls
        var bgColor = $("#bgColor").val();
        var fontName = $("#fontName").val();
        var fontSize = $("#fontSize").val();
        var borderStyle = $("input[name='borderStyle']:checked").val();
        var greetingText = $("#greetingText").val();
        
        // Apply background color, font, and font size
        $("#card").css({
          "background-color": bgColor,
          "font-family": fontName,
          "font-size": fontSize + "px"
        });
        
        // Apply border style
        if(borderStyle === "none") {
          $("#card").css("border", "none");
        } else {
          // 2px border, chosen style, black color
          $("#card").css("border", "2px " + borderStyle + " black");
        }
        
        // Update the greeting text
        $("#message").text(greetingText);
        
        // Show/hide the cake image
        if($("#defaultPic").is(":checked")){
          $("#cakeImg").show();
        } else {
          $("#cakeImg").hide();
        }
      });
    });
  </script>
</head>
<body>
  <!-- Left side controls -->
  <div style="float: left;">
    <p>Choose a background color:</p>
    <select id="bgColor">
      <option value="yellow" selected>Yellow</option>
      <option value="pink">Pink</option>
      <option value="lightblue">Light Blue</option>
      <option value="white">White</option>
    </select>
    
    <p>Choose a font:</p>
    <select id="fontName">
      <option value="Arial">Arial</option>
      <option value="Verdana" selected>Verdana</option>
      <option value="Times New Roman">Times New Roman</option>
      <option value="Courier">Courier</option>
    </select>
    
    <p>Specify a numeric font size:</p>
    <input type="number" id="fontSize" value="25">
    
    <p>Choose a border style:</p>
    <label><input type="radio" name="borderStyle" value="none" checked>None</label>
    <label><input type="radio" name="borderStyle" value="double">Double</label>
    <label><input type="radio" name="borderStyle" value="solid">Solid</label>
    
    <p>Add the Default Picture:</p>
    <label><input type="checkbox" id="defaultPic">Yes</label>
    
    <p>Enter the greeting text below:</p>
    <textarea id="greetingText" rows="4" cols="30">Happy Birthday, and many more</textarea>
    
    <br><br>
    <button id="updateBtn">Update</button>
  </div>
  
  <!-- Right side birthday card -->
  <div id="card" style="float: left; width: 300px; height: 400px; margin-left: 50px; padding: 20px; background-color: yellow;">
    <div id="message" style="text-align: center;">
      Happy Birthday, and many more
    </div>
    <img id="cakeImg" src="cake.jpeg" alt="Cake" 
         style="display: block; margin: 20px auto; width: 100px;"/>
  </div>
</body>
</html>
```

Q4 Item Bill

```html
<!DOCTYPE html>
<html>
<head><script src="../jquery-3.7.1.min.js"></script></head>
<body>
  <select id="brand">
    <option>HP</option><option>Nokia</option><option>Samsung</option><option>Motorola</option><option>Apple</option>
  </select><br>
  <input type="checkbox" value="Mobile" class="item">Mobile
  <input type="checkbox" value="Laptop" class="item">Laptop<br>
  Quantity: <input id="qty" type="number"><br>
  <button id="bill">Produce Bill</button>
  <script>
    const prices = { Mobile: 10000, Laptop: 40000 };
    $('#bill').click(() => {
      let total = 0, q = +$('#qty').val();
      $('.item:checked').each(function() {
        total += prices[this.value] * q;
      });
      alert('Total: ₹' + total);
    });
  </script>
</body>
</html>
```

AQ1 Bouncing Ball

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    #box { position: relative; width: 100px; height: 300px; border: 1px solid black; overflow: hidden; }
    #ball { width: 30px; height: 30px; border-radius: 50%; background: red; position: absolute; top: 0; left: 35px; }
  </style>
  <script src="../jquery-3.7.1.min.js"></script>
</head>
<body>
  <div id="box"><div id="ball"></div></div>
  <script>
    function bounce() {
      $('#ball').animate({ top: '270px' }, 500).animate({ top: '0px' }, 500, bounce);
    }
    bounce();
  </script>
</body>
</html>
```

AQ2 Cake popup text

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    #container { position: relative; width: 300px; }
    #container img { width: 100%; }
    #text {
      position: absolute; bottom: 0; background: rgba(0,0,0,0.5);
      color: white; width: 100%; text-align: center; display: none;
    }
  </style>
  <script src="../jquery-3.7.1.min.js"></script>
</head>
<body>
  <div id="container">
    <img src="cake.jpeg">
    <div id="text">Happy Birthday!</div>
  </div>
  <script>
    $('#container').hover(
      () => $('#text').slideDown(),
      () => $('#text').slideUp()
    );
  </script>
</body>
</html>
```

## Lab 2

Q1 Student BioData

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    label { display: block; margin-top: 8px; }
    table { margin-top: 10px; }
  </style>
</head>
<body>
  <h3>Student Bio-data</h3>
  <form>
    <label>Name: <input type="text"></label>
    <label>Gender:
      <input type="radio" name="gender">Male
      <input type="radio" name="gender">Female
    </label>
    <label>Languages:
      <input type="checkbox">English
      <input type="checkbox">Hindi
    </label>
    <table border="1">
      <tr><td>DOB</td><td><input type="date"></td></tr>
      <tr><td>Email</td><td><input type="email"></td></tr>
    </table>
    <button type="submit">Submit</button>
  </form>
</body>
</html>
```

Q2 Employee CRUD

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee CRUD Operations</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }

        h1, h2 {
            text-align: center;
        }

        form {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-top: 10px;
        }

        input {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            margin-bottom: 10px;
        }

        button {
            padding: 10px 20px;
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        th, td {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: center;
        }

        th {
            background-color: #007BFF;
            color: white;
        }
    </style>
</head>
<body>
    <h1>Employee Management System</h1>
    <form id="employeeForm">
        <input type="hidden" id="employeeId">
        <label for="name">Name:</label>
        <input type="text" id="name" required>
        <label for="position">Position:</label>
        <input type="text" id="position" required>
        <button type="submit">Submit</button>
    </form>
    <h2>Employee List</h2>
    <table id="employeeTable">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Position</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
    </table>
    <br>
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            let employees = [];
            const employeeForm = document.getElementById('employeeForm');
            const employeeTable = document.getElementById('employeeTable').getElementsByTagName('tbody')[0];

            employeeForm.addEventListener('submit', event => {
                event.preventDefault();
                const id = document.getElementById('employeeId').value;
                const name = document.getElementById('name').value;
                const position = document.getElementById('position').value;

                if (id) {
                    updateEmployee(id, name, position);
                } else {
                    createEmployee(name, position);
                }

                employeeForm.reset();
            });

            function createEmployee(name, position) {
                const id = Date.now().toString();
                employees.push({ id, name, position });
                renderEmployees();
            }

            function readEmployees() {
                return employees;
            }

            function updateEmployee(id, name, position) {
                employees = employees.map(employee => employee.id === id ? { id, name, position } : employee);
                renderEmployees();
            }

            function deleteEmployee(id) {
                employees = employees.filter(employee => employee.id !== id);
                renderEmployees();
            }

            function renderEmployees() {
                employeeTable.innerHTML = '';
                readEmployees().forEach(employee => {
                    const row = employeeTable.insertRow();
                    row.insertCell(0).innerText = employee.id;
                    row.insertCell(1).innerText = employee.name;
                    row.insertCell(2).innerText = employee.position;

                    const actionsCell = row.insertCell(3);
                    actionsCell.innerHTML = `
                        <button onclick="editEmployee('${employee.id}')">Edit</button>
                        <button onclick="deleteEmployee('${employee.id}')">Delete</button>
                    `;
                });
            }

            window.editEmployee = function (id) {
                const employee = employees.find(employee => employee.id === id);
                document.getElementById('employeeId').value = employee.id;
                document.getElementById('name').value = employee.name;
                document.getElementById('position').value = employee.position;
            }

            window.deleteEmployee = function (id) {
                deleteEmployee(id);
            }

            renderEmployees();
        });
    </script>
</body>
</html>
```

Q3 Bootstrap webpage

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bootstrap Webpage</title>
  <link href="../bootstrap-5.3.5-dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    .top-part {
      background-color: #f8f9fa;
      padding: 20px;
    }
    .bottom-part {
      background-color: #e9ecef;
      padding: 20px;
      display: flex;
      justify-content: space-between;
    }
    .bottom-section {
      flex: 1;
      margin: 0 10px;
      background-color: #fff;
      padding: 20px;
      border-radius: 5px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>

<div class="container">
  <!-- Top part -->
  <div class="top-part">
    <h2>Top Part</h2>
    <div class="input-group mb-3">
      <input type="text" class="form-control" placeholder="Enter something">
      <div class="input-group-append">
        <span class="input-group-text">@example.com</span>
      </div>
    </div>
    <button type="button" class="btn btn-primary">Button</button>
    <div class="btn-group" role="group">
      <button type="button" class="btn btn-secondary">Left</button>
      <button type="button" class="btn btn-secondary">Middle</button>
      <button type="button" class="btn btn-secondary">Right</button>
    </div>
  </div>

  <!-- Bottom part -->
  <div class="bottom-part">
    <div class="bottom-section">
      <h4>Section 1</h4>
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Enter something">
        <div class="input-group-append">
          <span class="input-group-text">@example.com</span>
        </div>
      </div>
      <button type="button" class="btn btn-success">Button 1</button>
    </div>
    <div class="bottom-section">
      <h4>Section 2</h4>
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Enter something">
        <div class="input-group-append">
          <span class="input-group-text">@example.com</span>
        </div>
      </div>
      <button type="button" class="btn btn-danger">Button 2</button>
    </div>
    <div class="bottom-section">
      <h4>Section 3</h4>
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Enter something">
        <div class="input-group-append">
          <span class="input-group-text">@example.com</span>
        </div>
      </div>
      <button type="button" class="btn btn-warning">Button 3</button>
    </div>
  </div>
</div>

<script src="../bootstrap-5.3.5-dist/js/bootstrap.min.js"></script>

</body>
</html>
```

Q4 Timetable carousel

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bootstrap Webpage</title>
  <link href="../bootstrap-5.3.5-dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    .top-part {
      background-color: #f8f9fa;
      padding: 20px;
    }
    .bottom-part {
      background-color: #e9ecef;
      padding: 20px;
      display: flex;
      justify-content: space-between;
    }
    .bottom-section {
      flex: 1;
      margin: 0 10px;
      background-color: #fff;
      padding: 20px;
      border-radius: 5px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>

<div class="container">
  <!-- Top part -->
  <div class="top-part">
    <h2>Top Part</h2>
    <div class="input-group mb-3">
      <input type="text" class="form-control" placeholder="Enter something">
      <div class="input-group-append">
        <span class="input-group-text">@example.com</span>
      </div>
    </div>
    <button type="button" class="btn btn-primary">Button</button>
    <div class="btn-group" role="group">
      <button type="button" class="btn btn-secondary">Left</button>
      <button type="button" class="btn btn-secondary">Middle</button>
      <button type="button" class="btn btn-secondary">Right</button>
    </div>
  </div>

  <!-- Bottom part -->
  <div class="bottom-part">
    <div class="bottom-section">
      <h4>Section 1</h4>
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Enter something">
        <div class="input-group-append">
          <span class="input-group-text">@example.com</span>
        </div>
      </div>
      <button type="button" class="btn btn-success">Button 1</button>
    </div>
    <div class="bottom-section">
      <h4>Section 2</h4>
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Enter something">
        <div class="input-group-append">
          <span class="input-group-text">@example.com</span>
        </div>
      </div>
      <button type="button" class="btn btn-danger">Button 2</button>
    </div>
    <div class="bottom-section">
      <h4>Section 3</h4>
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Enter something">
        <div class="input-group-append">
          <span class="input-group-text">@example.com</span>
        </div>
      </div>
      <button type="button" class="btn btn-warning">Button 3</button>
    </div>
  </div>
</div>

<script src="../bootstrap-5.3.5-dist/js/bootstrap.min.js"></script>

</body>
</html>
```

AQ1 Train Ticket

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    form { max-width: 300px; margin: auto; border: 1px solid #ccc; padding: 10px; border-radius: 10px; }
    label, input, select { display: block; width: 100%; margin-top: 10px; }
  </style>
</head>
<body>
  <form>
    <h3>Train Ticket Booking</h3>
    <label>Name <input type="text"></label>
    <label>From <input type="text"></label>
    <label>To <input type="text"></label>
    <label>Date <input type="date"></label>
    <label>Class
      <select><option>1A</option><option>2A</option><option>SL</option></select>
    </label>
    <button>Book Now</button>
  </form>
</body>
</html>
```

AQ2 Magazine cover

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="../bootstrap-5.3.5-dist/css/bootstrap.min.css">
  <style>
    .cover { background: url('cover.jpg') no-repeat center/cover; height: 100vh; color: white; text-shadow: 2px 2px 4px #000; }
  </style>
</head>
<body>
  <div class="cover d-flex flex-column justify-content-center align-items-center">
    <h1 class="display-2">Tech Today <span class="badge bg-danger">New</span></h1>
    <p class="lead">AI, Gadgets, Trends</p>
    <div class="btn-group">
      <button class="btn btn-primary">Subscribe</button>
      <button class="btn btn-outline-light">Read More</button>
    </div>
  </div>
</body>
</html>
```

## Lab 3

Q1 Mean, Variance, Std Dev from List

```python
def stats(nums):
    m = sum(nums)/len(nums)
    var = sum((x-m)**2 for x in nums)/len(nums)
    print(f"Mean: {m}, Variance: {var}, Std Dev: {var**0.5}")

nums = list(map(int, input("Enter numbers: ").split()))
stats(nums)
```

Q2 Student Details

```python
def student():
    s = input("Name RollNo Dept Addr Gender Marks1 Marks2 Marks3: ").split()
    name, marks = s[0], list(map(int, s[5:]))
    total, pct = sum(marks), sum(marks)/3
    print(f"{s[:5]}, Total: {total}, %: {pct}")
    return name, total, any(m<10 for m in marks)

students = [student() for _ in range(3)]
print("Max:", max(students, key=lambda x:x[1])[0])
print("Min:", min(students, key=lambda x:x[1])[0])
print("Fails:", [s[0] for s in students if s[2]])
```

Q3 10 most frequent words

```python
def top_words(fname):
    from collections import Counter
    with open(fname) as f:
        words = f.read().split()
    for w,c in Counter(words).most_common(10): print(w,c)

top_words("file.txt")
```

Q4 Sort word file

```python
# Read contents from the input file
with open("file.txt", "r") as file:
    lines = file.readlines()

# Strip whitespace, sort the lines, and write to output file
with open("output.txt", "w") as file:
    for line in sorted(line.strip() for line in lines):
        file.write(line + "\n")
```

AQ1 World Cup Winners

```python
def world_cup():
    d = {1975:'WI', 1979:'WI', 1983:'IND', 1987:'AUS', 1992:'PAK', 1996:'SL', 1999:'AUS', 2003:'AUS', 2007:'AUS', 2011:'IND', 2015:'AUS', 2019:'ENG'}
    from collections import Counter
    c = Counter(d.values())
    print("Best:", c.most_common(1)[0][0])
    print("Winners:", set(d.values()))

world_cup()
```

AQ2 Zip folder

```python
def backup(folder):
    import zipfile, os
    with zipfile.ZipFile(folder+'.zip','w') as z:
        for f in os.listdir(folder):
            z.write(os.path.join(folder,f))

backup("test_folder")  # replace with folder name
```

AQ3 Division by zero

```python
def DivExp(a,b):
    assert a>0, "a must be > 0"
    if b==0: raise ZeroDivisionError("b can't be 0")
    return a/b

a,b = map(int, input("Enter a b: ").split())
try: print("Result:", DivExp(a,b))
except Exception as e: print(e)
```

## Lab 4

Q1 Unique subsets from integers

```python
class Subsets:
    def get(self, nums):
        res = [[]]
        for n in nums:
            res += [r+[n] for r in res]
        return res

print(Subsets().get([1,2,3]))
```

Q2 Pair of elements that equal target

```python
class PairFinder:
    def find(self, nums, target):
        m = {}
        for i, n in enumerate(nums):
            if target-n in m: return [m[target-n], i]
            m[n] = i

print(PairFinder().find([2, 7, 11, 15], 9))
```

Q3 Item class

```python
class Inventory:
    def __init__(i): i.data = {}
    def add_item(i, id, name, count, price): i.data[id] = {"name": name, "count": count, "price": price}
    def update_item(i, id, count=None, price=None):
        if count is not None: i.data[id]["count"] = count
        if price is not None: i.data[id]["price"] = price
    def check_item_details(i, id): print(i.data.get(id))

inv = Inventory()
inv.add_item(101, "Pen", 50, 10)
inv.update_item(101, count=60)
inv.check_item_details(101)
```

Q4 Restaurant

```python
class Restaurant:
    def __init__(r):
        r.menu, r.tables, r.orders = {}, [], []
    def add_item_to_menu(r, name, price): r.menu[name] = price
    def book_tables(r, num): r.tables.append(num)
    def customer_order(r, item): r.orders.append(item)
    def show(r): print("Menu:", r.menu); print("Tables:", r.tables); print("Orders:", r.orders)

res = Restaurant()
res.add_item_to_menu("Pizza", 150)
res.add_item_to_menu("Burger", 80)
res.book_tables(5)
res.customer_order("Pizza")
res.show()
```

AQ1 Caps string

```python
class Stringer:
    def get_String(s): s.txt = input("Enter: ")
    def print_String(s): print(s.txt.upper())

s = Stringer(); s.get_String(); s.print_String()
```