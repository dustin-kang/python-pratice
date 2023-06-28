from abc import ABCMeta, abstractmethod

# 1. Product : 인터페이스
class Ipad(metaclass=ABCMeta):
    """
    ### Product Interface
    자식 클래스가 생성할 수 있는 모든 객체
    """
    @abstractmethod
    def set_info(self):
        pass

    @abstractmethod
    def set_core(self):
        pass


# 2. 구상 제품들
class IpadPro(Ipad):
    """
    ### 구상제품들
    인터페이스를 다양하게 구현하는 역할을 합니다.
    """
    def set_info(self):
        print("This Product is iPad Pro")

    def set_core(self):
        print("Core is M1Pro")

class IpadAir(Ipad):
    """
    ### 구상제품들
    인터페이스를 다양하게 구현하는 역할을 합니다.
    """
    def set_info(self):
        print("This Product is iPad Air")

    def set_core(self):
        print("Core is M2")

# Factory
class PadFactory(metaclass=ABCMeta):
    """
    ### Creator Class
    - 새로운 제품의 객체를 `팩토리 메소드`를 통해 반환합니다.
    - 구상 크리에이터들로 분업합니다.
    """
    @abstractmethod
    def createIpad(self):
        pass


# ConcreateFactory
class ProLineFactory(PadFactory):
    """
    ### 구상 Creator Class
    - 기초 팩토리 메서드를 오버라이딩하여 다른 유형의 제품을 반환합니다. 
    """
    def createIpad(self):
        return IpadPro()
    
class AirLineFactory(PadFactory):
    """
    ### 구상 Creator Class
    - 기초 팩토리 메서드를 오버라이딩하여 다른 유형의 제품을 반환합니다. 
    """
    def createIpad(self):
        return IpadAir()
    

# Client
class Client():
    def use(self, version):

        # 사용자의 요구의 따라 생산할 factory 생성
        if version == 'Pro':
            factory = ProLineFactory()
        elif version == 'Air':
            factory = AirLineFactory()
        else:
            return
        
        # 제품 생산
        myipad = factory.createIpad()
        # 생산된 제품 사용
        myipad.set_info()

        # template Method 호출
        # myipad = factory.set_info()



if __name__ == '__main__':
    clinet = Client()
    clinet.use('Pro')
    clinet.use('Air')




