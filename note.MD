# String Python
## Chuỗi
- Chiều dài chuỗi hãy sử dụng hàm len().

- Để kiểm tra 1 cụm từ có trong chuỗi hay không ta sử dụng từ khóa "in"
    - Ví dụ: 
        - txt = "The best things in life are free"
        - print("free" in txt)
- Ngược lại sử dụng từ khóa "not in" để kiểm tra 1 cụm từ không có trong chuỗi hay không.

## Slicing Strings: 
- Slicing:
    - Ví dụ:
        - b = "Hello, world!"
        - print(b[2:5]) => "llo"
- Slice from the start:
    - example:
        - b = "Hello, world!"
        - print(b[:5]) => "Hello"
- Slice from the end:
    - example:
        - b = "Hello, world!"
        - print(b[2:]) => "llo, world!"
- Negative indexing:
    - example:
        - b = "Hello, world!"
        - print(b[-5:-2]) => "orl"

## Modify Strings
### Upper case:
    - example:
        - a = "Hello, world!"
        - print(a.upper()) => "HELLO, WORLD"

### Lower Case:
    - example:
        - a = "Hello, world!"
        - print(a.lower()) => "hello, world!"

## Remove Whitespace:
    - example:
        - a = " Hello, world!"
        - print(a.strip()) => "Hello, world!"

## Replace string:
    - example:
        - a = " Hello, world!"
        - print(a.replace("H", "J)) => "Jello, world!"

## Split String:
    - example:
        - a = "Hello, world!"
        - print(a.split(",")) => ["Hello, world!"]

# Python Lists
## Python Lists
    - Lists được dùng để lưu trữ nhiều item trong 1 biến
    - Lists được sắp xếp, thay đổi và cho phép trùng lặp.
    - Python Collections (Arrays)
        - List: là 1 bộ sưu tập được sắp xếp và có thể thay đổi. Cho phép các item trùng lặp.
        - Tuple: là 1 bộ sưu tập được sắp xếp và không thể thay đổi. Cho phép các item trùng lặp.
        - Set: là 1 bộ sưu tập không có thứ tự, không thể thay đổi và không được lập chỉ mục. Không có item trùng lặp.
        - Dictionary: là 1 collection được sắp xếp và có thể thay đổi. Không có thành viên trùng lặp.
## Add List Items
    - Để thêm 1 item vào cuối danh sách, ta sử dụng hàm append().
    - Để thêm 1 item và 1 index cụ thể, ta sử dụng hàm insert().
    - Để thêm 1 list khác vào list hiện tại, hãy sử dụng hàm extend(). // giống array_merge() của PHP 
    - Hàm extend() không chỉ nối thêm list, mà ta có thể thêm bất kỳ đối tượng có thể lặp lại nào (tuple, set, dictionary)

## Remove List Items
    - thisList = ["apple", "orange", "banana"]
    - Phương thức remove() được dùng để loại bỏ mục chỉ định. Nếu list có nhiều giá trị được chỉ định, thì nó sẽ xóa giá trị đầu tiên xuất hiện.
    - Phương thức pop(): 
        - Loại bỏ chỉ mục đã chỉ định, nếu không được chỉ định index thì nó sẽ xóa chỉ mục cuối.
        - Ví dụ: thisList.pop(1)
    - Từ khóa del xóa 1 index đã chỉ định
        - ví dụ: del thisList[0]
    Từ khóa này cũng có thể xóa toàn bộ list

    - Phương thức clear(): làm trống list => trả về mảng hoặc collection rỗng.

# Loop Lists
## Loop through a list
    - Có thể lặp qua các mục trong list bằng cách sử dụng vòng lặp 'for'.
        - Ví dụ:
            thisList = ["apple", "orange", "banana"]
            for x in thisList:
                print(x)

### Loop through the index numbers
    - Có thể lặp qua các mục trong danh sách bằng cách tham khảo số chỉ mục của chúng.
    - Sử dụng các hàm range() và len() để tạo 1 vòng lặp phù hợp.
    - Ví dụ:
        thisList = ["apple", "orange", "banana"]
        for i in range(len(thisList)):
            print(thisList[i])

## Sử dụng vòng lặp while:
    - có thể lặp qua các mục trong danh sách bằng cách sử dụng vòng lặp while.
    - Sử dụng hàm len() để xác định độ dài.
    - Ví dụ: 
        thisList = ["apple", "orange", "banana"]
        i = 0
        while i < len(thisList):
            print(thisList[i])
            i = i + 1

## Looping using list comprehension
    - Ví dụ:
        thisList = ["apple", "orange", "banana"]
        [print(x) for x in thisList]

## Sort lists
### Sort list alphanumberically
    - Các đối tượng danh sách có 1 phương thức sort() sẽ sắp xếp danh sach theo thứ tự chữ và số, tăng dần theo mặc định

### Sort Descending
    - Để sắp xếp theo chiều ngược lại, ta sử dụng đối số reverse = True
    - Ví dụ: list.sort(reverse = True)

### Customize sort function
    - Bạn có thể tùy chỉnh chức năng của riêng mình bằng cách sử dụng từ khóa đối số .key = function
    - Hàm sẽ trả về một số sẽ được sử dụng để sắp xếp danh sách(Số thấp nhất trước):
    - Ví dụ:
        def myFunc(n):
            return abs(n-50)
        
        thisList = [100, 50, 65, 82, 23]
        thisList.sort(key = myFunc)
        print(thisList)

### Case Insensitive sort
    - Theo mặc định, phương thức sort() này phân biệt chữ hoa chữ thường, dẫn đễ tất cả các chữ cái viết hoa được sắp xếp trước chữ cái viết thường.
    - Nếu muốn hàm sắp xếp không phân biệt hoa thường, hãy sử dụng hàm chính str.low.
    - Ví dụ:
        thislist = ["banana", "Orange", "Kiwi", "cherry"]
        thislist.sort(key = str.lower)
        print(thislist)

### Reverse Order
    - Phương thức reverse() đảo ngược thứ tự sắp xếp hiện tại của các phần tử.
    - Ví dụ:
        thislist = ["banana", "Orange", "Kiwi", "cherry"]
        thislist.reverse()
        print(thislist)

## Copy Lists
### Copy a list
    - Có nhiều cách để tạo 1 bản sao, 1 cách là sử dụng phương thức List có sẵn copy()
    - Ví dụ:
        thislist = ["apple", "banana", "cherry"]
        mylist = thislist.copy()
        print(mylist)

    - Một cách khác để tạo bản sao là sử dụng phương thức list():
    - Ví dụ:
        thislist = ["apple", "banana", "cherry"]
        mylist = list(thislist)
        print(mylist)

## Join Lists
### Join two lists
    - Có 1 số cách để nối hoặc ghép hai hoặc nhiều danh sách trong Python
    - Một trong nhưng cách dễ nhất là sử dụng toán tử +
    - Ví dụ:
        list1 = ["a", "b", "c"]
        list2 = [1, 2, 3]

        list3 = list1 + list2
        print(list3)

    - Một cách # để nối 2 danh sách là thêm tất cả các mục từ list2 và list1, từng mục một
    - Ví dụ:
        list1 = ["a", "b" , "c"]
        list2 = [1, 2, 3]

        for x in list2:
        list1.append(x)

    - Hoặc ta có thể sử dụng phương thức extend(), với mục đích là thêm các phần tử từ danh sach này sang danh sách khác:
    - Ví dụ:
        list1 = ["a", "b" , "c"]
        list2 = [1, 2, 3]

        list1.extend(list2)
        print(list1)

## List Methods
    - append()	Adds an element at the end of the - list
    - clear()	Removes all the elements from the list
    - copy()	Returns a copy of the list
    - count()	Returns the number of elements with the - specified value
    - extend()	Add the elements of a list (or any - iterable), to the end of the current list
    - index()	Returns the index of the first element - with the specified value
    - insert()	Adds an element at the specified - position
    - pop()	Removes the element at the specified - position
    - remove()	Removes the item with the specified - value
    - reverse()	Reverses the order of the list
    - sort()	Sorts the list

## Python Tuples
### Tuple
    - Được sử dụng để lưu trữ nhiều mục trong 1 biến duy nhất.
    - Là 1 bộ sư tập được sắp xếp theo thứ tự và không thể thay đổi.
    - Ví dụ:
        thistuple = ("apple", "banana", "cherry")
        print(thistuple)
### Tuple Items
    - Các mục trong bộ dữ liệu được sắp xếp theo thứ tụ, không thể thay đổi và cho phép các giá trị trùng lặp.
    - Các mục tuple được lập chỉ mục, như 1 list thông thường bắt đầu từ 0
### Ordered
    - Các bộ dữ liệu được sắp xếp theo thứ tự, điều đó có nghĩa là các mục có 1 thứ tự xác định và thứ tự đó sẽ không thay đổi.
### Unchangeable
    - Các bộ dữ liệu không thể thay đổi, nghĩa là chúng ta không thể thay đổi, thêm hoặc bớt các mục sau khi bộ dữ liệu đã được tạo
### Allow duplicates
### Tuple length
### Create tuple with one item
### Tuple items - data types


## Python If else
- Equals: a == b
- Not Equals: a != b
- Less than: a < b
- Less than or equal to: a <= b
- Greater than: a > b
- Greater than or equal to: a >= b

### Elif
    - tương tự else if trong PHP
    - Ví dụ:
        a = 33
        b = 33
        if b > a:
        print("b is greater than a")
        elif a == b:
        print("a and b are equal")

### Else
### Short hand if
    - Ví dụ:
        if a > b: print("a is greater than b")

### Short hand if ...else
    - Nếu bạn chỉ cần 1 dòng để xử lý, 1 dành cho if và 1 dành cho else bạn có thể đặt tất cả và trong cùng 1 dòng.
    - Ví dụ:
        a = 2
        b = 330
        print("A") if a > b else print("B")
    
    - Cũng có thể có nhiều câu lệnh else trên cùng 1 dòng.
    - Ví dụ:
        a = 330
        b = 330
        print("A") if a > b else print("=") if a == b else print("B")

### And
    - tường tự toán sử tử logic && trong PHP
    - Ví dụ:
        a = 200
        b = 33
        c = 500
        if a > b and c > a:
        print("Both conditions are True")

### Or
### Not
### Nested if (lồng nhau)
### The pass statement
    - trả về dạng void, tức là no content

## Python while loops
## Python For loops
    - Vòng lặp for được sử dụng để lặp lại 1 chuỗi (list, set, dictionary, ...)
    - Từ khóa for ít giống trong các ngôn ngữ lập trình khác và hoạt động giống  1 phương thức lặp hơn như được tìm thấy trong các ngôn nghữ lập trình hướng đối tượng khác.
    - Để ngắt vòng lặp ta có thể dùng từ khóa break.
    - Ví dụ:
        fruits = ["apple", "banana", "cherry"]
        for x in fruits:
        print(x)
        if x == "banana":
            break

    - Để bỏ qua 1 vòng lặp ta có thể sử dụng từ khóa continue.
    - Ví dụ:
        fruits = ["apple", "banana", "cherry"]
        for x in fruits:
        if x == "banana":
            continue
        print(x)

    - Hàm range() để lặp qua 1 bộ mã với số lần xác định.
    - Ví dụ:
        for x in range(6):
            print(x)
    
    - Từ khóa else sẽ được chạy khi vòng lặp kết thúc, và nó sẽ không hoạt động nếu gặp break.
    - Ví dụ:
        for x in range(6):
            print(x)
        else:
            print("Finally finished!")

    - Các vòng lặp không thể trống, nhưng nếu vì lý do nào đó bạ có 1 vòng lặp for mà không có nội dụung, hãy đưa câu lệnh pass để tránh gặp lỗi.
    - Ví dụ:
        for x in [0, 1, 2]:
            pass

## Python Functions
- Function là 1 khối code chỉ được chạy khi được gọi.
### Arbitrary Arguments, *args
    - Nếu bạn không có bao nhiêu đối số sẽ được truyền vào hàm, hãy thêm * trước tên tham số trong hàm đã định nghĩa.
    - Ví dụ:
        def my_function(*kids):
            print("The youngest child is " + kids[2])

        my_function("Emil", "Tobias", "Linus")


### Arbitrary Keyword Arguments, **kwargs (Đối số từ khóa tùy ý)
    - Nếu bạn không biết có bao nhiêu đối số từ khóa sẽ được truyền vào hàm của mình, hãy thêm hai dấu hoa thị: ** trước tên tham số trong định nghĩa hàm.
    - Bằng cách này, hàm sẽ nhận được 1 từ điển các đối số và có thể truy cập các mục tương ứng.
    - Ví dụ:
        def my_function(**kid):
            print("His last name is " + kid["lname"])

        my_function(fname = "Tobias", lname = "Refsnes")

## Python Lambda
    - Lambda function laf 1 hàm ẩn danh nhỏ.
    - Hàm lambda có thể nhận bất kỳ số lượng đối số nào nhưng chỉ có thể có 1 biểu thức.
    - Cú pháp: lambda arguments : expression
    - ví dụ:
        x = lambda a : a + 10
        print(x(5))

### Tại sao nên sử dụng hàm lambda?
    - Sức mạnh của lambda được thể hiện rõ hơn khi bạn sử dụng chúng như một hàm ẩn danh bên trong 1 hàm khác.
    - Giả sử bạn có 1 hàm định nghĩa nhận vào 1 đối số và đối số đó sẽ được nhân với 1 số chưa xác định:
        def myfunc(n):
            return lambda a : a * n

    - Hoặc sử dụng hàm định nghĩa tương tự để tạo 1 hàm luôn nhân 3 số bạn gửi vào:
        def myfunc(n):
            return lambda a : a * n

        mytripler = myfunc(3)

        print(mytripler(11))

## Python Arrays
- Lưu ý: Hướng dẫn bạn cách sử dụng Lists dưới dạng Arrays, tuy nhiên để làm viếc với mảng trong Python, bạn sẽ phải nhập 1 thư viện, như thư viên NumPy.
- Phương thức mảng:
    - append():	Adds an element at the end of the list
    - clear():	Removes all the elements from the list
    - copy():	Returns a copy of the list
    - count():	Returns the number of elements with the specified value
    - extend():	Add the elements of a list (or any iterable), to the end of the current list
    - index():	Returns the index of the first element with the specified value
    - insert():	Adds an element at the specified position
    - pop()	Removes the element at the specified position
    - remove():	Removes the first item with the specified value
    - reverse():	Reverses the order of the list
    - sort():	Sorts the list

## Python Classes and Objects
- Python là 1 ngôn ngữ hướng đối tượng
- Hầu hết mọi thứ trong Python đều là 1 đối tượng, vói các thuộc tính và phương thức.
- Class giống như 1 hàm tạo đối tượng hoặc 1 "bản thiết kế" để tạo đối tượng.

### Create a class
- để tạo 1 class ta sử dụng từ khóa class:
- Ví dụ:
    class MyClass:
        x = 5

### Create object
- ví dụ:
    p1 = MyClass()
    print(p1.x)

### The __init__() function
    - hàm __init__(), hàm này luôn được thực thi khi lướp được khởi tạo.
    - Sử dụng hàm __init__() để gán giá trị cho thuộc tính đối tượng hoặc các thao tác khác cần thực hiện khi đối tượng được tạo:
    - Ví dụ:
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        p1 = Person("John", 36)

        print(p1.name)
        print(p1.age)

### The __str__() function
    - Hàm __str__() kiểm soát nhưng gì sẽ được trả về khi đối tượng lớp được biểu diễn dưới dạng 1 chuỗi.
    - nếu hàm __str__() ko được đặt biểu diễn chuỗi của đối tượng sẽ được trả về.
    - Ví dụ:
        - Biểu diễn chuỗi của một đối tượng KHÔNG CÓ hàm __str__():
            class Person:
                def __init__(self, name, age):
                    self.name = name
                    self.age = age

            p1 = Person("John", 36)

            print(p1)

        - Biểu diễn chuỗi của một đối tượng VỚI hàm __str__():
            class Person:
                def __init__(self, name, age):
                    self.name = name
                    self.age = age

                def __str__(self):
                    return f"{self.name}({self.age})"

            p1 = Person("John", 36)

            print(p1)

### Object Methods
    - Các đối tượng cũng có thể chứa các phương thức. Các phương thức trong đối tượng là các hàm thuộc về đối tượng.
    - Ví dụ:
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def myfunc(self):
                print("Hello my name is " + self.name)

        p1 = Person("John", 36)
        p1.myfunc()

#### Luư ý: Tham ssoo self này là tham chiếu đến phiên bản hiện tại của lớp và được sử dụng để truy cập các biến thuộc lớp.

### The self Parameter
    - Nó không cần phải được đặt tên là self, bạn có thể gọi nó là gì bạn thích, nhưng nó phải là tham số đầu tiên của bất kỳ hàm nào trong lớp.
    - Ví dụ:
        class Person:
            def __init__(mysillyobject, name, age):
                mysillyobject.name = name
                mysillyobject.age = age

            def myfunc(abc):
                print("Hello my name is " + abc.name)

        p1 = Person("John", 36)
        p1.myfunc()

### Modify Object properties
    - Bạn có thể sử đổi thuộc tính trên các đối tượng như thế này:
    - Ví dụ:
        p1.age = 40

### Delete object properties
    - Bạn có thể xóa thuộc tính của 1 đối tượng bằng cách sử dụng từ khóa del.
    - Ví dụ:
        del p1.age

### Delete object
    - Có thể xóa 1 đối tượng bằng có sử dụng từ khóa del.
    - Ví dụ:
        del p1

### The pass statement
    - Định nghĩa class không được để trong, nhưng nếu vì lý do nào đó bạn có định nghĩa class ko có nội dung thì hãy đưa câu lệnh pass vào để tránh bị lỗi.
    - Ví dụ:
        class Person:
            pass

## Python Inheritance
    - Kế thừa cho phép chúng ta định nghĩa 1 lớp kế thừa tắt cả các phương thức và thuộc tính từ 1 lớp khác.
    - Class cha là lớp được kế thừa từ đó, còn được gọi là lớp cở sở.
    - Class con là lớp kế thừa từ lớp khác, còn gọi là lớp dẫn xuất.

### Create a parent class
     - Ví dụ:
        class Person:
            def __init__(self, fname, lname):
                self.firstname = fname
                self.lastname = lname

            def printname(self):
                print(self.firstname, self.lastname)

            #Use the Person class to create an object, and then execute the printname method:

        x = Person("John", "Doe")
        x.printname()

### Create a child class
    - Ví dụ:
        class Student(Person):
            pass

### __init__() function
    - Khi bạn thêm hàm __init__(), lớp con sẽ không còn kế thừa hàm __init__() của lớp cha nữa.
    - Lưu Y: __init__() con sẽ ghi đè sự kế thừa của hàm __init__() cha.
    - Để giữ tính kế thừa hàm __init__(), hàm thêm lệnh gọi vào hàm __init__() cha.
    - Ví dụ:
        class Student(Person):
            def __init__(self, fname, lname):
                Person.__init__(self, fname, lname)

### super() Function
    - Python cũng có 1 hàm super() sẽ làm cho lớp con kế thừa tất cả các phương thức và thuộc tính từ lóp cha của nó:
    - Ví dụ:
        class Student(Person):
            def __init__(self, fname, lname):
                super().__init__(fname, lname)

    - Khi bạn sử dụng hàm super(), bạn không cần phải sử dụng tên của phần tử cha, nó sẽ tự động kế thừa các phương pháp và thuộc tính từ phần tử cha của nó.

### Add properties
    - Ví dụ:
        class Student(Person):
            def __init__(self, fname, lname):
                super().__init__(fname, lname)
                self.graduationyear = 2019

### Add Methods
    - Ví dụ:
        class Student(Person):
            def __init__(self, fname, lname, year):
                super().__init__(fname, lname)
                self.graduationyear = year

            def welcome(self):
                print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

## Python Iterator
    - Trình vòng lặp là 1 đối tượng chứa một số lượng giá trị có thể đếm được.
    - Trình vòng lặp là 1 đối tượng có thể được lặp lại, nghĩa là bạn có thể duyệt qua tất cả các giá trị.
    - Về mặt kỹ thuật, trong Python, iterator là 1 đối tượng thực hiện giao thức iterator, bao gồm các phương thức __iter__() và __next__().

### Interator vs Iterable
    -   Lists, tuples, dictionaries and sets đều là các đối tượng có thể lặp lại. Chúng là các thùng chứa có thể lặp lại mà bạn có thể lấy 1 trong vong lặp từ đó.
    - Tất cả các đối tượng này đều có 1 phương thức iter() được sử dụng để lấy 1 trình vòng lặp.
    - Ví dụ:
        mytuple = ("apple", "banana", "cherry")
        myit = iter(mytuple)

        print(next(myit))
        print(next(myit))
        print(next(myit))

    - Ngay cả các chuỗi cũng là các đối tượng có thể lặp lại và có thể tả về 1 trình vòng lặp.
    - Ví dụ:
        mystr = "banana"
        myit = iter(mystr)

        print(next(myit))
        print(next(myit))
        print(next(myit))
        print(next(myit))
        print(next(myit))
        print(next(myit))

### Create a iterator
    - Phương thức __iter__() hoạt động tương tự phương thức __init__(), có thể thực hiện các thao tác khởi tạo..., nhưng phải luôn trả về chính đối tượng iterator.
    - Phương thức __next__() cũng cho phép bạn thực hiện các thao tác và phải trả về mục tiếp theo trong chuỗi.
    - Ví dụ:
        class MyNumbers:
            def __iter__(self):
                self.a = 1
                return self

            def __next__(self):
                x = self.a
                self.a += 1
                return x

        myclass = MyNumbers()
        myiter = iter(myclass)

        print(next(myiter))
        print(next(myiter))
        print(next(myiter))
        print(next(myiter))
        print(next(myiter))

### Stop
    - để ngăn việc lặp lại diễn ra mãi mãi, chúng ta có thể sử dụng câu lệnh StopIteration.
    - Trong phương thức __next__(), ta có thể thêm điều kiện kết thúc để phải sinh lỗi nếu việc lặp lại được thực hiện 1 số lần xác định.
    - Ví dụ:
        class MyNumbers:
            def __iter__(self):
                self.a = 1
                return self

            def __next__(self):
                if self.a <= 20:
                x = self.a
                self.a += 1
                return x
                else:
                raise StopIteration

        myclass = MyNumbers()
        myiter = iter(myclass)

        for x in myiter:
            print(x)

## Python Polymorphism (Tính đa hình)
    - Từ "đa hình" có nghĩa là "many forms" và trong lập trình, nó đề cập đến các phương thức/hàm/ toán từ có cùng tên có thể được thực thi trên nhiều đối tượng hoặc lớp.

### Function polymorphism (Đa hình hàm)
### Class polymorphism (đa hình lớp)
    - Ví dụ:
        class Car:
            def __init__(self, brand, model):
                self.brand = brand
                self.model = model

            def move(self):
                print("Drive!")

            class Boat:
            def __init__(self, brand, model):
                self.brand = brand
                self.model = model

            def move(self):
                print("Sail!")

            class Plane:
            def __init__(self, brand, model):
                self.brand = brand
                self.model = model

            def move(self):
                print("Fly!")

        car1 = Car("Ford", "Mustang")       #Create a Car class
        boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
        plane1 = Plane("Boeing", "747")     #Create a Plane class

        for x in (car1, boat1, plane1):
        x.move()

### Inheritance class polymorphism (Đa hình lớp kế thừa)
    - Ví dụ:
        class Vehicle:
            def __init__(self, brand, model):
                self.brand = brand
                self.model = model

            def move(self):
                print("Move!")

            class Car(Vehicle):
            pass

            class Boat(Vehicle):
            def move(self):
                print("Sail!")

            class Plane(Vehicle):
            def move(self):
                print("Fly!")

        car1 = Car("Ford", "Mustang") #Create a Car object
        boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
        plane1 = Plane("Boeing", "747") #Create a Plane object

        for x in (car1, boat1, plane1):
        print(x.brand)
        print(x.model)
        x.move()

    - Lớp con kế thừa các thuộc tính và phương thức từ lớp cha
    
## Python scrope (Tính phạm vi)
    - Một biến chỉ có sẵn trong vùng mà nó được tạo ra. Điều này được gọi là scope(phạm vi).

### Local scope
    - 1 biến được tạo bên trong 1 hàm thuộc phạm vi cục bộ của hàm đó và chỉ có thể được sử dụng bên trong hàm đó.
    - Ví dụ:   
        def myfunc():
            x = 300
            print(x)

        myfunc()

#### Function inside function (Hàm bên trong hàm)
    - Ví dụ:
        def myfunc():
            x = 300
            def myinnerfunc():
                print(x)
            myinnerfunc()

        myfunc() => 300

### Global scope
    - Biến được tạo trong phần chình của mã python là biến toàn cục và thuộc phạm vi toàn cục.
    - Các biến toàn cục có sẵn trong mọi phạm vi, toàn cục và cục bộ.
    - Ví dụ:
        x = 300

        def myfunc():
                print(x)    

        myfunc()
        print(x)
    - 1 Biến được tạo bên ngoài hàm là biến toàn cục và bất kỳ ai cũng có thể sử dụng.

### Global key:
    - Nếu cần tạo 1 biến toàn cục nhưng bị kẹt trong phạm vi cục bộ, ta có thể sử dụng từ khóa global.
    - Từ khóa global làm cho biến có tính toàn cục.
    - Ví dụ:
        def myfunc():
            global x
            x = 300

        myfunc()

        print(x)

    - Ngoài ra, hãy sử dụng từ khóa global nếu muốn thay đổi biến toàn cục bên trong hàm.
    - Ví dụ:
        x = 300

        def myfunc():
            global x
            x = 200

        myfunc()

        print(x)

### Nonlocal key:
    - Từ khóa nonlocal được sử dụng để làm việc với các biến bên trong các hàm lồng nhau.
    - Từ khóa này làm cho biến thuộc về hàm bên ngoài.
    - Ví dụ:
        def myfunc1():
            x = "Jane"
            def myfunc2():
                nonlocal x
                x = "hello"
            myfunc2()
            return x

        print(myfunc1()) // hello


## Python modules
### What is module:
    - Hãy coi 1 module giống như 1 thư viện mã.
    - 1 tệp chứa tập hợp các hàm bạn muốn đưa vào ứng dụng của mk.

### Create a module
    - Để tạo 1 module, chỉ cần lưu mã bạn muốn vào 1 tệp có phầm mở rộng tệp .py
    - Ví dụ: lưu code và 1 tệp có tên là mymodule.py
        def greeting(name):
            print("Hello, " + name)

### Use a module
    - Để có thể sử dụng module mà ta vừa tạo ta sử dụng câu lệnh import.
    - Ví dụ:
        import mymodule

        mymodule.greeting("Jonathan")

### Variables in module
    - Module có thể chứa các hàm, như đc mô tả, nhưng cũng có thể chứa các biến thoại mọi loại (list, dictionary, object, ...).
    - Ví dụ: Lưu mã này vào tập tinmymodule.py
        person1 = {
            "name": "John",
            "age": 36,
            "country": "Norway"
        }

    Nhập mô-đun có tên mymodule và truy cập từ điển Person1:
        import mymodule

        a = mymodule.person1["age"]
        print(a)

### Naming a module
### Re-naming a module
    - Ví dụ:
        import mymodule as mx

        a = mx.person1["age"]
        print(a)

### Built-in modules
    - Ví dụ:
        import platform

        x = platform.system()
        print(x)

### Using the dir() function
    - Có 1 hàm tích hợp để liệt kê tất cả các tên hàm (hoặc biến) trong 1 module. Chức năng dir():
    - Ví dụ:
        import platform

        x = dir(platform)
        print(x)
    - Lưu ý: hàm dir() có thể dược sử dụng trên tất cả các module, kể cả những module bạn tự tạo.

### Input from mmodule
    - Bạn có thể chọn chỉ nhập các phần tù module bằng cách sử dụng từ khóa from:
    - Ví du: Module có tên mymodulecó một chức năng và một từ điển:
        def greeting(name):
        print("Hello, " + name)

        person1 = {
            "name": "John",
            "age": 36,
            "country": "Norway"
        }
    Chỉ nhập từ điển Person1 từ mô-đun:
        from mymodule import person1

        print (person1["age"])