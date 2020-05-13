在某些应用程式中，我们可能会让对象根据某种内部状态来进行不同的操作。
例如 考虑下面这个代表网络连接的类

# class Connection:
#     def __init__(self):
#         self.state = "CLOSED"
    
#     def read(self):
#         if self.state != "OPEN":
#             raise RuntimeError("Not open")
#         print("reading")
    
#     def write(self):
#         if self.state != "OPEN":
#             raise RuntimeError("Not open")
        
#         print("writing")
        
#     def open(self):
#         if self.state == "OPEN":
#             raise RuntimeError("Aleary open")
        
#         self.state = "OPEN"
    
#     def close(self):
#         if self.state == "CLOSED":
#             raise RuntimeError("Already closed")
    
#         self.state = "CLOSED"
        
# 上面的代码其实没有什么问题，但有很多条件检查，代码变得很复杂。其次代码的性能下降了，因为在读写之前总是要检查状态


# 一个更优雅的方式是将每种状态以一个单独的类来定义,然后再Connection类中使用这些状态类


class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)
        
    def new_state(self,newstate):
        self._state = newstate
        
    def read(self):
        return self._state.read(self)
    
    def write(self,data):
        return self._state.write(data)

    def open(self):
        return self._state.open(self)
    
    def close(self):
        return self._state.close(self)
    
    
class ConnectionState():
    @staticmethod
    def read(conn):
        raise NotImplementedError()
    
    @staticmethod
    def write(conn,data):
        raise NotImplementedError()
    
    @staticmethod
    def open(conn):
        raise NotImplementedError()
    
    @staticmethod
    def close(conn):
        raise NotImplementedError()

    
    
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')
    
    @staticmethod
    def write(conn):
        raise RuntimeError('Not open')
    
    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)
    
    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')
    

class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print("reading")
    
    @staticmethod
    def write(conn):
        print("writing")
    
    @staticmethod
    def open(conn):
        raise RuntimeError('Already closed')
    
    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)
    

# 这样的好处：
#   1、没有了那些条件判断，性能增强了（大量的条件判断是难以维护和解读的
#   2、这样代码更优雅、易读

# 静态方法：相比于类方法和实例方法，他不和类或者实例绑定
# 这里的做法是将Connection类的实例作为参数传给ClosedConnectionState或OpenConnectionState
# 见 def write(conn): 这里的conn 就是Connection类的实例

# 关于为什么要有基类 以及 NotImplementedError 是为了确保在子类中实现了所需的方法 

# 另一个办法是修改实例的__class__属性,而其他保持不变
# 这样的方法时消除了额外的间接关系，随着状态的改变，实例自己的类型也会改变
# 虽然但是面向对象的拥趸不喜欢这种做法，但在技术上可行，并且会让代码执行得更快


class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)
        
    def new_state(self,newstate):
        self.__class__ = newstate
        
    def read(self):
        return self._state.read(self)
    
    def write(self,data):
        return self._state.write(data)

    def open(self):
        return self._state.open(self)
    
    def close(self):
        return self._state.close(self)