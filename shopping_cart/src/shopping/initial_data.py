from customer import Customer
from department import Department
from item import Item

nextDepartmentId = 1
nextItemId = 1

def createDepartment(name):
    global nextDepartmentId
    dept = Department(name, nextDepartmentId)
    nextDepartmentId += 1
    return dept
    
def createItem(name, departmentId, price):
    global nextItemId
    item = Item(name, nextItemId, departmentId, price)
    nextItemId += 1
    return item
    
def initialize():
    books = createDepartment("Books")
    music = createDepartment("Music")
    software = createDepartment("Software")
    video = createDepartment("Video")
    
    books.addItem(createItem("Bailees favorite book 1", books, 9.99))
    books.addItem(createItem("Bailees favorite book 2", books, 12.95))
    books.addItem(createItem("Bailees favorite book 3", books, 8.98))
    
    music.addItem(createItem("Bailees favorite song 1", music, .99))
    music.addItem(createItem("Bailees favorite song 2", music, .99))
    music.addItem(createItem("Bailees favorite albulm 1", music, 12.16))
    
    software.addItem(createItem("FincherNet Ultimate", software, 1200.00))
    software.addItem(createItem("Microsoft Office", software, 99.99))
    software.addItem(createItem("FincherNet Ultimate Pro", software, 9000.00))
    
    video.addItem(createItem("Bailees favorite movie 1", video, 9.99))
    video.addItem(createItem("Bailees favorite movie 2", video, 11.00))
    video.addItem(createItem("Bailees favorite movie 3", video, 8.95))
    
    departments = [books, music, software, video]
    customers = [Customer("Fred"), Customer("Wilma"), Customer("Barney"), Customer("Betty")]
    
    return (departments, customers)
    