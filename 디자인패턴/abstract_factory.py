from abc import ABCMeta, abstractclassmethod

# Product
class Phone(metaclass=ABCMeta):
    """
    추상 제품 인터페이스(Phone)
    - `touch` 기능
    """
    @abstractclassmethod
    def touch(self):
        pass

class Tablet(metaclass=ABCMeta):
    """
    추상 제품 인터페이스(Phone)
    - `draw` 기능 
    - `touch` 기능
    """
    @abstractclassmethod
    def draw(self):
        pass
    
    def touch(self):
        pass


# concreteProduct
class IPad(Tablet):
    """
    Apple 사의 Pad 제품 인터페이스 (구상 제품)
    """
    def draw(self):
        print("애플 펜슬을 이용해 그릴 수  있습니다.")
    
    def touch(self):
        print("PadOS 16 버전을 사용하고 있습니다.")

class Iphone(Phone):
    """
    Apple 사의 Phone 제품 인터페이스 (구상 제품)
    """
    def touch(self):
        print("iOS 16 버전을 사용하고 있습니다.")

class GalaxyTabS(Tablet):
    """
    Samsung 사의 Pad 제품 인터페이스 (구상 제품)
    """
    def draw(self):
        print("S펜을 이용해 그릴 수  있습니다.")
    
    def touch(self):
        print("안드로이드 12L 버전을 사용하고 있습니다.")

class GalaxyS(Phone):
    """
    Samsung 사의 Phone 제품 인터페이스 (구상 제품)
    """
    def touch(self):
        print("안드로이드 13을 사용하고 있습니다.")


# Abstract Factory
class Factory(metaclass=ABCMeta):
    """
    추상 팩토리 인터페이스
    : 추상 제품을 생성하기 위한 함수 집합
    """
    @abstractclassmethod
    def createPhone(self):
        pass

    @abstractclassmethod
    def createPad(self):
        pass

# ConcreteFactory
class AppleFactory(Factory):
    """
    Apple 사의 구상 팩토리
    : 추상 팩토리의 생성 메서드를 구현하는 함수
    - 제품들의 특정 변형들만 해당
    """
    def createPad(self):
        return IPad()
    
    def createPhone(self):
        return Iphone()
    

class SamsungFactory(Factory):
    """
    Samsung 사의 구상 팩토리
    : 추상 팩토리의 생성 메서드를 구현하는 함수
    - 제품들의 특정 변형들만 해당
    """
    def createPad(self):
        return GalaxyTabS()
    
    def createPhone(self):
        return GalaxyS()
    

# Client
class Client():
    """
    클라이언트
    : 클라이언트 객체는 추상 인터페이스를 통해 팩토리/제품 변형 객체들과 작업을 할 수 있습니다. 
    """
    def buy(self, company):
        
        if company == 'Apple':
            factory = AppleFactory()
        elif company == 'Samsung':
            factory = SamsungFactory()
        else:
            return
        

        pad = factory.createPad()
        phone = factory.createPhone()


        pad.touch()
        pad.draw()
        phone.touch()

if __name__ == '__main__':
    client = Client()
    client.buy('Apple')
    print()
    client.buy('Samsung')