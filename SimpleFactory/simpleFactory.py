'''
简单工厂模式
'''


class TechnicalBooks(object):
    def publish(self):
        return 'Python Book'


class LiteraryBooks(object):
    def publish(self):
        return 'Black Hole Book'


class SimpleFactory(object):
    @staticmethod
    def publish_book(name):
        if name == 'technical':
            return TechnicalBooks()
        elif name == 'literary':
            return LiteraryBooks()


it_books = SimpleFactory.publish_book('technical')
ly_books = SimpleFactory.publish_book('literary')

print(it_books.publish())
print(ly_books.publish())

'''
工厂方法
'''
import abc


class TechnicalBooks(object):
    def publish(self):
        return 'Python Book'


class LiteraryBooks(object):
    def publish(self):
        return 'Black Hole Book'


# 抽象工厂
class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def publish_book(self):
        pass


class TechnicalFactory(AbstractFactory):
    def publish_book(self):
        return TechnicalBooks()


class LiteraryFactory(AbstractFactory):
    def publish_book(self):
        return LiteraryBooks()


it_books = TechnicalFactory().publish_book()
ly_books = LiteraryFactory().publish_book()

print(it_books.publish())
print(ly_books.publish())

'''
抽象工厂模式
'''
import abc


# 出版书籍
class TechnicalBooks(object):
    def publish(self):
        return 'publish Python Book'


class LiteraryBooks(object):
    def publish(self):
        return 'publish Black Hole Book'


# 印刷书籍
class PrintingTechnicalBooks(object):
    def printing(self):
        return 'Print Python Book'


class PrintingLiteraryBooks(object):
    def printing(self):
        return 'Print Black Hole Book'


# 抽象工厂
class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def publish_book(self):
        pass

    @abc.abstractmethod
    def print_book(self):
        pass


class TechnicalFactory(AbstractFactory):
    def publish_book(self):
        return TechnicalBooks()

    def print_book(self):
        return PrintingTechnicalBooks()


class LiteraryFactory(AbstractFactory):
    def publish_book(self):
        return LiteraryBooks()

    def print_book(self):
        return PrintingLiteraryBooks()


# 实例化工厂对象
it = TechnicalFactory()
ly = LiteraryFactory()

# 印刷书籍
it_print = it.print_book()
ly_print = ly.print_book()

# 出版书籍
it_publish = it.publish_book()
ly_publish = ly.publish_book()

print(it_print.printing())
print(ly_print.printing())
