
class Car:
    def __init__(self):
        self.__wheels = None
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels = wheel

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print('body: ', self.__body.shape)
        print('engine: ', self.__engine.horsepower)
        print('tire size: ', self.__wheels.size)


# 创建一个生成器接口
class Builder:
    def getWheel(self):
        pass

    def getEngine(self):
        pass

    def getBody(self):
        pass


# 每个单独的属性类
class Wheel(object):
    size = None


class Engine(object):
    horsepower = None


class Body(object):
    shape = None


# 实现生成器接口
class JeepBuilder(Builder):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = 'SUV'
        return body


class Director(object):
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()

        body = self.__builder.getBody()
        car.setBody(body)

        engine = self.__builder.getEngine()
        car.setEngine(engine)

        wheel = self.__builder.getWheel()
        car.attachWheel(wheel)
        return car


def main():
    jeepBuilder = JeepBuilder()
    director = Director()

    print('Jeep')
    director.setBuilder(jeepBuilder)
    jeep = director.getCar()
    jeep.specification()


if __name__ == '__main__':
    main()
