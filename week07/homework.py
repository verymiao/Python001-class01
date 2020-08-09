from abc import ABCMeta, abstractmethod

class Zoo():
    all_animal = set()
    def __init__(self,name):
        self.name = name

    def add_animal(self,animal):
        if animal in self.all_animal:
            print(f'{self.name}存在\'{animal.name}\', 不允许重复添加')
        else:
            self.all_animal.add(animal)
            print(f'\'{animal.name}\'成功加入{self.name}')

    def del_animal(self,animal):
        if animal in self.all_animal:
            self.all_animal.remove(animal)
            print(f'\'{animal.name}\'移除成功')
        else:
            print(f'{self.name}不存在\'{animal.name}\'')

    def __getattr__(self, item):
        for i in self.all_animal:
            if item == i.class_name():
                return True
            else:
                return False

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,animal_type, somatotype, disposition):
        self.animal_type = animal_type
        self.somatotype = somatotype
        self.disposition = disposition
        if self.somatotype == '中等' and animal_type == '食肉':
            self.is_ferocious = True
        else:
            self.is_ferocious = False

    @classmethod
    def class_name(cls):
        return cls.__name__

class Cat(Animal):
    sound = '喵喵喵'
    def __init__(self,name,animal_type, somatotype, disposition):
        self.name = name
        super().__init__(animal_type, somatotype, disposition)
        self.sounds = '喵喵喵'

    @classmethod
    def sounds(cls):
        return cls.sound

    @property
    def is_pets(self):
        if self.disposition == '温顺':
            return True
        else:
            return False

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
