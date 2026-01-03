---
title: 博客第二次改版的说明及一些笔记
date: 2024/10/24
categories: 软件使用
tags:
  - blog
  - python
  - pelican

---

- [升级说明](#升级说明)
- [升级博客过程中的笔记(由 ChatGPT 生成)](#升级博客过程中的笔记由-chatgpt-生成)
  - [类型注解](#类型注解)
  - [`itertools.chain`](#itertoolschain)
  - [示例代码：使用 🛠️ multiprocessing.Queue 实现生产者-消费](#示例代码使用-️-multiprocessingqueue-实现生产者-消费)
  - [示例代码：使用 🔄 while True 实现无限循环的应用](#示例代码使用--while-true-实现无限循环的应用)
    - [1. 实现用户输入验证](#1-实现用户输入验证)
    - [2. 服务器监听 🖥️](#2-服务器监听-️)
    - [3. 多进程的任务分配 👥🔄](#3-多进程的任务分配-)
  - [动态导入的使用场景](#动态导入的使用场景)
  - [`getattr()` 的用法](#getattr-的用法)
    - [示例代码](#示例代码)
    - [注意事项](#注意事项)
  - [使用注意事项 ⚠️](#使用注意事项-️)
- [Acknowledge](#acknowledge)


## 升级说明

最近终于能抽出一些时间, 打算把博客升级一下, 修复之前的一些 bug.
但是发现之前写的程序很乱. 而且当时水平不如现在, 程序思路很乱.
这次过了两年多, 决定使用 [`Pelican`](https://getpelican.com/) 生成, 然后再使用一些插件, 自己写一些插件, 把原来的主题移植过来. 就成为了现在呈现的版本.

之前自己写静态博客生成器原因是:

- 本站的需求比较简单
- 想要练习写程序
- Hexo 等, 更新之后有时会产生一些兼容问题
- 难以随心所欲的修改博客的样式, 添加一些新的页面, 组件

现在使用 [`Pelican`](https://getpelican.com/) 的原因是

- 练习写程序. 由于博客源文件中有一些格式比较特别, 所有要自己设置一下. 这个过程中了解了 [`Pelican`](https://getpelican.com/) 的插件机制, 学些到了[许多知识](#升级博客过程中的笔记由-chatgpt-生成).
- 由于现在会自己写插件, 所以兼容行问题可以自己解决了. 同时也学会了自己写主题, 可以随心所欲的修改博客的样式.
- 之前的需求都实现了,同时还可用获得 [`Pelican`](https://getpelican.com/) 的好处. 比如: 许许多多的主题, 丰富的插件(自己写也很方便).

## 升级博客过程中的笔记(由 ChatGPT 生成)

### 类型注解

`Tuple[str, ...]：` 这是类型注解，表示 `mandatory_properties` 的类型是一个字符串元组（tuple），并且元组中的元素类型是字符串（str）。... 表示元组的长度是可变的，可以包含任意数量的字符串。

### `itertools.chain`
`itertools.chain` 是 🐍 `Python` 标准库 `itertools` 模块中的一个函数，用于将多个可迭代对象🔗连接在一起，生成一个连续的单个迭代器。它可以接受任意数量的可迭代对象，并依次迭代每个可迭代对象的元素，就像将它们“链接”成一个整体。

### 示例代码：使用 🛠️ multiprocessing.Queue 实现生产者-消费

```python
import multiprocessing  # 🛠️ 导入多进程模块
import time  # ⏳ 导入时间模块

def producer(queue):  # 🏭 生产者函数
    for i in range(5):
        print(f"Producing item {i}")  # 🛠️ 生产物品
        queue.put(i)  # 📥 将物品放入队列
        time.sleep(1)  # ⏱️ 延时 1 秒

def consumer(queue):  # 🛍️ 消费者函数
    while True:
        item = queue.get()  # 取出队列中的一个元素 📤
        if item is None:  # 接收到 None 表示生产者已结束 🚫
            break
        print(f"Consuming item {item}")  # 🛠️ 消费物品

if __name__ == "__main__":
    queue = multiprocessing.Queue()  # 📦 创建队列

    # 创建生产者进程和消费者进程 👥
    producer_process = multiprocessing.Process(target=producer, args=(queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))

    # 启动生产者和消费者进程 ▶️
    producer_process.start()
    consumer_process.start()

    # 等待生产者完成 ⏳
    producer_process.join()

    # 生产者结束后，向队列中放入一个 None，通知消费者退出 🚫
    queue.put(None)

    # 等待消费者完成 ⏳
    consumer_process.join()

    print("Main process is finishing.")  # 🎬 主进程结束
```

### 示例代码：使用 🔄 while True 实现无限循环的应用

`while True:` 是一个常见的无限循环结构，广泛应用于需要持续运行、持续监听或者重复执行某项任务的场景中。以下是几个使用 `while True:` 的实际例子：

#### 1. 实现用户输入验证
在用户输入中，我们可以用 `while True:` 来不断请求用户输入，直到输入满足条件为止：

```python
while True:  # 🔄 无限循环请求用户输入
    user_input = input("Enter a number (q to quit): ")  # 📥 用户输入
    if user_input == "q":
        print("Quitting...")  # 🚪 退出程序
        break
    try:
        number = int(user_input)
        print(f"You entered: {number}")
    except ValueError:
        print("Invalid input, please enter a number.")  # ⚠️ 输入无效
```

#### 2. 服务器监听 🖥️
在服务器应用程序中，我们可以用 `while True:` 来持续监听请求，例如一个简单的 TCP 服务器：

```python
import socket  # 🌐 导入套接字模块

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建服务器套接字
server_socket.bind(('localhost', 8080))  # 绑定地址和端口
server_socket.listen(5)  # 监听连接
print("Server is listening on port 8080...")  # 🖥️ 服务器监听

while True:  # 🔄 持续监听客户端连接
    client_socket, address = server_socket.accept()  # 接受客户端连接
    print(f"Connection from {address} has been established.")  # 🤝 连接建立
    client_socket.send(bytes("Welcome to the server!", "utf-8"))  # 发送欢迎消息
    client_socket.close()  # 关闭客户端连接
```

#### 3. 多进程的任务分配 👥🔄
在某些场景下，可以使用 `while True:` 来持续从队列中取任务并进行处理，如生产者-消费者模型：

```python
import multiprocessing
import time

def worker(queue):  # 工作者函数
    while True:
        task = queue.get()  # 从队列中取任务 📤
        if task is None:  # 任务队列结束标志 🚫
            break
        print(f"Processing task: {task}")  # 🔧 处理任务
        time.sleep(1)  # ⏱️ 模拟处理时间

if __name__ == "__main__":
    task_queue = multiprocessing.Queue()  # 📦 创建任务队列

    # 添加任务 📋
    for i in range(5):
        task_queue.put(f"Task {i}")

    # 添加结束标志 🚫
    task_queue.put(None)

    # 启动工作进程 ▶️
    process = multiprocessing.Process(target=worker, args=(task_queue,))
    process.start()

    # 等待进程完成 ⏳
    process.join()

    print("All tasks are completed.")  # 🎬 所有任务完成
```

### 动态导入的使用场景

`__import__()` 是 Python 中用于动态导入模块的内置函数，通常用于模块名在运行时才确定的情况，提供了一种灵活的导入机制。它在以下场景中非常有用：

1. **插件系统**：可以根据用户需求或配置文件选择性地导入某些模块。例如，某些插件可能需要在运行时按需加载。

2. **模块管理**：当模块的名称是动态生成或用户输入的，使用 `__import__()` 可以让程序根据名字导入相应的模块。

示例代码：

```python
module_name = "math"  # 模块名可能从用户输入或配置文件中获取
module = __import__(module_name)  # 动态导入模块

# 使用导入的模块
print(module.sqrt(16))  # 输出: 4.0
```

### `getattr()` 的用法

`cls = getattr(module, cls_name)` 是 Python 中一种动态获取属性的方式，用于从模块或对象中获取名称为 `cls_name` 的属性。这里 `getattr()` 函数被用来从 `module` 中获取名为 `cls_name` 的类，变量 `cls` 最终会指向该类。

#### 示例代码
假设你有一个模块 `shapes`，其中定义了两个类 `Circle` 和 `Square`。你可以通过字符串名称动态地从模块中获取类。

`shapes.py` 模块：
```python
# shapes.py
class Circle:
    def draw(self):
        print("Drawing a Circle")

class Square:
    def draw(self):
        print("Drawing a Square")
```

主代码：
```python
import shapes

# 动态获取类名
cls_name = "Circle"
cls = getattr(shapes, cls_name)

# cls 现在指向 Circle 类，可以创建其实例
shape = cls()
shape.draw()  # 输出: Drawing a Circle
```

#### 注意事项
- **属性不存在时引发异常**：如果 `name` 不存在且未提供 `default` 参数，`getattr()` 会引发 `AttributeError`。为避免异常，可以传递一个默认值。
  ```python
  cls = getattr(module, "NonExistentClass", None)
  if cls is None:
      print("Class not found")
  ```
- **安全性问题**：使用 `getattr()` 获取属性需要特别小心，因为它可以动态地访问任意属性或方法，可能会带来安全性风险。如果用户能够控制传递给 `getattr()` 的字符串，他们可以试图访问不应暴露的内部类或方法。因此，在使用时要确保输入是可信的或经过适当的验证。

### 使用注意事项 ⚠️
1. **`break` 退出**：`while True:` 是无限循环，所以为了避免程序一直运行下去，通常需要使用 `break` 来在合适的条件下跳出循环。
2. **性能问题 🖥️**：在某些情况下，使用 `while True:` 可能会导致程序占用大量 CPU 资源，因此在循环中应该使用适当的延时（如 `time.sleep()` ⏱️) 或等待机制来减少 CPU 的占用。
3. **结束条件 🚪**：务必为循环设置合理的结束条件，避免程序进入死循环导致资源浪费。

`while True:` 是一种简单但非常强大的循环结构，广泛应用于需要不断重复某些操作的场景，如输入验证、监听服务器、生产者-消费者模型等。它可以确保程序不断运行，直到某个条件触发 `break` 退出循环，从而灵活地控制程序的执行流程。

## Acknowledge

ChatGPT