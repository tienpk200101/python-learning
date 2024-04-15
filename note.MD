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