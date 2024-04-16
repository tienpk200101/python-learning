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
    - nếu hàm __str__() ko được đặtm biểu diễn chuỗi của đối tượng sẽ được trả về.
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